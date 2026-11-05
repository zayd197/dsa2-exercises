import random

#this function does recursion. It visits i, then call itself for the next index

def visit(instructions, i):
    #base case: the index is past the end of the list, so we stop
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
