#int to binary only, binary to int is much simpler

import math

def int_to_binary(int_input):
    # init a leftover int and string
    leftover = int_input
    binary = ""
    # for loop backwards
    for i in range(8, -1, -1):
        if(math.pow(2,i)<=leftover):
            leftover -= math.pow(2,i)
            binary += "1"
        else:
            binary +="0"
    return binary

# 귀찮아서 int() 씀
def binary_to_int(binary_input):
    binary_input_str = str(binary_input)
    return int(binary_input_str, 2)

if __name__=="__main__":
    userinput = int(input("Enter int: "))
    print("{} in binary is {}".format(userinput, int_to_binary(userinput)))
