from OOPSDemo import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 3)

    def getCompleteData(self):
        return self.num + self.summation() + self.num2


obj3 = ChildImpl()

print(obj3.getCompleteData())
