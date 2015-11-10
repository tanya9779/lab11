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
    def __lt__(self, other):
        return self.x < other.x or self.x==other.x and self.y<other.y
    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)
    def radius(self):
        return math.sqrt(self.x**2+self.y**2)
    def radius(self):
        return math.sqrt(self.x**2+self.y**2)
    def __iadd__(self,other):
        self.x+=other.x
        self.y+=other.y
        return self
    def __itruediv__(self,other):
        self.x/=other.x
        self.y/=other.y
        return self
if __name__=='__main__':
    Arr=[]
    n=int(input())
    for i in range(n): 
		Arr.append(Point(input()))

    sum=0
    center_point=Point(0,0)
    for i in Arr:
        center_point+=i
    center_point/=Point(n,n)
    print(center_point)
