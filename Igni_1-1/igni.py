from bin import class_definitions as c_d
<<<<<<< HEAD
from data_process.bin_processor import obj_manager
from data_process.external_imports import datetime

# topic object
ds_obj=c_d.topic(name="Data Science")
ds_obj.set_data({"Description":\
                 "This is a data science topic(class) object"})
om_1=obj_manager(ds_obj.get_data())
print(*om_1.display())
om_1.add("Name","Data Science")
om_1.add("Date",datetime.datetime.now())
print(*om_1.display(),"\tmap_object")
om_1.new_value("Date",datetime.datetime.now())
=======
from data_process.bin_processor import obj_data_manager

# topic object
ds_obj=c_d.topic(name="Data Science")

# tracker object
ds_tracker_obj=c_d.tracker(name="DS Tracker")

# creating a dict manager object
m1=obj_data_manager()
>>>>>>> 531b2419e17c745abf2c0ca6ff6ae3eec267d8ef
