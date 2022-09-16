print("Hello There! How can i help you?\n")

while True:
        operation = int(input("Select the operation you want to execute: \n[1] Sum\n[2] Subtract\n[3] Multiply\n[4] Divide\n: "))
        if operation in (1, 2, 3, 4):

            x = float(input("Enter the first value: "))
            y = float(input("Enter the second value: "))

            def sum(x,y):
                return x + y

            def subtract(x,y):
                 return x - y
                
            def multiply(x,y):
                return x * y
                    
            def divide(x,y):
                return x / y
                
            if operation == 1:
                print(x, "+", y, "=", sum(x,y))
            elif operation == 2:
                print(x, "-", y, "=", subtract(x,y))
            elif operation == 3:
                print(x, "*", y, "=", multiply(x,y))
            elif operation == 4:
                print(x, "/", y, "=", divide(x,y))

            again = input("Another operation? (yes/no): ")
            if again == "no":
                break
        else:
            print("Invalid input!")                     
