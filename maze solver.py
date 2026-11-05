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


#backtracking approach

def backtracking(maze, start, end):
    path=[start]        #the route we are on right now (works like a stack)
    visited=[start]     #every square we have ever stepped on

    while len(path) > 0:
        row=path[-1][0]     #the last square in the path is where we are now
        col=path[-1][1]

        if (row,col) == end:    #have we found the exit?
            return True, visited

        moved=False

        if moved == False and row+1 < SIZE and maze[row+1][col] == PATH and (row+1,col) not in visited:  #going down
            path.append((row+1,col))
            visited.append((row+1,col))
            moved=True
       
        if moved == False and col+1 < SIZE and maze[row][col+1] == PATH and (row,col+1) not in visited: #going right
            path.append((row,col+1))
            visited.append((row,col+1))
            moved=True
     
        if moved == False and col-1 >= 0 and maze[row][col-1] == PATH and (row,col-1) not in visited: #going left
            path.append((row,col-1))
            visited.append((row,col-1))
            moved=True
       
        if moved == False and row-1 >= 0 and maze[row-1][col] == PATH and (row-1,col) not in visited: #going up
            path.append((row-1,col))
            visited.append((row-1,col))
            moved=True

        #dead end: no new square to move to, so go back one square
        if moved == False:
            path.pop()

    return False, visited   #path is empty: we went all the way back to the start

#drawing the maze with the visited squares coloured in

def show_visited(maze, visited, start, end, title):
    picture=[]
    for row in range(SIZE):
        picture_row=[]
        for col in range(SIZE):
            if (row,col) == start:
                picture_row.append([0, 0.8, 0])     #green = entrance
            elif (row,col) == end:
                picture_row.append([1, 0, 0])       #red = exit
            elif (row,col) in visited:
                picture_row.append([1, 0.8, 0])     #yellow = visited
            elif maze[row][col] == WALL:
                picture_row.append([0, 0, 0])       #black = wall
            else:
                picture_row.append([1, 1, 1])       #white = not visited
        picture.append(picture_row)

    plt.imshow(picture)
    plt.title(title)
    plt.savefig("visited.png")   #saves a copy of the picture for the report
    plt.show()


#running the approach the user chose

start=openings[0]   #entrance at the top
end=openings[1]     #exit at the bottom

if approach == "backtracking":
    print("backtracking it is!")
    success, visited = backtracking(maze, start, end)
    if success:
        print("We made it out!")
        show_visited(maze, visited, start, end, "Backtracking: exit found")
    else:
        print("We got lost.")
        show_visited(maze, visited, start, end, "Backtracking: no route found")
    print("We visited", len(visited),"squares")

else:
    print("las vegas it is!")
    success, visited = las_vegas(maze, start, end)
    if success:
        print("We made it out!", len(visited) - 1, "steps.")
        show_visited(maze, visited, start, end, "Las Vegas: exit found")
    else:
        print("We got lost after 200 steps")
        show_visited(maze, visited, start, end, "Las Vegas: failed after 200 steps")
    print("We visited", len(visited), "square")


#success rate of each approach after 10000 runs

RUNS=10000
las_vegas_successes=0
backtracking_successes=0

print()
print("Running each approach", RUNS, "times, please wait...")

for i in range(RUNS):
    success, visited = las_vegas(maze, start, end)
    if success:
        las_vegas_successes=las_vegas_successes+1

    success, visited = backtracking(maze, start, end)
    if success:
        backtracking_successes=backtracking_successes+1

las_vegas_rate=las_vegas_successes/RUNS*100
backtracking_rate=backtracking_successes/RUNS*100

print("Las Vegas has", las_vegas_successes, "successes out of", RUNS, "=", round(las_vegas_rate, 2), "%")
print("Backtracking has", backtracking_successes, "successes out of", RUNS, "=", round(backtracking_rate, 2), "%")


