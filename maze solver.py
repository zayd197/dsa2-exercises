import matplotlib.pyplot as plt

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
