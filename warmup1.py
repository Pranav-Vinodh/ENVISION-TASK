import numpy as np
import pandas as pd
import matplotlib as mpl

numbers = input("enter a sequence of numbers separated by commas: ")
numbers_list = numbers.split(',')

new_list = [int(num)**2 if int(num)%2!=0 else int(num) for num in numbers_list ]

print(", ".join(map(str,new_list)))