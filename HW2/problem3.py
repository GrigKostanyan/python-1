import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", type = str)
parser.add_argument("w1", type = str)
parser.add_argument("w2", type = str)

args = parser.parse_args()

print 'The given text:', args.text
print 'The first word:', args.w1
print 'The second word:', args.w2

print 'The new text:', args.text.replace(args.w1, args.w2)
