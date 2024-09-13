import AdditionalFunctionSportTickets


# This function is used to select teams for purchasing tickets
def select_team(teams_list, packages):
    # While user is selecting, loop through teams
    while True:
        # Lists all Colorado teams in array
        print("Check out our outstanding Colorado teams below!")
        # Loops through list of teams to present to customer (Use enumerate for listing index)
        for index, team_names in enumerate(teams_list.keys()):
            print("(%d) %s" % ((index + 1), team_names))

        # Looks for customers selection and returns when matched
        team_number = AdditionalFunctionSportTickets.input_validation("\nWhich sports team are we looking to purchase"
                                                                      " tickets from? (Enter the number or 0 to exit)"
                                                                      ": ", len(teams_list), 1, 0)

        # If valid selection, return number
        if team_number is not None:
            if team_number == 0:  # Exit to main screen if 0
                return 0, 0, 0, 0, 0, 0

            package_number, seat_selected = seat_selection(team_number, teams_list, packages)  # Move to next step

            if package_number != 0:
                # Converts dictionary keys into a list, stores it
                selected_team = list(teams_list.keys())[team_number - 1]
                team_details = teams_list[selected_team]  # Retrieves appropriate seats and prices and stores it
                seat_section = team_details["Seats"][seat_selected - 1]  # Retrieves seat section based on seat selected
                seat_price = team_details["Prices"][seat_selected - 1]  # Retrieves seat price based on selected seat
                total_price = seat_price * package_number  # Calculates the total
                package_selected = packages[package_number - 1]

                return selected_team, seat_section, total_price, package_selected, package_number, team_details


# This function is used to display all the team information and prompt for seat selection
def seat_selection(team_index, teams_data_info, packages):
    while True:
        selected_team = list(teams_data_info.keys())[team_index - 1]  # Converts dictionary keys into a list, stores it
        team_details = teams_data_info[selected_team]  # Retrieves appropriate seats and prices and stores it
        print("\nWelcome to the %s ticket service!\n" % selected_team)

        # Pull the respected seats and prices and stores them
        seats = team_details["Seats"]
        prices = team_details["Prices"]

        # If there is a sale going on, let customer know
        if "Percentage" in team_details:
            sales_percentage = team_details["Percentage"]
            print("All tickets are %.0f%% off today\n" % (sales_percentage * 100))
        # If there is a charity going on, let customers know
        if "Charity" in team_details:
            charity_percentage = team_details["Charity"]
            print("We will be giving %.0f%% of your purchase to charity today!\n" % (charity_percentage * 100))

        # Loop through the seating's and prices offered for selected team
        for position, index in enumerate(range(len(seats))):
            print("(%d) %s -> $%.2f" % ((position + 1), seats[index], prices[index]))

        seat_number = AdditionalFunctionSportTickets.input_validation("\nWhich seat level would you like to purchase?"
                                                                      " (Enter the number or 0 to go back): ",
                                                                      len(seats), 1, 0)

        # If valid selection, return number
        if seat_number is not None:
            if seat_number == 0:  # Go back
                return 0, seat_number

            package_number_return = ticket_quantity(packages)  # Move to next step

            # Returns information
            if package_number_return != 0:
                return package_number_return, seat_number


# This function grabs the package deal selected by user and returns to main
def ticket_quantity(package_deals):
    while True:
        print("\nBelow is our package deals!")
        for position, index in enumerate(range(len(package_deals))):
            print("(%d) %s" % ((position + 1), package_deals[index]))

        package_number = AdditionalFunctionSportTickets.input_validation("Which package deal would you like to "
                                                                         "purchase? (Enter the number or 0 to go back"
                                                                         "): ", len(package_deals), 1, 0)
        # Determines to go back a step or return information
        if package_number is not None:
            if package_number == 0:
                return 0
            else:
                return package_number
