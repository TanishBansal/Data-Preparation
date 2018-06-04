
import os

i = 10001
     
for filename in os.listdir("D:\Giscle Internship\data"):
    dst ="image_" + str(i) + ".jpg"
    src =''+ filename
    dst =''+ dst
    os.rename(src,dst)
    i += 1
 
