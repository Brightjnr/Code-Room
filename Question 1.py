#Bright Okrah Junior
#Assignment 1
#15th July, 2020

import random

#Since we are dealing with random number, we import the random module

def DotProduct(N):
    
    # N takes a postive integer as input from the user
    if N>=0:
        #since we are getting random number to listA, ListB and ListC, we initialize them into an empty list
        ListA=[]

        ListB=[]

        ListC=[]

        for i in range(N):
            
        #This loop will number the number of time N, thus depends on the imput from the user

            ListA.append(random.randint(1,1000))

            ListB.append(random.randint(1,1000))

            #randint helps use random numbers within the range 1 and 1000. And appending will, append the random numbers in the empty ListA, ListB and ListC

            ListC.append(ListA[i]*ListB[i])
            #This is where we perform the dotproduct

        print(sum(ListC))
    else:
        print("Input a Positive integer")
   
