import collections
import json
import queue
import threading
import os
import sys
import time
from math import ceil

import sportsbetting as sb
from sportsbetting.auxiliary_functions import *
from sportsbetting.database_functions import *
from sportsbetting.user_functions import *

from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

### Get all sport competitions ###
# Get all sport competitions (football, basketball, tennis
# handball, rugby, hockey-sur-glace)
@app.get("/sports")
async def get_all_sport_competitions():
    all_sport = get_all_sports()

    for each_sport in all_sport:
        comp_list = get_all_competitions(each_sport)
        main_list = get_main_competitions(each_sport)
        curr_list = get_all_current_competitions(each_sport)
        for each_comp in comp_list:
            sb.SPORT_COMP[each_comp] = {
                "important" : each_comp in main_list,
                "active" : each_comp in curr_list,
                "sport": each_sport
            }
    return sb.SPORT_COMP

### Get a precise sport ###
@app.get("/sport/{sport_id}")
async def get_sport_id(sport_id: str):
    outData = {}
    comp_list = get_all_competitions(sport_id)
    main_list = get_main_competitions(sport_id)
    curr_list = get_all_current_competitions(sport_id)
    
    for each_comp in comp_list:
        outData[each_comp] = {
            "important" : each_comp in main_list,
            "active" : each_comp in curr_list,
            "sport": sport_id
        }

    return outData

### Get a precise competitions match ###
@app.get("/sport/competition/{competition_id}")
async def get_comp_id(competition_id: str):
    res = parse_competition("France - Ligue 1", competition_id)
    return res