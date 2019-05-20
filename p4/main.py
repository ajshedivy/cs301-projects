# project: p4
# submitter-netid: awelper
# partner-netid: ajshedivy

correct=0
count=0
tries=input("How many tries do you want for each question: ")
tries=int(tries)
def askQuestion(question, answer, hint):
    global correct
    global count
    count=count+1
    w = tries
    while w>0:
        print(question)
        x=input("Your answer: ")
        x=str(x)
        if x.lower().strip()==answer:
            correct+=1
            return print("Congratulations! You got it right.")
        elif w==2:
            print("You have this many remaining tries: " + str(w))
            print(hint)
            w-=1
        elif w==1:
            w-=1
            return print("You answered "+print(str(x))+" The correct answer is "+print(str(answer)))
        else:
            w-=1
            print("You have this many remaining tries: " + str(w))
        

askQuestion("What is the type of the following? \"1.0\" + \"2.0\" \n a) int \n b) float \n c) str \n d) bool \n e) NoneType \n ", "c", hint="Check the textbook")

askQuestion("What is the type of the following? \"1\" * 2 \n ", "str", hint="notice the quotes!")

askQuestion("What does this expression evaluate to? \n True != (3 < 2) \n ", "true", hint="Calcuate the right side first. Don't forget != means not equal to.")

        
print("You tried "+str(count)+" questions and got "+str(correct)+" right.")
