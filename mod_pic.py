# -*- coding:utf-8 -*-

import random
import sys

from PIL import Image, ImageDraw

print("请将此脚本与需要处理的图片放在同一文件夹内\n")
filepath = input("请输入要处理的图片名：")

add_point = input("是否加点[Y|n][默认添加]:")
if len(add_point) == 0:
    add_point = 'y'

add_line = input("是否加线[Y|n][默认添加]:")
if len(add_line) == 0:
    add_line = 'y'

color = input("设置填充颜色，输入想要颜色的英文名即可，如[red]，默认黑色：")
if len(color) == 0:
    color = "black"

pic = Image.open(filepath)
w, h = pic.size
oldname = filepath
newname = 'new_' + oldname

draw = ImageDraw.Draw(pic)

if "y" or "Y" in add_point:
    for i in range(int((w + h) / 2)):
        point_x = random.randint(0, w)
        point_y = random.randint(0, h)
        # draw.point([point_w, point_h], 'black')
        draw.ellipse((point_x, point_y, point_x + 3, point_y + 3), color, color)

if "y" or "Y" in add_line:
    for i in range(int(w / 4)):
        line_x = random.randint(0, w)
        line_y = random.randint(0, h)
        line_xx = random.randint(line_x - 200, line_x + 150)
        line_yy = random.randint(line_y - 200, line_y + 150)
        draw.line([(line_x, line_y), (line_xx, line_yy)], fill=color, width=2)

pic.save(newname)
print("已经保存为" + newname + ",按任意键退出程序~")
exit = input("")
if len(exit) != 0:
    sys.exit()
