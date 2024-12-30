import os
from abc import abstractmethod
from typing import List


class CMDExecutor:
    def __init__(self):
        self.system: List[FileComponent] = []
        self.browse_history: List[Directory] = [Directory("root")]
        
    def start(self):
        while True:
            command = input(f"Enter command ({self.browse_history[-1].name}): ")
            if command == "exit" or command == "quit":
                break
            self.execute(command)
            
    def __parse_command(self, command_line: str):
        command_components = command_line.split(" ")
        if command_line.strip() == "" or command_components[0].strip() == "":
            print("Command not found")
        command = command_components[0]
        if command == "ls":
            print(self.browse_history[-1].show_curr_dir())
        elif command == "cd":
            if len(command_components) < 2:
                print("Invalid command")
            if len(self.browse_history) == 0:
                print("No directories found")
            to_directory = command_components[1]
            if to_directory == "..":
                if len(self.browse_history) == 1:
                    print("Already at root")
                self.browse_history.pop()
                return
            directories = self.browse_history[-1].directories
            exist = False
            for directory in directories:
                if directory.name == to_directory:
                    exist = True
                    self.browse_history.append(directory)
                    break
            if not exist:
                print("File not found")
        elif command == "mkdir":
            if len(command_components) < 2:
                print("Invalid command")
            self.browse_history[-1].create_directory(command_components[1])
        elif command == "clear" or command == "cls":
            os.system('clear')
            
    def execute(self, command_line: str):
        return self.__parse_command(command_line)


class FileComponent:
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_type(self):
        pass
    
    def has_next_level(self):
        return self.get_type() == "directory"


class Directory(FileComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self.directories: List[Directory] = []
        self.files: List[File] = []

    def get_type(self):
        return "directory"
    
    def show_curr_dir(self):
        if len(self.directories) == 0 and len(self.files) == 0:
            return "Empty directory"
        curr_dir = "\t".join([dir.name for dir in self.directories]) + "\t".join([file.name for file in self.files])
        return curr_dir
    
    def create_file(self, name: str):
        file = File(name)
        self.files.append(file)
        
    def create_directory(self, name: str):
        if name == "":
            print("Invalid directory name")
        for directory in self.directories:
            if directory.name == name:
                choice = input("Directory already exists, want to overwrite? (y/n)")
                if choice.lower() == "y" or choice.lower() == "yes":
                    self.directories = [dir for dir in self.directories if dir.name != name]
                    self.directories.append(Directory(name))
                    return
                else:
                    return
        self.directories.append(Directory(name))


class File(FileComponent):
    def __init__(self, name: str):
        super().__init__(name)

    def get_type(self):
        return "file"


executor = CMDExecutor()
executor.start()

