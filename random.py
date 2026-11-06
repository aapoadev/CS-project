# Hogwarts house sorting 
# This program asks the user questions and sorts them into a Hogwarts house

def questions():
    """Asks questions from user and returns answers as a list. The list called answers is useful because I further append to it to basically collect the answers of the user adding up a b c or d 
    """
    answers = [] 

    # Q1
    print("Question 1: What is your favourite quality?", end=" ") #we use the end=" " to make sure next line is not joined with previous 
    print("a) bravery  b) intelligence  c) loyalty  d) ambition")
    answers.append(input("choice: ").lower()) #the reason we edit the list with lower is incase the user puts a capital A for example to answer their choice, this would make sure its lowercase so the program understands its the variable we mean 

    # Q2
    print("Question 2: What is your favorite season?", end=" ")
    print("a) Summer  b) Spring  c) Autumn  d) Winter")
    answers.append(input("Your choice: ").lower())

    # Q3
    print("Question 3: Which place would you want to be in right now?", end=" ")
    print("a) India!  b) France oolala  c) Romaniaaaa  d) My house.")
    answers.append(input("Your choice: ").lower())

    # Q4
    print("Question 4: What would you do in your free time?", end=" ")
    print("a) yoga in the hills  b) read a book by the fireplace  c) party with my friends!  d) sleep.")
    answers.append(input("Your choice: ").lower())

    # Q5
    print("Question 5: Are you a cat or dog person?", end=" ")
    print("a) dog  b) cat  c) dog and cat  d) snake!!! ")
    answers.append(input("Your choice: ").lower())

    return answers #this basically saves the answers for the function and program 


def calculate_scores(answers):
    """ this function calculates the total scores by running the loop for all question instances, and adding a +1 to every alphabet the user picks, the alphabets correspond to a hogwarts house"""
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0

    for answer in answers: 
        if answer == "a": #this for example means if the user chose a in n/5 questions, add +1 to the gryffinfor account
            gryffindor += 1 #the += symbol means to add the mentioned value to the current amount, since everything starts with 0, it adds 1 for every choice in every loop
        elif answer == "b":
            ravenclaw += 1
        elif answer == "c":
            hufflepuff += 1
        elif answer == "d":
            slytherin += 1

    return gryffindor, ravenclaw, hufflepuff, slytherin #this will return the users points for ALL instances, so the program can then choose the highest points instance


def determine_house(scores):
    """this function finds the house with highest score"""
    gryffindor, ravenclaw, hufflepuff, slytherin = scores #we have now stored the new calculated values for all variables 
    max_score = max(scores)

    if gryffindor == max_score:
        return "Gryffindor"
    elif ravenclaw == max_score:
        return "Ravenclaw"
    elif hufflepuff == max_score:
        return "Hufflepuff"
    else:
        return "Slytherin"
#the if else loop is essentially there so program can run EVERY instance, and determine the best fit (the one with highest score)

def main(): #this is essentially the main function, all of the other functions we went through exist in this one. Essentially this is the function that runs the program 
    """Runs the Sorting Hat Quiz program."""
    print("Welcome to rudis sorting hat quiz, please choose any alphabet from a b c or d aligning with your preferance, i hope u are happy with your results!")

    answers = questions()  # Step 1: this part of function gets answers to questions first
    scores = calculate_scores(answers)  # Step 2: this part calculates which account/house/instance has most/max points 
    house = determine_house(scores)  # Step 3: this function determines which one is the highest, and the reasons its in the same function with the step 2 is because it would genuinely overcrowd step2 and create a mess 

    print("\nThe Sorting Hat has decided...") #the \n essentially works the same as end = " " it just makes sure we are starting a new line to have the print function output on 
    print("u are a", house + "!")  #this is the result of the code!!!


main() #we use this to run the whole function 