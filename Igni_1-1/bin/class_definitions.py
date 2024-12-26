# Cointains class definitions.

# Importing internal imports 
from data_process.internal_imports import refs
<<<<<<< HEAD
=======

>>>>>>> 531b2419e17c745abf2c0ca6ff6ae3eec267d8ef

# Importing external imports
from data_process import external_imports as ei

# igni is the blueprint for custom "base" object
class igni():
    app_version=1.1
    def __init__(self,name) -> None:
        self.name=str(name)
        pass

# This is the blueprint for custom "topic" object 
class topic(igni):
    def __init__(self, name):
        super().__init__(name)
        self._obj_name=name.strip()
        self._obj_name=self._obj_name.replace(" ","_")
        self._obj_data_storage_path=refs.path["data_store"]["topics"]+f"{self._obj_name}"
        self.__timestamp_dict={"Start":None,
                          "Pause":None,
                          "Stop":None}
        self._obj_data=None

    # Add data to object
    def set_data(self,data):
        self._obj_data=data

    # Object data storage path getter
    def _get_storage_path(self):
        return self._obj_data_storage_path
    
    # Add function to show object data
    def get_data(self):
        return self._obj_data
    
    # A fucntion to show dates
    def _show_timestamps(self):
        return [(timestamp, time) for timestamp, time in self.__timestamp_dict.items()]

# This is the blueprint for custom "tracker" object
class tracker(topic):
    def __init__(self, name) -> None:
        super().__init__(name)
        self._obj_name=name.strip()
        self._obj_name=self._obj_name.replace(" ","_")
        self._obj_data_storage_path=refs.path["data_store"]["trackers"]+f"{self._obj_name}"
       
        # To store other objects and their links
        self._obj_data={}           # {"obj_name":{obje_p1":value},}