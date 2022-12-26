    #####  FOLLOW THE STEPS  #####
    
1. Make sure to have or install django framework
2. 
		pip install django


3. Create new project

4.Clone project repository :


	git clone https://github.com/MarioDavidov/djangorestAPI.git

5.Install reqgurements :

	pip install -r requirements.txt
	pip freeze > requirements.txt
	

6. In main settings connect youre datebase to the aplication
	
        'NAME': '*****',
        'USER': '*****',
        'PASSWORD': '*****',
        'HOST': '*****',
        'PORT': *****,

7.Enter new SECRET KEY


    Use https://djecrety.ir/ to generate SECRET KEY fast and easy
    

8.Migrate project


 	 python manage.py makemigrations
 	 python manage.py migrate
	 

9. Create a new superuser for easier use of the application


	 python manage.py createsuperuser
	 
	 
10.Run the project



   	python manage.py runserver
   
   
11.Enter the admin page (/admin/). Start using the app
