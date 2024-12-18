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
        self.__timestamp_dict={"Start":None,
                          "Pause":None,
                          "Stop":None}
    
    def _get_storage_path(self):
        return self.__obj_data_storage_path

    # A fucntion to show dates
    def _show_timestamps(self):
        # f_string=f"Topic object {self.__obj_name}"
        '''
        for timestamp in self.__timestamp_dict.keys():
            if self.__timestamp_dict[timestamp]:
                yield [timestamp,self.__timestamp_dict[timestamp]]
            else:
                yield [timestamp,None]
        '''
        yield (timestamp, time) for timestamp, time in self.__timestamp_dict.items()

# This is the blueprint for custom "tracker" object
class tracker(igni):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.__obj_name=name.strip()
        self.__obj_name=self.__obj_name.replace(" ","_")
        self.__obj_data_storage_path=ii.path_dict["data_store"]["trackers"]+f"{self.__obj_name}"
    
    def _get_storage_path(self):
        return self.__obj_data_storage_path
    
