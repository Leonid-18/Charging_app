# Run server by command:
```
docker-compose up
```

# Registration 
send POST
``````
http://127.0.0.1/user/register
``````

body example:
```buildoutcfg
    {
    "username": "admin_1",
    "password": "12345678!",
    "password2": "12345678!",
    "email": "myss@gmail.com",
    "first_name": "name",
    "last_name": "last name",
    "is_staff": "true"
    }
```
# Login

send POST
``````
http://127.0.0.1/user/login
``````
body example:
```buildoutcfg
    {
     "username": "mock",
    "password": "12345678!"
    }
```

YOU HAVE TO add Bearer token to header after login!

# User info

You have to call  GET

``````
http://127.0.0.1/user/me
``````


# Start charging

You have to call POST

``````
http://127.0.0.1/billing/start-charging
``````

body example:
```buildoutcfg
    {
    "user": "1",
    "type": "USD"
}
```

and we receive billing in our data

