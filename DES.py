__author__ = 'NichoEnGiani'

plaintextK = "0 1 2 3 4 5 6 7 8 9 A B C D E F"

initialPermutation = {'58', '50', '42', '34', '26', '18', '10', '2',
                      '60', '52', '44', '36', '28', '20', '12', '4',
                      '62', '54', '46', '38', '30', '22', '14', '6',
                      '64', '56', '48', '40', '32', '24', '16', '8',
                      '57', '49', '41', '33', '25', '17', '9', '1',
                      '59', '51', '43', '35', '27', '19', '11', '3',
                      '61', '53', '45', '37', '29', '21', '13', '5',
                      '63', '55', '47', '39', '31', '23', '15', '7'}

PC1 = [57, 49, 41, 33, 25, 17 , 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 36, 34, 53,
       46, 42, 50, 36, 29, 32 ]

ascii2bin = {"0": "0000",
              "1": "0001",
              "2": "0010",
              "3": "0011",
              "4": "0100",
              "5": "0101",
              "6": "0110",
              "7": "0111",
              "8": "1000",
              "9": "1001",
              "A": "1010",
              "B": "1011",
              "C": "1100",
              "D": "1101",
              "E": "1110",
              "F": "1111"}

def _convertPlain2bin(plaintext):
    K = ""
    print(plaintext)
    for l in plaintext:
        if l != " ":
            K += ascii2bin[l]
    return K

def _permutatePC1(K):
    result = ""
    for p in PC1:
        result += K[p-1]
    return result

def _permutatePC2(K):
    result = ""
    for p in PC2:
        result += K[p-1]
    return result

def _leftShift(K, val):
    K1 = K[0:int(len(K)/2)]
    K2 = K[int(len(K)/2):len(K)]
    return K1[val:len(K1)] + K1[0:val] + K2[val:len(K2)] + K2[0:val]

if __name__ == "__main__":
    print("Welcome to main")
    K = _convertPlain2bin(plaintextK)
    print(K)
    K = _permutatePC1(K)
    print(K)
    K = _leftShift(K, 1)
    print(K)
    K1 = _permutatePC2(K)
    print(K1)