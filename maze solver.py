import matplotlib.pyplot as plt

WALL = 1
PATH = 0
SIZE = 21 #maze is 21 by 21

image=plt.imread("maze(1).png") #reading the maze image

square_size=len(image) // SIZE

print(WALL)

