'''
Bright Okrah Junior
Assignment 2
23rd July, 2020
Source: Gisele
'''
import random
import time
def interpolation(Arr, target):
    lowest=0
    highest=(len(Arr)-1)
    get=False
    dif=highest-lowest
    startTime= time.time()
    middle=0
    while middle<highest:
        if highest<lowest:
            if Arr[lowest]==target:
                get==True
            get==True
            endTime=time.time()
            return(endTime-startTime)
        middle=  lowest + (((highest - lowest)  // (Arr[highest] - Arr[lowest])) * (target - Arr[lowest]))
        if Arr[middle] == target:  
            found = True
        else:
            if target<Arr[middle]:
                hoghest=middle-1
            else:
                lowest=middle+1
    return (endTime-startTime)


def BS (sequence,item):
    begin_index=0
    end_index=len(sequence)-1
    while begin_index<=end_index:
        midpoint=begin_index+(end_index-begin_index)//2
        midpoint_value=sequence[midpoint]
        if midpoint_value==item:
            return midpoint
        elif item<midpoint_value:
            end_index=midpoint-1
        else:
            begin_index=midpoint+1
    return None

            
Intervall=[]
for i in range(5):
    Time=time.time()
    List = random.sample(range(1,32767),100)
    NList=sorted(List)
    print(NList)
    Inputt= int(input("Input number: "))
    print(BS(NList,Inputt))
    endTime= time.time()
    Interval=(endTime-Time)*1000
    Intervall.append(Interval)
print (sum(Intervall)//5)





Intervall=[]
for i in range(5):
    Time=time.time()
    List = random.sample(range(1,32767),1000)
    NList=sorted(List)
    print(NList)
    Inputt= int(input("enter number: "))
    print(interpolation(Nlist,1000,Inputt))
    endTime= time.time()
    Interval=(endTime-Time)*1000
    Intervall.append(Interval)
print (sum(Intervall)//5)











Intervall=[]
for i in range(5):
    Time=time.time()
    List = random.sample(range(1,32767),5000)
    NList=sorted(List)
    print(NList)
    Inputt= int(input("input number: "))
    print(interpolation(NList,5000,Inputt))
    endTime= time.time()
    Interval=(endTime-startTime)*1000
    Intervall.append(Interval)
print (sum(Intervall)//5)      

    

