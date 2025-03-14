# Draw Lines in Pygame / No Functions

# Pygame game template

import pygame
import sys
import config  # Import the config module
import random


def init_game():
    pygame.init()
    pygame.font.init()  # Inisialize fonts here
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
    font_name = "FreeMono(1).ttf"
    font_color1 = config.RED    # Use a color from config
    font_color2 = config.BLUE
    font_color3 = config.GREEN
    font_size_normal = 36
    font_size_bold_italic = 30
    font_size_custom = 48

    # Using a True Type Font (.ttf)
    custom_font_name = "Caveat-VariableFont_wght.ttf"


    def draw_text(screen, text, x, y, font_size, color, font_name=None, bold=False, italic=False):
        if font_name:
            font = pygame.font.Font(font_name, font_size)
        else:
            font = pygame.font.Font(None, font_size)
    
        font.set_bold(bold)
        font.set_italic(italic)
    
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))
    



 
    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Fill the screen with a background color 
        screen.fill(config.WHITE) 

        # Example 1: Draw normal text
        draw_text(screen, "You Win!!", 50, 50, font_size_custom, font_color1)

        # Example 1: Draw normal text
        draw_text(screen, "You Lose!!", 423, 67, font_size_custom, font_color2, italic=True)
        
        # Example 2: Draw italic and bold text
        draw_text(screen, "Round 2...Fight!!", 300, 300, font_size_custom, font_color3, bold=True)

        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































