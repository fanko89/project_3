def a():
    b()
    d()

def b():
    c()

def c():
    pass

def d():
    pass

a()