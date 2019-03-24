from PIL import Image, ImageDraw, ImageFont
#import PILimage
from sys import *
import linecache
import mimetypes
import requests
import secrets
import xdrlib
import sys
import os

#CODE COMMENTS
#// You should not comment on the first and second line of your fournace code
#// You should define the type on the first line to avoid error

#FILE PATH
filePath = str(input('File to compile (only the file name, not the extension): ')) + ".frnc"

#COUNT NUMBER OF LINE IN THE CODE
countLine = 1
for line in open(filePath): countLine += 1

#INITIALIZE THE CACHE FOLDER
if not os.path.exists("cache"):
    os.makedirs("cache")

#INITIALIZE THE IMAGE FOLDER
if not os.path.exists("image"):
    os.makedirs("image")


#///////////////////////////////////////////////////#
#SQUARE FUNCTIONS
def get_sizeSquare(i):
    return linecache.getline(filePath, i).split()[5]

#RECTANGLE FUNCTIONS
def get_widthRectangle(i):
    return linecache.getline(filePath, i).split()[5]

def get_heightRectangle(i):
    return linecache.getline(filePath, i).split()[6]

#ONIMAGE RESERVED FUNCTIONS
#SQUARE
def get_posXSquare(i):
    return linecache.getline(filePath, i).split()[6]

def get_posYSquare(i):
    return linecache.getline(filePath, i).split()[7]

#SQUARE & RECTANGLE FUNCTIONS
def get_R(i):
    return linecache.getline(filePath, i).split()[1]

def get_G(i):
    return linecache.getline(filePath, i).split()[2]

def get_B(i):
    return linecache.getline(filePath, i).split()[3]

def get_A(i):
    return linecache.getline(filePath, i).split()[4]

#RECTANGLE
def get_posXRectangle(i):
    return linecache.getline(filePath, i).split()[7]

def get_posYRectangle(i):
    return linecache.getline(filePath, i).split()[8]

#TEXT
#POSITIONS
def get_posXText(i):
    return linecache.getline(filePath, i).split()[6]

def get_posYText(i):
    return linecache.getline(filePath, i).split()[7]

#SIZE
def get_sizeText(i):
    return linecache.getline(filePath, i).split()[5]

#FONT FAMILY    
def get_fontFamilyText(i):
    return linecache.getline(filePath, i).split()[8]

#TEXT (on the text)
def get_textText(i):
    textText = ''
    for words in linecache.getline(filePath, i).split()[9:]:
        textText += ''.join(words) + ' '

    textText = textText[:-1]
    return textText

#GET IMAGE FROM URL
#DOWNLOAD IMAGE FROM URL
def get_imageUrl(i):
    return linecache.getline(filePath, i).split()[1]

#IMAGE NAME
def get_exportImageName(i):
    return linecache.getline(filePath, i).split()[2]
    
#PUT AN IMAGE
#GET THE IMAGE NAME
def get_imageName(i):
    return linecache.getline(filePath, i).split()[1]
    
#IMAGE POSX
def get_imagePosX(i):
    return linecache.getline(filePath, i).split()[2]
    
#IMAGE POSY
def get_imagePosY(i):
    return linecache.getline(filePath, i).split()[3]
#///////////////////////////////////////////////////#



#VARIABLES
tmpNbrName = 1

#TRY TO DEFINE THE BIG TYPE
def searchBigType():
    try:
        return linecache.getline(filePath, 1).split()[1]
    except:
        print("\nBigTypeNotFound[1]: The big type is not defined! (BigType: onimg, lbyl)")
        sys.exit()


#COMPILE THE CODE
if __name__ == "__main__":
    #TYPE LBYL -> EXPORT LINE BY LINE
    if searchBigType() == "lbyl":
        for i in range(1, countLine):
            #print(linecache.getline(filePath, i))
            #CATCH VOID ERROR WITH A -> TRY, EXCEPT
            try:
                #DETECT RECTANGLE TYPE
                if str(linecache.getline(filePath, i).split()[0]) == "rectangle":
                    img = Image.new('RGBA', (int(get_widthRectangle(i)), int(get_heightRectangle(i))), (int(get_R(i)), int(get_G(i)), int(get_B(i)), int(get_A(i))))

                    #SAVE WITH THE TYPE NAME + CURRENT LINE NUMBER
                    img.save('rectangle_' + str(tmpNbrName) + '.png')
                    #ADD 1 TO THE CURRENT LINE NUMBER
                    tmpNbrName += 1

                #DETECT SQUARE TYPE
                elif str(linecache.getline(filePath, i).split()[0]) == "square":
                    img = Image.new('RGBA', (int(get_sizeSquare(i)), int(get_sizeSquare(i))), (int(get_R(i)), int(get_G(i)), int(get_B(i)), int(get_A(i))))
                    
                    #SAVE WITH THE TYPE NAME + CURRENT LINE NUMBER
                    img.save('square_' + str(tmpNbrName) + '.png')
                    #ADD 1 TO THE CURRENT LINE NUMBER
                    tmpNbrName += 1

                #DETECT COMMENT
                elif str(linecache.getline(filePath, i).split()[0]).startswith("#"):
                    True

                #TYPE NOT FOUND
                else:
                    if str(linecache.getline(filePath, i).split()[0]) != "type": 
                        print("TypeNotFound[0]: The type on line " + str(i) + " was not found!")
                        sys.exit()
                    else:
                        True

            #VOID ERROR -> PRINT
            except:
                True    

    #TYPE ONIMG -> ADD POSX AND POSY
    elif searchBigType() == "onimg":
        #DEFINE THE BACKGROUND IMAGE -> NO COMMENT HERE
        render = Image.new('RGBA', (int(get_widthRectangle(2)), int(get_heightRectangle(2))), (int(get_R(2)), int(get_G(2)), int(get_B(2)), int(get_A(2))))
        for i in range(1, countLine):
            #print(linecache.getline(filePath, i))
            #CATCH VOID ERROR WITH A -> TRY, EXCEPT
            try:
                #DETECT RECTANGLE TYPE
                if str(linecache.getline(filePath, i).split()[0]) == "rectangle":
                    img = Image.new('RGBA', (int(get_widthRectangle(i)), int(get_heightRectangle(i))), (int(get_R(i)), int(get_G(i)), int(get_B(i)), int(get_A(i))))

                    #PASTE THE IMAGE TO THE RENDER THEN DELETE IT
                    img.save('rectangle_' + str(tmpNbrName) + '.png')
                    img = Image.open('rectangle_' + str(tmpNbrName) + '.png')
                    render.paste(img, (int(get_posXRectangle(i)), int(get_posYRectangle(i))))
                    os.remove('rectangle_' + str(tmpNbrName) + '.png')
                    render.save('render.png')
                    #ADD 1 TO THE CURRENT LINE NUMBER
                    tmpNbrName += 1

                #DETECT SQUARE TYPE
                elif str(linecache.getline(filePath, i).split()[0]) == "square":
                    img = Image.new('RGBA', (int(get_sizeSquare(i)), int(get_sizeSquare(i))), (int(get_R(i)), int(get_G(i)), int(get_B(i)), int(get_A(i))))
                    
                    #PASTE THE IMAGE TO THE RENDER THEN DELETE IT
                    img.save('square_' + str(tmpNbrName) + '.png')
                    img = Image.open('square_' + str(tmpNbrName) + '.png')
                    render.paste(img, (int(get_posXSquare(i)), int(get_posYSquare(i))))
                    os.remove('square_' + str(tmpNbrName) + '.png')
                    render.save('render.png')
                    #ADD 1 TO THE CURRENT LINE NUMBER
                    tmpNbrName += 1

                #DETECT TEXT TYPE
                elif str(linecache.getline(filePath, i).split()[0]) == "text":
                    #FONT TYPE (+size)
                    fnt = ImageFont.truetype(str(get_fontFamilyText(i)), int(get_sizeText(i)))
                    d = ImageDraw.Draw(render)
                    d.text((int(get_posXText(i)),int(get_posYText(i))), str(get_textText(i)), font=fnt, fill=(int(get_R(i)), int(get_G(i)), int(get_B(i)), int(get_A(i))))
                    #SAVE FINAL RESULT
                    render.save('render.png')
                    #d.save('render.png')

                #DETECT URL IMG
                elif str(linecache.getline(filePath, i).split()[0]) == "getImgFromUrl":
                    #TRY
                    try:
                        #DOWNLOAD THE IMAGE FROM THE URL - DECLARATION
                        url = get_imageUrl(i)
                        imgName = get_exportImageName(i)
                        #REQUEST
                        response = requests.get(url)
                        #DOWNLOAD THE IMAGE
                        if response.status_code == 200:
                            with open("image/" + imgName, 'wb') as f:
                                f.write(response.content)
                        #ADD 1 TO THE CURRENT LINE NUMBER
                        tmpNbrName += 1
                    except:
                        print("ImageNotFound[3]: The image on line " + str(i) + " wasn't found!")
                        sys.exit()
                        
                #PUT IMG
                elif str(linecache.getline(filePath, i).split()[0]) == "putImg":
                    #TRY
                    try:
                        #CHECK FILE EXISTANCE
                        fh = open("image/" + get_imageName(i), "r")
                        #PASTE IT
                        img = Image.open("image/" + get_imageName(i))
                        render.paste(img, (int(get_imagePosX(i)), int(get_imagePosY(i))))
                        #SAVE THE RENDER
                        render.save("render.png")
                        #ADD 1 TO THE CURRENT LINE NUMBER
                        tmpNbrName += 1
                    except:
                        print("\nImageNotFound[3]: The image on line " + str(i) + " wasn't found!")
                        sys.exit()

                #DETECT COMMENT
                elif str(linecache.getline(filePath, i).split()[0]).startswith("#"):
                    True

                #KILL ERROR
                elif str(linecache.getline(filePath, i).split()[0]) == "background":
                    True

                #TYPE NOT FOUND
                else:
                    if str(linecache.getline(filePath, i).split()[0]) != "type": 
                        print("\nTypeNotFound[0]: The type on line " + str(i) + " was not found!")
                        sys.exit()
                    else:
                        True

            #VOID ERROR -> PRINT
            except:
                True    
                    
        render.save('render.png')

    #BIG TYPE NOT FOUND ERROR
    else:
        print("\nBigTypeNotFound[1]: The big type is not defined! (BigType: onimg, lbyl)")
        sys.exit()
    
