'''main.py page with plugin code'''
import os
import importlib.util
from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    '''command interface'''
    @abstractmethod
    def execute(self):
        '''method to represent action being performed'''

class Calculator:
    '''Calculator class'''
    def __init__(self):
        self.commands = {}
        self.load_plugins()

    def load_plugins(self):
        '''to load plugins'''
        plugins_dir = "plugins"
        if not os.path.exists(plugins_dir):
            print("No plugins directory found.")
            return

        for filename in os.listdir(plugins_dir):
            if filename.endswith(".py"):
                plugin_name = os.path.splitext(filename)[0]
                spec = importlib.util.spec_from_file_location(plugin_name, os.path.join(plugins_dir, filename))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for name in dir(module):
                    obj = getattr(module, name)
                    if hasattr(obj, '__bases__') and Command in obj.__bases__:
                        self.commands[name.lower()] = obj

    def run(self):
        '''to run program'''
        while True:
            user_input = input("Enter command:").strip().lower()

            if user_input == "exit":
                print("Exiting")
                break

            command_parts = user_input.split()
            command_name = command_parts[0]

            if command_name not in self.commands:
                print("Invalid command.")
                continue

            try:
                x = float(command_parts[1])
                y = float(command_parts[2])
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid numbers.")
                continue

            command = self.commands[command_name](x, y)
            result = command.execute()
            print("Result:", result)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
