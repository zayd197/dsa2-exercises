import matplotlib.pyplot as plt
import random

WALL = 1
PATH = 0
SIZE = 21 #maze is 21 by 21

image=plt.imread("maze(1).png") #reading the maze image

square_size=len(image) // SIZE

#turning the maze into a grid of 1s and 0s
maze=[]

for row in range(SIZE):
    maze_row=[]
    for col in range(SIZE):   #finding the middle pixel
        y=row*square_size+square_size // 2
        x=col*square_size+square_size // 2
        pixel = image[y][x]

        if len(image.shape) ==3: #dividingpixle into light and dark
            brightness=pixel[0]
        else:
            brightness=pixel

        if brightness<0.5:
            maze_row.append(WALL)
        else:
            maze_row.append(PATH)

    maze.append(maze_row)

#drawing the maze in the terminal

for row in range(SIZE):
    line = ""
    for col in range(SIZE):
        if maze[row][col]==WALL:
            line=line+"##"
        else:
            line=line+"  "
    print(line)

#finding the entrance and exit of the maze. They will be the path squares on the outside edge of the maze.
openings=[]
for row in range(SIZE):
    for col in range(SIZE):
        if row == 0 or col == 0 or row == SIZE -1 or col == SIZE -1:
            if maze[row][col] == PATH:
                openings.append((row,col))
print("Entry/Exit has been found at (row,column):",openings)

#Now we are going to ask the user which approach he will use

approach=""

while approach != "backtracking" and approach !="las vegas":
    print("Which approach do you want to use? backtracking or las vegas?")
    approach=input("Your choice:")

    if approach != "backtracking" and approach != "las vegas":
        print("Please choose backtracking or las vegas")



#las vegas approach

def las_vegas(maze, start, end):
    row=start[0]
    col=start[1]
    previous=None #the square we just came from
    visited=[(row,col)]  #this is every square we have stepped on in order
    steps=0

    while steps<200:        #making a list of squares we are allowed to move to
        possible_moves=[]

        if row-1>=0 and maze[row-1][col] == PATH:   #up
            possible_moves.append((row-1, col))

        if row + 1 < SIZE and maze[row + 1][col] == PATH:  #down
            possible_moves.append((row + 1, col))

        if col - 1 >= 0 and maze[row][col - 1] == PATH:     #left
            possible_moves.append((row, col - 1))

        if col + 1 < SIZE and maze[row][col + 1] == PATH:  #right
            possible_moves.append((row, col + 1))

        if len(possible_moves)>1 and previous in possible_moves: #this says dont go straight back unless it is the only way
            possible_moves.remove(previous)

        next_square=random.choice(possible_moves) #picking a random move from the allowed list possible_moves
        previous=(row,col)
        row=next_square[0]
        col=next_square[1]
        visited.append((row,col))
        steps=steps+1

        if (row,col)==end:  #have we found the exit?
            return True, visited

    return False,visited  #200 steps used without finding the exit

start=openings[0] #entrance at the top
end=openings[1]  #exit at the bottom

if approach == "backtracking":
    print("backtracking it is!")
else:
    print("las vegas it is!")
    success, visited = las_vegas(maze, start, end)
    if success:
        print("Success! Found the exit in", len(visited) - 1, "steps.")
    else:
        print("Failed: no exit found after 200 steps.")
    print("Number of squares visited:", len(visited))

    successes=0 #test the algorithm to see how many successes in 1000 runs
    for i in range(1000):
        success, visited = las_vegas(maze, start, end)
        if success:
            successes=successes+1
    print("We have had", successes, "successes out of 1000")

