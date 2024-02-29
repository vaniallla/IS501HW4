'''menu plugin'''
from main import Command


class MenuCommand(Command):
    '''menu'''
    def __init__(self, command_dict):
        self.command_dict = command_dict

    def execute(self):
        print("Available commands:")
        for command_name in self.command_dict:
            print(command_name)
