import sys

#Create the image (make sure it's rectangular!)
im = [list('.........##########..............'),
    list('........############.............'),
    list('.......##############............'),
    list('.......##....##....##............'),
    list('.......##....##....##............'),
    list('.......##############............'),
    list('.......##############............'),
    list('........############.............')]

HEIGHT = len(im)
WIDTH = len(im[0])

def floodFill(image, x, y, newChar, oldChar = None):
    if oldChar == None:
        #oldChar defaults to the character at x, y.
        oldChar = image[x][y]
    if oldChar == newChar or image[x][y] != oldChar:    
        #Base Case
        return
    
    image[x][y] = newChar #Change the character.

    #Uncomment to view each step:
    #printImage(image)

    #Change the neighboring characters.
    if y + 1 < HEIGHT and image[y + 1][x] == oldChar:
        #Recursive Case
        floodFill(image, x, y + 1, newChar, oldChar)
    if y - 1 >= 0 and image[y - 1][x] == oldChar:
        #Recursive Case
        floodFill(image, x, y - 1, newChar, oldChar)
    if x + 1 < WIDTH and image[y][x + 1] == oldChar:
        #Recursive Case
        floodFill(image, x + 1, y, newChar, oldChar)
    if x - 1 >= 0 and image[y][x - 1] == oldChar:
        #Recursive Case
        floodFill(image, x - 1, y, newChar, oldChar)
    return #Base Case

def printImage(image):
    for y in range(HEIGHT):
        #Print each row.
        for x in range(WIDTH):
            #Print each column.
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')

printImage(im)
floodFill(im, 4, 4, 'o')
printImage(im)