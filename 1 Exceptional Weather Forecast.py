# Task 1

while True:
    user_input = input("Please enter the temerature in degrees Fahrenheit: ")

    try:
        temp = float(user_input)
        break
    except ValueError:
        print(f"{user_input} is not a valid temperature.  Please try again.")

# Task 2

def temp_conversion(temp):

    try:
        converted_temp = (temp - 32) * 5/9
    except Exception as e:
        print(f"Error: {e}")

# Task 3

    else:
        print(f"Your temperature in Celsius is {converted_temp}.")
    finally:
        print("Thank you for using the weather forecast app.")

temp_conversion(temp)