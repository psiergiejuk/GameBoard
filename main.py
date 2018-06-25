import pygame
pygame.init()
pygame.display.set_mode((800, 600))
#pygame.display.set_mode((1280, 800), pygame.FULLSCREEN)
key_map = {
        pygame.K_w: "up",
        pygame.K_s: "down",
        pygame.K_d: "right",
        pygame.K_a: "left",
        pygame.K_q: "tleft",
        pygame.K_e: "tright",
        pygame.K_r: "reload",
        pygame.K_f: "help",
        pygame.K_LCTRL: "lie",
        pygame.K_SPACE: "jump",
        pygame.K_LSHIFT: "sprint",
        pygame.K_UP: "lup",
        pygame.K_DOWN: "ldown",
        pygame.K_RIGHT: "lright",
        pygame.K_LEFT: "lleft",
        pygame.K_z: "drive",
        pygame.K_x: "exit",
        }
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()

    #Checking Keys
    keys = pygame.key.get_pressed()
    for key in key_map:
        if keys[key]:
            print(key_map[key],  end=' ')
    print()
    print(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
