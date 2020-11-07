
# * Run-length encoding
# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to 
# represent repeated successive charactors as a single count and charactor.
# For example the string,
# "AAAABBBCCDAA" would be
# "4A3B2C1D2A"
# 1: start
# 2: set the first char as key pos = 0
# 3: go throught the string from pos + 1
# 4: if char at pos+1 is same as key , count + 1 , pos + 1
# 5: else store count and current key , then set key = pos + 1
# 6: if pos == len(string) - 1 , stop



# Function to do the encoding
def encode(string):
    output = []
    pos = 0

    while pos < len(string):
        count = 1
        char = string[pos]

        for x in range(pos +1, len(string)):
            if char == string[x]:
                count += 1
                pos += 1
            
            else:
                break

        output.append(str(count))
        output.append(char)
        pos += 1

    return "".join(output)


if __name__=='__main__':
    user_input = input("Enter the string : ")
    print(encode(user_input))
