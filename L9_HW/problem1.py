num = [7, 8, 120, 25, 44, 20, 27]
print num

i = len(num) - 1
while i >= 0:
  if num[i] % 2 == 0:
    num.pop(i)
  i -= 1

print num
