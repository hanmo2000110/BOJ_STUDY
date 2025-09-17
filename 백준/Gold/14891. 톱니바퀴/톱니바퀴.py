

class Gear :
    def __init__(self,gear, idx):
        self.gear = gear
        self.idx = idx

    def turn(self,dir, gears, check) :
        check[self.idx] = False
            
        if self.idx > 0 and check[self.idx - 1] and self.getLeft() != gears[self.idx-1].getRight() :
            gears[self.idx-1].turn(dir * -1, gears,check)
                
        if self.idx < 3 and check[self.idx + 1] and self.getRight() != gears[self.idx+1].getLeft():
            gears[self.idx+1].turn(dir * -1, gears,check)
        
        if dir == 1:
            self.gear.insert(0, self.gear.pop(7))
        else :
            self.gear.append(self.gear.pop(0))
            
        return

    def getLeft(self):
        return self.gear[6]
    
    def getRight(self):
        return self.gear[2]
    
    def getTop(self):
        return self.gear[0]

gears = [Gear(list(map(int, list(input().rstrip()))),i) for i in range(4)]
K = int(input())
check = [True,True,True,True]
for _ in range(K):
    idx, dir = map(int, input().split())
    check = [True,True,True,True]
    
    gears[idx-1].turn(dir,gears,check)
        

print(sum(gears[i].getTop() * 2**i for i in range(4)))
