from PIL import Image 

im=Image.open('images\\2_2.jpg')   #读取图片

width=int(im.size[0]/32);
height=int(im.size[1]/32);
fh=open('digits\\testDigits2\\2_2.txt','w')   #数字二进制文件存储地址及文件

for i in range(32):
    for j in range(32): 
        #获取像素点颜色
        colorsum=0;
        for m in range(width):
            for n in range(height):
                color=im.getpixel((j*10+m,i*10+n))
                colorelement=color[0]+color[1]+color[2]
                if(colorelement == 0):
                    colorsum-=1;
                else:
                    colorsum+=1;
     
        if(colorsum<=0):
            fh.write('1')
        else:
            fh.write('0')       
    fh.write('\n')
fh.close()