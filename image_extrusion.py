from PIL import Image
import numpy
import sys
numpy.set_printoptions(threshold=sys.maxsize)

frames = []
for i in range(35,3,-1):
    im = Image.open("lights/lights "+"("+str(i+1)+").png")
    np_im = numpy.array(im)
    frames.append(np_im)

base=frames[0]
touched=set()
for i in range(1,32): 
    print(i)
    nxt=frames[i]
    for i in range(720):
        for j in range(1280):
            base_rgb=(base[i][j][0],base[i][j][1],base[i][j][2])
            next_rgb=(nxt[i][j][0],nxt[i][j][1],nxt[i][j][2])
            diff=0
            for k in range(3):
                diff+=abs(int(base_rgb[k])-int(next_rgb[k]))
            if diff > 325:
                if (i,j) not in touched:
                    base[i][j]=nxt[i][j]
                    touched.add((i,j))


        
new_im = Image.fromarray(base)
new_im.save("extruded.png")