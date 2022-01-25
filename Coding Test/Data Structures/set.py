# Do not allow having duplicated data
# No order
# It takes O(1) time to find and modify the data

data = set([1, 1, 2, 3, 4, 4, 5])  # => {1,2,3,4,5}
data = {1, 1, 2, 3, 4, 4, 5}  # => {1,2,3,4,5}

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

union = a | b  # 1,2,3,4,5,6,,7
intersection = a & b  # 3,4,5
difference = a - b  # 1,2

# add new elem
data.add(6)

# insert several new elems
data.update([7, 8])

# remove specific elem
data.remove(3)
