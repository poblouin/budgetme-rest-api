# BudgetMe API

BudgetMe API written in Python with Django REST Framework.

Front-end is here : https://github.com/poblouin/budgetme-angular-app

### Integration tests

You only need to run pytest, the pytest.ini is defined. Coverage is also installed with requirements.


### django-kronos

Note: The following commands must be ran within the sourced env of the project.

To run the scheduled transaction task

    $ python manage.py process_scheduled_transactions
    
To register the task to cron

    $ python manage.py installtasks

### env file

In config/settings, there is a .env file that is read by the production config. In this file, you must put the following config so that the app can work properly.

    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB=budgetme
    DJANGO_SETTINGS_MODULE=config.settings.[local,production]
    DATABASE_URL=postgres://{user}:{pass}@db/budgetme
    DJANGO_SECRET_KEY=
    DJANGO_ALLOWED_HOSTS=
    DJANGO_ADMIN_URL=
    DJANGO_SENTRY_DSN=
