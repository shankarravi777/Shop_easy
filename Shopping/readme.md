## Project: Shop Easy

The shop easy websites allow consumers to shop for products and services from the comfort of their own homes. This is particularly useful for people who may not have easy access to physical stores, or who prefer the convenience of shopping online.



## How to start it

-   Create a new project folder called 'Shopping' and then cd into the folder via the terminal and execute these commands:
    
   ```
pyenv local 3.10.7 # this sets the local version of python to 3.10.7
python3 -m venv .venv # this creates the virtual environment for you
source .venv/bin/activate # this activates the virtual environment
pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
```
    
   
    
-   then We used Django ([https://www.djangoproject.com](https://www.djangoproject.com/)) as our web framework for the application. We installed that with
    
    ```
     pip install Django==4.1.2
    
    ```
    
-   Now we can start to create the site using the django admin tools. Issue this command, and don't forget the '.' at the end of the line, which says 'create the project in this directory'. This will create the admin part of our application, which will sit alongside the actual site.
    
    ```
    django-admin startproject mysite .
    

- We need to specify some settings for the site, which we do in the mysite/settings.py file. Open this and add this line above the line for pathlib import Path:
    
    
    ```
      import os

- Now go to the end of the file to add a line specifying the root directory for the static files.
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
- Now go further up the file to 'ALLOWED_HOSTS' so that we can run this beyond 'localhost' and 127.0.0.1, which are the only allowed ones if this is empty. Modify this accordingly to suit your needs:

```
ALLOWED_HOSTS = [ 'https://groupindia.onrender.com','groupindia.onrender.com', '127.0.0.1', 'beyondlaura-exceptvisa-8000.codio-box.uk', 'localhost', 'spendminimum-stadiumjaguar-8000.codio-box.uk', 'politicpermit-freedompastel-8000.codio-box.uk', 'opinionwave-octaviagordon-8000.codio-box.uk', 'ingridinfo-designlogo-8000.codio-box.uk', 'salsanurse-arthurcosmos-8000.codio-box.uk', 'infohavana-maydaypenguin-8000.codio-box.uk', 'rajapicture-comedystatic-8000.codio-box.uk', 'miketopic-rentgraph-8000.codio-box.uk','rajapicture-comedystatic-8000.codio-box.uk']
```
- Although we are not using a database for this application, django uses one in the background. We now need to configure this database, which you saw was already detailed in the settings.py file. As django has a built-in admin tool, it already knows some of the tables that it needs to use. We can set this up with the command:

```
           python3 manage.py migrate
```
## Start the server 

    
- We can now use the manage.py command tool to start the development server by entering this command in the terminal:    
    ```
      python3 manage.py runserver
    ```
- If you're doing this on another platform, then you might need to use this instead (change the port number from 8000 as required):
```
      python3 manage.py runserver 0.0.0.0:8000
```
 - If it went well, then you should see the python rocket launching your site when you open the browser at the site.  

## Creating the Story content

Leave the server running. Open a new terminal and navigate as required to the same directory. We can now set about creating the space for our Shopping，
```
    python3 manage.py startapp group_india
```
- This will create a new folder for us including space for database migrations, and other details specific to our content. 

- Django needs to know the urls of the site so that it can serve up pages to visitors, and tell others that the page requested isn't part of the site. We do that by opening mysite/urls.py and adding a line for the pages that will be under Shopping.

-   First, add 'include' to the line with 'import path' so that it reads

  ```
           from django.urls import path, include
```
  
-   Second, add this line (plus the , at the end of the line above it), to have django find your Shopping pages:
```
path('', views.store, name='store'),

path('register/', views.register, name='register'),

path('login/', views.login_view, name='login'),

path('logout/', views.login, name='logout'),

path('cart',views.cart,name='cart'),

path('checkout',views.checkout,name='checkout'),

path('update_item/',views.updateItem,name='update_Item'),

path('process_order/',views.processOrder,name='process_order')
```
- Third, we need to modify the settings.py file in the mysite app, so that it knows to include the 'Shopping' contents. We do this by adding a line in the section on 'INSTALLED_APPS'. Add this line to the end of the block ( plus the , at the end of the line above it).

 ```
        ''myapp',,
```
- Fourth, we need to tell Shopping about the URLs it is using, so that they can be added to the list of URLs (pages) used by 'eshop'. We do that by creating the file urls.py in the 'Shopping' folder. It should hold these details:
```
from django.urls import path
         
from . import views

  urlpatterns = [

path('', views.store, name='store'),

path('register/', views.register, name='register'),

path('login/', views.login_view, name='login'),

path('logout/', views.login, name='logout'),

path('cart',views.cart,name='cart'),

path('checkout',views.checkout,name='checkout'),

path('update_item/',views.updateItem,name='update_Item'),

path('process_order/',views.processOrder,name='process_order')

]
```


- we're now passing in the 'request' object to the index method, and use that in the template rendering, and we also create a dictionary object to pass to the template. The ideas are the same, but the syntax is slightly different.

- For the templates we need to put the main.html file into a 'templates' directory. Create that, and then create a 'Shopping' directory under 'templates'. This is a Django convention, and helps us separate out the content for our site if we added other components to the site.

- Now create a blank main.html file and put this code into it. This is almost the same as what we used in the flask version. We've only changed the text in the file
```
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">

<meta http-equiv="X-UA-Compatible" content="ie=edge">

<title>ShopEasy</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

<link rel="stylesheet" type="text/css" href="/css/main.css">

<script type="text/javascript">

var user  =  '{{ request.user }}';

function getToken(name) {

let cookieValue  =  null;

if (document.cookie  &&  document.cookie  !==  '') {

const cookies  =  document.cookie.split(';');

for (let i  =  0; i  <  cookies.length; i++) {

const cookie  =  cookies[i].trim();

if (cookie.substring(0, name.length +  1) === (name  +  '=')) {

cookieValue  = decodeURIComponent(cookie.substring(name.length +  1));

break;

}
```
- We are now ready to run the changes to see the page load. Stories should now appear when you load the page on the site. You can change the nouns, adjectives and other parts of mystory with values from Faker. Go to  [https://faker.readthedocs.io/en/stable/providers.html](https://faker.readthedocs.io/en/stable/providers.html)  and look through the options for Standard Providers and make some changes to mystory

 ##  Creating the functions 
- This view retrieves all products from the `Product` model and renders the `store.html` template, passing in the retrieved products as context.
- Open up views.py and add modify the views method so that it looks like this:
 ```
def store(request):

products = Product.objects.all()

context = {'products': products}

return render(request, 'registration/store.html', context)

  
  

def register(request):

form = UserCreationForm()

  

if request.method ==  'POST':

form = UserCreationForm(request.POST)

if form.is_valid():

user = form.save()

login(request, user)

return redirect('store')

  

context = {'form': form}

return render(request, 'registration/register.html', context)

  
  

def login_view(request):

if request.method ==  'POST':

form = AuthenticationForm(request=request, data=request.POST)

if form.is_valid():

username = form.cleaned_data.get('username')

password = form.cleaned_data.get('password')

user = authenticate(request, username=username, password=password)

if user is  not  None:

login(request, user)

return redirect('store')

else:

form = AuthenticationForm()

return render(request, 'registration/login.html',{

'form': form

})
```
- This now accepts the variable  from the form and  sends back to the page for display.

- Open up main.html and modify the page to look like this:
```
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">

<meta http-equiv="X-UA-Compatible" content="ie=edge">

<title>ShopEasy</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

<link rel="stylesheet" type="text/css" href="/css/main.css">

<script type="text/javascript">

var user  =  '{{ request.user }}';

function getToken(name) {

let cookieValue  =  null;

if (document.cookie  &&  document.cookie  !==  '') {

const cookies  =  document.cookie.split(';');

for (let i  =  0; i  <  cookies.length; i++) {

const cookie  =  cookies[i].trim();

if (cookie.substring(0, name.length +  1) === (name  +  '=')) {

cookieValue  = decodeURIComponent(cookie.substring(name.length +  1));

break;

}
```
- We need to add a line to the settings.py file that will tell Django that the csrf token used in our form is valid. Add this line below the Allowed hosts line:
```
CSRF_TRUSTED_ORIGINS =  ['https://scharlau.pythonanywhere.com', 'localhost']
```
- Amend the server name to suit your system. Save the changes, and reload the pages to see it in action.
## Do Some  changes
- We're now ready for you to modify the site to learn a bit more about how you use Django and understand the relationship between the components. This is mostly a quick intro without models and tables to let you focus on the structure of a Django application.

- You can take this further  stages:

    1.  Clean up the code in views.py by moving the functions to a separate method so that you can add more features to the page, and  display the features in webpage 
  2.  This view renders the `register.html` template, which contains a form for creating a new user account. When the form is submitted, the view attempts to create a new user account using the `UserCreationForm` provided by Django's
  3.  Push the boundaries further to see what else you might do with Django.

    

## Installation

- Clone or download the project code:

```
git clone https://github.com/your_username/app.git

```

- Enter the project directory:

```
cd app

```

- To create and activate a Python virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate

```

- Python dependencies required to install the project:

```
 pip install Django==4.1.2
 pyenv install 3.11.0
 pip install --upgrade pip
 pip3 install whitenoise
```

- Run the application (take the codio run as an example)

```
python3 manage.py runserver 0.0.0.0:8000
```

- Visit the following URL in your Web browser to view the application:

```
https://rajapicture-comedystatic-8000.codio-box.uk/

```

## USE

1.  The page displays a list of applications. You can click the Details button to see the details of your application.
2.  On the application list page, you can use the paging control to browse applications on different pages.




