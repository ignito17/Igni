# Contains path definitons of the project
# Is static         -- 27/10/2024

# A dictionary to store path data of the project, output type is string
path_dict={"absolute":"D:\\Study_Shelf\\Resources\\codes\\python\\projects\\Igni\\Igni_1-1\\",
      "root":"/",
      "bin":"/bin/",
      "data_process":"/data_process/",
      "data_store":{"topics":"/data_store/topics/",
                    "trackers":"/data_store/trackers/"},
      "dump":"/dump/"}

class Namespace():
    pass

refs=Namespace()
refs.path=path_dict