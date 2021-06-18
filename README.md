# TA-YAB

1. ## Virtual Environments

    1. ### Install the virtualenv package
        ```bash
        $ pip install virtualenv
        ```

    2. ### Create the virtual environment
        ```bash
        $ virtualenv env
        ```

    3. ### Activate the virtual environment
        - #### Mac OS / Linux
          ```bash
          $ source env/bin/activate
          ```
        - #### Windows
          ```bash
          $ env\Scripts\activate
          ```

    4. ### Deactivate the virtual environment
        ```bash
        (env) $ deactivate
        ```

2. ## Install Requirements Packages
    ```
    $ pip install -r requirements.txt
    ```

3. ## Start Django Project
    ```
    $ python manage.py runserver
    ```
    
[django runserver]( https://docs.djangoproject.com/en/3.2/ref/django-admin/#runserver )
