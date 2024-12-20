from bin import class_definitions as c_d
from data_process.bin_processor import obj_manager

# topic object
ds_obj=c_d.topic(name="Data Science")

# tracker object
ds_tracker_obj=c_d.tracker(name="DS Tracker")
m_1=obj_manager(ds_tracker_obj.get_data())
print(*m_1.display())
m_1.add("Prabhat Kumar",23)
print(*m_1.display())
print(ds_tracker_obj.get_data())
m_1.add("Sujeet Sharma",23)
print(*m_1.display())
print(ds_tracker_obj.get_data())
m_1.reset()
print(*m_1.display())
print(ds_tracker_obj.get_data())