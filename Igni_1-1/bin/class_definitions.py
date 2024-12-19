# Cointains class definitions.

# Importing internal imports 
from data_process.internal_imports import refs
from data_process.bin_processor import obj_manager

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
        self.__obj_data_storage_path=refs.path["data_store"]["topics"]+f"{self.__obj_name}"
        self.__timestamp_dict={"Start":None,
                          "Pause":None,
                          "Stop":None}
        self.__obj_data=None

    # Add data to object
    def add_data(self,data):
        self.__obj_data=data

    # Object data storage path getter
    def _get_storage_path(self):
        return self.__obj_data_storage_path
    
    # Add function to show object data
    def show_data(self):
        for x in self.__obj_data:
            yield x
    
    # A fucntion to show dates
    def __show_timestamps(self):
        return [(timestamp, time) for timestamp, time in self.__timestamp_dict.items()]

# This is the blueprint for custom "tracker" object
class tracker(igni):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.__obj_name=name.strip()
        self.__obj_name=self.__obj_name.replace(" ","_")
        self.__obj_data_storage_path=refs.path["data_store"]["trackers"]+f"{self.__obj_name}"
       
        # To store other objects and their links
        # self.__object_map={}    # {"obj_name":{"obj_p1":value},}
        self.__track_map={}     # {"obj_name":{obje_p1":value},}