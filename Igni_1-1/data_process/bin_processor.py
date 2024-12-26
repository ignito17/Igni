# Managing dictinoary objects of classes

def obj_manager(reference_map:dict):
    local_map=reference_map.copy()

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
        for key in local_map.keys():
            if key==obj_key:
                local_map[obj_key]=obj_value
                return
            else:
                return f"No key found with name {obj_key}" 

    def commit():
        reference_map.update(local_map)
        return reference_map
    
    def reset():
        local_map.clear()
        return
        
        # Earlier this was a nested method of class tracker.
        # self.obj_manager.display=display
    obj_manager.display=display
    obj_manager.add=add
    obj_manager.remove=remove
    obj_manager.new_value=new_value
    obj_manager.commit=commit
    obj_manager.reset=reset
    return obj_manager