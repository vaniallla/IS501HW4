'''addition plugin'''
from calculator import Command

class AdditionCommand(Command):
    '''addition command'''
    def __init__(self, operands):
        self.operands = operands

    def execute(self):
        result = sum(self.operands)
        print(f"The result of addition is: {result}")

if __name__ == "__main__":
    operands = [int(x) for x in input("Enter numbers to add (separated by spaces): ").split()]
    command = AdditionCommand(operands)
    command.execute()
