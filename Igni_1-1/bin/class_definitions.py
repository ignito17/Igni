# Cointains class definitions.

# Importing internal imports 
from data_process import internal_imports as ii

# Importing external imports
from data_process import external_imports as ei

# igni is the blueprint for custom "base" object
class igni():
    app_version=1-1
    def __init__(self,name) -> None:
        self.name=str(name)
        pass

# This is the blueprint for custom "topic" object 
class topic(igni):
    def __init__(self, name):
        super().__init__(name)
        self.__obj_name=name.strip()
        self.__obj_name=self.__obj_name.replace(" ","_")
        self.__obj_data_storage_path=ii.path_dict["data_store"]["topics"]+f"{self.__obj_name}"
    
    def _get_storage_path(self):
        return self.__obj_data_storage_path

# This is the blueprint for custom "tracker" object
class tracker(igni):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.__obj_name=name.strip()
        self.__obj_name=self.__obj_name.replace(" ","_")
        self.__obj_data_storage_path=ii.path_dict["data_store"]["trackers"]+f"{self.__obj_name}"
    
    def _get_storage_path(self):
        return self.__obj_data_storage_path
    
