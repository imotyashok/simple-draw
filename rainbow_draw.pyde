import random

import random

gameScreen = 0

def setup():
    size(500,500)
    background(250,212,0)
    noStroke()
    
def draw():
    if (mousePressed == True):
        if (mouseButton == LEFT):
            ellipse(mouseX,mouseY,33,33)
            fill(random.randint(1,256),random.randint(1,256),random.randint(1,256))
        if (mouseButton == RIGHT):
            background(250,212,0) # clears the previous drawing 
        
        
