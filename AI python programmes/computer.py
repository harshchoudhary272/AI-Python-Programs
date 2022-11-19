class Computer:
    def __init__(self, ram, hdd):
        self.ram = ram
        self.hdd = hdd
 
    def config(self):
        print('Computer Configuration Details')
        print(self.ram, ' ', self.hdd)
 
comp1 = Computer('16GB', '500GB')
comp2 = Computer('12GB', '1000GB')
 
comp1.config()
comp2.config()