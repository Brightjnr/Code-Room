#Bright Okrah Junior
#Assignment 1
#15th July, 2020

import math
#Since we are dealing with math related objects, we import the math module
class Point:
    def __init__(self,x,y):
        self.x=x
        
        self.y=y
        
    def getX(self):
        return self.x
    def getY(self):
        return self.y
#Creating a rectangle class
class Rectangle:
    def __init__(self,topRightCorner, bottomLeftCorner):
#we set the parameters to "self. " to make them accessible
        self.topright = topRightCorner
        self.bottomleft = bottomLeftCorner
        self.width=self.topright.getX()-self.bottomleft.getX()
        self.length=self.topright.getY()-self.bottomleft.getY()
    def gettopright(self):
        return self.topright
    def getbottomleft(self):
        return self.bottomleft
    def getwidth(self):
        return self.width
    def getlength(self):
        return  self.length
    #the perimter of the rectangle
    def perimeter(self):
            return (2 * (self.width)) + (2 * (self.length))
    #The area of the rectangle
    def area(self):
            return ((self.width) * (self.length))
    
def intersection(Rec1, Rec2):
    toprightOfRec1=Rec1.gettopright()
    
    toprightOfRec2=Rec2.gettopright()
    
    bottomleftOfRec1=Rec1.getbottomleft()
    
    bottomleftOfRec2=Rec2.getbottomleft()

    inter1=[False, False, False, False]
    if pointIn(toprightOfRec1,Rec1):
        inter1[0]=True
    elif pointIn(toprightOfRec2,Rec1):
        inter1[1]=True
    elif pointIn(bottomleftOfRec1,Rec1):
        inter1[2]=True
    elif pointIn(bottomleftOfRec2,Rec1):
        inter1[3]=True
    
    inter2=[False, False, False, False]
    if pointIn(toprightOfRec1,Rec2):
        inter1[0]=True
    elif pointIn(toprightOfRec2,Rec2):
        inter1[1]=True
    elif pointIn(bottomleftOfRec1,Rec2):
        inter1[2]=True
    elif pointIn(bottomleftOfRec2,Rec2):
        inter1[3]=True
    elif inter2.count(True)>0 and inter1.count(True)<3:
        return True
    else:
        return False
def pointIn(Point,Rectangle):
    if not (Point.getX()>Rectangle.getbottomleft.getX() and Point.getX()):
        return False
    elif not (Point.getY()>Rectangle.getbottomleft.getY() and Point.getY()):
        return False
    else:
        return True

