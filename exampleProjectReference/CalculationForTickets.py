import AdditionalFunctionSportTickets


# This function will take payments from the customer to purchase tickets
def ticket_payment(total):

    # While user inputs info, loop through
    while True:
        print("\nYour total will be ${:.2f}".format(total))

        payment_code = input("Please enter your zip code to pay or 0 to cancel transaction: ")

        if payment_code.isdigit():
            if int(payment_code) == 0:
                print("\n***Transaction Cancelled***")
                return None
            elif len(str(payment_code)) == 5:
                return payment_code
            else:
                print("Invalid Input")
        else:
            print("Input must be a number!")


# This function will see if the user would like their receipt or not!
def take_receipt(team, seat, total, package, package_number, keys):

    print("\nThank you for your purchase!")
    receipt = AdditionalFunctionSportTickets.yes_or_no("Would you like your receipt? \n(1) Yes \n(2) No\n")

    # If user wants receipt, print it
    if receipt == 1:
        print("\nReceipt"
              "\n\tTeam: " + team +
              "\n\tSeats: " + seat +
              "\n\tPackage: " + package +
              "\n\tTotal: ${:.2f}".format(total))
        if "Percentage" in keys:
            sales_percentage = keys["Percentage"]  # Calls for percentage in dictionary, stores it
            reversed_amount = (total / package_number) / (1 - sales_percentage)  # Reverses back to original price
            saved_amount = (reversed_amount * package_number) - total  # Calculates amount saved
            print("\tYou saved: ${:.2f}".format(saved_amount))
        # If the admin added a charity event, let customer how much will be donated
        if "Charity" in keys:
            charity_total = total * keys["Charity"]
            print("\tAmount Going to Charity: ${:.2f}".format(charity_total))

    print("\nEnjoy the game!")


# This function checks for appropriate input for percentages
def percentage_valid(prompt):
    while True:
        sales_percentage = input(prompt)

        if sales_percentage.isdigit():
            sales_percentage = float(sales_percentage) / 100
            if 0.01 <= sales_percentage <= 0.99:
                return sales_percentage
            else:
                print("Input is out of range!")
        else:
            print("Input is not an integer!")
