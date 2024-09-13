# This function checks for integer/float and range of selection validation
def input_validation(prompt, max_input, min_input, cast_switch):
    while True:
        selection = input(prompt)

        # Initialize input_number to None
        input_number = None

        # Try converting to float
        try:
            input_number = float(selection)
            # If float switch, input_number should remain float
            if cast_switch == 0:
                # If cast_switch 0 and input_number has no decimal, convert to int
                if input_number.is_integer():
                    input_number = int(input_number)
                else:
                    print("Invalid input. Please input an integer.")
                    continue
        except ValueError:
            print("Invalid input. Please input a valid number.")
            continue  # Restart loop if input is invalid

        # If input is within range or zero, return
        if min_input <= input_number <= max_input or input_number == 0:
            return input_number
        else:
            print("Invalid selection")


# This function is used for all yes and no prompts and returns the selection
def yes_or_no(prompt):
    while True:
        is_yes = input(prompt)

        if is_yes.isdigit():
            is_yes = int(is_yes)
            if is_yes == 1 or is_yes == 2:  # 1 is always Yes and 2 is always No
                return is_yes
            else:
                print("Invalid selection")
        else:
            print("Invalid input. Please input an integer!")
