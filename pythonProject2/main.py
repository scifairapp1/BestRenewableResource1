print("welcome to my bestie test. are you excited?")
answer = input("enter your answer . for example YUP,NOPE")
if answer == "YUP":
    print("yay! me too!")
if answer == "NOPE":
    print("Aw man! that is impossible")
print("When did I get my vaccine first dose?")
answer = input("enter your answer . for example AUGUST 28,AUGUST 27, AUGUST 29, AUGUST 26")
if answer == "AUGUST 28":
    print('whoops! you are incorrect!')
if answer == "AUGUST 29":
    print('whoops! you are incorrect!')
if answer == "AUGUST 26":
    print('whoops! you are incorrect!')
if answer == "AUGUST 27":
    print('yay! you got it right!')
print("Which ice cream flavor do I prefer? Chocolate brownie or butterscotch?")
answer = input("enter your answer . for example CHOCOLATE BROWNIE,BUTTERSCOTCH")
if answer == "CHOCOLATE BROWNIE":
    print('whoohoo! you got it right!')
if answer == "BUTTERSCOTCH":
    print("both are soo good! this is a tricky one")
    print("my final answer is....")
    answer = input("choose 1 . for example CONTINUE THE SUSPENSE,HURRY UP ALREADY!")
    if answer == "CONTINUE THE SUSPENSE":
        print("Whoohoo!")
    if answer == "HURRY UP ALREADY!":
        print("okay okay, don't be a bossy butt!")
print("the answer is BOTH! HA GOTCHA!!")
print("the next question is...")
print("What is my favorite place to travel to?")
answer = input("enter your answer . for example CHINA,SWITZERLAND,MEXICO")
if answer == "CHINA":
    print("WRONG YOU BUTT!")
if answer == "SWITZERLAND":
    print("YOU GOT THAT RIGHT AT LEAST")
if answer == "MEXICO":
    print("WRONG YOU BUTT!")
print('tally up your score and multiply by 33.333333333. If you got the ice cream one wrong, minus 16 points')
print('i can make this easier for you by coding a calculator')
opr = input(" enter the operation . for example SUBTRACT,MULTIPLY")
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))
if opr == "SUBTRACT":
    result = (num1 - num2)
if opr == "MULTIPLY":
    result = (num1 * num2)
print("result is :"+str(result))
opr = input(" enter the operation . for example SUBTRACT,MULTIPLY")
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
if opr == "SUBTRACT":
    result = (num1 - num2)
if opr == "MULTIPLY":
    result = (num1 * num2)
print("result is :"+str(result))