September 2021 
Final version - includes tests

Requirements.txt is updated in Aug 2022

Includes all tests (unittest, pytest, selenium)

------------------------
## Running the application
-----------------------

### To run this example:
- Start the application with the following command:
```
Windows:    set FLASK_DEBUG=1 && python -m flask run
Mac/Linux:   export FLASK_DEBUG=1 && python -m flask run
```

### To run the tests:
- run the tests for Model (unittest)
    ``` 
    python -m unittest -v tests\test_models.py 
    ```
- run the tests for routes (pytest)
    ```
    python -m pytest -v tests\test_routes.py
    ```
- run the 