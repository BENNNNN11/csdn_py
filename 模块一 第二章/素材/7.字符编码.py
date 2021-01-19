print(ord('A'))
print(ord('我'))

print(chr(65))
print(chr(25105))

# 传输和保存  需要对字符进行 编解码，utf-8通用编解码

x = b'ABC' # 字节数组，byte数组

print(x)

# 中文编码范围超过了ASC编码范围，报错
# x = b'你好' # 字节数组，byte数组
#
# print(x)

# 在bytes中，无法显示ASC字符的字节，用\x##来显示
print('你好'.encode('gbk'))
print('ABC'.encode('utf-8'))

print(b'\xc4\xe3\xba\xc3'.decode('gbk'))


# 中文占用多少字节
print(len('你好AB'))

print(len('你好'.encode('utf-8')))
print(len('你好'.encode('gbk')))
