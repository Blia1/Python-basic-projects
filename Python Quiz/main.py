#Python quiz app

print("Welcome to python quiz game :)")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay let's play!")

answer = input("How old is creator of this app? ")
if answer == '15':
    print("Correct!")
else: 
    print("incorrect!")

answer = input("Who won Didgori war in 1121? ")
if answer == "Georgia":
    print("Correct!")
else: 
    print("incorrect!")


answer = input("What is creator's favorite music genre? ")
if answer == "Jazz":
    print("Correct!")
else: 
    print("incorrect!")

answer = input("Simplify 20 ")
if answer == '10+10' or '19+1' or '11+9' or '15+5':
    print("Correct!")
else: 
    print("incorrect!")