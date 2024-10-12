f = ""
adventureBranches={}
hintAware=False

#User is prompted to choose between two adventure options
def adventureSelection(userName,points):
    global f
    global hintAware

    print("\nIt's time to see some real-world problem-solving from you, {0}. I'm going to give you a short choose-your-own-adventure hypothetical so you can prove your decision making skills.".format(userName))
    adventureChoice=input("Would you prefer to do the (A)nt hypothetical or the (S)py hypothetical?")
    acceptableChoice=["S","s","A","a"]
    while adventureChoice not in acceptableChoice:
        print("aHEM. It really isn't that difficult.")
        points["geohnHappy"]=points["geohnHappy"]-1
        adventureChoice=input("\n(A)nt (S)py?")
    points["geohnHappy"] = points["geohnHappy"] +1
    if adventureChoice== "A" or adventureChoice=="a":
        f=open("Ant_Adventure.txt")
        if points["geohnHappy"]>1:
            print("\npsst! {0}, since you've got me in a good mood, I'll give you a little warning: beware static electricity.\n Just in case it comes up . \n".format(userName))
            hintAware=True
    elif adventureChoice=="S" or adventureChoice=="s":
        f=open("Spy_Adventure.txt")


#Chosen adventure's corresponding text file is read into a dictionary
def advDictCreation(userName,points):
    global f
    global adventureBranches
    adventureBranches={}
    nextLine=f.readline()
    while nextLine != "":
        lineBits=nextLine.split(":")
        adventureBranches[lineBits[0]]={}
        adventureBranches[lineBits[0]]["text"]=lineBits[1].format(userName)
        if len(lineBits) == 3:
            adventureBranches[lineBits[0]]["pointValue"]=int(lineBits[2])
        nextLine=f.readline()
    return adventureBranches


#user inputs A or B which correlates to a key of the dictionary created above.
#This loops until an end of the story is reached
#adventure point value recorded
def userAdvExperience(userName,points):
    global f
    global adventureBranches
    global hintAware
    abSelect=input("\n\n"+adventureBranches["Start"]["text"])

    while abSelect != "A" and abSelect != "B":

        abSelect=input(" \nUppercase 'A' or 'B'. It really is quite simple. You said you're at a university?")
        points["geohnHappy"]=points["geohnHappy"]-1

    abChain=abSelect
    repeatSelf=""

    while len(adventureBranches[abChain]) ==1:
        abSelect=input("\n\n"+ adventureBranches[abChain]["text".format(userName)])
        while abSelect != "A" and abSelect != "B":
            print("\n{1}Listen, {0} I know you've typed A or B correctly before. I remember everything, I'm a machine, I'm a monster. \nI. \nAM. \nGEOHN.\n".format(userName,repeatSelf))
            abSelect= input("Type A or B.".format(userName,repeatSelf))
            repeatSelf= "I don't like repeating myself. "
            points["geohnHappy"]=points["geohnHappy"]-1
        abChain = abChain + abSelect
    if abChain == "BB":

        if hintAware==True:
            abChain = "BC"

            
    print("\n", adventureBranches[abChain]["text"])
    points["adventure"]=points["adventure"]+adventureBranches[abChain]["pointValue"]
    return points



