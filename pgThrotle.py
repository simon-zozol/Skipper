#cette librairie set a bouger un sprite
#avec les 4 touche directionelle du clavier
#Elle utilise pyGame pour gerer les touche
#Le sprite est n'importe quel objet acepteant les fonction suivante
# getX, setX, getY, setY getVx, getVy, setVx, setVy, getAx, getAy, setAx, setAy
# Ceci dit, si les valeur corespondant a la creation de Throtle sont nulle, ces methodes sont optionelle
import pygame

from pgSprite.euclid import Vector2


def isZeroVector(vector):
    return vector.x != 0 and vector.y != 0

#If the given "something" is a vector2 then just return it(not a clone)
#Else, try to return a new vector
def makeVector2(something):
    if isinstance(something, Vector2):
        return something
    else:
        return Vector2(something[0],something[1])

class Throtle:
 #   def __init__(self,sprite, x=0,y=0,vx=0,vy=0,ax=0,ay=0):
    def __init__(self,sprite, deltaPosition=(0,0),deltaSpeed=(0,0),deltaAcceleration=(0,0)): 
        self.sprite = sprite

        self.deltaPosition = makeVector2(deltaPosition)
        self.deltaSpeed  = makeVector2(deltaSpeed)
        self.deltaAcceleration = makeVector2(deltaAcceleration)

    #si touche droite => keyX=-1, gauche=>keyX=+1, haut=>keyY=-1, bas=>key=+1 
    def move(self,keyX, keyY):
        sprite = self.sprite
        
        if self.deltaPosition.__nonzero__() :
            sprite.setVx (self.deltaPosition.x*keyX)
            sprite.setVy (self.deltaPosition.y*keyY)
                 
        if self.deltaSpeed.__nonzero__() :
            sprite.setAx (self.deltaSpeed.x*keyX)
            sprite.setAy (self.deltaSpeed.y*keyY)

        # ca ne gere pas proprement (ou en tout ca diferement) le temp ou on presse la touche 
        if self.deltaAcceleration.__nonzero__() :
            sprite.setAx (sprite.getAx + self.deltaAcceleration.x*keyX)
            sprite.setAy (sprite.getAy + self.deltaAcceleration.y*keyY)
                         
        

    def readKeyboard(self):
        keyX=0
        keyY=0
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            keyX -=1
        if pressed[pygame.K_RIGHT]:
            keyX +=1
        if pressed[pygame.K_UP]:
            keyY -=1
        if pressed[pygame.K_DOWN]:
            keyY +=1
        if keyY != 0 or keyX != 0 :
            self.move(keyX,keyY)

    def __str__(self):
        return mobileToSstr(self)
