class Csestudent:
    stream = 'cse' #class variable

    def __init__(self,name,roll):
        self.name = name #instance variable
        self.roll = roll #instance variable
    
    def show(self):
        print(self.name, ' ', self.roll, ' ', self.stream)

stud = Csestudent('harsh', 361)
stud_1 = Csestudent('Sid', 2)
stud.show()
stud_1.show()
