# Definitions
import requests
import pandas as pd 
import json
import datetime
from time import sleep
import numpy as np

from gmapi import * 
from config import *
from centers import *


# Constants
khribga_high_left = ["32.907227","-6.957063"]
jadida_high_left = ["33.263203", "-8.541662"]
berkane_hight_left = ["34.950850", "-2.336993"]


# Height and Width
city_height = 5000 
city_width = 5000
multip = 100 # 1111 m
# multip = 10000 # 11 m
# multip = 1000 # 111 m
# multip = 100 # 1111 m 
# multip = 10 # 11 km

# Variables
city_name = "Berkane"
city_high_left = berkane_hight_left
business_type = "establishment"
keyword = ""
business_total = 60

# Processing Centers
city_exterms = get_extermes(city_high_left,city_height,city_width)
centers = get_centers(city_exterms[0],city_exterms[1])
centers
pd.DataFrame(centers).to_csv("centers.csv")

if(input("Are you ok with the cucrrent coverage y/N : ")=="Y"):
    print(ok)
else:
    print("aborted")