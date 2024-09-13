import AdminAccess
import CustomerAccess
import CalculationForTickets
import AdditionalFunctionSportTickets

# Start of teams dictionary
teams_data = {

    # Keys
    "Denver Broncos": {
        # Nested Keys
        "Seats": ["Home Side", "Visitor Side", "Southside Field Goal", "Northside Field Goal"],
        "Prices": [200.00, 100.00, 50.00, 50.00]
    },  # End of Denver Broncos

    "Denver Nuggets": {
        "Seats": ["Court side", "Mid Seats", "Upper Seats"],
        "Prices": [150.00, 100.00, 50.00]
    },  # End of Denver Nuggets

    "Colorado Avalanches": {
        "Seats": ["Glass Seating", "Suite/Club", "Corners of Rink", "Nose Bleeds Seating"],
        "Prices": [200.00, 150.00, 100.00, 50.00]
    },  # End of Colorado Avalanches

    "Colorado Rapids": {
        "Seats": ["Center field Team Side", "Center field Non-Team Side", "Goal side", "Standing"],
        "Prices": [80.00, 50.00, 30.00, 10.00]
    },  # End of Colorado Rapids

    "Colorado Rockies": {
        "Seats": ["Infield", "Rooftop", "Outfield", "Pavilion"],
        "Prices": [110.00, 80.00, 50.00, 20.00]
    },  # End of Colorado Rockies

    "Colorado Mammoths": {
        "Seats": ["Lower Level", "Suite/Club", "Nosebleeds", "Standing"],
        "Prices": [45.00, 35.00, 20.00, 10.00]
    },  # End of Colorado Mammoths

    "Colorado Switchbacks": {
        "Seats": ["Center Field Team Side", "Center field Non-Team Side", "Goal side", "Standing"],
        "Prices": [30.00, 25.00, 15.00, 5.00]
    }  # End of Colorado Switchbacks

}  # End of teams_data dictionary

# Start of menu_functions
# This dictionary will allow for functions to be called based on user selection (simplified if/elif/else)
menu_functions = {
    1: AdminAccess.sales_event,
    2: AdminAccess.charity_event,
    3: AdminAccess.team_editor,
    4: AdminAccess.seating_name_change,
    5: AdminAccess.change_seating_prices,
    6: AdminAccess.change_package_deals,
    7: AdminAccess.view_teams_info
}  # End of menu_functions dictionary

seat_packages = ["Single Ticket", "Double Ticket", "Triple Ticket", "Quadruple Ticket"]
admin_options = ["Add Sales Event", "Add Charity Event", "Edit Team Names", "Edit Seating Names", "Edit Seating Prices",
                 "Edit Package Deals", "View Teams Info", "Exit"]
password = "7215"

# Loops until admin/customer wants to leave
while True:
    print("Welcome to Colorado sports ticket service!")
    customer_read = AdditionalFunctionSportTickets.yes_or_no("Are you a customer? \n(1) Yes \n(2) No\n")

    # If customer, go to purchase tickets for team
    if int(customer_read) == 1:
        print("")
        team_selected, seat_selected, total_price, package_selected, package_number, team_keys = \
            CustomerAccess.select_team(teams_data, seat_packages)

        # Goes to Customer file
        if team_selected != 0 and seat_selected != 0 and total_price != 0 and package_selected != 0 and \
                package_number != 0 and team_keys != 0:
            is_paid = CalculationForTickets.ticket_payment(total_price)

            if is_paid is not None:
                CalculationForTickets.take_receipt(team_selected, seat_selected, total_price, package_selected,
                                                   package_number, team_keys)

    # If admin, go to admin to update information
    elif int(customer_read) == 2:
        print("")
        gained_access = AdminAccess.admin_access(password)  # Goes to Admin file

        # If password is successful, go to admin menu
        if gained_access == 1:
            while True:
                menu_selection = AdminAccess.menu(admin_options)

                # If the last option is picked (always exit), then leave admin section
                if menu_selection == len(admin_options):
                    break

                # Grab selected function and store it
                selected_option = menu_functions.get(menu_selection)
                # Find menu option and go to function
                if selected_option:
                    selected_option(teams_data, seat_packages)
        else:
            print("You have entered the password incorrectly too many times. Goodbye >:(")
            break

    # Checks to see if program ends
    escape = AdditionalFunctionSportTickets.yes_or_no("\nAre we ready to logout? \n(1) Yes \n(2) No\n")
    print("")
    # If yes is selected, exit program
    if escape == 1:
        break
