def my_range(n):
  i = 0
  while (i < n + 1):
    yield i
    i += 1
  print "there are no values left"

for i in my_range(5):
  print i
