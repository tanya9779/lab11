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

if __name__=='__main__':
    Arr=[]
    n=int(input())
    for i in range(n): 
		Arr.append(Point(input()))
    max_d=-1
    max_point=Point(0,0)
    for i in Arr:
        if i.radius()>max_d:
            max_d=i.radius()
            max_point=i
    print(max_point)        


