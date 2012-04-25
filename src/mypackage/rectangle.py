'''
Created on 06-04-2012

@author: Damian
'''

class Rectangle(object):
    '''
    Represents rectangle 
    '''

    def __init__(self, width, height):
        '''
        Constructor.
        
        Must take width and height of a rectangle.
        '''
        self._width = width
        self._height = height
               
    def flip(self):
        '''
        Flips rectangle.
        '''
        tmp = self._height
        self._height = self._width
        self._width = tmp
        
    def get_height(self):
        '''
        Returns a height of a rectangle
        '''
        return self._height
    
    def get_width(self):
        '''
        Returns a width of a rectangle
        '''
        return self._width
    
class Rectangles(object):
    '''
    Represents a list of rectangles
    '''
    
    def __init__(self):
        '''
        Constructs empty list of the rectangles.
        '''
        self._max_width = 0
        self._max_height = 0
        self._heights_sum = 0
        self._widths_sum = 0
        self._areas_sum = 0
        self.list = []
    
    def insert(self, width, height):
        '''
        Inserts new rectangle into a list.
        '''    
        #we don't want to have height bigger whan width
        if height > width:
            tmp = width
            width = height
            height = tmp
                
        if not self.list:
            #list is empty
            self._max_width = width
            self._max_height = height
            self._widths_sum = width
            self._heights_sum = height
            self._areas_sum = width * height
        else:
            #there is something in the list
            if width > self._max_width:
                self._max_width = width
            if height > self._max_height:
                self._max_height = height
            self._widths_sum += width
            self._heights_sum += height
            self._areas_sum += width * height
        
        rectangle = Rectangle(width=width, height=height)    
        self.list.append(rectangle)
                
    def sort(self):
        '''
        Sorts rectangles according to width.
        '''
        self.list.sort(key=lambda rectangle: rectangle.get_width(), reverse=True)
        
    def get_max_width(self):
        '''
        Returns maximum width of a rectangle.
        '''            
        #return max(self.list, key=lambda rectangle: rectangle.width).width
        return self._max_width
    
    def get_max_height(self):
        '''
        Returns maximum width of a rectangle.
        '''
        #return max(self.list, key=lambda rectangle: rectangle.height).height
        return self._max_height
    
    def get_heights_sum(self):
        '''
        Returns sum of heights of all rectangles
        '''
        #=======================================================================
        # sumOfHeights = 0
        # for rectangle in self.list:
        #    sumOfHeights += rectangle.height
        # return sumOfHeights
        #=======================================================================
        return self._heights_sum
    
    def get_widths_sum(self):
        '''
        Returns sum of widths of all rectangles
        '''
        #=======================================================================
        # sumOfWidths = 0
        # for rectangle in self.list:
        #    sumOfWidths += rectangle.width
        # return sumOfWidths
        #=======================================================================
        return self._widths_sum  
          
    def get_areas_sum(self):
        '''
        Returns sum of areas of all rectangles.
        '''
        #=======================================================================
        # sumOfAreas = 0
        # for rectangle in self.list:
        #    sumOfAreas += rectangle.height * rectangle.width
        # return sumOfAreas
        #=======================================================================
        return self._areas_sum
