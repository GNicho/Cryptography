__author__ = 'NichoEnGiani'

plaintextK = "0 1 2 3 4 5 6 7 8 9 A B C D E F"

ascii2bin = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

PC1 = [57, 49, 41, 33, 25, 17 , 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 36, 34, 53, 46, 42, 50, 36, 29, 32 ]

E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

S_BOXES = {1: [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
         2: [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
         3: [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
         4: [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
         5: [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
         6: [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
         7: [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
         8: [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]}

def _convertPlain2bin(plaintext):
    K = ""
    for l in plaintext:
        if l != " ":
            K += ascii2bin[l]
    return K

def _permutate(K, list):
    result = ""
    for p in list:
        result += K[p-1]
    return result

def _leftShift(K, val):
    K1 = K[0:int(len(K)/2)]
    K2 = K[int(len(K)/2):len(K)]
    return K1[val:len(K1)] + K1[0:val] + K2[val:len(K2)] + K2[0:val]

def _format(string, groupsize):
    pos = 0
    result = ""
    while pos < len(string):
        result += string[pos:pos+groupsize] + " "
        pos += groupsize
    return result

def _binAddition(bin1, bin2):
    pos = 0
    result = ""
    for bit in bin1:
        result += str(int(bin1[pos]) ^ int(bin2[pos]))
        pos += 1
    return result

def _substituteSbox(bin):
    x = 0
    result = []
    while x < int(len(bin) / 6):
        bits = bin[x*6:(x+1)*6]
        row = int((bits[0:1] + bits[5:6]),2)
        col = int(bits[1:5],2)
        result.append("{0:04b}".format(S_BOXES[x+1][row][col]))
        x += 1
    return result

if __name__ == "__main__":
    print("Welcome to DES encryption")
    K = _convertPlain2bin(plaintextK)
    print("Our plaintext in HEX is: " + plaintextK)
    print("To bin: " + _format(K, 4))

    K1 = _permutate(_leftShift(_permutate(K, PC1), 1), PC2)
    print("\nDerive the first subkey K1\nK1: " + _format(K1, 4))

    L0 = _permutate(K, IP)[0:int(len(_permutate(K, IP))/2)]
    R0 = _permutate(K, IP)[int(len(_permutate(K, IP))/2):int(len(_permutate(K, IP)))]
    print("\nDerive L0 and R0\nL0:" + _format(L0, 4) + "\nR0:" + _format(R0, 4))

    ER0 = _permutate(R0, E)
    print("\nExpand R0 to get E[R0]\nE[R0]: " + _format(ER0, 6))

    print("\nCalculate A=E[R0]+K1")
    A = _binAddition(ER0, K1)
    print("A: " + _format(A, 6))

    print("\nCalculate S-box substitutions")
    SBOX = _substituteSbox(A)
    print("Sj Bj: " + _format(A, 6))
    for val in SBOX:
        print("S-box"+ str(SBOX.index(val)+1) + " => " + val)