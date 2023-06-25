def power(entry):
    return entry ** 2

a = [2,4,3,10,11]
b = []

# long way with for 
for i in a:
    b.append(power(i))
print(b)

# efficient and more speed
b = list(map(power, a))
print(b)
print(list(map(power, (1,2,3,4))))




# long way 
for i in a:
    if i > 4:
        b.append(i)
    else:
        pass


# short way with filter
def filter_g_4(entry):
    if i > 4:
        return True
    else:
        return False
b = list(filter(filter_g_4, a))





from functools import reduce
# long way
counter = 0 
for i in a:
    counter += i
print(counter)

# short way
def sum(entry1, entry2):
    return entry1 + entry2

print(reduce(sum, a))