'''
Created on 06-04-2012

@author: Damian
'''
from sys import stdout, stderr

class Table(object):
    '''
    Class representing a table.
    
    We can try to put rectangles on a table.
    '''

    def __init__(self, rectangles):
        '''
        Constructor
        ''' 
        self.rectangles = rectangles
        #we want to have rectangles sorted
        self.rectangles.sort()
        self.height = self.rectangles.get_heights_sum()
        self.width = self.rectangles.get_max_width()
        self.cells = []
        self.clean()        
        self._min_width = self._min_height = 0
        
    def find_solution(self):
        '''
        Tries to find best location for all rectangles.
        '''
        rectangles_count = len(self.rectangles.list)
        for index, rectangle in enumerate(self.rectangles.list):
            self._min_width, self._min_height = self.get_min_dimensions()
            if self.put(rectangle) == -1: 
                exit("Some strange error occured!\n\
                It should not happen.\nQuit!\n")                
            stderr.write(str((index + 1) * 100 / rectangles_count) + "%\n")
        else:
            #if we are able to place all rectangles 
            #on a table:
            self.show()
            min_width, min_height = self.get_min_dimensions()
            #print best solution
            stdout.write(str(min_width * min_height) + "\n")
            stderr.write("Sum of areas: " \
                         + str(self.rectangles.get_areas_sum()) + \
                         "\n(" + str(min_width) + "," + str(min_height) + ")\n")
                         
    def put(self, rectangle):
        '''
        Tries to put a rectangle inside the table.
        
        If it is possible it places it and returns 0.
        If it is not possible it just returns -1.
        '''
        #we iterate through all cells to find right place for a rectangle
        for i in range(self.height):
            for j in range(self.width):
                #this 'if' is used only to improve execution time
                if self.cells[i][j] == " ":
                    #we must check all cells "under" rectangle
                    if not self.check(i, j, rectangle):
                        #free place found
                        return 0
        else:
            #impossible to place a rectangle on a table
            return -1
                    
    def check(self, i, j, rectangle):
        '''
        Checks if it is possible to place rectangle in a table.
        '''
        #we must check first if it's possible to place a rectangle
        #in vertical, like this |
        #in this case we limit allowed table size to current "border"
        #of ENCLOSING "rectangle"
        #if it fails, then we try to place a rectangle in horizontal,
        #like this -
        #in this case we limit area to all available cells in a table
        for max_dimensions in [[self._min_height, self._min_width], \
                               [self.height, self.width]]:            
            #we must flip a rectangle to allow for horizontal and vertical tries
            rectangle.flip()
            #if rectangle is inside current "border", we can proceed
            if i + rectangle.get_height() <= max_dimensions[0] \
            and j + rectangle.get_width() <= max_dimensions[1]:
                possible = True
                for a in range(i, i + rectangle.get_height()):
                    for b in range(j, j + rectangle.get_width()):
                        if self.cells[a][b] != " ":
                            #cell already taken by other rectangle
                            #we cannot place our rectangle here
                            possible = False
                if possible:
                    self.place(i, j, rectangle) 
                    return 0
        return -1
            
    def place(self, i, j, rectangle):
        '''
        Stores rectangle inside the table
        
        We assume, that we've found proper location for a rectangle.
        '''
        for a in range(i, i + rectangle.get_height()):
            for b in range(j, j + rectangle.get_width()):
                if a == i or a == i + rectangle.get_height() - 1:
                    if b == j or b == j + rectangle.get_width() - 1:
                        self.cells[a][b] = "+"
                    else:
                        self.cells[a][b] = "-"
                elif b == j or b == j + rectangle.get_width() - 1:
                    self.cells[a][b] = "|"
                else:
                    self.cells[a][b] = "x" 
                                        
    def show(self):
        '''
        Prints cells' values into stderr.
        '''
        min_width, min_height = self.get_min_dimensions()
        for i in range(min_height):
            for j in range(min_width):
                stderr.write(self.cells[i][j])
            stderr.write("\n")
              
    def get_min_dimensions(self):
        '''
        Returns minimal dimensions of a table, which encloses all rectangles
        '''
        min_width = 0
        min_height = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i][j] != " ":
                    if i > min_height:
                        min_height = i
                    if j > min_width:
                        min_width = j
        return min_width + 1, min_height + 1                   
                
    def clean(self):
        '''
        Cleans the table.
        '''
        self.cells = [[' ' for i in range(self.width)] for j in range(self.height)] 
        
