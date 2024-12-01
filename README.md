# QuickStock, Developed in Python

Developed by Students at University of Colorado, Colorado Springs.

Overview of Software: 

  A local inventory management system to be used by small businesses as an alternative to paid management systems used by large corporations. 

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

    
  Test Cases:

      There are 4 test cases that are available to run:
      
        1. test_login.py
        
          This test checks the correct behavior of login validation, password visibility toggling, and security question handling. It ensures that login success              and failure trigger appropriate responses, and that the password field's visibility can be toggled on or off. Additionally, the tests validate the                  handling of a security question, including the display of the hint and the validation of the answer. Mock objects, like QMessageBox, are used to                    simulate user interactions and prevent actual pop-ups during testing
          
        2. test_inventory.py
        
          This test focuses on key operations such as adding and removing table rows, saving data with validation, searching and filtering items, and enabling row            editing. The test ensures that new rows are correctly added to the table and that rows can be removed as expected. It also checks the valid_save function           to verify that items are properly validated for unique names and valid entries before saving. Additionally, the tests confirm that searching                        functionality filters the table correctly, and that specific rows can be made editable with a distinct visual cue (blue background). The test also checks           if the table's layout responds correctly to window resizing. Mock objects, like MagicMock, are used to simulate external interactions, preventing                   reliance on the actual UI and allowing for controlled testing of the internal logic.
          
        3. test_sales.py

          This test ensures that the core features of setting up date ranges, managing checkboxes for item selection, and updating sales data work as expected. For           the SalesPeriodWidget, the test verifies the correct initialization and functionality of date pickers, ensuring that a 10-day period is set by default              and that the selected dates can be correctly retrieved. For the SalesScreen, the test focuses on interactions with checkboxes representing different                sales items. It ensures that checkboxes are properly created, added to the UI, and their states can be accessed and manipulated. Additionally, the tests            verify that methods for updating sales data and pie chart information are called correctly, with appropriate arguments passed. Mocking techniques are               used to prevent actual database calls and simulate the behavior of external dependencies, allowing for a more controlled testing of internal logic. The             test also includes checks for UI elements like checkboxes and verifies that actions like updating sales and pie chart data trigger the expected functions.
        
        4. test_settings.py

        This test verifies the functionality of the SettingsWidget in the settings screen. It checks the initialization of the widget, ensuring that UI elements            like the reset button and username/password/security fields are correctly displayed and functional. The test ensures proper handling of empty or mismatched         username inputs, with appropriate error messages shown via QMessageBox. The visibility of password fields is also tested, confirming that toggling the              checkbox correctly changes the display mode. Additionally, it tests resetting the credentials to default, updating the security question, and the behavior          of the home button. Mocking is used to simulate user interactions and avoid actual UI popups.

      Run them in an ide (like PyCharm) to see how they work
