#Magic methods: __getitem__, __setitem__, __delitem__
#used for indexing: w/o it couldn't be possible to get 
#particular value of Vector: v=Vector(1,2,2),e.g. v[1] 

class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)
    
    #v[item]
    def __getitem__(self, item):
        if 1<=item<len(self.values):
            return self.values[item-1]
        else:
            raise IndexError('Index is out of collection')

    def __setitem__(self, key, value):
        if 1<=key<len(self.values):
            self.values[key] = value
        elif key>len(self.values):
            diff = key - len(self.values)
            self.values.extend([0]*diff)
            self.values[key-1] = value
        else:
            raise IndexError('Index is out of collection')

    def __delitem__(self,key):
        if 1<=key<len(self.values):
            del self.values[key]
        else:
            raise IndexError('Index is out of collection')
#Task
class Building:

    def __init__(self, floor):
        self.companies = [None] * floor

    def __getitem__(self,floor):
        return self.companies[floor]

    def __setitem__(self,key,name):
        self.companies[key] = name
        
    def __delitem__(self,floor):
        del self.companies[floor]
