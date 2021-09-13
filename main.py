import pygame, sys, random, time
import array
from pygame.locals import *

grid = (200, 200)
size = 5
ruleset = (1,1,0,1,1,1,1,0)
startpoint = 100

def cellstart(cells):
    for x in range(0, grid[0]):
        for y in range(0, grid[1]):
            cells[x][y] = 0

    cells[0][startpoint] = 1
    return cells

def display(cells, screen):
    pygame.display.set_caption('Celluar Automaton by Colton')
    
    for i in range(grid[0]):
        for j in range(grid[1]):
            if cells[j][i] == 0:
                pygame.draw.rect(screen, (255,255,255), (i*size,j*size,size,size), 0)
            if cells[j][i] == 1:
                pygame.draw.rect(screen, (0,0,0), (i*size,j*size,size,size), 0)
    pygame.display.update()

def mainloop(screen, clock, cells):
    cycle = 0
    max = grid[0]
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#this checks to see of the user closes the window
                pygame.quit()
                sys.exit()
        
        #time.sleep(0.1)
        tempcells = nextcycle(cells, cycle)
        
        for i in range(0, grid[0]):
            cells[cycle+1][i] = tempcells[i]


        display(cells, screen)

        
        if cycle == max-2: 
            cycle = 0
        cycle += 1



def nextcycle(cells, cycle):
    
    newcells = [0 for y in range(grid[0])]

    for j in range(grid[0]):
            newcells[j] = 0
    
    for i in range(1, grid[0] - 1):
        left = 0
        mid = 0
        right = 0


        left = cells[cycle][i-1]
        mid = cells[cycle][i]
        right = cells[cycle][i+1]
        newcells[i] = rules(left, mid, right)
        
    
    return newcells
        

def rules(left, mid, right):#this checks the inputed rules and give a 1 or a 0

    

    if (left == 1 and mid == 1 and right == 1): 
        
        return ruleset[0]
    elif (left == 1 and mid == 1 and right == 0): 
        
        return ruleset[1]
    elif (left == 1 and mid == 0 and right == 1):
        
        return ruleset[2]
    elif (left == 1 and mid == 0 and right == 0):
        
        return ruleset[3]
    elif (left == 0 and mid == 1 and right == 1):
        
        return ruleset[4]
    elif (left == 0 and mid == 1 and right == 0):
        #print("hello")
        return ruleset[5]
    elif (left == 0 and mid == 0 and right == 1):
        #print("hello2")      
        return ruleset[6]
    elif (left == 0 and mid == 0 and right == 0):
        #print("hello3")
        
        return ruleset[7]
    return 0





def main():
    print("Welcome to Colton's Cellular Automata")



    pygame.init()
    screen = pygame.display.set_mode((grid[0]*size, grid[1]*size))
    screen.fill(pygame.Color("white"))
    clock = pygame.time.Clock    
    cells = [[0 for y in range(grid[1])] for x in range(grid[0])]
    cells = cellstart(cells)
    mainloop(screen, clock, cells)
    
main()
