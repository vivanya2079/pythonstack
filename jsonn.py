import json

# Writing JSON data to a file
x = [1, "sample", "hello"]
with open("C:/Users/vivan/Music/myfilee.txt", "w") as f:
    json.dump(x, f)

# Reading JSON data from the file
with open("C:/Users/vivan/Music/myfilee.txt", "r") as f:
    data = json.load(f)

# Now, 'data' contains the JSON data from the file as a Python list
print(data)
