import numpy as np

class Point:
    
    #constructor
    def __init__(self, *magnitudes):
        self.mags =  magnitudes
        self.ord = len(magnitudes)
        self.eventUIDSet = set()
    
     # overload + operator
    def __add__(self, other): 
        if isinstance(other, Point):
            sum = np.array(self.mags) + np.array(other.mags)
            self.mags = list(sum)
            return  Point(*sum)
        elif isinstance(other, list):
            sum = np.array(self.mags) + np.array(other)
            self.mags = list(sum)
            return Point(*sum)
        elif isinstance(other, (float,int)):
            sum = np.array(self.mags) + other
            self.mags = list(sum)
            return Point(*sum)

    # overload - operator
    def __sub__(self, other): 
        if isinstance(other, Point):
            sum = np.array(self.mags) - np.array(other.mags)
            return  Point(*sum)
        elif isinstance(other, list):
            sum = np.array(self.mags) - np.array(other)
            return Point(*sum)
        elif isinstance(other, (float,int)):
            sum = np.array(self.mags) - other
            return Point(*sum)

    def __len__(self):
        return self.ord
    
    def __iter__(self):
        return iter(self.mags)
    
    #overload == operator
    def __eq__(self, other):
        if isinstance(other, Point) and self.mags == other.mags:
            return True
        return False
    
    def __hash__(self):
        return super().__hash__()
    
    #toString method
    def __str__(self):
        return str(self.mags)
    
    #add uid to event uid set
    def bindEvent(self, uid):
        self.eventUIDSet.add(uid)
    
    #remove uid from set
    def unbindEvent(self, uid):
        self.eventUIDSet.remove(uid)
    
    #get event uids
    def getBindings(self):
        return self.eventUIDSet
    
    #is in box bounds
    def isInBoundingBox(self, min, max):
        for i in range(self.ord):
            if (min[i] > self.mags[i] and max[i] < self.mags[i]): 
                return False
        return True
