# Ask for 3 numbers and print the average.
#use this :
#number1 , number2 , number3 = map(float, input("Entrer 3 numbers seperated by comma: ").split(","))
#or use :
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
number3 = float(input("Enter another number: "))


average = (number1 + number2 + number3) / 3
print("The average is: ", round(average , 2))
# or
print(f"The average is: {average:0.2f}")