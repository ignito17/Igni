# Contains path definitons of the project
# Is static         -- 27/10/2024

path_dict={"root":"/",
      "bin":"/bin/",
      "data_process":"/data_process/",
      "data_store":{"topics":"/data_store/topics/",
                    "trackers":"/data_store/trackers/"},
      "dump":"/dump/"}

class Namespace():
    pass

refs=Namespace()
refs.path=path_dict