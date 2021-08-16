import pygame

class TextZone:
    try: 
        defaultFont = pygame.font.Font(None,50)
    except:
        pygame.init()
        defaultFont = pygame.font.Font(None,50)
    
    def __init__(self, topLeft, bottomRight, font=None):
        if font is None:
            self.font = TextZone.defaultFont
        else:
            self.font = font

        self.topLeft = topLeft
        self.bottomRight = bottomRight

    def write(self, text, screen, color=(255,255,255,0)):
        #pygame.draw.rect(self.screen, BLACK, [0, 0, 1000, 100])
        #On converti le text en un bitmap (surface pygame)
        text = self.font.render(text, True, color)
        screen.blit(text,self.topLeft)
        
