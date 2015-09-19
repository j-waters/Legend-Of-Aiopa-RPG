import pygame as py
import Variables as v
import MenuItems 
import entityClasses 
import guiClasses 
from functools import reduce
from os import listdir

import Map
import entityClasses
import MenuItems
import guiClasses
from pygame.color import Color as colour
import sys
def mainMenu():
    py.init()
    v.screen = py.display.set_mode((640, 480),py.HWSURFACE|py.DOUBLEBUF)
    MenuItems.screen = v.screen
    buttons = py.sprite.Group()
    texts = []
    buttons.add(MenuItems.Button("New Game", (160, 380), 80, colour("Light Green"), colour("Dark Green"), "Resources\Fonts\MorrisRoman.ttf", "play"))
    texts.append(MenuItems.Text("The Legend", (90, 60), 80, colour("red"), "Resources\Fonts\RunicClear.ttf"))
    texts.append(MenuItems.Text("Of Aiopa", (160, 140), 80, colour("red"), "Resources\Fonts\RunicClear.ttf"))
    
    fade = MenuItems.fadeIn()
    fade.fadeIn = True
    while True:
        py.event.pump()
        MenuItems.fill_gradient(v.screen, colour("cyan"), colour("dark blue"))
        for text in texts:
            text.draw()
        buttons.update()
        v.events = []
        v.events = py.event.get()
        for event in v.events:
            if event.type == py.QUIT:
                sys.exit()
            elif event.type == py.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.pressed():
                        id = button.ID
                        if id == "play":
                            classSelection()
                            return
        fade.draw()
        fade.opacity -= 1
        py.display.flip()

def game():
    py.init()
    v.screen = py.display.set_mode((640, 480),py.HWSURFACE|py.DOUBLEBUF)
    v.screen.fill(colour("Green"))
    v.screen.fill(colour("Red"))
    v.p_class = entityClasses.Player()
    v.p_class.sheetImage = "Resources/Images/Male_Basic.png"
    v.p_class.initSheet()
    v.clock = py.time.Clock()
    py.time.set_timer(py.USEREVENT, 200)

    tileset = entityClasses.SpriteSheet("Resources/Images/Tile_Land2.png", 12, 16)
    v.hitList = py.sprite.Group()
    v.map1 = [["0","0","0","0","0","0","0","0","0","0"],
            ["#","0","0","0","#","#","0","0","0","0"],
            ["#","#","0","#","#","#","#","#","0","0"],
            ["#","#","#","#","0","0","0","#","0","0"],
            ["#","#","#","#","0","0","0","0","0","0"],
            ["#","#","#","#","0","0","0","0","0","0"],
            ["#","#","#","#","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0","0","0"],]
    v.allTiles = py.sprite.Group()
    tiles = Map.generateMap(v.map1, tileset)
    v.cur_weapon = entityClasses.Sword()
    v.cur_weapon.image = "Resources/Images/Sword_1.png"
    v.cur_weapon.get_rend()
    v.hits = py.sprite.Group()
    v.hits.add(entityClasses.HitBox(centre(v.screen)[0] + (5 * v.scale), centre(v.screen)[1] - (5 * v.scale), (2 * v.scale), (20 * v.scale), "Right"))
    v.hits.add(entityClasses.HitBox(centre(v.screen)[0] - (5 * v.scale), centre(v.screen)[1] - (5 * v.scale), (2 * v.scale), (20 * v.scale), "Left"))
    v.hits.add(entityClasses.HitBox(centre(v.screen)[0] - (3 * v.scale), centre(v.screen)[1] - (8 * v.scale), (8 * v.scale), (2 * v.scale), "Top"))
    v.hits.add(entityClasses.HitBox(centre(v.screen)[0] - (3 * v.scale), centre(v.screen)[1] + (16 * v.scale), (8 * v.scale), (2 * v.scale), "Bottom"))
    v.allNpc = py.sprite.Group()
    weaponSlot = guiClasses.weaponSlot()

    v.particles = py.sprite.Group()

    npc = entityClasses.NPC("Groblin Lvl. 1", 100, 100, 5)
    while True:
        v.ticks += 1
        #print(v.clock.get_fps())
        v.screen.fill(colour("Dark Green"))
        py.event.pump()
        v.events = []
        v.events = py.event.get()
        v.clock.tick(30)
        tiles.update()
        tiles.draw(v.screen)
        v.p_class.draw()
        v.cur_weapon.update()
        v.allNpc.update()
        v.allNpc.draw(v.screen)
        v.p_class.update()
        v.playerStopped = False

        v.cur_weapon.draw()
        v.particles.update()
        #v.hits.draw(v.screen)
        guiClasses.update_health()
        weaponSlot.draw()


        py.display.flip()
        for event in v.events:
            if event.type == py.QUIT:
                sys.exit()
            elif event.type==py.VIDEORESIZE:
                v.screen = py.display.set_mode(event.dict['size'],py.HWSURFACE|py.DOUBLEBUF)

        keys_pressed = py.key.get_pressed()
        if keys_pressed[py.K_SPACE]:
            v.cur_weapon.attacking = True

def classSelection():
    py.init()
    v.screen = py.display.set_mode((640, 480),py.HWSURFACE|py.DOUBLEBUF)

    classes = py.sprite.Group()
    classes.add(MenuItems.characterSelector("Resources/Images/PaladinClass.png", (v.screen.get_rect()[2]/2, v.screen.get_rect()[3]/2), "Paladin"))
    classes.add(MenuItems.characterSelector("Resources/Images/MageClass.png", (v.screen.get_rect()[2]/4, v.screen.get_rect()[3]/2), "Mage"))
    py.time.set_timer(py.USEREVENT + 1, 10)
    
    v.custimizationStage = "Class Selection"
    
    os = MenuItems.optionSlate()
    
    attOptions = py.sprite.Group()
    AoX = 100
    for attribute in v.Attributes:
        attOptions.add(MenuItems.optionAttribute(AoX, attribute))
        AoX += 30
    #attOptions.add(MenuItems.optionAttribute(100, "Max Health"))
    #attOptions.add(MenuItems.optionAttribute(130, "Speed"))
    
    labels = py.sprite.Group()
    labels.add(MenuItems.textLabel("Define Character Attributes", (250, 40), colour("Black"), "Resources/Fonts/RPGSystem.ttf", 35))
    labels.add(MenuItems.textLabel("Skill Points Remaining:", (250, 65), colour("grey"), "Resources/Fonts/RPGSystem.ttf", 30))
    labels.add(MenuItems.textLabel("skillPoints", (500, 65), colour("green"), "Resources/Fonts/RPGSystem.ttf", 30, True))
    
    buttons = py.sprite.Group()
    buttons.add(MenuItems.Button("Back", (10, 440), 30, colour("red"), colour("brown"), "Resources\Fonts\RunicSolid.ttf", "back"))
    buttons.add(MenuItems.Button("Continue", (550, 417), 20, colour("brown"), (153, 76, 0), "Resources\Fonts\RunicSolid.ttf", "continue"))

    background = MenuItems.shiftingGradient((50, 0, 0), (205, 0, 0))
    
    aps = py.sprite.Group()
    
    num = 1
    for i in listdir("Resources/Images/Character Customisation/Body"):
        aps.add(MenuItems.apearanceSelector("Resources/Images/Character Customisation/Body/" + i, "Body", num))
        num += 1
    
    ap = MenuItems.appearancePreview()
    while True:
        py.event.pump()
        v.events = []
        v.events = py.event.get()
        
        background.draw()
        
        classes.update()
        classes.draw(v.screen)
        
        os.update()
        attOptions.update()
        
        for button in buttons:
            if button.ID == "back":
                button.update()
            else:
                if v.custimizationStage == "Attributes":
                    button.update()
        
        if v.custimizationStage == "Attributes":
            labels.update()
        if v.custimizationStage == "Customisation":
            aps.update()
            aps.draw(v.screen)
            ap.draw()
            for key in v.testAppearance:
                v.testAppearance[key] = None
            
        for event in v.events:
            if event.type == py.QUIT:
                sys.exit()
            elif event.type == py.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.pressed():
                        id = button.ID
                        if id == "back":
                            mainMenu()
                            return
                        if id == "continue":
                            if v.custimizationStage == "Attributes":
                                v.custimizationStage = "Customisation"
                                for ao in attOptions:
                                    ao.save()
                        
            
        
        #v.characterHovered = False

        py.display.flip()

def centre(screen):
    return screen.get_rect()[2] / 2, screen.get_rect()[3] / 2