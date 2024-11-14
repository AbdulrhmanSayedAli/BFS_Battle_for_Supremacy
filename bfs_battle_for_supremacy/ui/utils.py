import pygame


main_color = (245, 176, 66)
main_color_hover = (207, 149, 58)
secondary_color = (108, 245, 66)
secondary_color_hover = (116, 186, 95)
tile_main_color = (100, 237, 95)
tile_secondary_color = (81, 173, 78)


def get_font(size: int):
    return pygame.font.Font(None, size)
