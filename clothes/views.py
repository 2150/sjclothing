from django.shortcuts import render, redirect


clothes = [
    {'caps': ['psd_cap_mockup.png', 'vintage cap.jfif', 'white cap.jfif']},
    {'coats': ['coat pant.jfif', 'green jacket coat.jfif']},
    {'hats': ['crocket baby hats.jfif', 'easy childrens hats.jfif', 'girls cloche hat.jfif', 'straw hat.jfif',
              'womens red hat.jfif']},
]

isAuthenticated = True

def home(request):
    return render(request, 'index.html', {'clothes': clothes})


def check_authentication(request, *args, **kwargs):
    print(isAuthenticated)
    print("Parameter: ", kwargs)
    return render(request, 'cart.html', {'isAuthenticated': isAuthenticated})

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