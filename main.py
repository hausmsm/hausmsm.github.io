from common.commonsum import commonsum
from equip.equip_selection import equip_selection
from common.nonemblemcalculations import nonemblemcalculations
from common.emblemcalculations import emblemcalculations
import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
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
st.header("Weapon Selections")

## Weapon
with st.beta_expander("Weapon"):
    _,wep1,_,wep2,_,wep3,_ = st.beta_columns([0.02,0.303,0.02,0.303,0.02,0.303,0.02])
    weapon_type = wep1.selectbox("Choose Weapon Type",["Mythic Empress","Ancient Empress","Necro","Fafnir"])
    if weapon_type == "Mythic Empress":
        weapon_level = wep2.slider("Choose Weapon Level", min_value=30, max_value=40)
    else:
        weapon_level = wep2.slider("Choose Weapon Level", min_value=30, max_value=50)
    weapon_sf_level = wep2.slider("Weapon SF Level", min_value=0, max_value=31)
    if weapon_type in ["Mythic Empress","Ancient Empress"]:
        weapon_refine_level = wep2.slider("Weapon Refinement Level",min_value=1,max_value=10)
    if weapon_type != "Fafnir":
        weapon_stat = wep1.radio("Choose Weapon Stat",["Boss ATK","Crit DMG","Crit Rate","EXP"])
    else:
        weapon_stat = "None"
    weapon_emblem = wep3.radio("Choose Weapon Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
    weapon_emblem_level = wep3.slider("Weapon Emblem Level", min_value=1,max_value=5)

## Secondary Weapon
with st.beta_expander("Secondary Weapon"):
    _,swep1,_,swep2,_ = st.beta_columns([0.02,0.47,0.02,0.47,0.02])
    swep_type = swep1.selectbox("Choose Secondary Weapon Type",["Normal Class Specific","Longinus Spear"])
    swep_rank = swep2.selectbox("Choose Secondary Weapon Rank",["Unique","Legendary","Mythic"])
    _,swep3,_ = st.beta_columns([0.02,0.96,0.02])
    if swep_rank == "Unique":
        swep_sf_level = swep3.slider("SWep SF Level",min_value=0,max_value=11)
    elif swep_rank == "Legendary":
        swep_sf_level = swep3.slider("SWep SF Level", min_value=0, max_value=13)
    else:
        swep_sf_level = swep3.slider("SWep SF Level", min_value=0, max_value=16)
    if swep_type == "Longinus Spear":
        swep_level = swep3.slider('Sharenian Ability', min_value=1, max_value=10)

st.header("Armor Selections")
## Hat
with st.beta_expander("Hat"):
    _,hat1,_,hat2,_,hat3,_ = st.beta_columns([0.02,0.303,0.02,0.303,0.02,0.303,0.02])
    hat_type = hat1.selectbox("Choose Hat Type",["Mythic Empress","Ancient Empress","Necro","Fafnir"])
    if hat_type != "Fafnir":
        hat_stat = hat1.radio("Choose Hat Stat",["Boss ATK","Crit ATK","Crit DMG","EXP"])
    else:
        hat_stat = "None"
    if hat_type == "Mythic Empress":
        hat_level = hat2.slider('Hat Level', min_value=30,max_value=40)
    else:
        hat_level = hat2.slider('Hat Level', min_value=30,max_value=50)
    hat_sf_level = hat2.slider("Hat SF Level", min_value=0,max_value=30)
    hat_emblem = hat3.radio("Choose Hat Emblem Stat",["Crit DMG","Boss ATK","Phy/Mag ATK"])
    hat_emblem_level = hat3.slider("Hat Emblem Level", min_value=1,max_value=5)

## Glove
with st.beta_expander("Gloves"):
    _,glove1,_,glove2,_,glove3,_ = st.beta_columns([0.02,0.303,0.02,0.303,0.02,0.303,0.02])
    glove_type = glove1.selectbox("Choose Glove Type",["Mythic Empress","Ancient Empress","Necro"])
    glove_stat = glove1.radio("Choose Glove Stat",["ACC","Crit Atk","Crit Dmg","EXP"])
    if glove_type == "Mythic Empress":
        glove_level = glove2.slider('Glove Level', min_value=30, max_value=40)
    else:
        glove_level = glove2.slider('Glove Level', min_value=30, max_value=50)
    glove_sf_level = glove2.slider("Glove SF Level", min_value=0, max_value=30)
    glove_emblem = glove3.radio("Choose Glove Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
    glove_emblem_level = glove3.slider("Glove Emblem Level", min_value=1, max_value=5)

## Top+Bottom/Outfit
with st.beta_expander("Top+Bottom/Outfit"):
    tbo_type = st.selectbox("Choose Combination",["Top+Bottom","Outfit"])
    if tbo_type == "Outfit":
        _,outfit1,_,outfit2,_,outfit3,_ = st.beta_columns([0.02,0.303,0.02,0.303,0.02,0.303,0.02])
        outfit_type = outfit1.selectbox("Choose Outfit Type",["Mythic Empress","Ancient Empress"])
        outfit_stat = outfit1.radio("Choose Outfit Stat", ["Boss ATK", "Crit ATK", "MP Rec", "EXP"])
        if outfit_type == "Mythic Empress":
            outfit_level = outfit2.slider('Outfit Level', min_value=30, max_value=40)
        else:
            outfit_level = outfit2.slider('Outfit Level', min_value=30, max_value=50)
        outfit_sf_level = outfit2.slider("Outfit SF Level",min_value=0,max_value=30)
        outfit_emblem = outfit3.radio("Choose Outfit Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
        outfit_emblem_level = outfit3.slider("Outfit Emblem Level", min_value=1, max_value=5)
    else:
        _,tb1,_,tb2,_ = st.beta_columns([0.02, 0.47, 0.02, 0.47, 0.02])
        top_level = tb1.slider("Top Level",min_value=30, max_value=50)
        top_sf_Level = tb1.slider("Top SF Level", min_value=0, max_value=20)
        top_emblem = tb1.radio("Choose Top Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
        top_emblem_level = tb1.slider("Top Emblem Level", min_value=1, max_value=5)
        btm_level = tb2.slider("Bottom Level", min_value=30, max_value=50)
        btm_sf_Level = tb2.slider("Bottom SF Level", min_value=0, max_value=20)
        btm_emblem = tb2.radio("Choose Bottom Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
        btm_emblem_level = tb2.slider("Bottom Emblem Level", min_value=1, max_value=5)


## Shoulders
with st.beta_expander("Shoulder"):
    _,shoulder1,_,shoulder2,_,shoulder3,_ = st.beta_columns([0.02, 0.303, 0.02, 0.303, 0.02, 0.303, 0.02])
    shoulder_type = shoulder1.selectbox("Choose Shoulder Type",["Mythic Empress","Ancient Empress","Necro"])
    shoulder_stat = shoulder1.radio("Choose Shoulder Stat", ["Crit Atk", "EXP", "HP Rec", "MP Rec"])
    if shoulder_type == "Mythic Empress":
        shoulder_level = shoulder2.slider('Shoulder Level', min_value=30, max_value=40)
    else:
        shoulder_level = shoulder2.slider('Shoulder Level', min_value=30, max_value=50)
    shoulder_sf_level = shoulder2.slider("Shoulder SF Level",min_value=0,max_value=30)
    shoulder_emblem = shoulder3.radio("Choose Shoulder Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
    shoulder_emblem_level = shoulder3.slider("Shoulder Emblem Level", min_value=1, max_value=5)

## Shoes
with st.beta_expander("Shoes"):
    _,shoes1,_,shoes2,_,shoes3,_ = st.beta_columns([0.02, 0.303, 0.02, 0.303, 0.02, 0.303, 0.02])
    shoes_type = shoes1.selectbox("Choose Shoes Type",["Mythic Empress","Ancient Empress","Necro"])
    shoes_stat = shoes1.radio("Choose Shoes Stat", ["Crit Atk", "EVD", "EXP", "HP Rec"])
    if shoes_type == "Mythic Empress":
        shoes_level = shoes2.slider('Shoes Level', min_value=30, max_value=40)
    else:
        shoes_level = shoes2.slider('Shoes Level', min_value=30, max_value=50)
    shoes_sf_level = shoes2.slider("Shoes SF Level",min_value=0, max_value=30)
    shoes_emblem = shoes3.radio("Choose Shoes Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
    shoes_emblem_level = shoes3.slider("Shoes Emblem Level", min_value=1, max_value=5)

## Belt
with st.beta_expander("Belt"):
    _,belt1,_,belt2,_,belt3,_ = st.beta_columns([0.02, 0.303, 0.02, 0.303, 0.02, 0.303, 0.02])
    belt_type = belt1.selectbox("Choose Belt Type",["Mythic Empress","Ancient Empress","Necro"])
    belt_stat = belt1.radio("Choose Belt Stat", ["ACC", "Crit Rate", "Drop", "EXP"])
    if belt_type == "Mythic Empress":
        belt_level = belt2.slider('Belt Level', min_value=30, max_value=40)
    else:
        belt_level = belt2.slider('Belt Level', min_value=30, max_value=50)
    belt_sf_level = belt2.slider("Belt SF Level",min_value=0, max_value=30)
    belt_emblem = belt3.radio("Choose Belt Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
    belt_emblem_level = belt3.slider("Belt Emblem Level", min_value=1, max_value=5)

## Cape
with st.beta_expander("Cape"):
    _,cape1,_,cape2,_,cape3,_ = st.beta_columns([0.02, 0.303, 0.02, 0.303, 0.02, 0.303, 0.02])
    cape_type = cape1.selectbox("Choose Cape Type",["Mythic Empress","Ancient Empress","Necro"])
    cape_stat = cape1.radio("Choose Cape Stat", ["Crit Rate", "EVD", "EXP", "Meso"])
    if cape_type == "Mythic Empress":
        cape_level = cape2.slider('Cape Level', min_value=30, max_value=40)
    else:
        cape_level = cape2.slider('Cape Level', min_value=30, max_value=50)
    cape_sf_level = cape2.slider("Cape SF Level",min_value=0, max_value=30)
    cape_emblem = cape3.radio("Choose Cape Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
    cape_emblem_level = cape3.slider("Cape Emblem Level", min_value=1, max_value=5)

st.header("Accessory Selections")
## Necklace
with st.beta_expander("Necklace"):
    necklaces = st.multiselect("Choose 2 Necklaces",["Horntail Necklace (Unique)","Horntail Necklace (Legendary)","Mu Lung Dojo Pendant (Epic)","Mu Lung Dojo Pendant (Unique)","Ifia's Necklace","Spigelmann's Necklace of Chaos"])
    if len(necklaces) == 2:
        _,neck1,_,neck2,_ = st.beta_columns([0.02,0.47,0.02,0.47,0.02])
        if necklaces[0] in ["Horntail Necklace (Unique)","Horntail Necklace (Legendary)","Ifia's Necklace"]:
            neck1_sf_level = neck1.slider(f"{necklaces[0]} SF Level", min_value=0, max_value=5)
            if neck1_sf_level == 5:
                neck1_emblem_stat = neck1.radio(f"Choose {necklaces[0]} Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                neck1_emblem_level = neck1.slider(f"{necklaces[0]} Emblem Level", min_value=1,max_value=5)
        if necklaces[1] in ["Horntail Necklace (Unique)", "Horntail Necklace (Legendary)", "Ifia's Necklace"]:
            neck2_sf_level = neck2.slider(f"{necklaces[1]} SF Level", min_value=0, max_value=5)
            if neck2_sf_level == 5:
                neck2_emblem_stat = neck2.radio(f"Choose {necklaces[1]} Emblem Stat",
                                                ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                neck2_emblem_level = neck2.slider(f"{necklaces[1]} Emblem Level", min_value=1, max_value=5)
    else:
        st.write("Error: Please Select 2 Necklaces Only")

## Ring
with st.beta_expander("Rings"):
    rings = st.multiselect("Choose 4 Rings",["Cygnus Ring (Unique)","Cygnus Ring (Legendary)","Horntail Ring (Legendary)","Horntail Ring (Unique)","Kerning Tower 50F Ring","Kerning M Ring","Attendance Ring","Ifia's Ring","Noble Ifia's Ring","Master Soul Ring SS"])
    if len(rings) == 4:
        _,ring1,_,ring2,_,ring3,_,ring4,_ = st.beta_columns([0.02,0.225,0.02,0.225,0.02,0.225,0.02,0.225,0.02])
        if rings[0] in ["Cygnus Ring (Unique)","Cygnus Ring (Legendary)","Horntail Ring (Legendary)","Horntail Ring (Unique)","Ifia's Ring","Noble Ifia's Ring"]:
            ring1_sf_level = ring1.slider(f"{rings[0]} SF Level",min_value=0,max_value=5)
            if ring1_sf_level == 5:
                ring1_emblem_stat = ring1.radio(f"Choose {rings[0]} Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                ring1_emblem_level = ring1.slider(f"{rings[0]} Emblem Level", min_value=1, max_value=5)
        else:
            ring1.subheader(f"{rings[0]}")
        if rings[1] in ["Cygnus Ring (Unique)","Cygnus Ring (Legendary)","Horntail Ring (Legendary)","Horntail Ring (Unique)","Ifia's Ring","Noble Ifia's Ring"]:
            ring2_sf_level = ring2.slider(f"{rings[1]} SF Level",min_value=0,max_value=5)
            if ring2_sf_level == 5:
                ring2_emblem_stat = ring2.radio(f"Choose {rings[1]} Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                ring2_emblem_level = ring2.slider(f"{rings[1]} Emblem Level", min_value=1, max_value=5)
        else:
            ring2.subheader(f"{rings[1]}")
        if rings[2] in ["Cygnus Ring (Unique)","Cygnus Ring (Legendary)","Horntail Ring (Legendary)","Horntail Ring (Unique)","Ifia's Ring","Noble Ifia's Ring"]:
            ring3_sf_level = ring3.slider(f"{rings[2]} SF Level",min_value=0,max_value=5)
            if ring3_sf_level == 5:
                ring3_emblem_stat = ring3.radio(f"Choose {rings[2]} Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                ring3_emblem_level = ring3.slider(f"{rings[2]} Emblem Level", min_value=1, max_value=5)
        else:
            ring3.subheader(f"{rings[2]}")
        if rings[3] in ["Cygnus Ring (Unique)","Cygnus Ring (Legendary)","Horntail Ring (Legendary)","Horntail Ring (Unique)","Ifia's Ring","Noble Ifia's Ring"]:
            ring4_sf_level = ring4.slider(f"{rings[3]} SF Level",min_value=0,max_value=5)
            if ring4_sf_level == 5:
                ring4_emblem_stat = ring4.radio(f"Choose {rings[3]} Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                ring4_emblem_level = ring4.slider(f"{rings[3]} Emblem Level", min_value=1, max_value=5)
        else:
            ring4.subheader(f"{rings[3]}")
    else:
        st.write("Error: Please Select 4 Rings Only")
## Earring
with st.beta_expander("Earring"):
    _,earring1,_ = st.beta_columns([0.02,0.96,0.02])
    earring = earring1.selectbox("Choose Earring",["Horntail Earring (Unique)","Horntail Earring (Legendary)","Ifia's Earring"])
    earring_sf_level = earring1.slider("Earring SF Level",min_value=0,max_value=5)
    if earring_sf_level == 5:
        earring_emblem_stat = earring1.radio("Choose Earring Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
        earring_emblem_level = earring1.slider("Earring Emblem Level", min_value=1, max_value=5)

## Title
with st.beta_expander("Title"):
    _,title1,_ = st.beta_columns([0.02,0.96,0.02])
    title = title1.selectbox("Choose Title",["Holy Pink Beanity"])

## Badge
with st.beta_expander("Badge"):
    _, badge1, _ = st.beta_columns([0.02, 0.96, 0.02])
    badge = badge1.selectbox("Choose Badge", ["Crystal Ventus Badge"])

## Medal
with st.beta_expander("Medal"):
    _, medal1, _ = st.beta_columns([0.02, 0.96, 0.02])
    medal = medal1.selectbox("Choose Medal", ["Holy Pink Beanity"])

## Face Accessory
with st.beta_expander("Face Accessory"):
    _, face1, _ = st.beta_columns([0.02, 0.96, 0.02])
    face = face1.selectbox("Choose Face Accessory", ["Dark Premium Symbol (Legendary)"])

## Eye Accessory
with st.beta_expander("Eye Accessory"):
    _, eye1, _ = st.beta_columns([0.02, 0.96, 0.02])
    eye = eye1.selectbox("Choose Eye Accessory", ["Chaos Pink Bean Mark (Legendary)"])

## Common Stats Stuff
with st.beta_expander("Link Skills"):
    linkskills = ["HP/MP Rec (Wind Archer)", "Meso (Night Lord)", "Gold Leaf (Bow Master)",
                  "Fever Duration (Blaze Wizard)","Drop (Night Walker)","HP% (Thunder Breaker)","Fever Recharge (Aran)",
                  "Boss ATK (Evan)","KBK RES (Corsair)","Crit Rate (Shadower)","EXP (Mercedes)","MP% (Ice Lightning Mage)",
                  "Phy DEF (Dark Knight)","Phy ATK (Buccaneer)","PEN (Paladin)","Crit DMG (Phantom)","Mag ATK (Fire Poison Mage)",
                  "ACC (Marksman)","Mag DMG (Luminous)","Mag DEF (Dawn Warrior)","Alive Chance (Shade)","Boss DEF (Hero)",
                  "Abnormal Status RES (Battle Mage, Wild Hunter & Mechanic)","Boss ATK (Demon Slayer)","Phy DMG (Demon Avenger)",
                  "Party EXP (Bishop)"]

    _, links1, _ = st.beta_columns([0.02, 0.96, 0.02])
    links = links1.multiselect("Choose 12 Link Skills",linkskills)

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
