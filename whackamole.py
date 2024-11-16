# Lab 10 Whackamole
import pygame
import random


def draw_grid(pygame, screen, line_color): # draws the grid lines
    for i in range(20):
        pygame.draw.line(screen, line_color, (32 * i, 0), (32 * i, 512))

    for i in range(16):
        pygame.draw.line(screen, line_color, (0, 32 * i), (640, 32 * i))

def draw_mole(screen, mole_image, x, y): # draws the mole based on the square positions
    # x:0-19 y:0-15
    x_coord = x * 32 + 2
    y_coord = y * 32 + 1
    screen.blit(mole_image, mole_image.get_rect(topleft=(x_coord ,y_coord)))

def is_mole_hit(user_x, user_y, mole_x, mole_y): # checks if the mole was hit by user
    return user_x // 32 == mole_x and user_y // 32 == mole_y # checking the user input to the square position

def main():
    current_x = 0
    current_y = 0

    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        line_color = "black"

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN: # when the mouse is clicked
                    x, y = event.pos
                    if is_mole_hit(x, y, current_x, current_y):
                        current_x = random.randrange(0,20) # randomized columns
                        current_y = random.randrange(0,16) # randomized rows
            screen.fill("light green") # fill background
            draw_grid(pygame, screen, line_color) # draw grid
            draw_mole(screen, mole_image, current_x, current_y) # draw mole
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
