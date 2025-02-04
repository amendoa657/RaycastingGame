import pygame
import math

pygame.init()

largura, altura = 1280, 720

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Raycast")



player = pygame.Surface((100, 100), pygame.SRCALPHA)
player.fill((0, 0, 0))
playerRect = player.get_rect(center=(largura / 4, altura / 2))
playerSpeed = 3
rotate = 0
rotateSpeed = 3

colisao = [pygame.Rect(0, 0, 50, altura), pygame.Rect(largura - 50, 0, 50, altura), pygame.Rect(0, 0, largura, 50), pygame.Rect(0, altura - 50, largura, 50)]
bloco = pygame.Rect(300,500,100,100)


retangulo = pygame.Rect(largura-largura/3, altura/3, 10, altura)

clock = pygame.time.Clock()
def drawn():
    #tela.fill((150, 150, 255))
    rotated_player = pygame.transform.rotate(player, rotate)
    new_rect = rotated_player.get_rect(center=playerRect.center)
    tela.blit(rotated_player, new_rect.topleft)
    for i in colisao:
        pygame.draw.rect(tela, (0, 0, 0), i)
    pygame.draw.rect(tela, (0, 0, 0), bloco)
    tela.fill((50, 50, 255))
    desenhar_raycast()
    pygame.display.flip()

def desenhar_raycast():
    retangulo.x = 0
    for ang in range(90, -90, -1):
        ray_length = 901
        for depth in range(1,ray_length,10):
            end_pos = (
                playerRect.centerx + depth * math.cos(math.radians(rotate-ang/2)),
                playerRect.centery - depth * math.sin(math.radians(rotate-ang/2))
            )
            if any(wall.collidepoint(end_pos) for wall in colisao):
                break
            if bloco.collidepoint(end_pos):
                break

            print(((ray_length*720)/depth)/8)
        #if depth < ray_length-20:
        retangulo.height = ((ray_length*720)/depth)/8
        color = max(0,min(210,((ray_length*255)/depth)/8))
        retangulo.centery = 720 / 2
        pygame.draw.rect(tela,(color,color,color),retangulo)
        #pygame.draw.line(tela3d , (255, 0, 0), playerRect.center, end_pos,2)
        retangulo.x += 10

def input():
    global rotate
    pos = playerRect.center
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        #playerRect.y -=
        playerRect.x += playerSpeed * math.cos(math.radians(rotate))
        playerRect.y -= playerSpeed * math.sin(math.radians(rotate))
    if keys[pygame.K_s]:
        playerRect.x -= playerSpeed * math.cos(math.radians(rotate))
        playerRect.y += playerSpeed * math.sin(math.radians(rotate))
    if keys[pygame.K_a]:
        playerRect.x += playerSpeed * math.cos(math.radians(rotate+270))
        playerRect.y -= playerSpeed * math.sin(math.radians(rotate+270))
    if keys[pygame.K_d]:
        playerRect.x += playerSpeed * math.cos(math.radians(rotate+90))
        playerRect.y -= playerSpeed * math.sin(math.radians(rotate+90))

    if keys[pygame.K_LEFT]:
        rotate -= rotateSpeed
    if keys[pygame.K_RIGHT]:
        rotate += rotateSpeed

    if playerRect.collidelist(colisao) != -1:
        playerRect.center = pos





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    input()
    drawn()
    #get_fps()

    #print(pygame.time.Clock().tick(60))