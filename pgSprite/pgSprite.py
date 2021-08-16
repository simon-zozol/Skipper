import pygame

from pgSprite import sprite


class Animation(sprite.Animation):
    def __init__ (self,imageList=[]):
        # on s'assure que toute les image sont de type pyGame.Surface
        properList=[] 
        for image in imageList:
            if  (type(image) is pygame.Surface):
                #image = image.convert_alpha()
                properList.append(image)
            else:
                #ca marche pour un nom de fichier. Peut etre dans d'autre cas
                image = pygame.image.load(image)
                #image = image.convert_alpha()
                properList.append(image)
        super().__init__(properList) 
  

    def addImage(self,image):
        # on s'assure que l'image sont de type pyGame.Surface
        if  isinstance(image, pygame.Surface):
            self.imageList.append(image)
        else:
            #ca marche pour un nom de fichier. Peut etre dans d'autre cas
            image = pygame.image.load(image)
            self.imageList.append(image)

# TODO rendre compatible avec pyGame.Sprite
class Sprite(sprite.Sprite):
    def display(self, screen):
        screen.blit(self.image, (self.getX(), self.getY()))

    @property
    def rect(self):
        image = self.image
        result = pygame.Rect(self.getX(),self.getY(),image.get_width(), image.get_height())
        return result
    
    def collide(self, otherSprite):
        #return self.rect.colliderect(otherSprite.rect)
        return pygame.sprite.collide_mask(self, otherSprite)
    
        
        
