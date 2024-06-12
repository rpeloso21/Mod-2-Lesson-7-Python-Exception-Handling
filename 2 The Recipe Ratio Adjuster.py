# Task 1
message1 = "Please enter the original number of servicngs for the recipe.  Please use whole numbers: "
message2 = "How many servings do you wish to make today?  Please enter in whole numbers: "

def input_serving(message):
    while True:
        serving = input(message)

        try:
            num_serving = float(serving)
            if num_serving <= 0:
                raise ValueError
        except ValueError:
            print("Error: That is not a valid serving size.  Please try again.")
            continue
        else:
            return num_serving



while True:
    num_original_serving = input_serving(message1)
    num_current_serving = input_serving(message2)

    # Task 2
    try:
        adjustment_factor = num_current_serving/num_original_serving
        # Task 3
        print(f"For this serving size, please multiply all ingredients by {adjustment_factor}.")
    except ZeroDivisionError:
        print("Error: cannot divide by 0.  Please enter different serving sizes.")
        continue
    finally:
        print("Thank you for using our converter.  Enjoy your cooking!")
        break
    