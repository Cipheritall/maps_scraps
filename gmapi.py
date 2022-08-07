# Definitions
import requests
import pandas as pd 
import json
import datetime
from time import sleep
import numpy as np



def get_business_details(name,place_id,details="name%2Cwebsite%2Crating%2Cformatted_phone_number"):
  url = f"https://maps.googleapis.com/maps/api/place/details/json?fields={details}&place_id={place_id}&key={key}"
  details_list = json.loads(f""" ['{details.replace('%2C',"','")}'] """.replace("'",'"'))
  #print(f"{name}: {url}")
  payload={}
  headers = {}
  base_response = requests.request("GET", url, headers=headers, data=payload)
  got = {}
  if base_response.json()['status']=='OK':
    for attribute in details_list:
      try:
        got[attribute]=base_response.json()['result'][attribute]
      except:
        pass
  return got

def scrap_n_business_subresults(results):
  # first_shot.json()["results"]
  out_raw = []
  out_raw_unit={}
  for business in results:
    out_raw_unit["name"] = business["name"]
    got = get_business_details(business["name"],business["place_id"])
    try:
      out_raw_unit["formatted_phone_number"]=got["formatted_phone_number"]
    except:
      out_raw_unit["formatted_phone_number"]=""
      pass 
    try:
      out_raw_unit["website"]=got["website"]
    except:
      out_raw_unit["website"]=""
      pass 
    out_raw_unit["vicinity"] = business["vicinity"]
    # https://www.google.com/maps/@34.055403,-4.9881709,18.69z
    out_raw_unit["location"] = f'https://www.google.com/maps/@{business["geometry"]["location"]["lat"]},{business["geometry"]["location"]["lng"]},30z'
    out_raw_unit["types"] = business["types"]
    out_raw_unit["place_id"] = business["place_id"]
    out_raw.append(out_raw_unit)
    out_raw_unit = {}
  return out_raw
  

def get_places_nearby(place_center,radius,business_type,keyword,next_page_token=""):
  lat = place_center[0]
  lon = place_center[1]
  location = f"{lat}%2C{lon}"
  if next_page_token == "":
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={business_type}&keyword={keyword}&key={key}"
  else:
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={business_type}&keyword={keyword}&sensor=false&key={key}&pagetoken={next_page_token}"
  print(url)
  payload={}
  headers = {}
  base_response = requests.request("GET", url, headers=headers, data=payload)
  print(f"{place_center}: {base_response}")
  return base_response 

def scrap_n_business(n,place_center,radius,business_type,keyword):
  last_shot={}
  stop = 0
  business_index = 0
  current_shot = get_places_nearby(place_center,radius,business_type,keyword)
  out_raw = []
  out_raw = scrap_n_business_subresults(current_shot.json()["results"])
  business_index += len(current_shot.json()["results"])
  last_shot = current_shot
  #print(current_shot.json()["next_page_token"])
  while business_index<n or stop:
    sleep(2)
    token = ""
    try :
      token = current_shot.json()["next_page_token"]
    except:
      pass
    current_shot = get_places_nearby(place_center,radius,business_type,keyword,token)
    current_out_raw = scrap_n_business_subresults(current_shot.json()["results"])
    for out_raw_unit in current_out_raw:
      out_raw.append(out_raw_unit)
      business_index+=1
    #print(current_shot.json())
    if str(current_shot.json().items()).find("INVALID_REQUEST")>0 or str(current_shot.json().items()).find("next_page_token")<0 :
      print(current_shot.json().items())
      break
  return out_raw