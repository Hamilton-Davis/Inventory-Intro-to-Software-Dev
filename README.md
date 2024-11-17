# Inventory Software, Developed in Python

Developed by Students at University of Colorado, Colorado Springs.

Overview of Software, 

  A local inventory managment system to be used by small buisnesses as an alternative to payed managment systems used by large corperations. 

  Features:

    Inventory

      Add/Edit/Remove Stock
      Search for items
      Sort inventory by category

    Login

        Default login: user: admin;  password: password
        Logout from Home menu
        Update username/password
        Reset login to defaults

  To Install Dependencies:
    
    pip install PySide6
    pip install openpyxl
    pip install cryptography
    pip install pandas

  To Run:
    
    Compile and run main.py from [project root]/Inventory/main.py
    To generate test data, compile and run dballocation.py from [project root]/Inventory/main.py
        - Note that running this file more than once will create duplicate items in each genrated table

    Executable file to come with final version
