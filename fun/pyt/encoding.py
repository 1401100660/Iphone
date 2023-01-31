import sys

alphabet=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers=" 0123456789"

#argv relates to the arugments in the command line, for instance after the python command <filename> <arg0> <arg2>  ...
# argv holds the command line commands in a list and indexing that list follows the order above. 

print(sys.argv[0])

arg = sys.argv[1]
#to fullfill the list the iterating variable must be the same as the first variable.
characters = [i for i in arg]
x = ""
y = 0
for symbol in characters:
    x += str(alphabet.rfind(symbol))
    y += alphabet.rfind(symbol)

print(x, y)
