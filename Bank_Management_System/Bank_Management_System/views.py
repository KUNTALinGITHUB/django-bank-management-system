from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

customers=[]
accounts=[]

def home(request):
    return render(request, 'home.html')

def create_customer(request):
    customer_details=dict()
    alart=""
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        balance = request.POST.get('balance')

        if name and email and age and balance:
            customer_details = {
                'name':name,
                'email':email,
                'age':age,
                'balance':balance
            }
            customers.append(customer_details)
            alart="successfully"
        else:
            alart="unsuccessfully"
    
    context={
        'customers':customers,
        'alart':alart
    }
    return render(request, 'create_customer.html', context)

def update_customer(request):
    alart=""
    message=""
    context={}

    if request.method == "POST":
        action = request.POST.get("action")

        if action == 'search':
            Sname = request.POST.get('Sname')
            Semail = request.POST.get('Semail')

            if Sname and Semail:
                if len(customers) > 0 :
                    for i in customers:
                        if i['name'] == Sname and i['email'] == Semail:
                            alart="customers details avaliabel"
                            context={
                                'name':i['name'],
                                'email':i['email'],
                                'age':i['age'],
                                'balance':i['balance'],
                                'alart':alart
                            }
                            break
                else:
                    context={
                            'alart':"No customers exist"
                    }
            return render(request, 'update_customer.html', context )


    

        elif action == "update":
            Sname = request.POST.get('Sname')
            Semail = request.POST.get('Semail')

            name = request.POST.get('name')
            email = request.POST.get('email')
            age = request.POST.get('age')
            balance = request.POST.get('balance')

            if name and email and age and balance:
                for j in customers:
                    if j['name'] == Sname and j['email'] == Semail :
                        j['name'] = name
                        j['email'] = email
                        j['age'] = age
                        j['balance'] = balance
                        message="successfully"
                        break
                else:
                    message="not_found"
            else:
                message = "invalid"
    context.update({
        'message':message,
        'customers':customers
    })
    return render(request, 'update_customer.html', context)

def delete_customer(request):
    alert=""

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        if name and email and age:
            customer_removed = False
            account_removed = False

            # Remove customer
            for i in customers:  
                if i['name'] == name and i['email'] == email and i['age'] == age:
                    customers.remove(i)
                    customer_removed = True
                    break

            # Remove account
            for j in accounts: 
                if j['name'] == name and j['email'] == email and j['age'] == age:
                    accounts.remove(j)
                    account_removed = True
                    break

            # Final message
            if customer_removed and account_removed:
                alert = "Customer and account data removed successfully"
            elif customer_removed:
                alert = "Customer removed, but account not found"
            elif account_removed:
                alert = "Account removed, but customer not found"
            else:
                alert = "No matching customer or account found"

        else:
            alert = "All fields (name, email, age) are required"
    contexts={
        'customers':customers,
        'accounts':accounts,
        'alert':alert
    }
    return render(request, 'delete_customer.html', contexts)

def get_customer(request):
    alart=""
    details=[]
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            for i in customers:
                if i['name'] == name and i['email'] == email:
                    alart="find"
                    details.append([i['name'], i['email'], i['age'], i['balance']])
                    break
            else:
                alart ="not find"
    contexts={
        'alart': alart,
        'details': details
    }
    
    return render(request, 'get_customer.html', contexts)


def create_account(request):
    account_details=dict()
    alart=""

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        accnumber = request.POST.get('accnumber')

        for i in customers:
            if i['name'] == name and i['email'] == email and i['age'] == age :
                account_details={
                    'name':name,
                    'email':email,
                    'age':age,
                    'accnumber':accnumber
                }
                accounts.append(account_details)
                alart="successfully"
                break
        else:
            alart="unsuccessfully"

    contexts={
        'accounts':accounts,
        'alart':alart
    }
    return render(request,'create_account.html', contexts)

def get_account(request):
    alart=""
    Adetails=[]
    if request.method == "POST":
        name = request.POST.get('name')
        accnumber = request.POST.get('accnumber')

        if name and accnumber:
            for i in accounts:
                if i['name'] == name and i['accnumber'] == accnumber:
                    alart="find"
                    Adetails.append([i['name'], i['email'], i['age'], i['accnumber']])
                    break
            else:
                alart ="not find"
    contexts={
        'alart': alart,
        'Adetails': Adetails
    }
    
    return render(request, 'get_account.html', contexts)



def deposit(request):
    alart=""
    message=""

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        accnumber = request.POST.get('accnumber')
        depositamount = request.POST.get('depositamount')

        for i in accounts:
            if i['name'] == name and i['email'] == email and i['accnumber'] == accnumber :
                for j in customers:
                    if j['name'] == name and j['email'] == email :
                        j['balance'] = float(j['balance']) + float(depositamount)
                        alart="successfully"
                        message=j['balance']
                        break
                break
        else:
            alart="unsuccessfully"

    contexts={
        'customers':customers,
        'message':message,
        'alart':alart
    }

    return render(request, 'deposit.html', contexts)

def withdraw(request):
    alart=""
    message=""

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        accnumber = request.POST.get('accnumber')
        withdrawamount = request.POST.get('withdrawamount')

        for i in accounts:
            if i['name'] == name and i['email'] == email and i['accnumber'] == accnumber :
                for j in customers:
                    if j['name'] == name and j['email'] == email :
                        if float(withdrawamount) > float(j['balance']):
                            alart="insafficient"
                            break
                        else:
                            j['balance'] = float(j['balance']) - float(withdrawamount)
                            alart="successfully"
                            message=j['balance']
                            break
                break
        else:
            alart="unsuccessfully"

    contexts={
        'customers':customers,
        'message':message,
        'alart':alart
    }
    return render(request, 'withdraw.html', contexts)
