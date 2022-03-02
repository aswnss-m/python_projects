# The function takes a string as its parameter
def enc(st):
    letters= []; # TO STORE THE ENCRYPTED STRING

    # Get each charactor in string "ANJAN" => A , N , J, A, N
    for i in st:
        asc = ord(i) #FINDING THE ASCII VALUE

        # Small letter encryption
        if(asc>=97 and asc<=122):
            if(asc == 120): # char 'x'
                letters.append('a')
                continue
            elif(asc == 121): # char 'y'
                letters.append('b')
                continue
            elif(asc == 122): # char 'z'
                letters.append('c')
                continue
            else:
                letters.append(chr(ord(i)+3))

        # Capital Letter encryption
        elif(asc>=65 and asc<=90):
            if(asc == 88): # char 'X'
                letters.append('A')
                continue
            elif(asc == 89): # char 'Y'
                letters.append('B')
                continue
            elif(asc == 90): # char 'Z'
                letters.append('C')
                continue
            else:
                letters.append(chr(ord(i)+3))

        # skipping encrypting special charactors (whitespace , symbols etc..)
        else:
            letters.append(chr(asc))
    # join with.join(list)
    return "".join(letters)

if __name__ == "__main__":
    filename = input("Enter the filename : ")
    try:
        with open(filename,"r") as rfile:
            lines = rfile.readlines()
            with open("encrypted.txt","w") as wfile:
                for line in lines:
                    wfile.write(enc(line))
        print("file '{}' has been encrypted and stored in 'encrypted.txt'".format(filename))
    except Exception as e:
        print(e)
