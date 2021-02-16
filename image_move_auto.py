import pygame

# 스크린 전체 크기 지정
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

# pygame 초기화
pygame.init()

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame image auto")

# FPS 를 위한 Clock 생성
clock = pygame.time.Clock()

# 이미지 로딩 및 크기 변경
player = pygame.image.load("start/Player.png")
player = pygame.transform.scale(player, (40, 102))

# 이미지의 Rect 정보를 저장
player_Rect = player.get_rect()

# 이미지가 가운데 올 수 있도록 좌표값 수정
# python 3.8 이상에서 integer가 필요한 곳에  float 가 들어가면 DeprecationWarning이 나옴.
# 따라서 round() 처리를 해준다.
player_Rect.centerx = round(SCREEN_WIDTH * 0.5)
player_Rect.centery = round(SCREEN_HEIGHT * 0.5)

dx = 0
dy = 0

playing = True
while playing:
    # 이벤트 처리
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
    # 스크린 배경색 칠하기
    SCREEN.fill((255,255,255))

    # 키에 의해 증가된 값을 이미지의 좌표에 적용
    player_Rect.x += dx
    player_Rect.y += dy

    # 스크린의 우너하는 좌표에 이미지 복사하기, 좌표값은 Rect이용
    SCREEN.blit(player, player_Rect)

    # 작업한 스크린의 내용을 갱신하가ㅣ
    pygame.display.flip()

    # 1초에 60번 빈도로 순환하기
    clock.tick(60)