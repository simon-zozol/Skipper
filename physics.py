from pgSprite import XYZ

viscuosity = 0.1


# frotement = viscuosite*v
def shaffingPower1(mobile, visco=None):
        if visco == None: visco = viscuosity
        vx = XYZ.getVx(mobile)
        vy = XYZ.getVy(mobile)
        mobile.setAx(mobile.getAx()-visco*vx)
        mobile.setAy(mobile.getAy()-visco*vy)

# frotement = viscuosite*v*v
def shaffingPower2(mobile, visco=None):
        if visco == None: visco = viscuosity
        vx = XYZ.getVx(mobile)
        vy = XYZ.getVy(mobile)
        mobile.setAx(mobile.getAx()-visco*vx*vx)
        mobile.setAy(mobile.getAy()-visco*vy*vy)

#En gros, c'est le bilan des force, mais c'est pas plus complique de faire les acceleratins        
def class AccelerationSum:
    def __init__(self,dictAccX={},dictAccY={}):
        self.dictAccX = dictAccX
        self.dictAccY = dictAccY
