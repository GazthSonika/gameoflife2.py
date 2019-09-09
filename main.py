import pygame

from life import GOL
from generators import GOLBoardGeneratorRandom

## Quick example of how it works, a bit dirty one but the point was to
#  do nice game of life, not nice pygame wraper

size = 100
resolution = (1280, 720) #screen
speed = 24
window_title = "Game of Life"
being_size = (resolution[0] / size, resolution[1]/ size)

pygame.init()
Display = pygame.display.set_mode(resolution, 0, 32)
Bg_color = (0, 0, 0)
Fg_color = (0xff, 0xff, 0xff)

gol = GOL(size, GOLBoardGeneratorRandom())

clock = pygame.time.Clock()

running = True
paused = False
t = 0.0
print("Press space to pause, click to kill/res a `being`")
while(running):
    t += 1.9
    if speed < 1: speed = 1
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
         running = False  
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_SPACE:
                paused = not paused
            elif e.key == pygame.K_UP:
                speed += 1
            elif e.key == pygame.K_DOWN:
                speed -= 1
    #mouse
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if pressed1 or pressed2:
        pos = pygame.mouse.get_pos()
        x, y = (int(pos[0] / being_size[0]), int(pos[1] / being_size[1]))
        gol.board[y][x] = 1 if pressed1 else 0
        print(f'Swithing state of ({x}, {y})')

    if paused:
        pygame.display.set_caption(window_title + ' (paused)')
    else:
        gol.next_tick()
    pygame.display.set_caption(window_title + " " + str(speed))

    Display.fill(Bg_color)
    for r in range(gol.rows):
        pos_y = r * being_size[1]
        for c, val in enumerate(gol.board[r]):
            if val == 0: continue
            pos_x = c * being_size[0]
            pos =  (pos_x, pos_y, being_size[0]-1, being_size[1]-1)
            
            pygame.draw.rect(Display, (255, 0, 0), pos)
    
    pygame.display.update()
    clock.tick(speed)

print("Exiting")
pygame.quit()