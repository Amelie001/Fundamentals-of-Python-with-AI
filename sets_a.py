# Create a set

sampleSet = {1, 1, 2, 3, 2, 3, 4, 2, 1, 4, 5, 3, 3, 4, 5, 5}
print(sampleSet)

# Create a set from a list 

sampleList = [1, 2, 3, 4, 2, 8, 5, 3, 1, 2, 3, 4, 2, 1, 5, 4, 3, 3, 2]
sampleSet = set(sampleList)
print(sampleSet)

# Check if an element exists 

if 4 in sampleSet: 
    print("YES")

else: 
    print("NO")

# Add elements inside a set 

myset = set([])

myset.add(3)
myset.update([4, 4, 5, 3, 5])
print(myset)

# Remove an element 

myset.remove(5)
myset.discard(2)
myset.pop()
print(myset) 
myset.clear()
print(myset)

# Set operations 

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union 

print(a.union(b))
print(a | b)

# Intersection 

print(a.intersection(b))
print(a & b)

# Difference 

print(a.difference(b))
print(a - b)

# Symmetric difference 

print(a.symmetric_difference(b))
print(a ^ b) 