'''addition plugin'''
from main import Command

# Addition Command
class AdditionCommand(Command):
    '''command for addition'''
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        return self.num1 + self.num2
