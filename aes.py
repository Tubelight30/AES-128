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

def encrypt(plain_hex: str, keys:list):
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
        print(currStateMat)
        

key = "Thats my Kung Fu"
print("Key in hexadecimal:", str2hex(key))
plain = "Two One Nine Two"
print("Plain: ",str2hex(plain))

plain_hex = str2hex(plain)
key_hex = str2hex(key)

plainState = createState(plain_hex)
keyState = createState(key_hex)

keys = roundkeygen(key_hex)
encrypt(plain_hex,keys)

# a = 2;
# print(bin(a))
testing = xor_binary("00000000","10001011")
# print(len(testing))
print(testing)
# testing = testing[1:]
# print(testing)

bin_byte1 = hex2bin("2F")
temp = ""
# shift left 2
if(bin_byte1[0] == '1'):
    bin_byte1  = bin_byte1+"0"
    temp = xor_binary(bin_byte1,"100011011")
    temp = temp[1:]
else:
    bin_byte1 = bin_byte1[1:]+"0"
    temp = bin_byte1
ans = xor_binary(hex2bin("2F"),temp)
print(ans)