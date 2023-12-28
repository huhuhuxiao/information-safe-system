# 简谱数字序列
notations = '111114157166145123145143165162151164171126145162171115165143150'

# 将数字序列每两个划分为一组，并转换为ASCII码
def notations_to_ascii(notations):
    plaintext = ''
    for i in range(0, len(notations), 3):
        # 取两个数字为一组，转换为八进制数
        octave_number = notations[i:i+3]
        # 将八进制数转换为十进制数
        decimal_number = int(octave_number, 8)
        # 将十进制数转换为对应的ASCII字符
        char = chr(decimal_number)
        plaintext += char
    return plaintext

# 进行转换
plaintext = notations_to_ascii(notations)
print('Decrypted text:', plaintext)