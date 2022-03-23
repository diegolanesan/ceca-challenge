# ceca-challenge

Application built with React, Django REST framework, MySQL and Docker.

To run the application:

```
git clone https://github.com/thejungwon/docker-reactjs.git
cd ceca-challenge
docker-compose up
```

To interact with the backend and insert the example data:

```
docker-compose exec backend sh
python manage.py register-cars
```

Go to https://localhost:3000.
