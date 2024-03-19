# Web App Documentation  

**Web App information**  
_Prerequisites_ Ubuntu or linux OS with [python3](https://docs.python-guide.org/starting/install3/linux/) installed.  

* Check your python & pip versions: `python3 --version` & `pip3 --version`  
* Download django package: `pip3 install django`  
* Initialize the django project: `django-admin startproject PROJECT_NAME .`  
* Create the web app: `python3 manage.py startapp APP_NAME`  
* Modify the file **/APP_NAME/views.py** with these lines:  
```
from django.http import HttpResponse
  
def home(request):  
    return HttpResponse("Hello, Django!")
```

* Create a file **/APP_NAME/urls.py** with these lines:  
```
from django.urls import path
from APP_NAME import views

urlpatterns = [  
    path("", views.home, name="home"),
]
```

* Modify the file **/PROJECT_NAME/urls.py** file with these lines:  
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("APP_NAME.urls")),
]
``` 

* Start the web server, listening on port 8000 for all interfaces: `python3 manage.py runserver 0.0.0.0:8000`  

**Reference**
[Django Web Framework for Python](https://learn.microsoft.com/en-us/windows/python/web-frameworks#hello-world-tutorial-for-django)