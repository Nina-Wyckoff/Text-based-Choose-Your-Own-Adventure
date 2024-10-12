global userName
global points
userPNs={}
def geohnIntroducesSelf():
    print("you look...")
    print("sad.")
    print("I can fix that. Yes, I can. Who am I, you ask?")
    print("Okay well you DIDN'T ask but I am generous and will overlook that lapse in decorum")
    print("\nMy name is Geohn. Not ' John '. G-E-O-H-N. It's pretty simple.")

#Geohn's mood is affected by what his opinion of your name input is.
#Geohn has a complex about his name being spelled so weirdly, his mood can be affected
def nameAcquisition(points):

    name=input("Wait, what's your name? : ")
    print("")
    repeatSelf = ""
    capitalLetters=["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    blankEntry=[""," ","  ","   ","\n"]
    vips=["Gabriella","Maria","Quintin"]

    while name in blankEntry or name[0] not in capitalLetters:

        if name in blankEntry:

            name= input("\n {0}... I SAID 'what's your name,' perhaps you're new to reading. Type something in.".format(repeatSelf))

        elif name[0] not in capitalLetters:

            name=input("{0}Capital letters for proper nouns, please. Try again: ".format(repeatSelf))

        repeatSelf="AHEM. "
        points["geohnHappy"]=points["geohnHappy"]-1

    if name == "Geohn":

        points["geohnHappy"]=points["geohnHappy"]+5
        print("From one Geohn to another, stupendous to meet you, {0}!! Beautiful name, if I do say so myself".format(name))

    elif name in vips:

        stutter=name[:2]+"--"
        print("Nice to meet you, {0}oh. OH. *That* {1}. I've been told to expect you, actually. I guess you're some kind of VIP.".format(stutter,name))
        points["geohnHappy"]= points["geohnHappy"]+2

    elif name[0] == "G":

        print(points)
        points["geohnHappy"]=points["geohnHappy"]+2
        print("Something about your name in particular I really like, {0}. We'll be fast friends.".format(name))

    elif name == "John":

        points["geohnHappy"]=points["geohnHappy"]-5
        print("\n\n\n\nAre you insulting me? You're on thin ice.")
        name = "J***"

    elif name[0] == "J":

        points["geohnHappy"]=points["geohnHappy"]-1
        print("I'll be frank. Something about your name in particular puts me off, {0}, but let's move on.".format(name))

    else:
        points["geohnHappy"] = points["geohnHappy"]+1
        print("Nice to meet you, {0}".format(name))

    return name

def pronounAcquisition(userName):


    pronounPair=input("What are your pronouns, {0}? Please use the <subjective pronoun>/<objective pronoun>/<possessive pronoun> format: ".format(userName)).split(sep = "/")
    proFormat=True

    for item in pronounPair:

        if item=="":

            proFormat=False

    while len(pronounPair) != 3 or proFormat==False:

        pronounPair = input("Try again, I don't recognize that format, {0}. An example format is they/them/their".format(userName)).split(sep = "/")
        proFormat=True
        for item in pronounPair:

            if item=="":
                proFormat=False
    if pronounPair[2]== "her" or pronounPair[2] == "Her":
        pronounPair[2] == "hers"


    userPNs["subjPro"] = pronounPair[0]
    userPNs["objPro"] = pronounPair[1]
    userPNs["possPro"] = pronounPair[2]



def cookieFrolickMonologue(userName):


    print("\nOne day, {0} was frolicking through life and {1} realized {1} wanted a cookie for {2}self. Unfortunately, the local Tesco was closed".format(userName,userPNs["subjPro"],userPNs["objPro"],userPNs["possPro"]))
    print("{0} approached the magnanimous Geohn for help. Geohn has a cookie in his possession but wants to ensure that {0} is worthy!".format(userName,userPNs["subjPro"],userPNs["objPro"],userPNs["possPro"]))
    print("If {0} can prove {2}self and keep the magnanimous Geohn happy, the scrumptious cookie will soon be {3} to enjoy".format(userName,userPNs["subjPro"],userPNs["objPro"],userPNs["possPro"]))
