# Key-value pairs data structure
# Can use the immutable data for the key
# Finding and modification takes O(1)time

data = dict()
data['apple'] = 'red'
data['banana'] = 'yellow'
data['carrot'] = 'orange'

b = {
    'kyle': 97,
    'Tom': 98
}

# the list of keys
key_list = data.keys()

# the list of values(data)
value_list = data.values()

# the value of each key
for key in key_list:
    print(data[key])