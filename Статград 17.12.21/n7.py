from math import log2

colors = 65536
x = 5
y = 6
dpi = 128

bit_pixel = log2(colors)
File_bits = x * dpi * y * dpi * bit_pixel
File_Kbytes = File_bits // (2 ** 13)
print(File_Kbytes)
