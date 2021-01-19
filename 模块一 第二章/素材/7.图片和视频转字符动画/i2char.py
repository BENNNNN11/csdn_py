from PIL import Image  # 图片处理模块
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

# 获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 转换的字符集合，共70个，可自己优化添加，越多越逼真，每个字符对应一种或者几种亮度
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    # alpha 值为 0 的时候表示图片中该位置为空白
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    # 把RGB色域转换成灰度图 ，使用权重
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # ascii_char有70个，把256个灰度值分成70组
    unit = (256.0 + 1)/length
    # 当前像素的灰度属于70个组中的哪个组
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    # 1.通过PiL模块加载一张图片到内存
    im = Image.open(IMG)
    # 2.设置图片的尺寸
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
    txt = ""
    # 3.遍历提取图片中每行的像素的 RGB 值，调用 getchar 转成对应的字符
    for i in range(HEIGHT):
        for j in range(WIDTH):
            # 获取得到坐标 (j,i) 位置的 RGB 像素值（有的时候会包含 alpha 值），
            # 返回的结果是一个元组，例如 (1,2,3) 或者 (1,2,3,0)
            # 4.将所有的像素对应的字符拼接在一起成为一个字符串 txt
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    # 5.打印输出字符串 txt
    print(txt)
    
    # 6.如果执行时配置了输出文件，将打开文件将 txt 输出到文件，如果没有，
    # 则默认输出到 output.txt 文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)