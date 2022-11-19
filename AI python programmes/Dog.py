class Dog:
    species = ["canis lupus"]
    '''Blueprint of a
    dog''' 
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.state = "Sleeping"
    
    def command(self, x):
        if x == self.name:
            self.bark(2)
        elif x == "Sit":
            self.state = "Sit"
            print("Sit down..!!")
        else:
            self.state = "wag tail"
            print("Wag your tail..!!")
    def bark(self, freq):
        for i in range(freq):
            print("[" + self.name +"]: Woof..!!") 


            #class variable shared by all instance species = ["canis lupus"]
name = input("Enter name :")

obj = Dog("Tommy","Black")
obj_1 = Dog("Shelby", "White")

print(obj.color)
print(obj_1.color)

obj.bark(2)

obj_1.command("Sit")

print("[Shelby]:" + obj_1.state)

obj.command("No")
print("[Tommy]:" + obj.state)

obj_1.command("Shelby")

obj_1.species += ["Labrador"]
print(len(obj.species)==len(obj_1.species))
