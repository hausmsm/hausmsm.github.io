from common.commonsum import commonsum
from equip.equip_selection import equip_selection
from common.nonemblemcalculations import nonemblemcalculations
from common.emblemcalculations import emblemcalculations
import pandas as pd
import streamlit as st

st.title("Automatic Emblem Calculator")

# Character Selection
st.header("Class Selection")
with st.beta_expander("Class"):
    character_type = st.selectbox("Choose Class Type", ["Warrior", "Mage", "Archer", "Thief", "Pirate"])
    if character_type == "Warrior":
        character_class = st.selectbox("Choose Class", ["Dark Knight", "Hero", "Paladin", "Dawn Warrior", "Aran"])
        if character_class == "Dark Knight":
            type = "PHYSICAL"
            from classes.dk import dk
            char = dk()

        elif character_class == "Hero":
            type = "PHYSICAL"
            from classes.hero import hero
            char = hero()

        elif character_class == "Paladin":
            type = "PHYSICAL"
            from classes.pala import pala
            char = pala()

        elif character_class == "Dawn Warrior":
            type = "PHYSICAL"
            from classes.dw import dw
            char = dw()

        elif character_class == "Aran":
            type = "PHYSICAL"
            from classes.aran import aran
            char = aran()

    elif character_type == "Mage":
        character_class = st.selectbox("Choose Class",["Bishop","Ice Lightning Mage","Fire Poison Mage","Blaze Wizard","Evan","Luminous","Battle Mage"])
        if character_class == "Bishop":
            type = "MAGICAL"
            from classes.bsp import bsp
            char = bsp()

        elif character_class == "Ice Lightning Mage":
            type = "MAGICAL"
            from classes.ilm import ilm
            char = ilm()

        elif character_class == "Fire Poison Mage":
            type = "MAGICAL"
            from classes.fpm import fpm
            char = fpm()

        elif character_class == "Blaze Wizard":
            type = "MAGICAL"
            from classes.bw import bw
            char = bw()

        elif character_class == "Evan":
            type = "MAGICAL"
            from classes.evan import evan
            char = evan()

        elif character_class == "Luminous":
            type = "MAGICAL"
            from classes.lumi import lumi
            char = lumi()

        elif character_class == "Battle Mage":
            type = "MAGICAL"
            from classes.bam import bam
            char = bam()

    elif character_type == "Archer":
        character_class = st.selectbox("Choose Class",["Bow Master","Marksman","Wind Archer","Mercedes","Wild Hunter"])
        if character_class == "Bow Master":
            type = "PHYSICAL"
            from classes.bm import bm
            char = bm()

        elif character_class == "Marksman":
            type = "PHYSICAL"
            from classes.mm import mm
            char = mm()

        elif character_class == "Wind Archer":
            type = "PHYSICAL"
            from classes.wa import wa
            char = wa()

        elif character_class == "Mercedes":
            type = "PHYSICAL"
            from classes.merc import merc
            char = merc()

        elif character_class == "Wild Hunter":
            type = "PHYSICAL"
            from classes.wh import wh
            char = wh()

    elif character_type == "Thief":
        character_class = st.selectbox("Choose Class",["Night Lord","Shadower","Night Walker","Phantom"])
        if character_class == "Night Lord":
            type = "PHYSICAL"
            from classes.nl import nl
            char = nl()

        elif character_class == "Shadower":
            type = "PHYSICAL"
            from classes.shad import shad
            char = shad()

        elif character_class == "Night Walker":
            type = "PHYSICAL"
            from classes.nw import nw
            char = nw()

        elif character_class == "Phantom":
            type = "PHYSICAL"
            from classes.phan import phan
            char = phan()

    elif character_type == "Pirate":
        character_class = st.selectbox("Choose Class",["Corsair","Buccaneer","Thunder Breaker","Shade","Mechanic"])
        if character_class == "Corsair":
            type = "MAGICAL"
            from classes.csr import csr
            char = csr()

        elif character_class == "Buccaneer":
            type = "PHYSICAL"
            from classes.bucc import bucc
            char = bucc()

        elif character_class == "Thunder Breaker":
            type = "PHYSICAL"
            from classes.tb import tb
            char = tb()

        elif character_class == "Shade":
            type = "PHYSICAL"
            from classes.shade import shade
            char = shade()

        elif character_class == "Mechanic":
            type = "MAGICAL"
            from classes.mech import mech
            char = mech()

# Equipment Choosing
st.header("Equipment Selection")

## Weapon
with st.beta_expander("Weapon"):
    _,wep1,wep2,wep3,_ = st.beta_columns([0.02,0.32,0.32,0.32,0.02])
    weapon_type = wep1.selectbox("Choose Weapon Type",["Mythic Empress","Ancient Empress","Necro","Fafnir"])
    if weapon_type != "Fafnir":
        weapon_stat = wep2.radio("Choose Weapon Stat",["Boss ATK","Crit DMG","Crit Rate","EXP"])
    else:
        weapon_stat = "None"
    weapon_emblem = wep3.radio("Choose Weapon Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK", "Boss DEF"])
    if weapon_type in ["Mythic Empress","Ancient Empress"]:
        weapon_refine_level = wep1.slider("Weapon Refinement Level",min_value=1,max_value=10)
    weapon_level = wep1.slider("Choose Weapon Level",min_value=30,max_value=50)
    weapon_emblem_level = wep3.slider("Weapon Emblem Level", min_value=1,max_value=5)

## Secondary Weapon
with st.beta_expander("Secondary Weapon"):
    swep_type = st.selectbox("Choose Secondary Weapon Type",["Unique Class","Legendary Class","Mythic Class","Unique Longinus Spear","Legendary Longinus Spear","Mythic Longinus Spear"])
    if swep_type in ["Unique Longinus Spear","Legendary Longinus Spear","Mythic Longinus Spear"]:
        swep_level = st.slider('Sharenian Ability', min_value=1, max_value=10)

## Hat
with st.beta_expander("Hat"):
    hat1,hat2,hat3 = st.beta_columns(3)
    hat_type = hat1.selectbox("Choose Hat Type",["Mythic Empress","Ancient Empress","Necro","Fafnir"])
    if hat_type == "Mythic Empress":
        hat_level = hat1.slider('Hat Level', min_value=30,max_value=40)
    else:
        hat_level = hat1.slider('Hat Level', min_value=30,max_value=50)
    if hat_type != "Fafnir":
        hat_stat = hat2.radio("Choose Hat Stat",["Boss ATK","Crit ATK","Crit DMG","EXP"])
    else:
        hat_stat = "None"
    hat_emblem = hat3.radio("Choose Hat Emblem Stat",["Crit DMG","Boss ATK","Phy/Mag ATK"])
    hat_emblem_level = hat3.slider("Hat Emblem Level", min_value=1,max_value=5)

## Glove
with st.beta_expander("Gloves"):
    glove1,glove2,glove3 = st.beta_columns(3)
    glove_type = glove1.selectbox("Choose Glove Type",["Ancient Empress","Necro"])
    glove_level = glove2.radio("Glove Level",[30,40,50])
    glove_stat = glove3.radio("Choose Glove Stat",["ACC","Crit Atk","Crit Dmg","EXP"])

## Top+Bottom/Outfit
st.subheader("Top+Bottom/Outfit Selection")

equip_type_combination = st.radio("Equipment Combination",["Full Empress", "Full Necro", "2 Piece Fafnir + Empress","4 Piece Fafnir + Empress","2 Piece Fafnir + Necro","4 Piece Fafnir + Necro"])
if equip_type_combination == "Full Empress":
    equip_type = "1"
elif equip_type_combination == "Full Necro":
    equip_type = "2"
elif equip_type_combination == "2 Piece Fafnir + Empress":
    equip_type = "3"
elif equip_type_combination == "4 Piece Fafnir + Empress":
    equip_type = "4"
elif equip_type_combination == "2 Piece Fafnir + Necro":
    equip_type = "5"
else:
    equip_type = "6"

stat_type_combination = st.radio("Exp Set",["Normal","Partial Exp","Full Exp"])
if stat_type_combination == "Normal":
    stat_type = "1"
elif stat_type_combination == "Partial Exp":
    stat_type = "2"
else:
    stat_type = "3"

cash_type_combination = st.radio("Cash Set Combination",["3+3 Set","5 Set"])
if cash_type_combination == "3+3 Set":
    cash_type = "1"
else:
    cash_type = "2"

commonsum = commonsum(type, character_class)
equip = equip_selection(equip_type, stat_type, character_class, cash_type)
necalculations = nonemblemcalculations(commonsum, equip)


finalcalculations = emblemcalculations(necalculations, char)

atkstats = [finalcalculations.atk, finalcalculations.atkp, finalcalculations.dmg, finalcalculations.batk,
            finalcalculations.cr, finalcalculations.cd, finalcalculations.fd]

pskillstats = [finalcalculations.pname, finalcalculations.bpoutput(), finalcalculations.nbpoutput()]
sskillstats = [finalcalculations.sname, finalcalculations.bsoutput(), finalcalculations.nbsoutput()]
firstppercentage = -(finalcalculations.bpoutput() - finalcalculations.bpoutput())/ finalcalculations.bpoutput() * 100
secondppercentage = -(finalcalculations.bpoutput() - finalcalculations.sbpoutput())/ finalcalculations.bpoutput() * 100
firstspercentage = -(finalcalculations.bsoutput() - finalcalculations.bsoutput())/ finalcalculations.bsoutput() * 100
secondspercentage = -(finalcalculations.bsoutput() - finalcalculations.sbsoutput())/ finalcalculations.bsoutput() * 100

atkflamestats = ['ATK', necalculations.atkflame, necalculations.atkflamebase, necalculations.atklinecount]
crflamestats = ["CR", necalculations.crflame, necalculations.crflamebase, necalculations.crlinecount]
cdflamestats = ["CD", necalculations.cdflame, necalculations.cdflamebase, necalculations.cdlinecount]
flamestatsdf = pd.DataFrame(columns =['Type', 'Amount', 'Base Used', 'Number of Lines'])
flamestatsdf.loc[0] = atkflamestats
flamestatsdf.loc[1] = crflamestats
flamestatsdf.loc[2] = cdflamestats


embstats = [int(finalcalculations.ncdemb), int(finalcalculations.natkpemb), int(finalcalculations.nbatkemb), finalcalculations.bpoutput()
    , firstppercentage, finalcalculations.bsoutput(), firstspercentage]
sembstats = [int(finalcalculations.secondncdemb), int(finalcalculations.secondnatkpemb), int(finalcalculations.secondnbatkemb),
             finalcalculations.sbpoutput(), secondppercentage, finalcalculations.sbsoutput(), secondspercentage]
atkstatsdf = pd.DataFrame(columns=["ATK", "ATK%", "DMG%", "BATK%", "CR%", "CD%", "FD%"])
atkstatsdf.loc[0] = atkstats

skillstatsdf = pd.DataFrame(columns=["Skill", "Boss Output", "Non-Boss Output"])
skillstatsdf.loc[0] = pskillstats
skillstatsdf.loc[1] = sskillstats

embstatsdf = pd.DataFrame(columns=["CD Emb", "ATK Emb", "BATK Emb", "Primary DMG", "Primary %", "Secondary DMG", "Secondary %"])
embstatsdf.loc[0] = embstats
embstatsdf.loc[1] = sembstats
skillstatsdf['Boss Output'] = skillstatsdf['Boss Output'].apply(lambda x : "{:,}".format(x))
skillstatsdf['Non-Boss Output'] = skillstatsdf['Non-Boss Output'].apply(lambda x : "{:,}".format(x))

embstatsdf['Primary DMG'] = embstatsdf['Primary DMG'].apply(lambda x : "{:,}".format(x))
embstatsdf['Secondary DMG'] = embstatsdf['Secondary DMG'].apply(lambda x : "{:,}".format(x))
embstatsdf['Primary %'] = embstatsdf['Primary %'].apply(lambda x : "{:.2f}".format(x))
embstatsdf['Secondary %'] = embstatsdf['Secondary %'].apply(lambda x : "{:.2f}".format(x))

st.dataframe(skillstatsdf)
st.dataframe(flamestatsdf)
st.dataframe(atkstatsdf)
st.dataframe(embstatsdf)
