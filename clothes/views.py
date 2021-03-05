from django.shortcuts import render, redirect
from clothes.models import Item
from pathlib import Path


#clothes = [
#    {'caps': ['psd_cap_mockup.png', 'vintage cap.jfif', 'white cap.jfif']},
#    {'coats': ['coat pant.jfif', 'green jacket coat.jfif']},
#    {'hats': ['crocket baby hats.jfif', 'easy childrens hats.jfif', 'girls cloche hat.jfif', 'straw hat.jfif',
#              'womens red hat.jfif']},
#]

isAuthenticated = True

choosen_item = ""

item_Types = dict()

def home(request):
    setupClothing()

    print("Debuging after again:", item_Types["caps"][0].item_Price)
    
    return render(request, 'index.html', {'clothes': item_Types })

def setupClothing():
    items = Item.objects.all()
    
    item_Name = ""
    item_Image = ""
    item_Price = ""
    item_Description = ""

    #print("Debuging: " + clothes.item_Type)

    caps = []
    capps = {}
    coats = []
    hats = []
    shirts = []
    hoodies = []
    jackets = []
    skirts = []
    specials = []
    sweaters = []
    waistcoats = []
    for item in items:
        str_item = str(item)
        print("Item: " + str_item)
        if (str_item == "caps"):
            print("Ccaps")
            caps.append(item)
        elif (str_item == "shirts"):
            shirts.append(item)
        elif (str_item == "coats"):
            coats.append(item)
        elif (str_item == "hats"):
            hats.append(item)
        elif (str_item == "hoodies"):
            hoodies.append(item)
        elif (str_item == "jackets"):
            jackets.append(item)
        elif (str_item == "skirts"):
            skirts.append(item)
        elif (str_item == "specials"):
            specials.append(item)
        elif (str_item == "sweaters"):
            sweaters.append(item)
        elif (str_item == "waistcoats"):
            waistcoats.append(item)

        print("item: ", item.item_Image)
        
        setItem_Types("caps", caps)
        setItem_Types("shirts", shirts)
        setItem_Types("coats", coats)
        setItem_Types("hats", hats)
        setItem_Types("hoodies", hoodies)
        setItem_Types("jackets", jackets)
        setItem_Types("skirts", skirts)
        setItem_Types("specials", specials)
        setItem_Types("sweaters", sweaters)
        setItem_Types("waistcoats", waistcoats)


def setItem_Types(type, data):
    item_Types.__setitem__(type, data)

def check_authentication(request):
    setupClothing()
    print(isAuthenticated)
    choosen_item_path = request.GET.get('item')
    choosen_item_category = request.GET.get('item_category')
    choosen_item_name = request.GET.get('item_name')
    choosen_item_price = request.GET.get('itp')
    auth_context = {'isAuthenticated': isAuthenticated, 'choosen_item_path': choosen_item_path, 'itp': choosen_item_price, 'choosen_item_category': choosen_item_category, 'choosen_item_name': choosen_item_name}
    print("Parameter: ", choosen_item_name, ' ')
    #print("Debug Parameter: ", item_Types[choosen_item_category].index(choosen_item))
    return render(request, 'cart.html', {'auth_context': auth_context})

def register(request):
    if request.method == 'POST': 
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        print('Name: ' + name + '\nEmail: ' + email + '\nPassword1: ' + pass1 + '\nPassword2: ' + pass2)
        if pass1 == pass2:
            return render(request, 'login.html')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print('Email: ', email, '\nPassword: ', password)
        if email != "" and password != "":
            isAuthenticated = True
            return render(request, 'cart.html', {'email': email, 'password': password})
    return render(request, 'login.html')


def bought(request):
    setupClothing()
    choosen_item_category = request.GET.get('choosen_item_category')
    choosen_item_name = request.GET.get('choosen_item_name')
    choosen_item_num = int(request.POST.get('num_items'))
    choosen_item_path = request.GET.get('choosen_item_path')
    choosen_item_price = float(request.GET.get('itp'))
    pr = request.POST.get('price')

    total_cost = choosen_item_price * choosen_item_num
    print('Choosen Item Category: ', choosen_item_category, ' ', choosen_item_name, ' ', choosen_item_num, ' ', choosen_item_path, ' ', choosen_item_price, total_cost)
    choosen_item_context = {'choosen_item_category': choosen_item_category, 'choosen_item_name': choosen_item_name, 'choosen_item_num': choosen_item_num, 'choosen_item_path': choosen_item_path, 'total_cost': total_cost}

    print("Price: in Rands (R):", pr)
    return render(request, 'bought.html', {'choosen_item_context': choosen_item_context})


def contact_developer(request):
    return render(request, 'contact_developer.html', {'name': 'Uram Mnisi', 'email': 'urmnisi@gmail.com'})