info_tuple = ("小明", 21, 1.85)

# 格式化字符串后面的'()'本质上就是元祖
# print("%s 年龄是 %d 身高是 %.2f" % ("小明", 18, 1.75))
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple

print(info_str)