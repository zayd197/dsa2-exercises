import random

#this function does recursion. It visits i, then call itself for the next index

def visit(instructions, i):
    #base case: if the index is past the end of the list we stop and give back an empty list
    if i >= len(instructions):
        return []

    colour=instructions[i]

    if colour == "green":
        next_index=i+1                          #if green go to the next element

    elif colour == "red":
        next_index=2*i+1                        #if red go to index 2*i + 1

    else:
        #blue: find the next "blue" after this one, then go to the element after it
        next_index=len(instructions)            #if there is no other blue, we will stop
        for j in range(i+1, len(instructions)):
            if instructions[j] == "blue":
                next_index=j+1
                break

    #recursive case: this index, followed by every index visited from the next one
    return [i] + visit(instructions, next_index)

def follow_instructions(instructions: list[str])-> list[int]:  #takes the list and starts recursion at index 0
    return visit(instructions,0)


#first test, answer should be [0,4,5]

list1=["blue","green","red","blue","green","red"]
print("for example, for list",list1)
print("Indexes", follow_instructions(list1),"were visited")
print()

         
list2=["green","red","blue","green","blue","red","green"] #second test, the answer should be [0,1,3,4]
print("for list",list2)
print("Indexes", follow_instructions(list2),"were visited")
print()


list3=["red","green","green","blue","red","green","blue","green","red","blue"]#third test, the answer should be [0,1,2,3,7,8]
print("for list",list3)
print("Indexes", follow_instructions(list3),"were visited")
print()
