from random import randint, sample
from typing import List
import pygame
import time
pygame.init()

def render(list_rect: List[object], red_index: List[int]) -> None:
    """render the sticks

    Args:
        list_rect (List[object]): list of sticks
    """
    # fill backgound in black
    background.fill((0, 0, 0))

    # change sticks place and draw it
    for _ in range(len(list_rect)):
        list_rect[_].left = _*(600/number_of_data)
        pygame.draw.rect(surface=background, color=(250, 250, 250), rect=list_rect[_])

    # red sticks
    pygame.draw.rect(surface=background, color=(250, 0, 0), rect=list_rect[red_index[0]])
    pygame.draw.rect(surface=background, color=(250, 0, 0), rect=list_rect[red_index[1]]) 

    # update display
    screen.blit(background, (0, 0))
    pygame.display.flip()

def tri_selection(array: List[object], speed:float) -> list[object]:
    """sort an array

    Args:
        array (List[object]): array to sort
        speed (float): speed of the sort (seconds)

    Returns:
        list[object]: return the sorted array
    """
    size = len(array)
    for i in range(size-1):
        index_min = i
        for j in range(i+1, size):
            if array[j].height < array[index_min].height:
                index_min = j
        array[i], array[index_min] = array[index_min], array[i]   
        render(array, [i, index_min])
        time.sleep(speed)
    return array




rect_list = []
number_of_data = int(input("Enter a number between 100 and 600: "))
speed = float(input("Speed (seconds): "))

# generate an array of random int for sticks size
array = [randint(1, 120) for i in range(number_of_data)]

# generate a list of sticks
for i in range(number_of_data):
    rect_list.append(
        pygame.Rect(i*(600/number_of_data), 595-5*array[i], (600/number_of_data), 5+5*array[i]))

# init screen
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Basic sort insertion program')

# setup background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))


# render and sort the array of sticks
render(rect_list, [1, 1])
tri_selection(rect_list, speed)
    
# infinit loop
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
    screen.blit(background, (0, 0))
    pygame.display.flip()
