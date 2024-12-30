import os
from src.model.file import FileComponent, Directory, File
from typing import List

class CommandLineExecutor:
    def __init__(self):
        self.browse_history: List[Directory] = [Directory("root")]
        
    def start(self):
        while True:
            print(f"~{''.join(['/' + dir.name for dir in self.browse_history])}")
            command = input("$ ")
            if command == "exit" or command == "quit":
                break
            self.parse_and_execute(command)   
            print() 
    
    def parse_and_execute(self, command_line: str):
        command_line = command_line.strip()
        if command_line == "":
            print("Invalid command")
        command_components = command_line.split()
        command = command_components[0].lower()
        if command == "ls":
            curr_dir = self.browse_history[-1].show_curr_dir()
            print(curr_dir)
        elif command == "cd":
            to = command_components[1]
            if to == "..":
                if len(self.browse_history) == 1:
                    print("Already at root")
                    return
                self.browse_history.pop()
                return
            file_components = self.browse_history[-1].file_components
            exist = False
            for comp in file_components:
                if comp.name == to and comp.has_next_level():
                    exist = True
                    self.browse_history.append(comp)
                    break
            if not exist:
                print("Directory not found")
        elif command == "mkdir":
            if len(command_components) < 2:
                print("Invalid command")
            self.browse_history[-1].create_dir(command_components[1])
        elif command in ["cls", "clear"]:
            os.system('clear')
        elif command == "rmdir":
            dir_name = command_components[1]
            dir_found = False
            for dir in self.browse_history[-1].file_components:
                if dir.name == dir_name and dir.has_next_level():
                    dir_found = True
                    self.browse_history[-1].file_components = [file for file in self.browse_history[-1].file_components if file.name != dir_name]
                    break
            if not dir_found:
                print("Directory not found")
        elif command == "touch":
            if len(command_components) < 2:
                print("Invalid command")
            file_name = command_components[1]
            self.browse_history[-1].create_file(file_name)
    