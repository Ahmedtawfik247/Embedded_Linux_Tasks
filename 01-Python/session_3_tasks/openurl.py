#!/usr/bin/python3
import fav_web
if fav_web.x in fav_web.links:
    fav_web.firefox(fav_web.x)
    
else:
    print("You chose the wrong site name, please try again!")