## Usage

In /front run

```bash
docker-compose up
```

In /users run

```bash
docker-compose up
```

In /offers run

```bash
docker-compose up
```

In /chat run

```bash
pip install -r requirements.txt
docker run -p 6379:6379 -d redis:5
python manage.py runserver 8003
```

Then go to http://127.0.0.1:8000/
