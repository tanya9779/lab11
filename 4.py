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
    def __itruediv__(self,other) :
        self.x/=other.x
        self.y/=other.y
        return self
    def __sub__(self,other):
        return Point(self.x-other.x, self.y-other.y)
if __name__=='__main__':
    Arr=[]
    n=int(input())
    for i in range(n): 
		Arr.append(Point(input()))

    max_P=0
    for i in range(n-2):
        for j in range (i+1,n-1):
            for k in range (j+1,n):
                tmp=(Arr[i]-Arr[j]).radius()+(Arr[j]-Arr[k].radius()+(Arr[i]-Arr[k]).radius()
                if tmp > max_P:
					
                    max_P=tmp
                    
    print(max_P)


