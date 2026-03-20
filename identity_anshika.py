# Integer
a = 15
print("Integer before change:", id(a))
a = a + 5
print("Integer after change:", id(a))

# String
s = "hello"
print("\nString before change:", id(s))
s = s + " world"
print("String after change:", id(s))

# List
lst = [3, 4, 5]
print("\nList before change:", id(lst))
lst.append(4)
print("List after change:", id(lst))

# Tuple
t = (6,7,8)
print("\nTuple before change:", id(t))
t = t + (4,)
print("Tuple after change:", id(t))