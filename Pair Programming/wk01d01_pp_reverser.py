import sys

def reverser(input):
	input_revesed = reversed(input)
	result =str()
	for x in input_revesed:
		result += x
	print result

input = sys.stdin.readline()
reverser(input)
