class Customer:
    def __init__(self, name): #constuctor 
        self.name = name

    def details(self):
        print("Customer Details")
        print("Customer Name :", self.name)

class Consumer(Customer):
    def __init__(self, name, order_id): #constructor
        super().__init__(name)  #parent class constructor
        self.order_id = order_id

    def details(self):
        print("Consumer details")
        print(self.name, ' ', self.order_id)

customer = Customer('Harsh')
consumer = Consumer('Sid',1)

customer.details()
consumer.details()