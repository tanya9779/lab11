import math
class Point:
    def __init__(self,x='0',y='0'):
        if isinstance(x,str):
            self.x,self.y=list(map(float,x.split(',')))
        else:
             self.x=x
             self.y=y
        
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)
    def __lt__(self, other):
        return self.x < other.x or self.x==other.x and self.y<other.y
if __name__=='__main__':
    a=Point('5,4')
    b=Point(1.5,1.6)
    print(a+b)
