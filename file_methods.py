import os

file = open("sample.txt","w")
file.write("Coco is my dog.")
file.close()

file = open("demo.txt", "w")
file.write("hello, world")
file.close()

file = open("demo.txt", "w")
file.write("Coco\n")
file.write("Tesla\n")
file.write("Michi\n")
file.close()

file = open("demo.txt", "w")
lines = ["Dog\n", "Cat\n", "Pig\n"]
file.writelines(lines)
file.close()

file = open("demo.txt", "r")
data = file.read()
print(data)
file.close()

file = open("demo.txt", "r")
print(file.read(3))
file.close()

file = open("demo.txt", "r")
print(file.readline())
print(file.readline())
file.close()

file = open("demo.txt", "r")
lines = file.readlines()
print(lines)
file.close()

file = open("demo.txt", "r")
for line in file: 
    print(line.strip())
file.close()

file = open("demo.txt", "a")
file.write("\nTesla and Michi are my cats.")
file.close()

with open("demo.txt", "r") as file: 
    print(file.read())

os.remove("demo.txt")

# with open("photo.jpg", "rb") as file:
#     data = file.read()

# with open("copy.jpg", "wb") as file:
 #   file.write(data)