- First run
```bash 
python manage.py makemigrations
```

```bash 
python manage.py migrate
```

```bash 
python manage.py runserver
```

```bash
python -m smtpd -n -c DebuggingServer localhost:1025
```


### docker command for redis
```bash
docker run -p 6379:6379 -d redis:5
```
