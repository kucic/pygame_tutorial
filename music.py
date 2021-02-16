import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('MUSIC')
clock = pygame.time.Clock()
playing = True

# wav, mp3, ogg
pygame.mixer.music.load("start/bagroundsample.mp3")
# wav, ogg
sound_thunder = pygame.mixer.Sound("start/thunder.ogg")
# music stream 무한반복
pygame.mixer.music.play(-1)

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v + 0.1)
                print("volume up")
            if event.key == pygame.K_DOWN:
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v - 0.1)
                print("volume down")
            if event.key == pygame.K_LEFT:
                pygame.mixer.music.pause()
                print("일시 멈춤")
            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.unpause()
                print("다시 재생")
            if event.key == pygame.K_a:
                sound_thunder.play()
                print("천둥소리")

    SCREEN.fill((255,255,255))
    pygame.display.flip()
    clock.tick(60)