# # difference between list and tuple: List is mutable while Tuple is immutable (cannot be changed).

# names = ["Bella", "Simdi", "Glory"]

# print(len(names))

# for name in names:
#     print(name[2])

# # for loop
# i = 0

# for i in range(10):
#     i+=2
#     print(i)

# ## read files

# with open("names.txt", "r") as names:
#     for name in names:
#         print(name)

import os

folders = input("Please provide the names of directories with spaces in between: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("The directory "+ folder + " does not exist")
        continue
    except PermissionError:
        print("You do not have access to the folder " + folder)
        continue
    print("************** Listing the files in directory - " + folder)
    for file in files:
        print(file)