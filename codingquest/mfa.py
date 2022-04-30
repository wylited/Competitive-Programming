data = "0001011100100100110011111000010101100111111010110000001011000011110100111000010010110010000110100110001111110101100010001100010111111101000010111000011110100110010111000000001111101010010001010011010010100011111110111111010001111110100111010111001000000111101011000010101100111111010000001001101001010111000010000100011111010001100011111011111101011000010101100111000011110101100000000000001000111001010010101001100111111101000010101111101000111010111001001000001011100110000011110100001011100001111010110010010000010111001011001000001010101101111010001001001000111110101100100100100010000111000000101100001010111110101100010001110010100101111010110010100001111010101011001110100011111110100010110010011001001000000001010000110010000100001000111110111111010110001000110110011100110100110001111110101100001010110011111101000001100110000010000110000111110100110100111010010100000001100110111101000110100111101011000010101100111000011110101010001011010111001001001100010000100001111010011010100001100000100101000000111101011000001001100011001110000000011110111111010010101111111010001001001000111110100001011100001111010001001000110110001000001000011110100011011011110101110100111001011110101010110011100100001001111001001001000110000100011111010110010111000011111010111010011100101111011111101010000000011000110010100001000101101111010110010000101001110010111101011001010010100111010111000110010100000001000001001111011111111"

lookupdata = """A 0010
E 0000
T 0001
I 0011
N 0100
O 0101
S 0110
H 0111
R 10000
D 10001
L 10010
U 10011
C 10100
M 10101
F 10110
B 10111
F 1100000
Y 1100001
W 1100010
G 1100011
P 1100100
B 1100101
V 1100110
K 1100111
Q 1101000
J 1101001
X 1101010
Z 1101011
0 1110000
1 1110001
2 1110010
3 1110011
4 1110100
5 1110101
6 1110110
7 1110111
8 1111000
9 1111001
_ 1111010
. 1111011
' 1111100
* 1111111"""
index = 0

#Parse the lookup table into the graph



def negativecheck(length):
    global index;
    test = data[index:index+length]
    if test in lookup:
        index += length
        return lookup[test]
    else:
        return negativecheck(length-1)

# Put the avlues in the lookup into a dictionary
lookup = {}
for line in lookupdata.split('\n'):
    if line:
        key, value = line.split(' ')
        lookup[value] = key

# Convert the binary data to the values in lookup depending on the key
# and then join the values together
# Check if the longest value exists first (7) and if there isnt that isnt an option lower it until you get a value.

# loop through the data and find the output string
# Check if the 
results = []
while index < len(data):
    results.append(negativecheck(7))
    # Loop and print all the values of results in a single line
    for i in results:
        print(i, end = "");