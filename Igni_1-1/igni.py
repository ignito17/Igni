from bin import class_definitions as c_d

# topic object
ds_obj=c_d.topic(name="Data Science")
print(ds_obj._get_storage_path())
for x in ds_obj._show_timestamps():
    print(x, "\t", type(x))


# tracker object
ds_tracker_obj=c_d.tracker(name="ds_tracker")
print(ds_tracker_obj._get_storage_path())
ds_tracker_obj._manage_obj()
ds_tracker_obj._manage_obj.add()