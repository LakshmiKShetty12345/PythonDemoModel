class Calculator:
    num = 100 #class variables


    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b

        print("I am called when the new object is created")



    def GetData(self):
        print("Executing the methods inside te class")



    def summation(self):

        return self.firstnumber + self.secondnumber + Calculator.num




obj = Calculator(3,4)
obj.GetData()
print((obj.summation()))

obj1 = Calculator(1,2)
obj1.GetData()
print(obj1.summation())