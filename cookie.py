import turtle
import random
import introPieces
import adventurePieces
import turtlePieces


points={}
points["geohnHappy"]=0
points["adventure"]=0


introPieces.geohnIntroducesSelf()

userName=introPieces.nameAcquisition(points)

introPieces.pronounAcquisition(userName)

introPieces.cookieFrolickMonologue(userName)



adventurePieces.adventureSelection(userName,points)

adventurePieces.advDictCreation(userName,points)

adventurePieces.userAdvExperience(userName,points)

cookieStart = input ("To see your results, type 'R'")
while cookieStart != "R":
    cookieStart = input ("Come on, you're basically done. To see your results, type 'R'")

turtlePieces.graphGeneration(points)


        

     

    
