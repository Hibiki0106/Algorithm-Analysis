
from PIL import Image
import random

name = input('enter an image file name ：')
name = name + '.bmp'
puzzle = Image.open( name )


listOfpiece = []
for i in range(1, 10) : # 9 * 16            1 ~ 9
    for j in range(1, 17) : # 1 ~ 16
        
        piece = puzzle.crop((120*(j-1), 120*(i-1), 120*j-1, 120*i-1)) # 左，上，右和下
        # 0 0 119 119    120 0 239 119
        #
        #
        listOfpiece.append( piece )

for a in range(1, 10) :
    for b in range(1, 17) :
        r = random.randrange( 0, len(listOfpiece) ) # random.randrange( 0, 100 )  ->  0 ~ 99
        x = 120 * ( b - 1 )
        y = 120 * ( a - 1 )
        piece = listOfpiece[r]
        puzzle.paste( piece, (x, y) )

        del listOfpiece[r]

tittle = name.split('.')[0] + '_result.bmp'
puzzle.save(tittle)