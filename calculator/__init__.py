'''This page is refactored to have commands to perform the 4 operations'''
import os
import importlib.util
from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    '''command interface'''
    @abstractmethod
    def execute(self):
        '''method to represent action being performed'''

# Calculator
class Calculator:
    '''calculator class'''
    def __init__(self):
        self.commands = self.load_commands()

    def load_commands(self):
        '''load commands'''
        commands = {}
        plugin_dir = 'plugins'
        for file_name in os.listdir(plugin_dir):
            if file_name.endswith('.py') and file_name != '__init__.py':
                module_name = os.path.splitext(file_name)[0]
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(plugin_dir, file_name))
                plugin_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(plugin_module)
                for name, obj in plugin_module.__dict__.items():
                    if isinstance(obj, type) and issubclass(obj, Command) and obj != Command:
                        commands[name.lower()] = obj()
        return commands

    def run(self):
        '''executing calculator commands'''
        while True:
            print("Available commands: " + ", ".join(self.commands.keys()) + ", exit")
            user_input = input("Enter command and numbers in the following format (add 5 3): ").strip().lower()

            if user_input == "exit":
                print("Exiting")
                break

            command_parts = user_input.split()
            command_name = command_parts[0]

            if command_name not in self.commands:
                print("Invalid command.")
                continue

            # if command_name == "menu":
            #     MenuCommand(self.commands).execute()
            #     continue

            try:
                x = float(command_parts[1])
                y = float(command_parts[2])
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid numbers.")
                continue

            command = self.commands[command_name](x, y)
            result = command.execute()
            print("Result:", result)

# Main
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
