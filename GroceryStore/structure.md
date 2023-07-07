# APPLICATION STRUCTURE

---

- GroceryStore/
    - grocery_store.py --> main script where the application factory is imported
    - .flaskenv --> flask specific environment variables
    - config.py --> configuration classes for running app in different configurations
    - app.db --> sqlite3 file for the database

    ---

    - flaskr/ --> main package contains all the files for the application
        - *__ init __.py* --> application factory definition
        - models.py --> SQLAlchemy Database Model definitions
        - forms.py --> Classes for Flask-WTForms
        - extensions.py --> utility module to import and initialize all the used Flask-extensions

        ---

        - *BLUEPRINTS*

        ---

        - main/ --> handles the home page for the application
            - *__ init __.py*
            - routes.py
        
        - auth/ --> handles user signup and signin
            - *__ init __.py*
            - signin.py
            - signup.py

        - user/ --> handles the individual userpages
            - *__ init __.py*
            - userpage.py
        
        - admin/ --> handles the admin signin and admin main page
            - *__ init __.py*
            - admin_signin.py
            - admin.py

        ---

        - *JINJA TEMPLATES*
        
        ---
        
        - templates/ --> Jinja templates for the application
            - base.html --> base HTML has all the base fucntionality and bootstrap links

            - main/
                - index.html

            - auth/
                - signin.html
                - signup.html

            - user/
                - userpage.html

            - admin/
                - admin_signin.html
                - admin_index.html

        ---

        *MIGRATION DIRECTORY*

        ---

        - migrations/ --> Database migrations directory

            - versions/
                - version1.py
                - version2.py
                - ...
            
            - alembic.ini
            - env.py
            - README
            - script.py.mako

        ---

---