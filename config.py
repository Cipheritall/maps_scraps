# Maps api key
api_key = ""
with open(".key") as f:
    api_key = f.read()

# Constants
khribga_high_left = ["32.907227","-6.957063"]
jadida_high_left = ["33.263203", "-8.541662"]
berkane_hight_left = ["34.950850", "-2.336993"]


# Height and Width
city_height = 5000 
city_width = 5000
# Rayon --> multip
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