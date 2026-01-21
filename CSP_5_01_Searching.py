import random
def randomSearch(items:list, target) -> int:
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value
    tries=0
    for i in range(len(items)-1):
        index=random.randint(0,len(items)-1)
        tries+=1
        if items[index]==target:
            print(tries)
            return(index)
        

def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.
    for i in range(len(items)):
        if items[i]==target:
            return (i, i+1)
        else:
            continue
    return(-1, i+1)



def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
    checks=0
    left=0
    right=len(items)-1
    while left <=right:
        checks+=1
        mid=((left+right)//2)
        if items[mid]==target:
            return(mid,checks)
        elif items[mid]<target:
            left=mid +1
        else:
            right=mid-1
    return(-1, checks)
print(binarySearch([1,3,5,7,9],1))