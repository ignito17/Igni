# Cointains class definitions.
# Methods return literalls or strings only for  report codes 
# They also return generator objects in case of multiple outputs of data
# They always return in form of a data type or error type/return code

# Importing internal imports 
from data_process.internal_imports import refs

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
        self.__timestamp_dict={"start":None,
                          "pause":None,
                          "resume":None,
                          "finish":None}    # manages schedule    
        self._obj_data=None                 # manages topic data

    # Add data to object
    def set_data(self,data={}):
        self._obj_data=data

    # Object data storage path getter
    def _get_storage_path(self):
        return self._obj_data_storage_path
    
    # Add function to show object data
    def get_data(self):
        return self._obj_data
    
    # A function to generate timestamps data
    def _show_timestamps(self):
        for timestamp, time in self.__timestamp_dict.items():
            yield(timestamp,time)
    
    # Starting functionality for the timestamp_dict of the topic class
    def start(self,schedule=ei.datetime.datetime.now().isoformat()):
        if self.__timestamp_dict['finish']:
            return f'alredy finished',(self._obj_name,self.__timestamp_dict['finish'])
        elif self.__timestamp_dict['start'] or self.__timestamp_dict['pause']:
            self.__timestamp_dict['resume']=schedule
            return f'resume',(self._obj_name,self.__timestamp_dict['resume'])
        else:
            self.__timestamp_dict['start']=schedule
            return f'start',(self._obj_name,self.__timestamp_dict['start'])
    
    # Stoping functionality for the timestamp_dict of the topic class
    # Need to edit this function for finish functionality of the topic 
    # Either should add one more method or integrate in stop
    def stop(self,schedule=ei.datetime.datetime.now().isoformat()):
        if self.__timestamp_dict['finish']:
            return f'alredy finished',(self._obj_name,self.__timestamp_dict['finish'])
        elif self.__timestamp_dict['start'] or self.__timestamp_dict['resume']:
            self.__timestamp_dict['pause']=schedule
            return f'pause',(self._obj_name,self.__timestamp_dict['pause'])
        else:
            self.__timestamp_dict['finish']=schedule
            return f'finish',(self._obj_name,self.__timestamp_dict['finish'])

# This is the blueprint for custom "tracker" object
class tracker(topic):
    def __init__(self, name) -> None:
        super().__init__(name)
        self._obj_name=name.strip()
        self._obj_name=self._obj_name.replace(" ","_")
        self._obj_data_storage_path=refs.path["data_store"]["trackers"]+f"{self._obj_name}"
       
        # To store other objects and their links
        self._obj_data={}           # {"obj_name":{obje_p1":value},}