import pygame
import random
import sys

pygame.init()

screen=pygame.display.set_mode((600,600))

def Game():
    SnekPosX=300
    SnekPosY=300
    SnekPosXMove=0
    SnekPosYMove=0
    SnekSpeed=15
    Score=0
    SnekBody=[]

    FoodExists=False
    GameOver=False
    Lost=False

    Clock=pygame.time.Clock()
    while GameOver==False:
        while Lost==True:
            screen.blit((pygame.font.SysFont("comicsansms", 35).render("You Lost",True,(255,0,0))),(250,250))
            screen.blit((pygame.font.SysFont("comicsansms", 20).render("Do You Wish To Play Again?", True, (255,0,0))),(200,400))
            screen.blit((pygame.font.SysFont("comicsansms", 20).render("Press c to Continue or Press q to exit", True, (255,0,0))),(150,500))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    Lost=False
                    GameOver=True
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_c:
                        Game()
                    elif event.key==pygame.K_q:
                        Lost=False
                        GameOver=True
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Lost=False
                GameOver=True
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    SnekPosXMove=10
                    SnekPosYMove=0
                elif event.key==pygame.K_LEFT:
                    SnekPosXMove=-10
                    SnekPosYMove=0
                elif event.key==pygame.K_UP:
                    SnekPosXMove=0
                    SnekPosYMove=-10
                elif event.key==pygame.K_DOWN:
                    SnekPosXMove=0
                    SnekPosYMove=10
        if SnekPosX<0 or SnekPosX>590 or SnekPosY<0 or SnekPosY>590:
            Lost=True
        elif FoodExists==False:
            FoodPosX=random.randrange(0,600,10)
            FoodPosY=random.randrange(0,600,10)
            FoodExists=True
        elif SnekPosX==FoodPosX and SnekPosY==FoodPosY:
            screen.fill((0,0,0))
            Score+=1
            FoodExists=False
        SnekPosX+=SnekPosXMove
        SnekPosY+=SnekPosYMove
        screen.fill((0,0,0))
        screen.blit(pygame.font.SysFont("comicsansms",30).render("Score:%s"%(Score),True,(255,255,0)),(0,0))
        pygame.draw.rect(screen,(255,0,0),(FoodPosX,FoodPosY,10,10))
        Snek_Head = []
        Snek_Head.append(SnekPosX)
        Snek_Head.append(SnekPosY)
        SnekBody.append(Snek_Head)
        if len(SnekBody) > Score+1:
            del SnekBody[0]
 
        for x in SnekBody[:-1]:
            if x == Snek_Head:
                Lost = True
 
        for BodyDraw in SnekBody:
            pygame.draw.rect(screen, (0,255,0), [BodyDraw[0], BodyDraw[1], 10, 10])
        pygame.display.update()
        Clock.tick(SnekSpeed)

Game()
