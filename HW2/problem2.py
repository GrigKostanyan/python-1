import argparse

parser = argparse.ArgumentParser()

parser.add_argument('text', type = str)

args = parser.parse_args()
string = args.text

print 'The old string:', string

length = len(string)

if length >= 7 and length % 2 == 1:
  print 'Middle 3 characters: ', string[length/2 - 1: length/2 + 2]
  newStr = string[:length/2 -1 ] + string[length/2 - 1: length/2 + 2].upper() + string[length/2 + 2:]
  print 'The new string:', newStr
else:
  print 'Invalid string'
