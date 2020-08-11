from common.commonsum import commonsum
from classes.character_selection import character_selection
from equip.equip_selection import equip_selection
from common.nonemblemcalculations import nonemblemcalculations
from common.emblemcalculations import emblemcalculations
from scipy.optimize import linprog
import pandas as pd

while True:
    character_type = str(input("Please enter your class type:\n"
                               "WARRIOR, MAGE, ARCHER, THIEF, PIRATE\n")).upper()
    character_type_list = {"WARRIOR", "MAGE", "ARCHER", "THIEF", "PIRATE"}
    if character_type not in character_type_list:
        continue
    else:
        break

if character_type == "WARRIOR":
    warrior = character_selection().warrior()
    character_class = warrior
    if character_class == "DK":
        type = "PHYSICAL"
        from classes.dk import dk

        char = dk()

    elif character_class == "HERO":
        type = "PHYSICAL"
        from classes.hero import hero

        char = hero()

    elif character_class == "PALA":
        type = "PHYSICAL"
        from classes.pala import pala

        char = pala()

elif character_type == "MAGE":
    mage = character_selection().mage()
    character_class = mage
    if character_class == "BSP":
        type = "MAGICAL"
        from classes.bsp import bsp

        char = bsp()

    elif character_class == "ILM":
        type = "MAGICAL"
        from classes.ilm import ilm

        char = ilm()

    elif character_class == "FPM":
        type = "MAGICAL"
        from classes.fpm import fpm

        char = fpm()

    elif character_class == "BW":
        type = "MAGICAL"
        from classes.bw import bw

        char = bw()

    elif character_class == "EVAN":
        type = "MAGICAL"
        from classes.evan import evan

        char = evan()

    elif character_class == "LUMI":
        type = "MAGICAL"
        from classes.lumi import lumi

        char = lumi()

    elif character_class == "BAM":
        type = "MAGICAL"
        from classes.bam import bam

        char = bam()

elif character_type == "ARCHER":
    archer = character_selection().archer()
    character_class = archer
    if character_class == "BM":
        type = "PHYSICAL"
        from classes.bm import bm

        char = bm()

    elif character_class == "MM":
        type = "PHYSICAL"
        from classes.mm import mm

        char = mm()

    elif character_class == "WA":
        type = "PHYSICAL"
        from classes.wa import wa

        char = wa()

    elif character_class == "MERC":
        type = "PHYSICAL"
        from classes.merc import merc

        char = merc()

    elif character_class == "WH":
        type = "PHYSICAL"
        from classes.wh import wh

        char = wh()

elif character_type == "THIEF":
    thief = character_selection().thief()
    character_class = thief
    if character_class == "NL":
        type = "PHYSICAL"
        from classes.nl import nl

        char = nl()

    elif character_class == "SHAD":
        type = "PHYSICAL"
        from classes.shad import shad

        char = shad()

    elif character_class == "NW":
        type = "PHYSICAL"
        from classes.nw import nw

        char = nw()

    elif character_class == "PHAN":
        type = "PHYSICAL"
        from classes.phan import phan

        char = phan()

elif character_type == "PIRATE":
    pirate = character_selection().pirate()
    character_class = pirate
    if character_class == "CSR":
        type = "MAGICAL"
        from classes.csr import csr

        char = csr()

    elif character_class == "BUCC":
        type = "PHYSICAL"
        from classes.bucc import bucc

        char = bucc()

    elif character_class == "TB":
        type = "PHYSICAL"
        from classes.tb import tb

        char = tb()

    elif character_class == "SHADE":
        type = "PHYSICAL"
        from classes.shade import shade

        char = shade()

    elif character_class == "MECH":
        type = "MAGICAL"
        from classes.mech import mech

        char = mech()

# Equipment Choosing
while True:
    equip_type = str(input("Please enter your equipment type using the numbers:\n"
                           "FULL EMP (1), FULL NECRO (2), 2 PIECE FAF + EMP (3),"
                           " 4 PIECE FAF + EMP (4), 2 PIECE FAF + NECRO (5), 4 PIECE FAF + NECRO (6)\n")).upper()
    equip_type_list = {"1", "2", "3", "4", "5", "6"}
    if equip_type not in equip_type_list:
        continue
    else:
        break

while True:
    stat_type = str(input("Please enter your equipment stat using the numbers:\n"
                          "NORMAL (1), PARTIAL EXP [DOUBLE ML PEND + KTOWER RING + LEGENDS MEDAL] (2), FULL EXP (3) \n")).upper()
    stat_type_list = {"1", "2", "3"}
    if stat_type not in stat_type_list:
        continue
    else:
        break

while True:
    cash_type = str(input("Please enter your cash set style using the numbers:\n"
                          "3 + 3 (1), 5 SET (2) \n")).upper()
    cash_type_list = {"1", "2"}
    if cash_type not in cash_type_list:
        continue
    else:
        break
commonsum = commonsum(type, character_class)
equip = equip_selection(equip_type, stat_type, character_class, cash_type)
necalculations = nonemblemcalculations(commonsum, equip)


finalcalculations = emblemcalculations(necalculations, char)

atkstats = [finalcalculations.atk, finalcalculations.atkp, finalcalculations.dmg, finalcalculations.batk,
            finalcalculations.cr, finalcalculations.cd, finalcalculations.fd]

pskillstats = [finalcalculations.pname, finalcalculations.bpoutput(), finalcalculations.nbpoutput()]
sskillstats = [finalcalculations.sname, finalcalculations.bsoutput(), finalcalculations.nbsoutput(),
               finalcalculations.schance]
firstppercentage = -(finalcalculations.bpoutput() - finalcalculations.bpoutput())/ finalcalculations.bpoutput() * 100
secondppercentage = -(finalcalculations.bpoutput() - finalcalculations.sbpoutput())/ finalcalculations.bpoutput() * 100
firstspercentage = -(finalcalculations.bsoutput() - finalcalculations.bsoutput())/ finalcalculations.bsoutput() * 100
secondspercentage = -(finalcalculations.bsoutput() - finalcalculations.sbsoutput())/ finalcalculations.bsoutput() * 100


embstats = [finalcalculations.ncdemb, finalcalculations.natkpemb, finalcalculations.nbatkemb, finalcalculations.bpoutput()
    , firstppercentage, finalcalculations.bsoutput(), firstspercentage]
sembstats = [finalcalculations.secondncdemb, finalcalculations.secondnatkpemb, finalcalculations.secondnbatkemb,
             finalcalculations.sbpoutput(), secondppercentage, finalcalculations.sbsoutput(), secondspercentage]
atkstatsdf = pd.DataFrame(columns=["ATK", "ATK%", "DMG%", "BATK%", "CR%", "CD%", "FD%"])
atkstatsdf.loc[0] = atkstats

pskillstatsdf = pd.DataFrame(columns=["Primary Skill", "Boss Output", "Non-Boss Output"])
pskillstatsdf.loc[0] = pskillstats

sskillstatsdf = pd.DataFrame(columns=["Secondary Skill", "Boss Output", "Non-Boss Output", "Chance %"])
sskillstatsdf.loc[0] = sskillstats

embstatsdf = pd.DataFrame(columns=["CD Emb", "ATK Emb", "BATK Emb", "Primary DMG", "Primary %", "Secondary DMG", "Secondary %"])
embstatsdf.loc[0] = embstats
embstatsdf.loc[1] = sembstats

print(atkstatsdf, "\n")
print(pskillstatsdf, "\n")
print(sskillstatsdf, "\n")
print(embstatsdf)
