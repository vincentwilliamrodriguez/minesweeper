from mine import Minesweep

m=Minesweep()

def setup():
    size(700,700)
    
def draw():
    background(255)
    
    m.display()
    
    
def mousePressed():
    s=700/9
    
    if not m.over:
        m.op(floor(mouseX/s),floor(mouseY/s))
    
def keyPressed():
    global m
    
    if key=='r' and m.over:
        m=Minesweep()
