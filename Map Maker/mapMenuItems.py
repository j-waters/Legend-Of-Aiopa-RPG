import mapMakerVariables as v
import pygame as py

def toolTip():
    if not v.hoverPos == None:
        font = py.font.SysFont("Calibri", 20, True)
        label = font.render(str(v.hoverPos), 1, (255, 0, 0), (255, 255, 255, 100))
        v.screen.blit(label, py.mouse.get_pos())
        ymod = font.size(str(v.hoverPos))[1]
        for k, va in v.hoverData.items():
            if not va == None:
                label = font.render(str(k) + ": " + str(va), 1, (255, 0, 0), (255, 255, 255, 100))
                v.screen.blit(label, (py.mouse.get_pos()[0], py.mouse.get_pos()[1] + ymod))
                ymod += font.size(str(k) + ": " + str(va))[1]

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
    # This points to our sprite sheet image
    sprite_sheet = None
    images = None

    def __init__(self, file_name, rows, columns):
        """ Constructor. Pass in the file name of the sprite sheet. """

        self.rows = rows
        self.columns = columns

        # Load the sprite sheet.
        if type(file_name) is py.Surface:
            self.sprite_sheet = file_name.convert_alpha()
        else:
            self.sprite_sheet = py.image.load(file_name).convert_alpha()
        self.getGrid()


    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = py.Surface([width, height], py.SRCALPHA, 32).convert_alpha()
        image = image.convert_alpha()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Return the image
        return image

    def getGrid(self):
        width = self.sprite_sheet.get_size()[0] / self.columns
        height = self.sprite_sheet.get_size()[1] / self.rows
        all = []
        for h in range(self.rows):
            for w in range(self.columns):
                image = py.Surface([width, height], py.SRCALPHA, 32).convert_alpha()
                image.blit(self.sprite_sheet, (0, 0), (w * width, h * height, width, height))
                all.append(image)
        self.images = all

class button(py.sprite.Sprite):

    def __init__(self, text, pos, size, hovercolour, normalcolour, font, ID, centred = False, bsize=(0,0)):
        super().__init__()
        self.ID = ID
        self.hovered = False
        self.text = text
        self.pos = pos
        self.hcolour = hovercolour
        self.ncolour = normalcolour
        self.font = font
        self.font = py.font.Font(font, int(size))
        self.centred = centred
        self.size = bsize
        self.set_rect()
    
    def update(self):
        self.set_rend()
        py.draw.rect(v.screen, self.get_color(), self.rect)
        v.screen.blit(self.rend, self.rect)
        if self.rect.collidepoint(py.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False

    def set_rend(self):
        self.rend = self.font.render(self.text, True, (0,0,0))

    def get_color(self):
        if self.hovered:
            return self.hcolour
        else:
            return self.ncolour

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        if not self.centred:
            self.rect.topleft = self.pos
        if self.centred:
            self.rect.center = self.pos
        
        if not self.size[0] == 0:
            self.rect.width = self.size[0]
        if not self.size[1] == 0:
            self.rect.height = self.size[1]

    def pressed(self):
        mouse = py.mouse.get_pos()
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False


class textLabel(py.sprite.Sprite):
    
    def __init__(self, text, pos, colour, font, size, variable = False, centred = False):
        super().__init__()
        self.text = text
        self.pos = pos
        self.colour = colour
        self.font = font
        self.size = size
        self.variable = variable
        self.centred = centred
        
    def update(self):
        pos = self.pos
        font = py.font.Font(self.font, self.size)
        if not self.variable:
            label = font.render(self.text, 1, self.colour)
        if self.variable:
            label = font.render(str(getattr(v, self.text)), 1, self.colour)
        if self.centred:
            pos = list(self.pos)
            pos[0] -= font.size(self.text)[0] / 2
            pos[1] -= font.size(self.text)[1] / 2
            pos = tuple(pos)
    
        self.image = label
        self.rect = pos
        v.screen.blit(label, pos)
        
class textInput(py.sprite.Sprite):
    
    def __init__(self, pos, fontSize, characters, num, button="GO", default=[], type="str"):
        super().__init__()
        self.font = py.font.Font("../Resources/Fonts/RPGSystem.ttf", fontSize)
        self.rect = py.Rect(pos, self.font.size("W" * characters))
        self.rect.width += 20
        self.rect.height += 20
        self.string = default
        self.pos = pos
        self.characters = characters
        self.shift = False
        self.done = False
        self.button = button
        self.num = num
        self.type = type
        self.outText = ""
    
    def draw(self):
        if self.num == v.textNum:
            c = (255, 0, 0)
        else:
            c = (0, 0, 0,)
        py.draw.rect(v.screen, (255, 255, 255), self.rect)
        py.draw.rect(v.screen, c, self.rect, 5)
        x = self.pos[0] + 10
        y = self.pos[1] + 10
        for letter in self.string:
            ren = self.font.render(letter, 1, (0, 0, 0))
            v.screen.blit(ren, (x, y))
            x += self.font.size(letter)[0] + 5
    
    def update(self):
        global textEdit
        textEdit = True
        self.outText = "".join(self.string)
        if self.num == v.textNum:
            for event in v.events:
                if event.type == py.KEYDOWN:
                    if len(self.string) < self.characters:
                        if py.key.name(event.key) in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                            if py.key.get_mods() == py.KMOD_LSHIFT:
                                let = py.key.name(event.key).upper()
                            else:
                                let = py.key.name(event.key)
                            allow = True
                            if self.type == "int":
                                try:
                                    int(let)
                                    allow = True
                                except:
                                    allow = False
                            if allow:        
                                self.string.append(let)
                        if event.key == py.K_SPACE:
                            self.string.append(" ")
                    if event.key == py.K_BACKSPACE:
                        if len(self.string) > 0:
                            self.string.pop(-1)
        self.draw()
        
        if not self.button == None:
            label = self.font.render(self.button, 1, (0, 0, 0))
            butRect = py.Rect(self.rect.topright, (self.rect.height, self.rect.height))
            butRect.centerx += 5
            py.draw.rect(v.screen, (255, 255, 255), butRect)
            py.draw.rect(v.screen, (0, 0, 0), butRect, 5)
            v.screen.blit(label, (butRect.centerx - self.font.size(self.button)[0] / 2, butRect.centery - self.font.size(self.button)[1] / 2))
            for event in v.events:
                if event.type == py.MOUSEBUTTONDOWN:
                    if butRect.collidepoint(py.mouse.get_pos()):
                        global outText
                        outText = "".join(self.string)
                        self.done = True
                        py.time.wait(100)
        if self.rect.collidepoint(py.mouse.get_pos()):
            if py.mouse.get_pressed()[0]:
                v.textNum = self.num
        
        #py.display.flip()

class toggleButton(py.sprite.Sprite):
    
    def __init__(self, type, num):
        super().__init__()
        self.type = type
        self.num = num
        if self.type == "layer":
            self.image1 = py.image.load("Resources/Bottom Layer.png")
            self.image1 = py.transform.scale(self.image1, (50, 50))
            
            self.image2 = py.image.load("Resources/Top Layer.png")
            self.image2 = py.transform.scale(self.image2, (50, 50))
            size = (50, 50)
        if self.type == "hitbox":
            self.image1 = py.image.load("Resources/hitBox.png")
            self.image1 = py.transform.scale(self.image1, (50, 50))
            size = (50, 50)
        if self.type == "over":
            self.image1 = py.image.load("Resources/Over Player.png")
            self.image1 = py.transform.scale(self.image1, (50, 50))
            
            self.image2 = py.image.load("Resources/Under Player.png")
            self.image2 = py.transform.scale(self.image2, (50, 50))
            size = (50, 50)
        if self.type == "teleport":
            self.image1 = py.image.load("Resources/Teleport.png")
            self.image1 = py.transform.scale(self.image1, (50, 50))
            size = (50, 50)
        self.rect = py.Rect((20 + 100 * num, 10), size)
        self.state = None
        self.labels = py.sprite.Group()
        self.labels.add(textLabel(self.type + ":", (self.rect.midbottom[0], self.rect.midbottom[1] + 10), (255, 255, 255), "../Resources/Fonts/RPGSystem.ttf", 30, variable=False, centred=True))
        self.labels.add(textLabel("publicState", (self.rect.midbottom[0] + 40, self.rect.midbottom[1] - 5), (255, 255, 255), "../Resources/Fonts/RPGSystem.ttf", 30, variable=True, centred=False))
    
    def update(self):
        if self.type == "layer":
            self.state = v.eLayer
            if v.eLayer == "base":
                self.image = self.image1
            else:
                self.image = self.image2
            if self.rect.collidepoint((py.mouse.get_pos()[0], py.mouse.get_pos()[1] - 550)):
                for event in v.events:
                    if event.type == py.MOUSEBUTTONDOWN:
                        if v.eLayer == "base":
                            v.eLayer = "top"
                        else:
                            v.eLayer = "base"
        
        if self.type == "hitbox":
            self.state = v.editHitable
            if v.editHitable == False:
                self.image = self.image1.copy()
                self.image.fill((100, 100, 100), special_flags=py.BLEND_RGBA_MULT)
            else:
                self.image = self.image1
            if v.eLayer == "base":
                if self.rect.collidepoint((py.mouse.get_pos()[0], py.mouse.get_pos()[1] - 550)):
                    for event in v.events:
                        if event.type == py.MOUSEBUTTONDOWN:
                            v.editHitable = not v.editHitable
        
        if self.type == "over":
            self.state = v.overPlayer
            if v.overPlayer:
                self.image = self.image1.copy()
            else:
                self.image = self.image2.copy()
            if v.eLayer == "top":
                if self.rect.collidepoint((py.mouse.get_pos()[0], py.mouse.get_pos()[1] - 550)):
                    for event in v.events:
                        if event.type == py.MOUSEBUTTONDOWN:
                            v.overPlayer = not v.overPlayer
            else:
                self.image.fill((100, 100, 100), special_flags=py.BLEND_RGBA_MULT)
        
        if self.type == "teleport":
            self.state = v.makeTeleport
            if v.makeTeleport == False:
                self.image = self.image1.copy()
                self.image.fill((100, 100, 100), special_flags=py.BLEND_RGBA_MULT)
            else:
                self.image = self.image1
            if v.eLayer == "top":
                if self.rect.collidepoint((py.mouse.get_pos()[0], py.mouse.get_pos()[1] - 550)):
                    for event in v.events:
                        if event.type == py.MOUSEBUTTONDOWN:
                            v.makeTeleport = not v.makeTeleport
        
        if self.rect.collidepoint((py.mouse.get_pos()[0], py.mouse.get_pos()[1] - 550)):
            py.draw.rect(v.options, (200, 200, 0), self.rect)
            v.publicState = self.state
            self.labels.update()
            self.labels.draw(v.options)
        else:
            py.draw.rect(v.options, (200, 200, 200), self.rect)
        py.draw.rect(v.options, (0, 0, 0), self.rect, 2)
        v.options.blit(self.image, self.rect)

class makeTeleport():
    
    def __init__(self):
        self.back = py.Surface((200, 200))
        self.back.fill((100, 100, 0))
        v.textNum = 1
        self.tinps = py.sprite.Group()
        self.texts = py.sprite.Group()
        self.tinps.add(textInput((100, 350), 30, 2, 1, button=None, default=[], type="int"))
        self.texts.add(textLabel("Map ID:", (10, 360), (0, 0, 0), "../Resources/Fonts/RPGSystem.ttf", 30))
    
    def update(self):
        v.screen.blit(self.back, (0, 330))
        self.tinps.update()
        self.texts.update()