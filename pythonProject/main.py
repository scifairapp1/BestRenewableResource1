opr = input(" enter the operation . for example ADD,SUBTRACT,MULTIPLY,DIVIDE")
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
if opr == "ADD":
    result = (num1 + num2)
if opr == "SUBTRACT":
    result = (num1 - num2)
if opr == "MULTIPLY":
    result = (num1 * num2)
if opr == "DIVIDE":
    result = (num1 / num2)
print("butt is :"+str(result))


