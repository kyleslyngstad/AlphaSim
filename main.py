#####
# v. 0.0.01
# 01/03/2017
#####

import pygame

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

size = (1024,768)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("GodLand Aloha")
screen.fill(GREEN)

done = False
clock = pygame.time.Clock()

def pressed(rect,mouse):
    if mouse[0] > rect.topleft[0]:
        if mouse[1] > rect.topleft[1]:
            if mouse[0] < rect.bottomright[0]:
                if mouse[1] < rect.bottomright[1]:
                    return True
    else: return False

class landZone():
    def __init__(self,regionSlot,xPos,yPos,landZoneId):
        self.pop = 0
        self.elements = []
        self.genZone(xPos, yPos, regionSlot)
        self.id = landZoneId

    def genZone(self, zoneX, zoneY, regionSlot):
        xPos = 100 + (regionSlot)*250 + zoneX*25
        yPos = 100 + (regionSlot)*250 + zoneY*25
        zoneSquare = pygame.Rect(xPos,yPos,25,25)
        pygame.draw.rect(screen,BLACK,zoneSquare,2)
        self.rect = zoneSquare

    def selectZone(self):

        pygame.draw.line(screen,RED,self.rect.topleft,self.rect.bottomright,3)
        pygame.draw.line(screen,RED,self.rect.topright,self.rect.bottomleft,3)
    #def randZone()

class landRegion():
    listRegions = []
    def __init__(self,regionSlot):
        self.listZones = []
        self.regionSlot = regionSlot
        self.genRegion(regionSlot)
        landRegion.listRegions.append(self)

    def genRegion(self, regionSlot):
        regionPos = pygame.Rect(100+250*regionSlot,100+250*regionSlot,250,250)
        pygame.draw.rect(screen,WHITE,regionPos,0)
        landZoneId = 0
        for y in range(10):
            for x in range(10):
                self.listZones.append(landZone(regionSlot,x,y,landZoneId)) #.genZone(x,y,regionSlot)
                landZoneId += 1

class uiZone():
    #pygame.Surface()
    def __init__():
        self.target = 0

    #def showZone(self,regionSlot,zoneId):
test = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            for r in landRegion.listRegions:
                for z in r.listZones:
                    if(pressed(z.rect, mousePos)):
                        z.selectZone() #Need to change this function to just store the specified zone then use drawSelectedZone later after landRegion(0)
                        #if something else is clicked then selectZone will be set to 0 or None.
    if test is True:
        landRegion(0)
    test = False
    #This is where the drawSelectedZone will go.

    #pygame.draw.line(screen,RED,self.rect.topright,self.rect.bottomleft)
    #Use this to allow the user to drag and scroll.
    #screen.scroll(0,1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
