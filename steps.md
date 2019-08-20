Order of events
* project/urls.py gets the html request with the url path
* project/urls.py sends you to app/urls.py
* app/urls.py sends you to a function in app/views.py
* app/views.py grabs .models to access the database
* app/views.py creates context and grabs an html template from app/templates/app/
* app/views.py returns a rendered website from the context and template



