    #####  FOLLOW THE STEPS  #####
    
1. Make sure to have or install django framework
	pip install django

2. Create new project

3.Clone project repository : 
	git clone https://github.com/MarioDavidov/djangorestAPI.git

4.Install reqgurements : 
	pip install -r requirements.txt
	pip freeze > requirements.txt

5. In main settings connect youre datebase to the aplication
	
        'NAME': '*****',
        'USER': '*****',
        'PASSWORD': '*****',
        'HOST': '*****',
        'PORT': *****,

6.Enter new SECRET KEY 
    Use https://djecrety.ir/ to generate SECRET KEY fast and easy

7.Migrate project
 	 python manage.py makemigrations
 	 python manage.py migrate

8. Create a new superuser for easier use of the application
	 python manage.py createsuperuser

9.Run the project
   python manage.py runserver
   
10.Enter the admin page (/admin/). Start using the app
