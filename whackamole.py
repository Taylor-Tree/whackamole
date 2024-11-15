import pygame
import random


def main():
    running = True
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        mole_location = mole_image.get_rect(topleft=(mole_x, mole_y))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mole_location.collidepoint(mouse_x, mouse_y):
                        mole_x = random.randint(0, 19) * 32
                        mole_y = random.randint(0, 15) * 32
                        mole_location = mole_image.get_rect(topleft=(mole_x, mole_y))
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("sienna4")



            for i in range(0, 640, 32):
                pygame.draw.line(screen, "springgreen4", (i, 0), (i, 512))
            for i in range(0, 512, 32):
                pygame.draw.line(screen, "springgreen", (0, i), (640, i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
