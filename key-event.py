import pygame

# 전체 스크린의 가로, 세로 크기 설정
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

# 초기화
pygame.init()

# 스크린 생성
SCREEN = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

# WINDOW의 타이틀 설정
pygame.display.set_caption("pygame text")

# Clock 객체 생성
clock = pygame.time.Clock()

playing = True

while playing :
    ''' CODE '''
    for event in pygame.event.get() :
        # QUIT - ESC
        if event.type == pygame.QUIT :
            playing = False
            pygame.quit()
        # 키가 눌렸을 때
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("LEFT KEY INPUT")
            if event.key == pygame.K_DOWN:
                print("DOWN KEY INPUT")
            if event.key == pygame.K_UP:
                print("UP KEY INPUT")
            if event.key == pygame.K_RIGHT:
                print("RIGHT KEY INPUT")

        # 키가 때졌을 때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("LEFT KEY RELEASE")
            if event.key == pygame.K_DOWN:
                print("DOWN KEY RELEASE")
            if event.key == pygame.K_UP:
                print("UP KEY RELEASE")
            if event.key == pygame.K_RIGHT:
                print("RIGHT KEY RELEASE")
    # fps 설정, while 구문안에 넣는다.
    clock.tick(60)