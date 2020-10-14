
from OOPSDemo import Calculator
class ChildImplement(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 3)

    def GetCompleteData(self):
        return self.num2 + self.secondnumber + self.summation()


obj = ChildImplement()
print(obj.GetCompleteData())


