# looping dictonary

data_dict = {
    'up': 'upin',
    'ip': 'ipin',
    'ad': 'adit',
    'sp': 'sopo',
    'jrw': 'jarwo',
}

# loopin first try (yang keluar key nya)
for data in data_dict :
    print(data)

# operator untuk mengambil items / iterable
keys = data_dict.keys()
print(keys)

for key in data_dict.keys() :
    print(data_dict.get(key))

values = data_dict.values()
print(values)

for value in data_dict.values() :
    print(value)

items = data_dict.items()
print(items)

for item in data_dict.items() :
    print(item)

for key,value in data_dict.items() :
    print(f"key = {key}, value = {value}")