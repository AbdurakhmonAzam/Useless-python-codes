def a():
    spam='Ant'
    print('spam is '+spam)
    b()
    print('spam is '+spam)

def b():
    spam='Boobycat'
    print('spam is '+spam)
    c()
    print('spam is '+spam)

def c():
    spam='Lemonade'
    print('spam is '+spam)
    d()
    print('spam is '+spam)

def d():
    spam='Samurai'
    print('spam is '+spam)

a()