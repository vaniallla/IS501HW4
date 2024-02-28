'''exit plugin'''
import sys
from calculator import Command

# Menu Command
class ExitCommand(Command):
    '''exit'''
    def execute(self):
        sys.exit("Exiting...")
