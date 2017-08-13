import pygame,sys
import random
from pygame.locals import *
from utils import CURSOR, img, font
import gtk

resolution=(1200,900)

class Main_Class():
    resp_font = []

    def __init__(self):
        pygame.init()
        cursor = pygame.cursors.compile(CURSOR)
        pygame.mouse.set_cursor((32,32), (1,1), * cursor)
        self.ventana=pygame.display.set_mode((resolution))
        pygame.display.set_caption("Dinosaurio XD")
        self.mt = self.ran(img)
        self.principal()
        pygame.display.update()

    def image_load(self, path):
        return pygame.image.load(path)

    def ran(self, matriz):
        self.size = len(matriz)
        x = range(self.size)
        random.shuffle(x)
        return x

    def principal(self):
        self.fondo = self.image_load('img/background.png')
        self.ventana.blit(self.fondo, (0, 0))
        self.load_img()
        self.load_font()
        self.detection_click()

    def load_img(self):
        try:
            x = 75
            self.array = []
            self.resp = []
            for i in self.mt:
                image = self.image_load(img[i][0])
                rect = image.get_rect()
                rect.left = x
                rect.top = img[i][1]
                self.array.insert(0, rect)
                self.ventana.blit(image, rect)
                self.resp.append(img[i][2])
                x += 280
        except Exception, ex:
            print ex

    def load_font(self):
        x =140
        try:
            self.array_rect = []
            for i in range(4):
                image = self.image_load(font[i][0])
                rect = image.get_rect()
                rect.left = x
                rect.top = 580
                self.array_rect.append(rect)
                self.ventana.blit(image, rect)
                x += 280
            pygame.display.flip()

        except Exception, ex:
            print ex

    def validate(self):
        exito = False
        try:
            if len(self.resp_font) == 4:
                for x in range(4):
                    if self.resp[x] == self.resp_font[x]:
                        exito = True
                    else:
                        exito = False
                        break

                if exito:
                    print "Bien echo"
                else:
                    print "Intenta nuevamente"
                    del self.resp_font[:]
            else:
                pass
        except Exception, ex:
            print ex

    def detection_click(self):
        while True:
            while gtk.events_pending():
            	gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if self.array_rect[0].collidepoint(pos):
                        self.resp_font.append("A")
                        self.validate()

                    if self.array_rect[1].collidepoint(pos):
                        self.resp_font.append("B")
                        self.validate()

                    if self.array_rect[2].collidepoint(pos):
                        self.resp_font.append("C")
                        self.validate()

                    if self.array_rect[3].collidepoint(pos):
                        self.resp_font.append("D")
                        self.validate()

if __name__=='__main__':
    Main_Class()
