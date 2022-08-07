# Definitions
import requests
import pandas as pd 
import json
import datetime
from time import sleep
import numpy as np

# lat: y
# lon: x, 


key = "AIzaSyB8TweCbt1tm2N9TnRmhx6bMN5wguIFVAk"
radius = "500"

#["43.5836","7.10905"]
def get_extermes(high_left,height,width):
    # height : latitude  (in meter)
    # width  : longitude (in meter) 
    height_lat = height/100000.0
    width_lon = width/100000.0
    low_right=[f"{float(high_left[0])+height_lat}",f"{float(high_left[1])+width_lon}"]
    return [high_left,low_right]

def get_centers(high_left,low_right,radius=50):
  # plot multiple points in a map https://www.zeemaps.com/map?group=4464287&add=1#
  high = high_left[0]
  left = high_left[1]
  low = low_right[0]
  right = low_right[1]
  centers = []
  stop = 0
  # https://www.usna.edu/Users/oceano/pguth/md_help/html/approx_equivalents.htm
  # multip = 10000 # 11 m
  # multip = 1000 # 111 m
  # multip = 100 # 1111 m 
  # multip = 10 # 11 km
  # multip = 100 # 1111 m
  for i in range(abs(int(float(high)*multip-float(low)*multip))):
    for j in range(abs(int(float(right)*multip-float(left)*multip))):
      # if negatif
      if float(high)>0 and float(left)>0:
        center = [f"{float(high)+i/multip: .4f}",f"{float(left)+j/multip: .4f}"]
      elif float(high)>0 and float(left)<0:
        center = [f"{float(high)-i/multip: .4f}",f"{float(left)+j/multip: .4f}"]
      elif float(high)>0 and float(left)<0:
        center = [f"{float(high)+i/multip: .4f}",f"{float(left)+j/multip: .4f}"]
      
      centers.append(center)
  return centers

