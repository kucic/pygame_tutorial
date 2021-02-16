import pygame

# screen size
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

# pygame init
pygame.init()

# SCREEN 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('image move rect')

# clock setting
clock = pygame.time.Clock()

# image load
player = pygame.image.load('start/Player.png')
player = pygame.transform.scale(player, (40, 150))

# image rect
player_Rect = player.get_rect()

# image center
player_Rect.centerx = round(SCREEN_WIDTH * 0.5)
player_Rect.centery = round(SCREEN_HEIGHT * 0.5)

# player pos
dx = 0
dy = 0

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
        # 키가 눌렀을 때
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -5
            if event.key == pygame.K_RIGHT:
                dx = 5
            if event.key == pygame.K_UP:
                dy = -5
            if event.key == pygame.K_DOWN:
                dy = 5
        # 키가 떼졌을 때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dx = 0
            if event.key == pygame.K_RIGHT:
                dx = 0
            if event.key == pygame.K_UP:
                dy = 0
            if event.key == pygame.K_DOWN:
                dy = 0

    player_Rect.x += dx
    player_Rect.y += dy

    # left
    if player_Rect.left < 0:
        player_Rect.left = 0
    # right
    if player_Rect.right > SCREEN_WIDTH:
        player_Rect.right = SCREEN_WIDTH
    # up
    if player_Rect.top < 0:
        player_Rect.top = 0
    # down
    if player_Rect.bottom > SCREEN_HEIGHT:
        player_Rect.bottom = SCREEN_HEIGHT

    SCREEN.fill((255,255,255))
    SCREEN.blit(player, player_Rect)
    pygame.display.flip()
    clock.tick(60)