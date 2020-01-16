#!/usr/bin/env python3

"""
Parseur pour récupérer les promotions en cours
"""

import urllib
from pprint import pprint
from bs4 import BeautifulSoup

def get_promotions_france_pari():
    """
    Affiche les promotions proposées sur france pari
    """
    url = "https://www.france-pari.fr/promotions"
    soup = BeautifulSoup(urllib.request.urlopen(url), features="lxml")
    for line in soup.find_all():
        if "class" in line.attrs and "promo" in line["class"]:
            if "MultiBoost" not in line.text:
                promotion = list(line.stripped_strings)
                promotion.remove("J'en\xa0profite")
                print("\n".join(promotion))
                print()

def get_promotions_netbet():
    """
    Affiche les promotions proposées sur netbet
    """
    url = "https://www.netbet.fr/promotions"
    soup = BeautifulSoup(urllib.request.urlopen(url), features="lxml")
    for line in soup.find_all():
        if "class" in line.attrs and "resume-promo" in line["class"]:
            promotion = list(line.stripped_strings)
            promotion.remove("En savoir plus")
            print("\n".join(promotion))
            print()

def get_promotions_betclic():
    """
    Affiche les promotions proposées sur betclic
    """
    url = "https://www.betclic.fr/sport/"
    soup = BeautifulSoup(urllib.request.urlopen(url), features="lxml")
    urls_promo = []
    for line in soup.find_all():
        if "class" in line.attrs and "nav-window-promo" in line["class"]:
            children = line.findChildren("a", recursive=False)
            for child in children:
                url_promo = child["href"]
                if url_promo not in ["https://www.betclic.fr/calendrier-0?Streaming=true&Live=true",
                                     "https://www.betclic.fr/sponsoring_sponsoring.aspx"]:
                    urls_promo.append(url_promo)
    for url_promo in urls_promo:
        parse_promotion_betclic(url_promo)
    if not urls_promo:
        print("Pas de promotion en cours")

def parse_promotion_betclic(url_promo):
    """
    Affiche une promotion telle qu'affichée sur betclic
    """
    url = "https://www.betclic.fr/happy-loser-10-au-12-janvier-g4161"
    url = "https://www.betclic.fr/cashback-sports-us-g4147"
    url = "https://www.betclic.fr/cashback-foot-g4053"
    url = "https://www.betclic.fr/mission-us-semaine-2-g4011"
    url = url_promo
    soup = BeautifulSoup(urllib.request.urlopen(url), features="lxml")
    print(soup.find("title").text)
    dict_steps = {}
    dict_infos = {}
    for line in soup.find_all():
        if (("id" in line.attrs and "step-event-page" in line["id"])
                or ("class" in line.attrs and "module__title" in line["class"])):
            infos = list(line.stripped_strings)
            dict_steps[infos[0]] = infos[1]
        if "class" in line.attrs and (any(x in line["class"] for x in ["content-bloc-event-page",
                                                                       "module__bloc--50",
                                                                       "module__bloc--100"])):
            infos = list(line.stripped_strings)
            try:
                dict_infos[infos[0]] = infos[1]
            except IndexError:
                if "autres" in dict_infos:
                    dict_infos["autres"] += "\n"+infos[0]
                else:
                    dict_infos["autres"] = infos[0]
#         if "class" in line.attrs:
#             print(line["class"], line["class"])
    print("Étapes:")
    pprint(dict_steps)
    print("Infos:")
    pprint(dict_infos)

def get_promotions_pmu():
    """
    Affiche les promotions proposées sur pmu
    """
    url = "https://www.netbet.fr/promotions"
    soup = BeautifulSoup(urllib.request.urlopen(url), features="lxml")
    for line in soup.find_all():
        if "class" in line.attrs and "node-pmu-promotions" in line["class"]:
            promotion = list(line.stripped_strings)
            print("\n".join(promotion))
            print()