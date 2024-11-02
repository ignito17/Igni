from bin import class_definitions as c_d

ds_obj=c_d.topic(name="Data Science")
print(ds_obj._get_storage_path())
ds_tracker_obj=c_d.tracker(name="ds_tracker")
print(ds_tracker_obj._get_storage_path())