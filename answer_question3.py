

def destructively_remove_if(datalist, priority):
    if priority == "frequency":
        sorted_list = sorted(datalist, key=lambda i: i['frequency'])
    if priority == "last_upadated":
        sorted_list = sorted(datalist, key=lambda i: i['last_upadated'])

    return sorted_list


data_list = [{'id': "data1", 'last_upadated': "14-03-2022", 'frequency':  96},
             {'id': "data6", 'last_upadated': "14-03-2021", 'frequency': 56},
             {'id': "data7", 'last_upadated': "15-03-2021", 'frequency': 46},
             {'id': "datat", 'last_upadated': "18-03-2021", 'frequency': 86}]


print("Before:", data_list)
priority = input("enter your priory")  # it may be last_updated,frequency
destructively_remove_if(data_list, priority)
print("After:", sorted_list)
