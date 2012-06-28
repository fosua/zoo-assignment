class zoo:
    def __init__ (self,size,colour,name):
        self.name=name
        self.size = size
        self.colour = colour

class Animal(zoo):
	 def __init__ (self,feed,movement,reproduce,respirate):
	 zoo. __init__ (self,size,colour)
         self.feed = feed
         self.movement = movement
         self.reproduce = reproduce
         self.respirate = respirate
        
class structures(zoo):
    def __init__ (self,space,materials,shapes,functions):
    zoo. __init__(self,size,colour,name):
        self.space=space
        self.materials=materials
        self.shapes=shapes
        self.functions=functions
 
class buildings(structures):
    def __init__(self,roofing_used):
    structures.__init__(self,space,materials,shapes,functions):
        self.roofing_used=roofing_used
        print 'the roofing:'+roofing_used
    
class enclosures(structures):
    def __init__(self,shelter_provided)
    structures. __init__ (self,space,materials,shapes,functions):
        self.shelter_provided=shelter_provided
        print animals,'live in',shelter_provided
class people(zoo):
    def __init__(self,position):
        zoo. __init__(self,size,colour)
        self.position=position
class visitors(people):
    def __init__(self,photos):
    people. __init__(self,position):
        self.photos=photos
class staff(people):
    def __init__(self,id,salary):
    people. __init__(self,position):
        self.id=id
        self.position=position
    
    def identify(self):
        print'name:'+self.name
        print 'size:'+self.size
        print 'colour:'+self.colour
        print'material:'+self.material
        print'home:'+self.shelter_provided
        print'position:'+self.position
        print'id:'+self.id
        print'photos_taken'+self.photos_taken

class Mammals(Animals):
    
    def __init__ (self,hair,warm_blooded):
    Animals. __init(self, feed,movement, reproduce, respirate):
        self.hair= hair
        self.warm_blooded = warm_blooded
class Fishes(Animals):
    def __init__ (self,habitat_water, streamlined_body):
    Animals. __init(self, feed,movement, reproduce, respirate):
        self.habitat_water = habitat_water
        self.streamlined_body = streamlined_body
class Birds(Animals):
    def __init__ (self,wings,peaks, feathers):
    Animals. __init(self, feed,movement, reproduce, respirate):
        self.wings = wings
        self.beak = beak
        self.feathers = feathers
    def havewings(self):
        return self.wings
class Reptiles(Animals):
    def __init__ (self,vertebrates, dryscales):
    Animals. __init(self, feed,movement, reproduce, respirate):
        self.vertebrates = vertebrates
        self.dryscales = dryscales
    def havedryscales(self):
        return self.dryscales
class Amphibians(Animals):
    def __init__ (self,moiskin,coldblooded):
    Animals. __init(self, feed,movement, reproduce, respirate):
        self.moistskin = moistskin
        self.coldblooded = coldblooded
    def havemoistskin(self):
        return self.moistskin
sus=zoo('big','brown','mayi')
sus.identify()
