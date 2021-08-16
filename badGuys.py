import random

from pgSprite import pgSprite


class BadGuy(pgSprite.Sprite):
    # variable statique. ils ont tous la meme anim
    animationBadGuy = pgSprite.Animation(['mechant1-c.png','mechant2-c.png','mechant3-c.png','mechant4-c.png','mechant5-c.png'])
    animationBadGuy.frequence=2

    listBadGuy =[]

    #Factory that send bad guy with random trajectory
    #That is partly random initial Y, speed and acceleration
    def newBadGuyRandom():
        sprite = BadGuy()
        sprite.animation = BadGuy.animationBadGuy
        sprite.mobile.position.x = 1000
        sprite.mobile.position.y = random.randrange(50, 750, 1)
        sprite.mobile.speed.x = random.randrange(-200, -40)
        sprite.mobile.speed.y = random.randrange(-60, +60)
        sprite.mobile.acceleration.x = random.randrange(-80, +80)
        sprite.mobile.acceleration.y = random.randrange(-80, +80)
        
        if paramValid(sprite):
            BadGuy.listBadGuy.append(sprite)
            return sprite
        else:
            return BadGuy.newBadGuyRandom()

     #on surcharge update pour tuer le sprite s'il sort par le fond   
    def update(self):
        super().update()
        if self.getX() < -100 :
            self.kill()
            BadGuy.listBadGuy.remove(self)
            #avec un peu de chance, a la sortie de cette methode, le ramasse miette fait son oeuvre

    # MEthode statique pour tester colision entre 1 sprite (a priori le heros)
    # et tout les mechant de la liste
    # Return false si pas de colision. return le badGuy si colision
    def collideAny(ennemy):
        for badGuy in BadGuy.listBadGuy :
            if badGuy.collide(ennemy):
                return badGuy
        return False

#position qu'un mobile aura au temp t
#renvois un euclyd.Vector2
def pos(mobile,t):
        # on attend un mobile. Si on a un Sprite, on prend Sprite.Mobile
        if isinstance(mobile, pgSprite.Sprite):
            mobile = mobile.mobile
            
        return mobile.position + t*mobile.speed + 0.5*t*t*mobile.acceleration
        

     #   Les param du sprite sont en partie aleatoire
     # plutot que de me prendere le chou, je teste la position anticipe
     # en 4 instant different et je rejette si ca sort d'un certain cadre
def paramValid(sprite):
        # on teste a 3 moment diferent (2s,4s,6s) si le sprite ne sort pas verticalement
        for t in (2,4,6):
            forcastPos = pos(sprite.mobile, t)
            if forcastPos.y >820 or forcastPos.y < -20 :
                return False
            if t==2 and forcastPos.x < 100: #too fast
                return False

        if pos(sprite.mobile, 10).x > 0: # si le sprite n'est pas sortie par le fond apres 10s
            return False
        #Si le sprite n'a pas ete rejete, on renvoi True
        return True
            


                
            
        
    
