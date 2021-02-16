import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

WINDOW_TITLE = "Screen Rect"

pygame.init()

pygame.display.set_caption(WINDOW_TITLE)
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

isPlaying = True

'''
* 컴퓨터의 화면에 표시되는 많은 객체들(윈도우, 이미지)들은 크기(width, height)와 좌표(Coordinates or Position)를 가진다.
pygame.display.set_mode()로 스크린이 생성
스크린 제일 왼쪽 상단을 기준점으로 두고 오른쪽(X축)은 양수, 왼쪽은 음수, 위쪽(Y축)은 음수, 아래쪽은 양수가 된다.

Rect = Rectangle
* Rect는 좌표(X,Y)와 크기(Width,Height)를 가진다.

* Rect 의 가상 속성 값 (virtual attributes)
    pygame의 Rect는 각 모서리, 선분의 중간값등의 가상의 좌표를 제공
    
* pygame에서 생성되는 이미지와 각종 객체들은 모두 Rect 안에 존재, 이는 곧 Rect에서 제공하는 좌표와 크기값을 알아낼 수 있다.
    Rect 객체가 아닌 다른 객체에서 Rect객체를 생성하는 매서드는 get_rect() 이다.

* 속성값을 변경하면 모두 자동 업데이트 된다. 
'''

# rect
myRect = pygame.Rect(150,200,200,100)

def printMenu():
    print("[01] Rect")
    print("[02] x, y, w, h")
    print("[03] width, height")
    print("[04] left, right, top, bottom")
    print("[05] centerx, centery")
    print("[06] size")
    print("[07] topleft, topright")
    print("[08] midleft, midright, midtop, midbottom")

def selectMenu(input):
    if input == 1:
        print("/t Rect = ", myRect)
    elif input == 2:
        print("/t x = ", myRect.x)
        print("/t y = ", myRect.y)
        print("/t w = ", myRect.w)
        print("/t h = ", myRect.h)
    elif input == 3:
        print("/t width = ", myRect.width)
        print("/t height = ", myRect.height)
    elif input == 4:
        print("/t left = ", myRect.left)
        print("/t right = ", myRect.right)
        print("/t top = ", myRect.top)
        print("/t bottom = ", myRect.bottom)
    elif input == 5:
        print("/t centerx = ", myRect.centerx)
        print("/t centery = ", myRect.centery)
    elif input == 6:
        print("/t size = ", myRect.size)
    elif input == 7:
        print("/t topleft = ", myRect.topleft)
        print("/t topright = ", myRect.topright)
    elif input == 8:
        print("/t midleft = ", myRect.midleft)
        print("/t midright = ", myRect.midright)
        print("/t midtop = ", myRect.midtop)
        print("/t midbottom = ", myRect.midbottom)
    printMenu()

printMenu()

while isPlaying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("QUIT")
            pygame.quit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                selectMenu(1)
            if event.key == pygame.K_2:
                selectMenu(2)
            if event.key == pygame.K_3:
                selectMenu(3)
            if event.key == pygame.K_4:
                selectMenu(4)
            if event.key == pygame.K_5:
                selectMenu(5)
            if event.key == pygame.K_6:
                selectMenu(6)
            if event.key == pygame.K_7:
                selectMenu(7)
            if event.key == pygame.K_8:
                selectMenu(8)

    clock.tick(60)