try:
    # Code that may raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid integer!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result is {result}")
finally:
    print("This runs no matter what")
    