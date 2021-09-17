# salesforce

To use define your salesforce credentials in the `settings.py` file like this

```
CLIENT_ID = "<client_id>"

SECRET_ID = "<sec_id>"
RETURN_URL = "<return_url>"
SDFC_USER = "<salesforce username>"
PASSWORD = "<salesforce password>"

URL = "https://login.salesforce.com/services/oauth2/token"
```

Now, on command prompt, 
run the following commands in the given order:

1. `pip install -r requirements.txt`
2. ` python manage.py makemigrations`
3. ` python manage.py migrate`
4. ` python manage.py runserver`

Now,you can visit the provided url `http://127.0.0.1:8000`

Click, 'Refill button' to fetch data and fill in the database.

'Delete button' will delete all the data

To see the live changes in database, first make a superuser from command prompt

`python manage.py createsuperuser`

Fill the asked details.
Now run the server again and you can browse to `http://127.0.0.1:8000/admin`
Login with your credentials and you can see the changes that happen after all the button clicks ('Refill' and 'delete').
