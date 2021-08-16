import time

from pgSprite import euclid


def mobileToStr(obj):
    position = None
    speed= None
    acceleration = None

    try:
      x=obj.x
    except:
        try:
            x=obj.getX()
        except:
            x="N/A"
    try:
      y=obj.y
    except:
        try:
            y=obj.getY()
        except:
            y="N/A"
    try:
      vx=obj.vx
    except:
        try:
            vx=obj.getVx()
        except:
            vx="N/A"
    try:
      vy=obj.vy
    except:
        try:
            vy=obj.getVy()
        except:
            vy="N/A"
    try:
      ax=obj.ax
    except:
        try:
            ax=obj.getAx()
        except:
            ax="N/A"
    try:
      ay=obj.ay
    except:
        try:
            ay=obj.getAy()
        except:
            ay="N/A"
    return "x="+str(x)+", y="+str(y)+" vx="+str(vx)+", vy="+str(vy) +" ax="+str(ax)+", ay="+str(ay)

# on essaie de transformer un machin en un vector2
# return an euclid.Vector2 object
def trucToVector2(machin):
    try:
        result = euclid.Vector2(machin[0], machin[1])
    except:
        try:
            result = euclid.Vector2(machin.getX(), machin.getY())
        except:
            #If this one fail too, it throw an error
            result = euclid.Vector2(machin.x, machin.y)
    return result
        
        
                        
class Mobile:
        
    def __init__(self,position):
        if type(position)  is euclid.Vector2:
                self.position = position
        else:
                self.position = trucToVector2(position)
        
        self.t0 = time.time()  #top a partir duquel on mesure les temps. Comportement par defaut: c'est le temp du dernier update

        self.speed = euclid.Vector2(0, 0)
        self.acceleration = euclid.Vector2(0, 0)
        

        
    # met a jour position et speed en fonction tu temps ecoule
    # Par defaut, clock = now
    def update(self, clock = None):
        if clock == None: clock = time.time()
        lapse = clock - self.t0

        if self.speed is not None:
            self.position += lapse*self.speed
        if self.acceleration is not None:
            self.speed += lapse*self.acceleration
        
        self.t0=clock # t0 = date de dernier update

    def __str__(self):
        return mobileToStr(self)


#class MobileSurRail(Mobile):
    #TODO l'update est diferent
