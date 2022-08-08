# Maps api key
key = ""
with open(".key") as f:
    key = f.read()

# Constants
khribga_high_left = ["32.907227","-6.957063"]
jadida_high_left = ["33.263203", "-8.541662"]
berkane_hight_left = ["34.950850", "-2.336993"]
nice_high_left = ["43.692900", "7.261953"]

# Height and Width
city_height = 1100
city_width = 1100
# Rayon --> multip
multip = 100 # 1111 m
# multip = 10000 # 11 m
# multip = 1000 # 111 m
# multip = 100 # 1111 m 
# multip = 10 # 11 km

# Variables
city_name = "nice"
city_high_left = nice_high_left
business_type = "point_of_interest"
keyword = ""
business_total = 60