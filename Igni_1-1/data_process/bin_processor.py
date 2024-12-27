# Managing dictinoary objects of classes

def obj_data_manager(object_map:dict):     # To process object data
    local_map=object_map.copy()             # Copying the original dict

    # Display the current objects
    def display():
        for x, y in local_map.items():
            yield (x,y)
        
    # add k-v pair
    def add(obj_key,obj_value):
        local_map[obj_key]=obj_value
        return 
       
    # remove k-v pair
    def remove(obj_key):
        value=local_map.pop(obj_key)
        return (obj_key,value)
            
    # edit value 
    def new_value(obj_key,obj_value):
        if obj_key in local_map.keys():
            local_map[obj_key]=obj_value
            return f"{obj_key} updated with the new value {obj_value}"
        else:
            return f"{obj_key} not found"

    def commit():
        object_map.update(local_map)
        return object_map
    
    def reset():
        local_map.clear()
        return
        
        # Earlier this was a nested method of class tracker.
        # self.obj_data_manager.display=display
    obj_data_manager.display=display
    obj_data_manager.add=add
    obj_data_manager.remove=remove
    obj_data_manager.new_value=new_value
    obj_data_manager.commit=commit
    obj_data_manager.reset=reset
    return obj_data_manager