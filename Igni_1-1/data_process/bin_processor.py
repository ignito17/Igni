# Managing dictinoary objects of classes

def obj_manager(map_obj:dict):

    # Display the current objects
    def display():
        for x, y in map_obj.items():
            yield (x,y)
        
    # add k-v pair
    def add(obj_key,obj_value):
        map_obj[obj_key]=obj_value
        return 
       
    # remove k-v pair
    def remove(obj_key):
        value=map_obj.pop(obj_key)
        return (obj_key,value)
            
    # edit value 
    def new_value(obj_key,obj_value):
        for key in map_obj.keys():
            if key==obj_key:
                map_obj[obj_key]=obj_value
                return
            else:
                return f"No key found with name {obj_key}" 

    def commit():
        return map_obj
    
    def reset():
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