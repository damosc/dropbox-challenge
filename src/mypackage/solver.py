'''
Created on 06-04-2012

@author: Damian
'''
from table import Table
from rectangle import Rectangles
import time
from sys import stdin, stderr

if __name__ == '__main__':
    COUNT = stdin.readline()
    try:
        COUNT = int(COUNT)
    except ValueError:
        exit("Wrong format!\n")
    if COUNT < 1 or COUNT > 100:
        exit("Wrong number!\n\Number should be between 1 and 100.\n")
        
    RECTANGLES = Rectangles()
    for i in range(COUNT):
        line = stdin.readline()
        dimensions = line.split(' ')
        if len(dimensions) < 2:
            exit("Wrong parameters\n")
        try:
            width = int(dimensions[0])
            height = int(dimensions[1])
        except ValueError:
            exit("Wrong parameters\n")
        RECTANGLES.insert(width=width, height=height) 
    
    START_TIME = time.time()
    TABLE = Table(rectangles=RECTANGLES)
    stderr.write("Solving...\n")
    TABLE.find_solution()
    END_TIME = time.time()
    stderr.write("Execution time: " + str(END_TIME - START_TIME) + "\n")
