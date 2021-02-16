import pygame
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
TITLE = "IMAGE"

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

isPlaying = True

IMAGE = pygame.Surface((100, 60))
IMAGE.fill(pygame.Color('sienna2'))
pygame.draw.circle(IMAGE, pygame.Color('royalblue2'), (50, 30), 20)
# New width and height will be (50, 30).
IMAGE_SMALL = pygame.transform.scale(IMAGE, (50, 30))
# Rotate by 0 degrees, multiply size by 2.
IMAGE_BIG = pygame.transform.rotozoom(IMAGE, 0, 2)

# image load - image.load()
'''
JPG, PNG, GIF(non-animated), BMP, PCX, TGA(uncompressed), TIF, LBM(and PBM), PBM(and PGM, PPM), XPM
'''
player = pygame.image.load("start/Player.png").convert_alpha()
pygame.transform.rotozoom(player, 0, 2)
pygame.transform.scale(player, (50,20))
# 이미지 크기조정 : transform.scale()
rectPlayer = player.get_rect()
print(rectPlayer.center)
rectPlayer.centerx = round(SCREEN_WIDTH / 2)
rectPlayer.centery = round(SCREEN_HEIGHT / 2)
# pygame.transform.scale(player, (int(rectPlayer.width/10), int(rectPlayer.height/10)))


# 이미지 화면에 출력
'''
blit 함수로 그려줌, blit(이미지 객체, 이미지 좌표값)
SCREEN.blit(player,[200,250])
'''



while isPlaying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rectPlayer.y += 10
            if event.key == pygame.K_DOWN:
                rectPlayer.y -= 10
            if event.key == pygame.K_LEFT:
                rectPlayer.x -= 10
            if event.key == pygame.K_RIGHT:
                rectPlayer.x += 10
    # 스크린 배경색 칠하기
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(IMAGE, (50, 50))
    SCREEN.blit(IMAGE_SMALL, (50, 155))
    SCREEN.blit(IMAGE_BIG, (50, 230))

    # 스크린 에 이미지 그리기
    SCREEN.blit(player, rectPlayer)
    # 작업한 스크린의 내용을 갱신하기
    pygame.display.flip()
    # 1초에 60번
    clock.tick(60)