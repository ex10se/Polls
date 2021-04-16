# API для системы опросов пользователей
API позволяет администраторам выполнять всевозможные операции с опросами, 
вопросами опросов, а пользователям получать список активных опросов, 
отправлять ответы на вопросы и получать список своих ответов.
## Подготовка
    git clone https://github.com/ex10se/Polls.git
    cd Polls
## Docker
    docker-compose up --build
## Разработка
Windows

    virtualenv -p python venv
    cd venv/Scripts
    activate.bat
Linux

    sudo apt install libpq-dev python3-dev build-essential virtualenv
    virtualenv -p python venv
    cd venv/bin
    source activate

    cd ../..
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser

    python manage.py runserver

