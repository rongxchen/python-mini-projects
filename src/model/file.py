from abc import abstractmethod
from src.enum.file_type import FileType
from typing import List


class FileComponent:
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def get_type(self):
        pass
    
    def has_next_level(self):
        return self.get_type() == FileType.DIRECTORY
    
    def get_display_name(self):
        if self.has_next_level():
            return f"{self.name}/"
        return self.name
    

class Directory(FileComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self.file_components: List[FileComponent] = []
        
    def get_type(self):
        return FileType.DIRECTORY
    
    def show_curr_dir(self):
        if len(self.file_components) == 0:
            return "Empty directory"
        curr_dir = "\t".join([file_component.get_display_name() for file_component in self.file_components])
        return curr_dir
    
    def create_dir(self, name: str):
        for file_component in self.file_components:
            if file_component.name == name and file_component.has_next_level():
                choice = input("Directory already exists, want to overwrite? (y/n)").lower()
                if choice in ["y", "yes"]:
                    self.file_components = [file_component for file_component in self.file_components if file_component.name != name]
                    self.file_components.append(Directory(name))
                    return
                else:
                    return
        self.file_components.append(Directory(name))
        
    def create_file(self, name: str, suffix: str = ""):
        file = File(name, suffix)
        self.file_components.append(file)
    

class File(FileComponent):
    def __init__(self, name: str, suffix: str = ""):
        super().__init__(name)
        self.suffix = suffix
        
    def get_type(self):
        return FileType.FILE
        