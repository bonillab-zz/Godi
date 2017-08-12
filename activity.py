import pygame,sys
import random
from pygame.locals import *
from utils import CURSOR, ejercicios
import gtk

resolution=(1200,900)

class Main_Class():

    def __init__(self):
        pygame.init()
        cursor = pygame.cursors.compile(CURSOR)
        pygame.mouse.set_cursor((32,32), (1,1), * cursor)
        self.ventana=pygame.display.set_mode((resolution))
        pygame.display.set_caption("Dinosaurio XD")
        self.principal()
        pygame.display.update()

    def image_load(self, path):
          return pygame.image.load(path)

    def ran(self, matriz):
        r = random.choice(matriz)
        return r[0]

    def principal(self):
        self.fondo = self.image_load('img/background.png')
        self.ventana.blit(self.fondo, (0, 0))
        mt = self.ran(ejercicios)
        img1 = self.image_load(mt[0])
        rect = img1.get_rect()
        self.ventana.blit(img1, rect)
        pygame.display.flip()
        self.detection_click()

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
                    print pos

if __name__=='__main__':
    Main_Class()
