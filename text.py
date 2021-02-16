import pygame

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 400

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TEXT')

clock = pygame.time.Clock()

BLACK = (0,0,0)

# Font Create
myFont = pygame.font.SysFont("arial", 30, True, False)
'''
# Custom Font Create
myFont = pygame.font.Font("font-name", 30)
# Default Font Use
myFont = pygame.font.Font(None, 30)
# System Font List
print( pygame.font.get_fonts())

# Text Render - render( Text, antialias, color, background=None )
blit_text = myFont.render( "Pygame", True, BLACK)
'''
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
    SCREEN.fill((255,255,255))


    # Text를 Surface에 그리기 , 안티얼라이어싱, 검은색
    text_Title = myFont.render("PyGame Text Test", True, BLACK)
    text_Title2 = myFont.render("PyGame Text Test2", True, BLACK)

    # Rect create
    text_Rect = text_Title.get_rect()
    text_Rect.centerx = round(SCREEN_WIDTH*0.5)
    text_Rect.y = 50

    # Render Text
    SCREEN.blit(text_Title, text_Rect)
    SCREEN.blit(text_Title2, [50,200])

    # render
    pygame.display.flip()

    clock.tick(60)