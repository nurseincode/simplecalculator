print("Choose an operation:")
print("1 - Add")
print("2 - Substract")
print("3 - Multiply")
print("4 - Divide")
option = int(input("Choose an operation: "))
result = 0

if(option in [1,2,3,4]):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2 
    elif(option == 3):
        result = num1 * num2 
    elif(option == 4):
        result = num1 // num2 

else: 
    print("Invalid operation entered")

print("The result of the operation is {}".format(result))

# while True: 
#     try: 
#         print("==== Simple Calculator ====")
#         print("1 - Add")
#         print("2 - Substract")
#         print("3 - Multiply")
#         print("4 - Divide")
#         print("Q - Quit")

# # Ask the user to choose an operation
# option = int(input("Choose an operation (1-4): ")) # convert to int

# # Initialize result so it always exists
# result = None 

# if option in [1,2,3,4]: 
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     if(option == 1):
#         result = num1 + num2
#     elif(option == 2):
#         result = num1 - num2
#     elif(option == 3):
#         result = num1 * num2
#     elif(option == 4):
#         # Check for division by zero
#         if num2 != 0:
#         result = num1 / num2
#     else:
#         print("Error: Cannot divide by zero.")

# else: 
#     print("Invalid operation entered.")
   
# # Only print the result if a valid calculation was done
# if result is not None: 
# print(f"The result of the operation is {result}")