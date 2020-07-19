#Intro: this code is designed to display the word count of a book
##Date: 09/11/17
###Author: Manasi Mehta
counter = 0
def Main():
    global counter
    counter +=1
    canContinue = True
    while (canContinue == True):
        print ("A: count words ")
        print ("B: display file ")
        print ("C: display file in reverse")
        print ("D: quit")
        print ("Choose: A,B,C or D")
        userOption = input ("?")
        if (userOption.upper() == "A"):
            countWords()
        elif (userOption.upper() == "B"):
            newFile()
        elif (userOption.upper() == "C"):
            fileReverse()
        elif (userOption.upper() == "D"):
            canContinue = False
        else:
            print ("I do not understand " + userOption)
    print ("Goodbye!")

    counter -= 1
    
def newFile():
    print ("I am in display file")
    if(finish()== True):
        print ("What story do you want to read?")
        print ("A: Great Expectations")
        print ("B: A Christmas Carol")
        print ("Would you like to: ")
        story = input ("?")
        if story.upper() == ("A"):
            File = open("great expectations.txt","r")
            words = File.read()
            myLines = words.splitlines()
            for linecount in range (len(myLines)):
                print (myLines[linecount])
                    
        elif story.upper() == ("B"):
            File = open("a christmas carol.txt","r")
            words = File.read()
            myLines = words.splitlines()
            for linecount in range (len(myLines)):
                print (myLines[linecount])
        else:
            print ("I do not understand " + story)
        
def countWords():
    print ("I am in count words")
    if(finish()== True):
        print ("Would you like to count a specific word?")
        print ("Yes or No")
        userInput = input ("?")       
        if (userInput.lower()== "yes"):
            print ("What story do you want to read?")
            print ("A: Great Expectations")
            print ("B: A Christmas Carol")
            print ("Would you like to: ")
            story = input ("?")
                
            if story.upper() == ("A"):
                File = open("great expectations.txt","r")
                words = File.read()
                print ("What is the word you want to find?")
                userWord = input ("?")
                specificWord = words.count(userWord)
                if (specificWord == 1):
                    print ("There is " + str(specificWord) + " " + (userWord) + " in the whole text")
                else:
                    print("There are " + str(specificWord) + " " + (userWord) + "'s in the whole text")
                    
            elif story.upper() == ("B"):
                File = open("a christmas carol.txt","r")
                words = File.read()
                print ("What is the word you want to find?")
                userWord = input ("?")
                specificWord = words.count(userWord)
                if (specificWord == 1):
                    print ("There is " + str(specificWord) + " " + (userWord) + " in the whole text")
                else:
                    print("There are " + str(specificWord) + " " + (userWord) + "'s in the whole text")
            else:
                print ("I do not understand " + story)
            
        elif (userInput.lower()== "no"):
            print ("What story do you want to read?")
            print ("A: Great Expectations")
            print ("B: A Christmas Carol")
            print ("Would you like to: ")
            story = input ("?")
                
            if story.upper() == ("A"):
                File = open("great expectations.txt","r")
                words = File.read()
                print("There are " + str(len(words.split(" "))) + " words")
                    
            elif story.upper() == ("B"):
                File = open("a christmas carol.txt","r")
                words = File.read()
                print("There are " + str(len(words.split(" "))) + " words")
            else:
                print ("I do not understand " + story)
        else:
            print ("I do not understand " + userInput)
        
def fileReverse():
    print ("I am in display reverse")
    if(finish()== True):
        print ("What story do you want to read?")
        print ("A: Great Expectations")
        print ("B: A Christmas Carol")
        print ("Would you like to: ")
        story = input ("?")
            
        if story.upper() == ("A"):
            print ("please wait for it to load..")
            File = open("great expectations.txt","r")
            words = File.read()
            print (words[::-1])
                
        elif story.upper() == ("B"):
            print ("please wait for it to load..")
            File = open("a christmas carol.txt","r")
            words = File.read()
            print (words[::-1])
                
        else:
            print ("I do not understand " + story)
    
def finish():
    canContinue = True
    while (canContinue == True):
        print ("If you want to exit please type exit if not type no")
        answer = input ("?")
        if answer.lower() == ("exit"):
            return False
        elif answer.lower() == ("no"):
            print ("ok")
            return True
        else:
            print ("I do not understand " + answer)
######################################################
Main()

