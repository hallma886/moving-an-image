# Draw Lines in Pygame / No Functions

# Pygame game template

import pygame
import sys
import config  # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event

def main():

    screen = init_game()  # Initialize the game and get the screen
    clock = pygame.time.Clock() # Initialize the clock objecct
    
    backround_position = [0, 0]

    backround_image = pygame.image.load("saturn_family1.jpg").convert()
    player_image = pygame.image.load("player.png").convert()
    player_image.set_colorkey(config.BLACK)

    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running


        # Fill the screen with a background color 
        screen.fill(config.WHITE)
         
        screen.blit(backround_image, backround_position)

        player_position = pygame.mouse.get_pos()
        x = player_position[0] - (player_image.get_width()/2)
        y = player_position[1] - (player_image.get_height()/2)

        screen.blit(player_image, [x, y])
        pygame.display.flip()  # Update the display



        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































