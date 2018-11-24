import math
class cuboid:
    def __init__(self):
        self.length = self.get_len()
        self.breadth = self.get_bre()
        self.height = self.get_hei()
    def get_len(self):
        return input("=> Enter length: ")
    def get_bre(self):
        return input("=> Enter breadth: ")
    def get_hei(self):
        return input("=> Enter height: ")

class sphere:
    def __init__(self):
        self.radius = self.get_rad()
    def get_rad(self):
        return input("=> Enter radius. ")

class cone:
    def __init__(self):
        self.radius = self.get_rad()
        self.height = self.get_hei()
    def get_rad(self):
        return input("=> Enter the radius. ")
    def get_hei(self):
        return input("=> Enter the height")

class cylinder:
    def __init__(self):
        self.radius = self.get_rad()
        self.height = self.get_hei()
    def get_rad(self):
        return input("=> Enter the radius. ")
    def get_hei(self):
        return input("=> Enter the height")

class truncated_cone:
    def __init__(self):
        self.radiusshort = self.get_rad1()
        self.radiuslong = self.get_rad2()
        self.height = self.get_hei()
    def get_rad1(self):
        return input("=> Enter the shorter radius.")
    def get_rad2(self):
        return input("=> Enter the longer radius.")
    def get_hei(self):
        return input("=> Enter the height.")

class pyramid:
    def __init__(self):
        x = input("If the base of the pyramid is a square press 1, if rectangular press 2 and if triangular, press 3. ")
        print
        if x == 1:
            self.sqside = self.get_side()
            self.A = self.sqside**2
        elif x == 2:
            self.longside = self.get_side()
            self.shortside = self.get_side()
            self.A = self.longside * self.shortside
        elif x == 3:
            self.side1 = self.get_side()
            self.side2 = self.get_side()
            self.side3 = self.get_side()
            self.s = (self.side1+self.side2+self.side3)/2
            self.A = (self.s*(self.s-self.side1)*(self.s-self.side2)*(self.s-self.side3))**0.5
        
        self.height = self.get_hei()

    def get_side(self):
        return input("=> Enter a side of the base. ")
    def get_hei(self):
        return input("=> Enter the height of the pyramid. ")
class prism:
    def __init__(self):
        self.x = input("For normal triangular prism, press. For regular hexagonal prism, press 2. ")
        print
        if self.x == 1:
            self.side1 = self.get_side()
            self.side2 = self.get_side()
            self.side3 = self.get_side()
            self.s = (self.side1+self.side2+self.side3)/2
            self.A = (self.s*(self.s-self.side1)*(self.s-self.side2)*(self.s-self.side3))**0.5
        elif self.x == 2:
            self.side = self.get_side()
        self.height = self.get_hei()
        def get_side(self):
            return input("=> Enter a side of the triangular face. ")
        def get_hei(self):
            return input("=> Enter the height of the prism. ")


class Volume(cuboid,sphere,cone,cylinder,truncated_cone,pyramid,prism):
    def __init__(self):
        print "For cube or cuboid, press 1."
        print "For sphere, press 2."
        print "For cone, press 3."
        print "For cylinder, press 4."
        print "For truncated cone, press 5."
        print "For pyramid, press 6."
        print "For prism, press 7."
        print
        x = input("=> Enter the number of the figure for which you want to calculate the volume. ")
        print
        if x == 1:
            cuboid.__init__(self)
            print
            if self.height == self.breadth == self.length:
                print "The volume of the cube is", self.length * self.breadth * self.height
            else:
                print "The volume of the cuboid is",self.length * self.breadth * self.height

        elif x == 2:
            sphere.__init__(self)
            print
            print "The volume of the sphere is", float((4.0/3.0)*math.pi*(self.radius**3))
        
        elif x == 3:
            cone.__init__(self)
            print
            print "The volume of the cone is", float((1.0/3.0)*math.pi*self.height*(self.radius**2))
        elif x == 4:
            cylinder.__init__(self)
            print
            print "The volume of the cylinder is", float(math.pi*self.height*(self.radius**2))
        elif x == 5:
            truncated_cone.__init__(self)
            print 
            print "The volume of the truncated cone is", float((1.0/3.0)*math.pi*((self.radiusshort**2) + self.radiusshort*self.radiuslong + (self.radiuslong**2))*self.height)
        elif x == 6:
            pyramid.__init__(self)
            print
            print "The volume of triangular pyramid is", float((1.0/3.0)*self.A*self.height)
        elif x == 7:
            prism.__init__(self)
            print
            if self.x == 1:
                print "The volume of the prism is", float(self.A * self.height)
            elif self.x == 2:
                print "The volume of the hexagonal prism is",float((3.0/2.0)*(3**0.5)*self.side*self.side*self.height)
r = Volume()
