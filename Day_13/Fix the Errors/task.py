while True:
    try:
        age = int(input("How old are you? "))
        break  # exit the loop if conversion is successful
    except ValueError:
        print("You have entered an invalid number. Please try a numerical number.")


if age >= 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You can not drive at age {age}.")
