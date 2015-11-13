import pygame as py
import entityClasses
import Variables as v

def generateMap(map, sheet):
    allMap = map
    map = allMap[0]
    mody = int(len(map) / 2)
    modx = int(len(map[0]) / 2)
    sheet.getGrid()
    outmap = py.sprite.Group()
    size = [0, 0]
    size[0] = len(map[0]) * 30
    size[1] = len(map[1]) * 30
    baseMap = py.Surface(size)
    for row in range(len(map)):
        for tile in range(len(map[row])):
            if list(map[row][tile])[0] == "#":
                image = sheet.images[int(map[row][tile].replace('#', ""))]
                posx = (tile * 30)# - (modx * 30)
                posy = (row * 30)# - (mody * 30)
                baseMap.blit(image, (posx, posy))
                outmap.add(entityClasses.Tile((tile - modx, row - mody), 0, True))
            else:
                image = sheet.images[int(map[row][tile])]
                posx = (tile * 30)# - (modx * 30)
                posy = (row * 30)# - (mody * 30)
                baseMap.blit(image, (posx, posy))
    
    
    map = allMap[1]
    mody = int(len(map) / 2)
    modx = int(len(map[0]) / 2)
    outmap = py.sprite.Group()
    size = [0, 0]
    size[0] = len(map[0]) * 30
    size[1] = len(map[1]) * 30
    for row in range(len(map)):
        for tile in range(len(map[row])):
            if map[row][tile] != "-":
                if list(map[row][tile])[0] == "+":
                    over = True
                else:
                    over = False
                image = sheet.images[int(map[row][tile].replace('+', ""))]
                posx = (tile * 30)# - (modx * 30)
                posy = (row * 30)# - (mody * 30)
                baseMap.blit(image, (posx, posy))
                if over:
                    entityClasses.Tile((tile - modx, row - mody), 0, False, over, image) 
    
    v.MAP = BaseMap(baseMap)    

class BaseMap():
    
    def __init__(self, image):
        self.posx = 0
        self.posy = 0
        self.skin = image.convert()
        v.MAP = self
        self.oldScale = None
        self.oldPos = None
        self.reRender = False
    
    def update(self):
        if self.oldScale != v.scale:
            size = self.skin.get_rect().size
            self.image = py.transform.scale(self.skin, (int(size[0] * v.scale), int(size[1] * v.scale)))
            self.oldScale = v.scale
            self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = v.screenX / 2 + ((-v.playerPosX + (1 * self.posx) - 15) * v.scale)
        self.rect.centery = v.screenY / 2 + ((v.playerPosY + (1 * self.posy) - 15) * v.scale)
        self.draw()
        
    def draw(self):
        v.screen.blit(self.image, self.rect)

Maps = [[
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '#326', '#326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '#326', '#326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '#326', '#326', '#326', '#326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '#326', '#326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '#697', '#697', '#697', '#697', '#697', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '#18', '#18', '#18', '#18', '#18', '326', '326', '326', '326', '326', '326', '#326', '#326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '#18', '#18', '#18', '#18', '#18', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '#18', '#18', '18', '#18', '#18', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
['326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326', '326'],
], 
[
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+1538', '+1539', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+1350', '+1351', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+1570', '+1571', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+1350', '+1414', '+1415', '+1351', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+1602', '+1603', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '1382', '+1446', '+1447', '+1383', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+1382', '+1383', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+665', '+665', '+665', '+665', '+665', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+1000', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+896', '-', '+896', '-', '-', '-', '-', '-', '-', '-', '+1476', '+1477', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+928', '+1954', '+928', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '1986', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
]]