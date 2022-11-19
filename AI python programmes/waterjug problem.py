print("water jug problem")
x = int(input("enter volume in x:"))
y = int(input("enter volume in y:"))
while True:
    rno = int(input("enter the ruleno:"))
    if rno == 2:
        if y<3:
            x=0
            y=3
    if rno == 3:
        if x>0:
            x = 0
            y = 3
    if rno == 5:
        if x+y>4:
            x=4
            y=y-(4-x)
    if rno == 7:
        if x+y<4:
            x = x+y
            y = 0
    if rno == 9:
        x = 2
        y = 0
    print("volume of x",x)
    print("volume of y",y)
    
    if x==2:
        print("goal state is achieved")
        break
    
    
        