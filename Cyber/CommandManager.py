import os

class CommandManager():
    def execute(self,command):
        os.system(command)
    def Create(self,Addfile,CreateFile):
        self.execute(f"echo. >{CreateFile}")
        self.execute(f"copy {Addfile}")