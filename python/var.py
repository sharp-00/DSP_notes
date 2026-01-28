b = [1, 2, 3]
c = [4, 5]
a = [ b, c]
#print(a)
b[0] = 9
print(b)
#print(a)
d = b
b = [10, 11, 12]
#print(a)
d[1] = 25
#print(a)

print(b)
