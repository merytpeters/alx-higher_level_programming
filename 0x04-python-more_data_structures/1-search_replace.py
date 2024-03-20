def search_replace(my_list, search, replace):
    if my_list == [] or my_list is None:
        return []
    else:
        new_list = [replace if i is search else i for i in my_list]
        return (new_list)
