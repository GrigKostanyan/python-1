list1 = ["hello", 1, True]

list2 = list(list1)

n = int(raw_input("Enter the number of arguments: "))

for i in range(n):
  list2.append(raw_input())

print(list1)
print(list2)
