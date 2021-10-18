t1 = (2, "cat", "a", -2, "Anna")

l = list(t1)
l.remove("a")
t1 = tuple(l)
print t1

t2 = (1, 2, 3, 4, 5)
l = []
for i in range (0,2):
  l.append(t1[i])
for i in range (0,3):
  l.append(t2[i])
t3 = tuple(l)

print t3[2]

t4 = [(1, 3, 5), (8, 9), ("Anna", "Bob", "Alice")]
print t4[0][1]
