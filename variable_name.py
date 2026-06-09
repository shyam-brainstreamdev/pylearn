a = "name"
print("Value:", a, "\t\tType:", type(a).__name__)

b = 10
print("Value:", b, "\t\tType:", type(b).__name__)

c = [1, 2, 3]
print("Value:", c, "\tType:", type(c).__name__)

d = 23+3j
print("Value:", d, "\t\tType:", type(d).__name__)

e = {1, 2, 3}
print("Value:", e, "\tType:", type(e).__name__)

f = (1,2,3)
print("Value:", f, "\tType:", type(f).__name__)

f = {1:1,2:2}
print("Value:", f, "\tType:", type(f).__name__)

f = 10.20
print("Value:", f, "\t\tType:", type(f).__name__)

i = True
print("Value:", i, "\t\tType:", type(i).__name__)
print()
print("casting")
a = "10"
b = int(a)
print("Value:", b, "\t\tType:", type(b).__name__)

a = "abc def"
b = tuple(a)
print("Value:", b, "\tType:", type(b).__name__)