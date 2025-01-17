from abc import abstractmethod
from src.file_system.enum.file_type import FileType
from typing import List
from datetime import datetime


# ===============
# FILE COMPONENT
# ===============
class FileComponent:
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def get_type(self):
        pass
    
    @abstractmethod
    def get_size(self):
        pass
    
    def has_next_level(self):
        return self.get_type() == FileType.DIRECTORY
    
    def get_display_name(self):
        if self.has_next_level():
            return f"{self.name}/"
        return self.name
    

# ==========
# DIRECTORY
# ==========
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
        
    def create_file(self, name: str):
        file = File(name)
        self.file_components.append(file)
        
    def get_size(self):
        return sum([file_component.get_size() for file_component in self.file_components])
    
    
# =====
# FILE
# =====
class File(FileComponent):
    def __init__(self, name: str):
        if "." not in name:
            name, suffix = name, ".txt"
        else:
            name, suffix = name.split(".")
        super().__init__(name)
        self.suffix = "." + suffix
        self.content = "test content"
        self.created_at = self.__generate_timestamp()
        self.updated_at = self.__generate_timestamp()
        
    def __generate_timestamp(self):
        return int(datetime.now().timestamp() * 1000)
    
    def __from_timestamp(self, timestamp: int):
        return datetime.fromtimestamp(timestamp / 1000)
        
    def get_type(self):
        return FileType.FILE
        
    def get_size(self):
        return len(self.content)
    
    def get_info(self):
        info = "=" * 40 + "\n"
        info += f"Name: {self.name}\n"
        info += f"File type: {self.suffix}\n"
        info += f"Size: {self.get_size()} bytes\n"
        info += f"Created at: {self.__from_timestamp(self.created_at)}\n"
        info += f"Updated at: {self.__from_timestamp(self.updated_at)}\n"
        info += "=" * 40 + "\n"
        return info
        