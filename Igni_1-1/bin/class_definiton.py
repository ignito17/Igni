# Cointains class definitions.

# Importing internal imports 
from data_process import internal_imports

# catching path dict 
path=internal_imports.path

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
        self.__obj_data_storage_path=path["data_store"]+"obj_name"