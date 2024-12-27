from bin import class_definitions as c_d
from data_process.bin_processor import obj_data_manager
from data_process.external_imports import datetime

# topic object
ds_obj=c_d.topic(name="Data Science")
ds_obj.set_data({"Description":\
                 "This is a data science topic(class) object"})

ncert_obj=c_d.topic(name="NCERT BOOKS") 
ncert_obj.set_data({"Description":\
                    'This is a ncert topic (class) object'})

tracker_1=c_d.tracker(name="It Tracker")
# print(tracker_1.get_data(),type(tracker_1.get_data()))

print(*ds_obj._show_timestamps(),sep='\n')
print(ds_obj.start(),'\tfunction')
print(*ds_obj._show_timestamps(),sep='\n')
print(ds_obj.stop(),'\tfunction')
print(*ds_obj._show_timestamps(),sep='\n')
print('\n'*5)
print(ds_obj.start(),'\tfunction')
print(*ds_obj._show_timestamps(),sep='\n')
print(ds_obj.stop(),'\tfunction')
print(*ds_obj._show_timestamps(),sep='\n')