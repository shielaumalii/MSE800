# example 2
from random import randint
dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5) # Changed to randint(0, 5) to match index of dice_images
print(dice_images[dice_num])