a = [1, 4, 5, 7, 8, -2, 0, -1]

print a[2], a[4]

a_sorted = list(a)
a_sorted.sort(reverse = True)

print a
print(a_sorted)

for i in range(0, 3):
  print (a_sorted[i]),
print 
for i in range(1, 6):
  print (a_sorted[i]),
print

a_sorted.pop(3)
a_sorted.pop(2)
print a_sorted

b = ["grapes", "Potatoes", "tomatoes", "Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]
b_sorted = list(b)
b_sorted.sort()

c = []
for i in range(0,3):
  c.append(a[i])
for i in range(3, 6):
  c.append(b[i])
print c
