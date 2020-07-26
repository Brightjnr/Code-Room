'''
Bright Okrah Junior
Assignment 2
23rd July, 2020
'''

import random
import array

class Deque:
    Maxx=0
    length=array.array('i',[0])
    

    def __init__(self,arraylength):
        self.Maxx= arraylength
        self.length=array.array('i',[0]*Maxx)
        self.begin=0
        self.end=0
        self.size=0
    def __len__(self):
        return(self.length)
    def getLength(self):
        return(self.size)
    def isEmpty(self):
        return(self.begin)==0
    def isFull(self):
        return(self.size)==self.Maxx
    def addToFront(self,y):
        number=int(y)
        if self.isFull()==True:
            print('array is already full')
            return False
        elif self.isEmpty():
            self.length[self.begin]=number
            self.end=self.end + 1
            self.size=self.size +1
            print('add to front')
            return True
        self._begin -= 1 % self.Maxx
        self.length[self._begin] = number
        self.size += 1
        print("Added to front")
        return True
    
    def addToBack(self,y):
        number=int(y)
        if self.isFull()==True:
            print('array is already full')
            return False
        elif self.isEmpty():
            self.addToFront(y)
            self.size=self.size +1
            
            return True
        self.length[self.end]=number
        self.end=self.end %self.Maxx
        self.size=self.size+1
        print('add to back')
        return True
    def removeFromFront(self):
        if self.isEmpty():
            print("empty")
            return
        self.length[self.begin] = 0
        self.begin += 1 % self.Maxx
        self.size -= 1
        print(" removed")
        return
    def removeFromBack(self):
        if slef.isEmpty():
            print('Empty')
            return
        self.end=(self.end-1)%self.Maxx
        self.length[self.end]=0
        self.size=self.size-1
        print("removed From Back")
        return
def attempt1(deque):
    de = False
    while de == False:
        num = random.random()
        val = random.randrange(1, 101)
        if numb <= 0.1:
            if deque.isFull():
                de = True
            deque.addToFront(val)
        elif 0.1 < numb <= 0.3:
            if deque.isEmpty():
                de = True
            deque.removeFromFront()
        elif 0.3 < numb <= 0.4:
            if deque.isFull():
                de = True
            deque.addToBack(val)
        else:
            if deque.isEmpty():
                checker = True
            deque.removeFromBack()


     
        
        
