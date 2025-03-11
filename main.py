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
    
    # Define font properties
    font_name = "Caveat-VariableFont_wght.ttf"
    font_color1 = config.RED    # Use a color from config
    font_color2 = config.BLUE
    font_color3 = config.GREEN
    font_size_normal = 36
    font_size_bold_italic = 30
    font_size_custom = 48

    # Using a True Type Font (.ttf)
    custom_font_name = "Caveat-VariableFont_wght.ttf"

    # Define x,y coordinate pairs for top left of text rectangle (stamp)
    text_position_1 = [50, 50]
    text_position_2 = [225, 135]
    text_position_3 = [220, 370]

    def draw_text



 
    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Fill the screen with a background color 
        screen.fill(config.WHITE) 

        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































