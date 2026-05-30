array = ["apples", "bananas", "cucumbers"]

# Reading 

print(array[1]) # 0(1)

# Searching

print(array.index("bananas")) # O(n)

# Inserting

array.insert(1, "figs") #O(n+1)

print(array)

# Deleting

array.remove("figs") #O(n+1)

print(array)