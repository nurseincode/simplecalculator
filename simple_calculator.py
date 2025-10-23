
while True: # Start an infinite loop so the calculator keeps running until user chooses to quit
    try: # try/except block catches invalid input and prevents program crashes
        print("==== Simple Calculator ====")
        print("1 - Add")
        print("2 - Substract")
        print("3 - Multiply")
        print("4 - Divide")
        print("Q - Quit")

# Get the user's choice, 
        option = input("Choose an operation (1-4 Q to quit: ").strip() # strip method to remove whitespace to avoid accidental input issues

# If the user chooses to quit, exit the loop
        if option.upper() == 'Q':
            print("Exiting calculator. Goodbye!")
            break # Stop the while loop

        option = int(option) # Convert the option to an integer(only if not quitting)

        result = None

        if option in [1, 2, 3, 4]: # Check if the user chose a valid operation
            num1 = float(input("Enter first number: ")) # Use float() so it works with decimals
            num2 = float(input("Enter second number: "))

 # Perform the chosen operation
            if option == 1:
                result = num1 + num2
            elif option == 2:
                result = num1 - num2 
            elif option == 3:
                result = num1 * num2 
            elif option == 4:
                # Check for division by zero
                if num2 != 0:
                    result = num1 / num2 # Uses true division for accurate results
                else: 
                    print("Error: Cannot divide by zero.")



        else: 
            print("Invalid operation entered") # The user entered something other than 1-4

 # Only print the result if a valid operation was performed

        if result is not None:
            print(f"The result of the operation is: {result}")

# Handle non-numeric input errors gracefully

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        
        # Intitial code
# print("Choose an operation:")
# print("1 - Add")
# print("2 - Substract")
# print("3 - Multiply")
# print("4 - Divide")
# option = int(input("Choose an operation: "))
# result = 0

# if(option in [1,2,3,4]):
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     if(option == 1):
#         result = num1 + num2
#     elif(option == 2):
#         result = num1 - num2 
#     elif(option == 3):
#         result = num1 * num2 
#     elif(option == 4):
#         result = num1 // num2 

# else: 
#     print("Invalid operation entered")

# print("The result of the operation is {}".format(result))

