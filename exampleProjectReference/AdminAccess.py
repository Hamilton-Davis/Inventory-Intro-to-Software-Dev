import AdditionalFunctionSportTickets
import CalculationForTickets
import AdditionalAdminFunctions

# Submenu for seating editing
submenu_functions_seats = {
    1: AdditionalAdminFunctions.add_seats,
    2: AdditionalAdminFunctions.delete_seats,
    3: AdditionalAdminFunctions.rename_seats
}  # End of submenu_functions_seats dictionary

# Submenu for package editing
submenu_functions_packages = {
    1: AdditionalAdminFunctions.add_package,
    2: AdditionalAdminFunctions.delete_package,
    3: AdditionalAdminFunctions.rename_package
}  # End of submenu_functions_packages dictionary

# Submenu for package editing
submenu_functions_team_names = {
    1: AdditionalAdminFunctions.add_team,
    2: AdditionalAdminFunctions.remove_team,
    3: AdditionalAdminFunctions.rename_team
}  # End of submenu_functions_packages dictionary


# This function will check if user is allowed access to admin profile
def admin_access(password):
    i = 0

    # While you have 3 tries, enter the password
    while i <= 2:
        entered_password = input("Please enter the password: ")
        # If password is correct, move on
        if password == entered_password:
            return 1
        # If password is wrong, increment attempt counter
        else:
            print("Password is incorrect!")
            i += 1


# This function will display the admin menu and take selected option from menu and return
def menu(admin_menu):
    while True:
        print("\nWelcome, Admin!")
        for position, index in enumerate(range(len(admin_menu))):  # Displays menu options
            print("(%d) %s" % ((position + 1), admin_menu[index]))

        # Take in valid menu selection
        valid_menu_selection = AdditionalFunctionSportTickets.input_validation("What would you like to do?: ",
                                                                               len(admin_menu), 1, 0)

        # Return valid selection
        if valid_menu_selection is not None:
            return valid_menu_selection


# This function will find the teams with a sale and edit their prices
def sales_event(teams_info, package_deals):
    while True:
        print("\nWelcome to Sales Event Editor!")
        for index, team_names in enumerate(teams_info.keys()):  # Displays teams
            print("(%d) %s" % ((index + 1), team_names))

        # Checks for valid input
        valid_team_selection = AdditionalFunctionSportTickets.input_validation("Which team has a sale going on or 0 "
                                                                               "to go back to the main menu?: ",
                                                                               len(teams_info), 1, 0)

        # Once input is valid, ask for sales percentage
        if valid_team_selection is not None:

            if valid_team_selection == 0:
                break

            # Calculates percentage for sales
            sales_percentage = CalculationForTickets.percentage_valid("How much are the "
                                                                      "tickets off today? (Enter an integer of 1-99): ")

            team_name = list(teams_info.keys())[valid_team_selection - 1]  # Retrieves team name
            prices = teams_info[team_name]["Prices"]  # Retrieves price list
            seats = teams_info[team_name]["Seats"]  # Retrieves seat list
            # Loops through, calculates price
            updated_prices = [round(price - (price * sales_percentage), 2) for price in prices]
            teams_info[team_name]["Prices"] = updated_prices  # Updates prices in team dictionary
            teams_info[team_name]["Percentage"] = sales_percentage  # Updates the dictionary with the sales percentage
            # Will need to figure out how to round here *********
            print("\nThe %s got a sale of %.0f%% off tickets: " % (team_name, (sales_percentage * 100)))
            print("******************************************")
            # Loop through the seating's and new prices offered for selected team
            for position, index in enumerate(range(len(seats))):
                print("\t(%d) %s -> $%.2f" % ((position + 1), seats[index], updated_prices[index]))
            print("******************************************")
            print("Prices have been updated successfully...\n")

            # Leave to menu if answering No
            leave = AdditionalFunctionSportTickets.yes_or_no("Any more sales? \n(1) Yes \n(2) No\n")
            if leave == 2:
                break


# This function will grab the percentage going to charity
def charity_event(teams_info, package_deals):
    while True:
        print("\nWelcome to Charity Event Editor!")
        for index, team_names in enumerate(teams_info.keys()):  # Displays teams
            print("(%d) %s" % ((index + 1), team_names))

        # Checks for valid input
        valid_team_selection = AdditionalFunctionSportTickets.input_validation("Which team has a charity going on or "
                                                                               "0 to go back to the main menu?: ",
                                                                               len(teams_info), 1, 0)

        # Once input is valid, ask for charity percentage
        if valid_team_selection is not None:

            if valid_team_selection == 0:
                break

            # Calculates percentage for charity
            charity_percentage = CalculationForTickets.percentage_valid("What percentage of the tickets are going to "
                                                                        "charity today? (Enter an integer of 1-99): ")

            team_name = list(teams_info.keys())[valid_team_selection - 1]  # Retrieves team name
            teams_info[team_name]["Charity"] = charity_percentage  # Updates the dictionary with the charity percentage

            print("\nCharity event has been successfully added to the " + team_name)
            print("The customer's total sale will have %.0f%% go to charity\n" % (charity_percentage * 100))

            # Leave to menu if answering No
            leave = AdditionalFunctionSportTickets.yes_or_no("Any more charity events? \n(1) Yes \n(2) No\n")
            if leave == 2:
                break


# This function will edit team names whether it's to add, delete, or rename
def team_editor(teams_info, package_deals):
    while True:
        print("\nWelcome to the Team Name Editor!")
        submenu_selection = AdditionalFunctionSportTickets.input_validation("(1) Add a Team\n(2) Delete a Team\n(3) "
                                                                            "Rename a Team\nWhat would you like to "
                                                                            "do or 0 to go back?: ", 3, 1, 0)
        if submenu_selection is not None:
            if submenu_selection == 0:
                break

            # Grab selected function and store it
            selected_option = submenu_functions_team_names.get(submenu_selection)

            change_occurred = selected_option(teams_info)

            if change_occurred == 1:
                exit_to_menu = AdditionalFunctionSportTickets.yes_or_no("\nAre you done with team name "
                                                                        "settings?\n(1) Yes \n(2) No\n")
                # If admin is done, return to menu
                if int(exit_to_menu) == 1:
                    break


# This function will change the seat names (rename)
def seating_name_change(teams_info, package_deals):
    change_occurred = 0
    while True:
        print("\nWelcome to the Seat Name Editor!")
        print("Here's the list of teams:")
        # Lists sport teams
        for index, team_names in enumerate(teams_info.keys()):
            print("(%d) %s" % ((index + 1), team_names))

        # Check for valid input by admin
        team_index = AdditionalFunctionSportTickets.input_validation("Which team needs a seat edit or 0 to go back to"
                                                                     " the main menu?: ", len(teams_info), 1, 0)

        if team_index is not None:
            if team_index == 0:
                break

            # Convert dictionary keys into list, stores it
            selected_team_name = list(teams_info.keys())[team_index - 1]
            team_details = teams_info[selected_team_name]  # Retrieves appropriate seats and prices and store it
            seats = team_details["Seats"]  # Pulls seats of selected sports team, stores it
            prices = team_details["Prices"]

            while True:
                print("\nHere are the seat editing options for the %s:" % selected_team_name)
                submenu_selection = AdditionalFunctionSportTickets.input_validation("(1) Add a Seat\n(2) Delete a "
                                                                                    "Seat\n(3) Rename a Seat\n"
                                                                                    "What would you like to do or 0 "
                                                                                    "to go back?: ",
                                                                                    3, 1, 0)
                if submenu_selection is not None:
                    if submenu_selection == 0:
                        break

                    # Grab selected function and store it
                    selected_option = submenu_functions_seats.get(submenu_selection)

                    change_occurred = selected_option(selected_team_name, seats, prices, 1)

                    if change_occurred == 1:
                        exit_to_menu = AdditionalFunctionSportTickets.yes_or_no("\nWould you like to modify more "
                                                                                "seats? \n(1) Yes \n(2) No\n")
                        # If admin is done, return to menu
                        if int(exit_to_menu) == 2:
                            return
                        else:
                            break


# This function will let admin change specific seating prices
def change_seating_prices(teams_info, package_deals):
    seat_selected = 0  # Initializing (needed to use outside of loop as well)
    while True:
        print("\nWelcome to Seating Price Editor!")
        # Lists sport teams
        for index, team_names in enumerate(teams_info.keys()):
            print("(%d) %s" % ((index + 1), team_names))

        # Check for valid input by admin
        team_index = AdditionalFunctionSportTickets.input_validation("Which team needs seat price change or 0 to go "
                                                                     "back to the main menu?: ", len(teams_info), 1,
                                                                     0)

        if team_index is not None:
            if team_index == 0:
                break

            selected_team_name = list(teams_info.keys())[team_index - 1]  # Convert dictionary keys into list, stores it
            team_details = teams_info[selected_team_name]  # Retrieves appropriate seats and prices and stores it
            seats = team_details["Seats"]  # Pulls seats of selected sports team, stores it
            prices = team_details["Prices"]  # Retrieves price list

            while True:
                print("\nHere is the list of seats for the %s:" % selected_team_name)
                # Lists selected sports teams seating and prices
                for index, seat_names in enumerate(seats):
                    print("(%d) %s -> $%.2f" % ((index + 1), seat_names, prices[index]))

                # Check for valid input by admin
                seat_index = AdditionalFunctionSportTickets.input_validation("Which seat will need a price change or "
                                                                             "0 to go back?: ", len(seats), 1, 0)

                # If valid, move to price change process
                if seat_index is not None:
                    if seat_index == 0:
                        break

                    is_price_changed = AdditionalAdminFunctions.seating_price_change_update(seats, seat_index, prices,
                                                                                            teams_info,
                                                                                            selected_team_name)
                    # If price was updated, break
                    if is_price_changed == 1:
                        break

        # If user updated a price, ask if they want to modify more
        if seat_selected != "0":
            # Check for if admin wants to modify more
            exit_to_menu = AdditionalFunctionSportTickets.yes_or_no("\nWould you like to modify another "
                                                                    "seating price? \n(1) Yes \n(2) No\n")
            # If admin is done, return to menu
            if int(exit_to_menu) == 2:
                break


# This function will change the package deals (add)
def change_package_deals(teams_info, package_deals):
    while True:
        print("\nWelcome to Package Deals Editor!")

        submenu_selection = AdditionalFunctionSportTickets.input_validation("(1) Add a Package\n(2) Delete a Package"
                                                                            "\n(3) Rename a Package\nWhat would you "
                                                                            "like to do or 0 to go back to the main "
                                                                            "menu?: ", len(package_deals) - 1, 1, 0)

        if submenu_selection is not None:
            if submenu_selection == 0:
                break

            selected_option = submenu_functions_packages.get(submenu_selection)

            change_occurred = selected_option(package_deals)

            if change_occurred == 1:
                exit_to_menu = AdditionalFunctionSportTickets.yes_or_no("\nWould you like to edit any more in the "
                                                                        "package setting? \n(1) Yes \n(2) No\n")
                # If admin is done, return to menu
                if exit_to_menu == 2:
                    return


# This function allows admin to see everything in the system for sports teams, seating, and pricing
def view_teams_info(teams_info, package_deals):
    print("\nHere's the list of the current teams seating and pricing:")
    for team_name, team_details in teams_info.items():  # Loops through teams
        print(team_name)
        seats = team_details["Seats"]  # Pulls seats of selected sports team, stores it
        prices = team_details["Prices"]  # Retrieves price list
        for index, seat_names in enumerate(seats):  # Loops through selected sports teams seating and prices
            print("\t(%d) %s -> $%.2f" % ((index + 1), seat_names, prices[index]))
