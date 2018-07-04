# BudgetMe API

BudgetMe API written in Python with Django REST Framework.

Front-end is here : https://github.com/poblouin/budgetme-angular-app

### Integration tests

You only need to run pytest, the pytest.ini is defined. Coverage is also installed with requirements.


### django-kronos

Note: The following commands must be ran within the sourced env of the project.

To run the scheduled transaction task

    $ python manage.py runtask process_scheduled_transactions
    
To register the task to cron

    $ $ python manage.py installtasks
