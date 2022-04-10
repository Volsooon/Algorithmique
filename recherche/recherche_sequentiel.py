from typing import List
from random import randint
import pygame
import time
pygame.init()


def recherche_sequentiel(tab: List[list], valrench: int) -> int:
    i = 0
    found = False
    NOT_FOUND = -1
    # Boucle de recherche
    while not found and i < len(tab):
        render(tab, i, "red")
        time.sleep(0.1)
        if tab[i][0] == valrench:
            found = True
        else:
            i += 1

    if found == True:
        render(tab, i, "green")
        return i
    if found != True:
        return NOT_FOUND
    
def render(list_rect: List[object], special_index: List[int], color: str) -> None:
    """render the sticks

    Args:
        list_rect (List[object]): list of sticks
    """
    # fill backgound in black
    background.fill((0, 0, 0))

    # change sticks place and draw it
    for _ in range(len(list_rect)):
        pygame.draw.rect(surface=background, color=(250, 250, 250), rect=list_rect[_][1])

    # color sticks
    if color == "red":
        pygame.draw.rect(surface=background, color=(250, 0, 0), rect=list_rect[special_index][1])
    if color == "green":
        pygame.draw.rect(surface=background, color=(0, 250, 0), rect=list_rect[special_index][1])


    # update display
    screen.blit(background, (0, 0))
    pygame.display.flip()


rect_list = []
number_of_data = 150
speed = 0.1

# generate an array of random int for sticks size
array = [randint(1, 120) for i in range(number_of_data)]

# generate a list of sticks
for i in range(number_of_data):
    rect_list.append(
        [array[i], pygame.Rect(i*(600/number_of_data), 595-5*array[i], (600/number_of_data), 5+5*array[i])])

# init screen
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Basic sort insertion program')

# setup background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))


# render and sort the array of sticks
render(rect_list, 1, "red")
print(recherche_sequentiel(rect_list, 10))

    
# infinit loop
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
    screen.blit(background, (0, 0))
    pygame.display.flip()
