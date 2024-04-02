s_matrix0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]
s_matrix1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]
s0 = 0
s1 = 0
row = 0
col = 0
s0_binary = [0, 0]
s1_binary = [0, 0]
result = [0, 0]
def to_digit(a, b):
    output = 0
    if a == 1 and b == 1:
        output = 3
    if a == 0 and b == 1:
        output = 1
    if a == 1 and b == 0:
        output = 2
    if a == 0 and b == 0:
        output = 0
    return output
def to_binary(num):
    if num == 3:
        result[0] = 1
        result[1] = 1
    elif num == 1:
        result[0] = 0
        result[1] = 1
    elif num == 2:
        result[0] = 1
        result[1] = 0
    elif num == 0:
        result[0] = 0
        result[1] = 0
k1 = [0] * 8
k2 = [0] * 8
afterp10 = [0] * 11
ls1 = [0] * 10
ls2 = [0] * 10
afterip = [0] * 8
afterep = [0] * 8
afterp4 = [0] * 4
aftersboxesone = [0] * 4
aftersboxestwo = [0] * 4
leftafterip = [0] * 4
rightafterip = [0] * 4
leftafterep = [0] * 4
rightafterep = [0] * 4
leftafterone = [0] * 4
rightafterone = [0] * 4
afteripinverse = [0] * 8
afterone = [0] * 8
aftertwo = [0] * 8
p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
p8 = [6, 3, 7, 4, 8, 5, 10, 9]
ip = [2, 6, 3, 1, 4, 8, 5, 7]
ep = [4, 1, 2, 3, 2, 3, 4, 1]
p4 = [2, 4, 3, 1]
ipinverse = [4, 1, 3, 5, 7, 2, 8, 6]
key = [0] * 11
plain = [0] * 8
print("S-DES Key Generation and Encryption.")
print("\n----------------------------------")
print("\n          KEY GENERATION          ")
print("\n----------------------------------")
key_input = input("\nEnter the 10-bit key: ")
key = [int(x) for x in key_input]
print("P10 Permutation is defined as: ", end="")
for i in range(10):
    print(p10[i], end=" ")
    index = p10[i]
    afterp10[i] = key[index - 1]
afterp10[i] = '\0'
print("\nAfter P10 = ", end="")
for i in range(10):
    print(afterp10[i], end=" ")
for i in range(5):
    if i == 4:
        ls1[i] = afterp10[0]
    else:
        ls1[i] = afterp10[i + 1]
for i in range(5, 10):
    if i == 9:
        ls1[i] = afterp10[5]
    else:
        ls1[i] = afterp10[i + 1]
print("\nAfter LS-1 = ", end="")
for i in range(10):
    print(ls1[i], end=" ")
print("\nP8 Permutation is defined as: ", end="")
for i in range(8):
    print(p8[i], end=" ")
index = 0
for i in range(10):
    index = p8[i]
    k1[i] = ls1[index - 1]
print("\nKey-1 is: ", end="")
for i in range(8):
    print(k1[i], end=" ")
for i in range(3):
    ls2[i] = ls1[i + 2]
ls2[3] = ls1[0]
ls2[4] = ls1[1]
for i in range(5, 8):
    ls2[i] = ls1[i + 2]
ls2[8] = ls1[5]
ls2[9] = ls1[6]
print("\nAfter LS-2 = ", end="")
for i in range(10):
    print(ls2[i], end=" ")
print("\nP8 Permutation is defined as: ", end="")
for i in range(8):
    print(p8[i], end=" ")
index = 0
for i in range(10):
    index = p8[i]
    k2[i] = ls2[index - 1]
print("\nKey-2 is: ", end="")
for i in range(8):
    print(k2[i], end=" ")
print("\n\n----------------------------------- ")
print("\n          S-DES ENCRYPTION          ")
print("\n----------------------------------- ")
plain_input = input("\nEnter the 8-bit plaintext: ")
plain = [int(x) for x in plain_input]
print("Initial Permutation is defined as: ", end="")
for i in range(8):
    print(ip[i], end=" ")
for i in range(8):
    index = ip[i]
    afterip[i] = plain[index - 1]
afterip[i] = '\0'
print("\nAfter IP = ", end="")
for i in range(8):
    print(afterip[i], end=" ")
print("\nExpand Permutation is defined as: ", end="")
for i in range(8):
    print(ep[i], end=" ")
for j in range(4):
    leftafterip[j] = afterip[j]
for j in range(4):
    rightafterip[j] = afterip[j + 4]
for i in range(4):
    index = ep[i]
    afterep[i] = rightafterip[index - 1]
for i in range(4, 8):
    index = ep[i]
    afterep[i] = rightafterip[index - 1]
afterep[i] = '\0'
print("\nAfter EP = ", end="")
for i in range(8):
    print(afterep[i], end=" ")
for i in range(8):
    k1[i] = k1[i] ^ afterep[i]
print("\nAfter XOR operation with 1st Key= ", end="")
for i in range(8):
    print(k1[i], end=" ")
row = to_digit(k1[0], k1[3])
col = to_digit(k1[1], k1[2])
s0 = s_matrix0[row][col]
to_binary(s0)
for j in range(2):
    s0_binary[j] = result[j]
row = to_digit(k1[4], k1[7])
col = to_digit(k1[5], k1[6])
s1 = s_matrix1[row][col]
to_binary(s1)
for j in range(2):
    s1_binary[j] = result[j]
for j in range(2):
    aftersboxesone[j] = s0_binary[j]
for i in range(2):
    aftersboxesone[i + 2] = s1_binary[i]
print("\nAfter first S-Boxes= ", end="")
for i in range(4):
    print(aftersboxesone[i], end=" ")
print("\nP4 is defined as: ", end="")
for i in range(4):
    print(p4[i], end=" ")
for i in range(4):
    index = p4[i]
    afterp4[i] = aftersboxesone[index - 1]
afterp4[i] = '\0'
print("\nAfter P4= ", end="")
for i in range(4):
    print(afterp4[i], end=" ")
for i in range(4):
    afterp4[i] = afterp4[i] ^ leftafterip[i]
print("\nAfter XOR operation with left nibble of after IP= ", end="")
for i in range(4):
    print(afterp4[i], end=" ")
for i in range(4):
    afterone[i] = rightafterip[i]
for i in range(4, 8):
    afterone[i] = afterp4[i - 4]
afterone[i] = '\0'
print("\nAfter first part= ", end="")
for i in range(8):
    print(afterone[i], end=" ")
for j in range(4):
    leftafterone[j] = afterone[j]
for j in range(4):
    rightafterone[j] = afterone[j + 4]
print("\nExpand Permutation is defined as: ", end="")
for i in range(8):
    print(ep[i], end=" ")
for i in range(4):
    index = ep[i]
    afterep[i] = rightafterone[index - 1]
for i in range(4, 8):
    index = ep[i]
    afterep[i] = rightafterone[index - 1]
afterep[i] = '\0'
print("\nAfter second EP = ", end="")
for i in range(8):
    print(afterep[i], end=" ")
for i in range(8):
    k2[i] = k2[i] ^ afterep[i]
print("\nAfter XOR operation with 2nd Key= ", end="")
for i in range(8):
    print(k2[i], end=" ")
row = to_digit(k2[0], k2[3])
col = to_digit(k2[1], k2[2])
s0 = s_matrix0[row][col]
to_binary(s0)
for j in range(2):
    s0_binary[j] = result[j]
row = to_digit(k2[4], k2[7])
col = to_digit(k2[5], k2[6])
s1 = s_matrix1[row][col]
to_binary(s1)
for j in range(2):
    s1_binary[j] = result[j]
for j in range(2):
    aftersboxestwo[j] = s0_binary[j]
for i in range(2):
    aftersboxestwo[i + 2] = s1_binary[i]
print("\nAfter second S-Boxes= ", end="")
for i in range(4):
    print(aftersboxestwo[i], end=" ")
print("\nP4 is defined as: ", end="")
for i in range(4):
    print(p4[i], end=" ")
for i in range(4):
    index = p4[i]
    afterp4[i] = aftersboxestwo[index - 1]
afterp4[i] = '\0'
print("\nAfter P4= ", end="")
for i in range(4):
    print(afterp4[i], end=" ")
for i in range(4):
    afterp4[i] = afterp4[i] ^ leftafterone[i]
print("\nAfter XOR operation with left nibble of after first part= ", end="")
for i in range(4):
    print(afterp4[i], end=" ")
for i in range(4):
    aftertwo[i] = afterp4[i]
for i in range(4, 8):
    aftertwo[i] = rightafterone[i - 4]
aftertwo[i] = '\0'
print("\nAfter second part= ", end="")
for i in range(8):
    print(aftertwo[i], end=" ")
print("\nInverse Initial Permutation is defined as: ", end="")
for i in range(8):
    print(ipinverse[i], end=" ")
for i in range(8):
    index = ipinverse[i]
    afteripinverse[i] = aftertwo[index - 1]
afteripinverse[j] = '\0'
print("\n\n----------------------------------------------------------------------")
print("\n             8-bit Ciphertext will be: ", end="")
for i in range(8):
    print(afteripinverse[i], end=" ")
print("\n\n----------------------------------------------------------------------")
