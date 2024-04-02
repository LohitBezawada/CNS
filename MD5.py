# Rotate left function
def left_rotate(x, amount):
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

# Initial hash values
a = 0x67452301
b = 0xEFCDAB89
c = 0x98BADCFE
d = 0x10325476

# Initialize the message
inputstring = input("Enter the message to find its MD5 Message Digest: ")
# inputstring = "This is a message sent by a computer user."
input_bytes = bytearray(inputstring, "utf-8")

# Pre-processing: padding the message
original_length = len(input_bytes) * 8
input_bytes.append(0x80)
while (len(input_bytes) * 8) % 512 != 448:
    input_bytes.append(0x00)
input_bytes += original_length.to_bytes(8, byteorder="little")

# Process the message in 512-bit blocks
for i in range(0, len(input_bytes), 64):
    chunk = input_bytes[i : i + 64]
    # Initialize hash values for this chunk
    aa, bb, cc, dd = a, b, c, d
    # Round 1
    for j in range(0, 64):
        f, g = 0, 0
        if j < 16:
            f = (bb & cc) | ((~bb) & dd)
            g = j
        elif j < 32:
            f = (dd & bb) | ((~dd) & cc)
            g = (5 * j + 1) % 16
        elif j < 48:
            f = bb ^ cc ^ dd
            g = (3 * j + 5) % 16
        else:
            f = cc ^ (bb | (~dd))
            g = (7 * j) % 16

        temp = dd
        dd = cc
        cc = bb
        bb = (
            bb
            + left_rotate(
                (
                    aa
                    + f
                    + int.from_bytes(chunk[4 * g : 4 * g + 4], "little")
                    + [0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xA953FD4E][j // 16]
                )
                & 0xFFFFFFFF,
                [7, 12, 17, 22][j // 16],
            )
        ) & 0xFFFFFFFF
        aa = temp

    # Update hash values for this chunk
    a = (a + aa) & 0xFFFFFFFF
    b = (b + bb) & 0xFFFFFFFF
    c = (c + cc) & 0xFFFFFFFF
    d = (d + dd) & 0xFFFFFFFF

# Concatenate hash values
result = (
    a.to_bytes(4, byteorder="little")
    + b.to_bytes(4, byteorder="little")
    + c.to_bytes(4, byteorder="little")
    + d.to_bytes(4, byteorder="little")
)

# Convert hash values to hex
hash_hex = "".join(format(byte, "02x") for byte in result)
print("Hash of the input string:")
print(hash_hex)
