
import turtle
import random

def cookieGeneration(totalScore):


        if totalScore>= 25:
            cookieColor=("#ECA65B")
            chipColor=("#442200")
        else:
            cookieColor=("#EEEEEE")
            chipColor=("#EEEEEE")
        turtle.color(cookieColor)
        turtle.speed(0)
        turtle.begin_fill()
        turtle.circle(150)
        turtle.end_fill()
        turtle.penup()
        turtle.color(chipColor)
        for chip in range(8):
            chipX=random.randint(-91,91)
            chipY=random.randint(44,227)
            turtle.goto(chipX,chipY)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(random.randint(8,13))
            turtle.end_fill()
            turtle.penup()
        if cookieColor == "#EEEEEE":
            turtle.color("black")
            turtle.goto(-105,120)
            turtle.write("Wow, if only there was a cookie here, but you don't deserve one. \n\nEmbarrassing.")
        turtle.hideturtle()


#adventure score and geohn's happiness score are determined and combined. Dictionaries are created to assign relevant graph parameters
def scoreCalc(points):

    global geohnScore
   
    if points["geohnHappy"] <= -5:
        geohnScore = {"points":-10, "color":"red"}
    elif points["geohnHappy"]  < 0:
        geohnScore = {"points":-5,"color":"red"}
    elif points["geohnHappy"] == 0:
        geohnScore={"points":0,"color":"light green"}
    elif points["geohnHappy"] < 5:
        geohnScore= {"points":5,"color":"light green"}
    else:
        geohnScore = {"points":10,"color":"light green"}
    advPoints=points["adventure"]
    points["adventure"]={"points":advPoints,"color":"green"}
    totalScore = points ["adventure"]["points"] + geohnScore["points"]

    cookieGeneration(totalScore)

    return geohnScore, totalScore

def keyGeneration(x,y):
    def square(color):
        turtle.color(color)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(20)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)
    def label(string):
        turtle.color("black")
        turtle.pendown()
        turtle.write(string+"=")
        turtle.penup()
        turtle.forward(80)
        turtle.left(90)
        turtle.forward(15)
        turtle.right(90)
    turtle.penup()
    turtle.pencolor("black")
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write("Key:")
    turtle.penup()
    turtle.goto(x,y-30)
    label("Adventure Points")
    square("green")
    label("Boost from Geohn's mood")
    turtle.penup()
    turtle.forward(20)
    square("light green")
    label("Penalty from Geohn's mood")
    turtle.penup()
    turtle.forward(30)
    square("red")
            
def barGeneration(barColor,scoreSegment):

    global geohnScore
    barLength = scoreSegment*8
    turtle.pendown()
    turtle.pencolor("black")
    turtle.color(barColor)
    turtle.begin_fill()
    for r in range(2):
        turtle.forward(barLength)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(barLength)

def barLabel(string,x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.color("black")
    turtle.pendown()
    turtle.write(string)
    turtle.penup()


        
    
def graphGeneration(points):

    scoreCalc(points)
    keyGeneration(-210,-40)
    turtle.penup()
    barLabel("your score:",-210,-90)
    turtle.goto(-210,-100)
    barGeneration(points["adventure"]["color"],points["adventure"]["points"])
    global geohnScore
    barGeneration(geohnScore["color"],geohnScore["points"])
    turtle.penup()
    barLabel("minimum score for cookie acquisition:",-210,-140)
    turtle.goto(-210,-150)
    barGeneration("green",25)
    turtle.penup()
    barLabel("max possible score:",-210,-190)
    turtle.goto(-210,-200)
    barGeneration("green",40)
    barGeneration("light green",10)
    
    
    

    
    
    
        

