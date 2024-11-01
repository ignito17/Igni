# Cointains class definitions.

import path_definitons as p_d
from data_process import import_modules
dt=import_modules.datetime

# igni is the blueprint for base custom object
class igni():
    def __init__(self,name) -> None:
        self.obj_details={"object_name":str(name),
                          "objec_type":"Igni",
                          "creation_time":dt.now()}
        self.__obj_data_storage=p_d.path["data_store"]+"obj_name"
        pass
    def get_obj_data_storage_path(self):
        print(self.__obj_data_storage)

to_do=igni("to_do")
to_do.get_obj_data_storage_path()
to_do.get_object_details()