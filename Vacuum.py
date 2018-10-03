import sys  # for system exit

class room:
  def __init__(self):
     self.dirty= False
  def suck(self):
     self.dirty= False
	 
A = room()
B = room()
cost=0
count=2  # no. of rooms
A.dirty = input("Is room A dirty: Enter True / False: ")
B.dirty = input("Is room B dirty: Enter True / False: ")
VacuumPos = input("Is Vacuum cleaner present in room A or B: ")
if(A.dirty=="False" and B.dirty== "False"):
   print("Both rooms already clean, total cost =0")
   sys.exit(0)   # system exit
print("Vaccum cleaner present in room ",VacuumPos)   
while count>0:   
  if( VacuumPos=='A' and A.dirty== "True"):
     A.suck()
     print("Cleaning room A, cost incremented by 1")
     cost+=1
     count-=1
  if (VacuumPos=='A' and B.dirty=="True"):
        print("Vacuum cleaner moving to room B, cost incremented by 1")
        cost+=1
        VacuumPos= "B"
  if( VacuumPos=='B' and B.dirty== "True"):
     B.suck()
     print("Cleaning room B, cost incremented by 1")
     cost+=1
  if(VacuumPos=='B' and A.dirty=="True"):
        print("Vacuum cleaner moving to room A, cost incremented by 1")
        cost+=1	
        VacuumPos= 'A'
  count-=1
print("Both rooms cleaned\nTotal cost= ",cost)  