# Cointains class definitions.

import path_definitons as p_d

# igni is the blueprint for base custom object
class igni():
    def __init__(self,name) -> None:
        self.name=str(name)
        self.__obj_data_storage=p_d.path["data_store"]+"obj_name"
        pass
    def get_obj_data_storage_path(self):
        print(self.__obj_data_storage)

to_do=igni("to_do")
to_do.get_obj_data_storage_path()