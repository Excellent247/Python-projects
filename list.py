# # difference between list and tuple: List is mutable while Tuple is immutable (cannot be changed).

# names = ["Bella", "Simdi", "Glory"]

# print(len(names))

# for name in names:
#     print(name[2])

# i = 0

# for i in range(10):
#     i+=2
#     print(i)

with open("names.txt", "r") as names:
    for name in names:
        print(name)