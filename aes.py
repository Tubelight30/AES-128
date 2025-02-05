AES_S_BOX = [
    ["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"],
    ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"],
    ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"],
    ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"],
    ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"],
    ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF"],
    ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"],
    ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"],
    ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"],
    ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"],
    ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"],
    ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"],
    ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"],
    ["70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E"],
    ["E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF"],
    ["8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"]
]

INV_AES_S_BOX = [
    ["52", "09", "6A", "D5", "30", "36", "A5", "38", "BF", "40", "A3", "9E", "81", "F3", "D7", "FB"],
    ["7C", "E3", "39", "82", "9B", "2F", "FF", "87", "34", "8E", "43", "44", "C4", "DE", "E9", "CB"],
    ["54", "7B", "94", "32", "A6", "C2", "23", "3D", "EE", "4C", "95", "0B", "42", "FA", "C3", "4E"],
    ["08", "2E", "A1", "66", "28", "D9", "24", "B2", "76", "5B", "A2", "49", "6D", "8B", "D1", "25"],
    ["72", "F8", "F6", "64", "86", "68", "98", "16", "D4", "A4", "5C", "CC", "5D", "65", "B6", "92"],
    ["6C", "70", "48", "50", "FD", "ED", "B9", "DA", "5E", "15", "46", "57", "A7", "8D", "9D", "84"],
    ["90", "D8", "AB", "00", "8C", "BC", "D3", "0A", "F7", "E4", "58", "05", "B8", "B3", "45", "06"],
    ["D0", "2C", "1E", "8F", "CA", "3F", "0F", "02", "C1", "AF", "BD", "03", "01", "13", "8A", "6B"],
    ["3A", "91", "11", "41", "4F", "67", "DC", "EA", "97", "F2", "CF", "CE", "F0", "B4", "E6", "73"],
    ["96", "AC", "74", "22", "E7", "AD", "35", "85", "E2", "F9", "37", "E8", "1C", "75", "DF", "6E"],
    ["47", "F1", "1A", "71", "1D", "29", "C5", "89", "6F", "B7", "62", "0E", "AA", "18", "BE", "1B"],
    ["FC", "56", "3E", "4B", "C6", "D2", "79", "20", "9A", "DB", "C0", "FE", "78", "CD", "5A", "F4"],
    ["1F", "DD", "A8", "33", "88", "07", "C7", "31", "B1", "12", "10", "59", "27", "80", "EC", "5F"],
    ["60", "51", "7F", "A9", "19", "B5", "4A", "0D", "2D", "E5", "7A", "9F", "93", "C9", "9C", "EF"],
    ["A0", "E0", "3B", "4D", "AE", "2A", "F5", "B0", "C8", "EB", "BB", "3C", "83", "53", "99", "61"],
    ["17", "2B", "04", "7E", "BA", "77", "D6", "26", "E1", "69", "14", "63", "55", "21", "0C", "7D"]
]


# Define the AES round constants as lists of hex string bytes.
ROUND_CONST = [
    ["01", "00", "00", "00"],
    ["02", "00", "00", "00"],
    ["04", "00", "00", "00"],
    ["08", "00", "00", "00"],
    ["10", "00", "00", "00"],
    ["20", "00", "00", "00"],
    ["40", "00", "00", "00"],
    ["80", "00", "00", "00"],
    ["1B", "00", "00", "00"],
    ["36", "00", "00", "00"]
]

MIX_COL_CONST = [
    ["02", "03", "01", "01"],
    ["01", "02", "03", "01"],
    ["01", "01", "02", "03"],
    ["03", "01", "01", "02"]
]

INV_MIX_COL_CONST = [
    ["0E", "0B", "0D", "09"],
    ["09", "0E", "0B", "0D"],
    ["0D", "09", "0E", "0B"],
    ["0B", "0D", "09", "0E"]
]


def hex2bin(s: str) -> str:
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'B': "1011",
          'C': "1100",
          'D': "1101",
          'E': "1110",
          'F': "1111"}
    bin = ""
    for i in range(len(s)):
        bin = bin + mp[s[i]]
    return bin
# Binary to hexadecimal conversion 
def bin2hex(s:str) -> str:
    mp = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'}
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]
 
    return hex
 
# Binary to decimal conversion
def bin2dec(binary:int)->int:
    
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal
 
# Decimal to binary conversion
def dec2bin(num:int)->str:
    res = bin(num).replace("0b", "")
    if(len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res
 
def xor_binary(bin_str1: str, bin_str2: str) -> str:
    result = []
    for b1, b2 in zip(bin_str1, bin_str2):
        result.append('1' if b1 != b2 else '0')
    
    return ''.join(result)
 
def multiply_binary(bin_str1: str, bin_str2: str) -> str:
    result = []
    for b1, b2 in zip(bin_str1, bin_str2):
        result.append('1' if b1 != b2 else '0')
    return ''.join(result)
 #ascii to hex
def str2hex(s):
    return s.encode().hex().upper()
def hex2str(s):
    return bytes.fromhex(s).decode()

def printWords(stateMat: list)->str:
    temp = ""
    for i in range(4):
        for j in range(4):
            temp += stateMat[j][i]
        temp+=" "
    print(temp)
    

def createState(text_hex:str) -> list:
    l = []
    for i in range(0,8,2):
        temp = []
        for j in range(0,len(text_hex),8):
            temp.append(text_hex[i+j:i+j+2])
        l.append(temp)
    return l


def roundkeygen(key_hex:str) -> list:
    roundKeys = [key_hex]
    
    for a in range(1,11):
        prevstate = createState(roundKeys[a-1])
        w = [[],[],[],[],[],[],[],[]]
        for i in range(4):
            for j in range(4):
                w[i].append(prevstate[j][i])
        
        temp_w3 = w[3].copy()
        #g(w[3])
        #1. circluar left shift w[3]
        w[3] = w[3][1:] + w[3][:1]
        #2. sbox
        for j in range(4):
            binary_byte = hex2bin(w[3][j])
            row = int(binary_byte[0:4],2)
            col = int(binary_byte[4:],2)
            s_hex_val = AES_S_BOX[row][col]
            w[3][j] = s_hex_val
        #3. add round constant
        for k in range(4):
            binary_byte1 = hex2bin(w[3][k])
            binary_byte2 = hex2bin(ROUND_CONST[a-1][k])
            round_xor = xor_binary(binary_byte1,binary_byte2)
            # round_xor = dec2bin(round_xor)
            w[3][k] = bin2hex(round_xor)
        
        
        #w[4] = w[0] xor g(w[3])
        for k in range(4):
            binary_byte1 = hex2bin(w[0][k])
            binary_byte2 = hex2bin(w[3][k])
            round_xor = xor_binary(binary_byte1,binary_byte2)
            # round_xor = dec2bin(round_xor)
            w[4].append(bin2hex(round_xor))
        # print(w[4])
        #w[5] = w[4] xor w[1]
        for k in range(4):
            binary_byte1 = hex2bin(w[4][k])
            binary_byte2 = hex2bin(w[1][k])
            round_xor = xor_binary(binary_byte1,binary_byte2)
            # round_xor = dec2bin(round_xor)
            w[5].append(bin2hex(round_xor))
        # print(w[5])
        #w[6] = w[5] xor w[2]
        for k in range(4):
            binary_byte1 = hex2bin(w[5][k])
            binary_byte2 = hex2bin(w[2][k])
            round_xor = xor_binary(binary_byte1,binary_byte2)
            # round_xor = dec2bin(round_xor)
            w[6].append(bin2hex(round_xor))
        # print(w[6])
        
        #w[7] = w[6] xor w[3] OR w[6] xor temp_w3
        # print(w[3])
        for k in range(4):
            binary_byte1 = hex2bin(w[6][k])
            binary_byte2 = hex2bin(temp_w3[k])
            round_xor = xor_binary(binary_byte1,binary_byte2)
            # round_xor = dec2bin(round_xor)
            w[7].append(bin2hex(round_xor))
        # print(w[7])
        
        temp = ""
        for i in range(4):
            for j in range(4):
                temp+=w[i+4][j]
        roundKeys.append(temp)
        
        
    return roundKeys

def encrypt(plain_hex: str, keys:list) -> str:
    print('ehho')

    #! round 0
    stateMat0 = createState(plain_hex)
    keyMat = createState(keys[0])
    xorRound0 = ""
    for i in range(4):
        for j in range(4):
            xorRound0 += bin2hex(xor_binary(hex2bin(stateMat0[j][i]),hex2bin(keyMat[j][i])))

    currStateMat = createState(xorRound0)

    for round in range(1,10):
        #! Round 1 to n

        #! Subbytes
        for r in range(4):
            for c in range(4):
                binary_byte = hex2bin(currStateMat[r][c])
                row = int(binary_byte[0:4],2)
                col = int(binary_byte[4:],2)
                s_hex_val = AES_S_BOX[row][col]
                currStateMat[r][c] = s_hex_val

        #! Shift Row
        currStateMat[1] = currStateMat[1][1:]+ currStateMat[1][:1]
        currStateMat[2] = currStateMat[2][2:]+ currStateMat[2][:2]
        currStateMat[3] = currStateMat[3][3:]+ currStateMat[3][:3]
        #! mix column
        #! not standard integer multiplication. We have to Galois Field
        #! we have to use irreducible polynomial x8+x4+x3+x+1(or 0x11B in hexadecimal)
        newStateMat = [
            ["00","00","00","00"],
            ["00","00","00","00"],
            ["00","00","00","00"],
            ["00","00","00","00"],
        ]
        for i in range(len(MIX_COL_CONST)):
            for j in range(len(currStateMat[0])):
                for k in range(len(currStateMat)):
                    #! result[i][j] += A[i][k] * B[k][j]
                    ans = 0
                    if(MIX_COL_CONST[i][k] == "01"):
                        ans = hex2bin(currStateMat[k][j])

                    elif(MIX_COL_CONST[i][k] == "02"):
                        bin_byte1 = hex2bin(currStateMat[k][j])
                        temp = ""
                        # shift left 2
                        if(bin_byte1[0] == '1'):
                            bin_byte1  = bin_byte1+"0"
                            temp = xor_binary(bin_byte1,"100011011")
                            temp = temp[1:]
                        else:
                            bin_byte1 = bin_byte1[1:]+"0"
                            temp = bin_byte1
                        ans = temp
                    else:
                        bin_byte1 = hex2bin(currStateMat[k][j])
                        temp = ""
                        # shift left 2
                        if(bin_byte1[0] == '1'):
                            bin_byte1  = bin_byte1+"0"
                            temp = xor_binary(bin_byte1,"100011011")
                            temp = temp[1:]
                        else:
                            bin_byte1 = bin_byte1[1:]+"0"
                            temp = bin_byte1

                        ans = xor_binary(hex2bin(currStateMat[k][j]),temp)

                    newStateMat[i][j] = bin2hex(xor_binary(hex2bin(newStateMat[i][j]),ans))
        # print(newStateMat)
        currStateMat = newStateMat

        #! add round key
        keyMat = createState(keys[round])
        xorRound = ""
        for i in range(4):
            for j in range(4):
                xorRound += bin2hex(xor_binary(hex2bin(currStateMat[j][i]),hex2bin(keyMat[j][i])))


        currStateMat = createState(xorRound)
        # print(currStateMat)
    
    for r in range(4):
            for c in range(4):
                binary_byte = hex2bin(currStateMat[r][c])
                row = int(binary_byte[0:4],2)
                col = int(binary_byte[4:],2)
                s_hex_val = AES_S_BOX[row][col]
                currStateMat[r][c] = s_hex_val

        #! Shift Row
    currStateMat[1] = currStateMat[1][1:]+ currStateMat[1][:1]
    currStateMat[2] = currStateMat[2][2:]+ currStateMat[2][:2]
    currStateMat[3] = currStateMat[3][3:]+ currStateMat[3][:3]

    keyMat = createState(keys[10])
    xorRound = ""
    for i in range(4):
        for j in range(4):
            xorRound += bin2hex(xor_binary(hex2bin(currStateMat[j][i]),hex2bin(keyMat[j][i])))

    currStateMat = createState(xorRound)
    # print(currStateMat)
    
    cipher = ""
    for i in range(4):
        for j in range(4):
            cipher += currStateMat[j][i]
    
    return cipher


def decrypt(cipher_hex:str, keys:list)->str:
    keys = keys[::-1]
    
    #! round 0: AddRoundKey
    stateMat0 = createState(cipher_hex)
    keyMat = createState(keys[0])
    xorRound0 = ""
    for i in range(4):
        for j in range(4):
            xorRound0 += bin2hex(xor_binary(hex2bin(stateMat0[j][i]),hex2bin(keyMat[j][i])))

    currStateMat = createState(xorRound0)
    
    print(currStateMat)
    
    for round in range(1,10):
        
        currStateMat[1] = currStateMat[1][3:] + currStateMat[1][:3]
        currStateMat[2] = currStateMat[2][2:]+ currStateMat[2][:2]
        currStateMat[3] = currStateMat[3][1:]+ currStateMat[3][:1]
        print(currStateMat)
        
        #! Subbytes
        for r in range(4):
            for c in range(4):
                binary_byte = hex2bin(currStateMat[r][c])
                row = int(binary_byte[0:4],2)
                col = int(binary_byte[4:],2)
                s_hex_val = INV_AES_S_BOX[row][col]
                currStateMat[r][c] = s_hex_val
        
        # printWords(currStateMat)
        
        #! add round key
        keyMat = createState(keys[round])
        xorRound = ""
        for i in range(4):
            for j in range(4):
                xorRound += bin2hex(xor_binary(hex2bin(currStateMat[j][i]),hex2bin(keyMat[j][i])))


        currStateMat = createState(xorRound)
        # printWords(currStateMat)
        
        
        #! mix column
        #! not standard integer multiplication. We have to Galois Field
        #! we have to use irreducible polynomial x8+x4+x3+x+1(or 0x11B in hexadecimal)
        newStateMat = [
            ["00","00","00","00"],
            ["00","00","00","00"],
            ["00","00","00","00"],
            ["00","00","00","00"],
        ]
        for outer in range(len(INV_MIX_COL_CONST)):
            for middle in range(len(currStateMat[0])):
                for inner in range(len(currStateMat)):
                    #! result[i][middle] += A[i][inner] * B[inner][middle]
                    ans = "00000000"
                    P1 = hex2bin(INV_MIX_COL_CONST[outer][inner])
                    P2 = hex2bin(currStateMat[inner][middle])
                    
                    partial_results = [P2]
                    index = len(P1)-P1.find("1")-1;
                    
                    for i in range(1,index+1):
                        temp = partial_results[i-1]
                        if(temp[0] == '1'):
                            temp  = temp+"0"
                            temp = xor_binary(temp,"100011011")
                            temp = temp[1:]
                        else:
                            temp = temp[1:]+"0"
                        partial_results.append(temp)
                    
                    for i in range(len(P1)):
                        if(P1[i] == "1"):
                            ans = xor_binary(partial_results[len(P1)-i-1],ans)
                        
                    newStateMat[outer][middle] = bin2hex(xor_binary(hex2bin(newStateMat[outer][middle]),ans))
        # printWords(newStateMat)
        currStateMat = newStateMat
    
    currStateMat[1] = currStateMat[1][3:] + currStateMat[1][:3]
    currStateMat[2] = currStateMat[2][2:]+ currStateMat[2][:2]
    currStateMat[3] = currStateMat[3][1:]+ currStateMat[3][:1]
    # print(currStateMat)
    
    #! Subbytes
    for r in range(4):
        for c in range(4):
            binary_byte = hex2bin(currStateMat[r][c])
            row = int(binary_byte[0:4],2)
            col = int(binary_byte[4:],2)
            s_hex_val = INV_AES_S_BOX[row][col]
            currStateMat[r][c] = s_hex_val
    
    # printWords(currStateMat)
    
    #! add round key
    keyMat = createState(keys[10])
    xorRound = ""
    for i in range(4):
        for j in range(4):
            xorRound += bin2hex(xor_binary(hex2bin(currStateMat[j][i]),hex2bin(keyMat[j][i])))


    currStateMat = createState(xorRound)
    
    plain = ""
    for i in range(4):
        for j in range(4):
            plain += currStateMat[j][i]
    
    return plain
    
    
        
        

key = "Thats my Kung Fu"
print("Key in hexadecimal:", str2hex(key))
plain = "Two One Nine Two"
print("Plain: ", str2hex(plain))

plain_hex = str2hex(plain)
key_hex = str2hex(key)

keys = roundkeygen(key_hex)

ciphertext = encrypt(plain_hex,keys)
print(ciphertext)

plaintext = decrypt(ciphertext,keys)
print(hex2str(plaintext))
