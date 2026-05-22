# Ask for 3 numbers and print their product.


#use this :
#number1 , number2 , number3 = map(float, input("Entrer 3 numbers seperated by comma: ").split(","))
#or use :
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
number3 = float(input("Enter another number: "))

multiplication = number1 * number2 * number3
print(f"The multiplication of {number1} and {number2} and {number3} is {multiplication:0.2f}")