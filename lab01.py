# 凯撒密码解密函数
def decrypt_caesar_cipher(ciphertext, initial_shift):
    plaintext = ''
    shift = initial_shift
    for char in ciphertext:

        unshifted_ascii = ord(char) + shift

        plaintext += chr(unshifted_ascii)
        shift = (shift + 1 - initial_shift) % 26 + initial_shift

    return plaintext

# 密文
ciphertext = 'afZ_r9VYfScOeO_UL^RWUc'
# 解密
plaintext = decrypt_caesar_cipher(ciphertext, 5)
print('Caesar Decrypted text:', plaintext)




# 仿射密码
# 扩展欧几里德算法，用于计算逆元
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# 计算乘法逆元 a^-1 mod m
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

# 解密函数 E(x) = a^-1(x - b) mod 26
def decrypt_affine_cipher(ciphertext, a, b):
    a_inv = modinv(a, 26)
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            # 转换字母为0-25的数字，然后使用仿射密码解密函数
            char_num = ord(char) - ord('a')
            decrypted_num = (a_inv * (char_num - b)) % 26
            decrypted_char = chr(decrypted_num + ord('a'))
            plaintext += decrypted_char
        else:
            # 非字母字符保留原样
            plaintext += char
    return plaintext

# 密文
ciphertext = 'welcylk'
# 给定的仿射密码加密函数密钥
a = 11
b = 6

# 解密
plaintext = decrypt_affine_cipher(ciphertext, a, b)
print('Affine Transformation Decrypted text:', plaintext)


