import time

from pgSprite import mobile as libMobile


class Animation:
    def __init__ (self,imageList=[]):
        self.imageList = imageList
        
        self.t0 = time.time()
        self.frequence = 10 #par default, 10 image/sec.
        #Note: si on change la frequence, il faut initialiser t0

    def addImage(image):
        self.imageList.append(image)

    def nbImage(self, clock = None):
        if clock == None: clock = time.time()
        lapse = clock - self.t0
        
        return int((lapse * self.frequence) % len(self.imageList))

    def getImage(self, clock = None):
        return self.imageList[self.nbImage(clock)]

    #par default, on cycle lineairement, mais on peu surcharger pour plus complexe.
    #surtout je fait un sprite generique qui apele animation.update()
    def update(self):
        return

class Sprite:
    def __init__(self, mobile=None, animation=None):
        if mobile==None: mobile = libMobile.Mobile((0,0))        
        if animation==None: animation = Animation()
        
        self.mobile = mobile
        self.animation = animation
        self.alive=True

    def update(self):
        self.mobile.update()
        self.animation.update()

    @property
    def image(self):
        return self.animation.getImage()

    def kill(self):
        self.alive = False

    def __str__(self):
        result = str(self.mobile) + ", image#="+str(self.animation.nbImage())
        return result

    #des racourcis
    def getPosition(self):return self.mobile.position
    def setPosition(self, positionVector):self.mobile.position = positionVector  # TODO: duck typer
    def getX(self):return self.mobile.position.x
    def getY(self):return self.mobile.position.y
    def setX(self, x):self.mobile.position.x = x   
    def setY(self, y):self.mobile.position.y = y
    def getSpeed(self):return self.mobile.speed
    def setSpeed(self, speedVector):self.mobile.speed = speedVector
    def getVx(self):return self.mobile.speed.x
    def getVy(self):return self.mobile.speed.y
    def setVx(self, x):self.mobile.speed.x = x   
    def setVy(self, y):self.mobile.speed.y = y
    def getSpeed(self):return self.mobile.speed
    def setSpeed(self, speedVector):self.mobile.speed = speedVector
    def getAx(self): return self.mobile.acceleration.x
    def getAy(self):return self.mobile.acceleration.y
    def setAx(self, x):self.mobile.acceleration.x = x   
    def setAy(self, y):self.mobile.acceleration.y = y        


