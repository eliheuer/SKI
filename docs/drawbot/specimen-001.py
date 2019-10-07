# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com

from drawBot import *
import math

#[W]IDTH,[H]EIGHT,[M]ARGIN,[F]RAMES
W,H,M,F = 1024,512,64,160

# GRID
def grid():
    stroke(2)
    strokeWidth(1)
    rect(M+M, M+M, W-(4*M), H-(4*M))
    stpX, stpY = 0, 0
    incX, incY = M, M
    for x in range(13):
        polygon(((M+M)+stpX, M+M),
                ((M+M)+stpX, H-(M+M)))
        stpX += incX
    for y in range(5):
        polygon((M+M, (M+M)+stpY),
                (W-(M+M), (M+M)+stpY))
        stpY += incY
        
# NEW PAGE
def new_page():
    newPage(W, H)
    frameDuration(1/24)
    fill(0)
    rect(-2, -2, W+2, H+2)

# MAIN
a = 0
font("../../fonts/variable/SKI-VF.ttf")
varWght = 700
flag = False

for axis, data in listFontVariations().items():
    print((axis, data))  # Get axis info from font

for frame in range(F): 
    new_page()
    font("../../fonts/variable/SKI-VF.ttf")
    grid() # Toggle for grid view
    fill(0)
    fill(1)
    
    # Set variations
    fontVariations(wght=varWght)

    stroke(None)
    fill(1)
    fontSize((M*7))
    tracking(None)

    text("كتاب", (M*2, M*3))
    varWght -= 5
    if varWght == 300:
        flag = True
    else:
        pass
        
    if flag == True:
        varWght += 10

    
    print(varWght, frame, flag)

saveImage("../specimens/specimen-001.gif")
