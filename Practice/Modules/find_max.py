def find_max(list):
    maximum = 0
    for i in list:
        if i > maximum:
            maximum = i
    return maximum

print(find_max([1, 2, 3]))

#package is a container for multiple modules. It is a directory or folder