from common.commonsum import commonsum
from equip.equip_selection import equip_selection
from common.nonemblemcalculations import nonemblemcalculations
from common.emblemcalculations import emblemcalculations
import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
st.title("Automatic Emblem Calculator")

st.sidebar.header("Summary")

# Character Selection
st.header("Class Selection")
from classes.character_selection import character_selection
char = character_selection()
st.sidebar.subheader("Class")
st.sidebar.write(f"{char.character_class}")

# Equipment Choosing
st.header("Weapon Selections")

## Weapon
from equip.weapon import weapon
wep = weapon(char.character_type,char.character_class)
with st.sidebar.beta_expander("Weapon"):
    st.write(f"{wep.type}")
    st.write(f"Level: {wep.level}")
    st.write(f"ATK: {wep.atk}")
    st.write(f"{wep.stat}: {wep.stat_amount:.1f}")
    st.write(f"SF: {wep.sf}")
    st.write(f"Emblem: {wep.emblem}")
    st.write(f"Emblem Level: {wep.emblem_level}")
    st.write(f"Emblem Stat Amount: {wep.emblem_amount}")

## Secondary Weapon
from equip.secweapon import secweapon
swep = secweapon()
with st.sidebar.beta_expander("Secondary Weapon"):
    st.write(f"{swep.rank} {swep.type}")
    st.write(f"SF: {swep.sf}")
    if swep.type == "Longinus Spear":
        st.write(f"Refinement Level: {swep.level()}")

st.header("Armor Selections")
## Hat
from equip.hat import hat
hat = hat()
with st.sidebar.beta_expander("Hat"):
    st.write(f"{hat.type}")
    st.write(f"Level: {hat.level}")
    st.write(f"{hat.stat}: {hat.stat_amount:.1f}")
    st.write(f"SF: {hat.sf}")
    st.write(f"Emblem: {hat.emblem}")
    st.write(f"Emblem Level: {hat.emblem_level}")
    st.write(f"Emblem Stat Amount: {hat.emblem_amount}")

## Glove
from equip.glove import glove
glove = glove()
with st.sidebar.beta_expander("Glove"):
    st.write(f"{glove.type}")
    st.write(f"Level: {glove.level}")
    st.write(f"{glove.stat}: {glove.stat_amount:.1f}")
    st.write(f"SF: {glove.sf}")
    st.write(f"Emblem: {glove.emblem}")
    st.write(f"Emblem Level: {glove.emblem_level}")
    st.write(f"Emblem Stat Amount: {glove.emblem_amount}")

## Top+Bottom/Outfit
from equip.tbo import tbo
tbo = tbo()
if tbo.tbo() == "Top+Bottom":
    with st.sidebar.beta_expander("Top+Bottom"):
        st.write(f"Top Level: {tbo.top_level}, Bottom Level: {tbo.btm_level}")
        st.write(f"Top SF: {tbo.top_sf}, Bottom SF: {tbo.btm_sf}")
        st.write(f"Top Emblem: {tbo.top_emblem}")
        st.write(f"Top Emblem Level: {tbo.top_emblem_level}")
        st.write(f"Top Emblem Stat Amount: {tbo.top_emblem_amount}")
        st.write(f"Bottom Emblem: {tbo.btm_emblem}")
        st.write(f"Bottom Emblem Level: {tbo.btm_emblem_level}")
        st.write(f"Bottom Emblem Stat Amount: {tbo.btm_emblem_amount}")
else:
    with st.sidebar.beta_expander("Outfit"):
        st.write(f"{tbo.type}")
        st.write(f"Level: {tbo.level}")
        st.write(f"{tbo.stat}: {tbo.stat_amount:.1f}")
        st.write(f"SF: {tbo.sf}")
        st.write(f"Emblem: {tbo.emblem}")
        st.write(f"Emblem Level: {tbo.emblem_level}")
        st.write(f"Emblem Stat Amount: {tbo.emblem_amount}")

## Shoulders
from equip.shoulder import shoulder
shoulder = shoulder()
with st.sidebar.beta_expander("Shoulder"):
    st.write(f"{shoulder.type}")
    st.write(f"Level: {shoulder.level}")
    st.write(f"{shoulder.stat}: {shoulder.stat_amount:.1f}")
    st.write(f"SF: {shoulder.sf}")
    st.write(f"Emblem: {shoulder.emblem}")
    st.write(f"Emblem Level: {shoulder.emblem_level}")
    st.write(f"Emblem Stat Amount: {shoulder.emblem_amount}")

## Shoes
from equip.shoe import shoe
shoes = shoe()
with st.sidebar.beta_expander("Shoes"):
    st.write(f"{shoes.type}")
    st.write(f"Level: {shoes.level}")
    st.write(f"{shoes.stat}: {shoes.stat_amount:.1f}")
    st.write(f"SF: {shoes.sf}")
    st.write(f"Emblem: {shoes.emblem}")
    st.write(f"Emblem Level: {shoes.emblem_level}")
    st.write(f"Emblem Stat Amount: {shoes.emblem_amount}")

## Belt
from equip.belt import belt
belt = belt()
with st.sidebar.beta_expander("Belt"):
    st.write(f"{belt.type}")
    st.write(f"Level: {belt.level}")
    st.write(f"{belt.stat}: {belt.stat_amount:.1f}")
    st.write(f"SF: {belt.sf}")
    st.write(f"Emblem: {belt.emblem}")
    st.write(f"Emblem Level: {belt.emblem_level}")
    st.write(f"Emblem Stat Amount: {belt.emblem_amount}")

## Cape
from equip.cape import cape
cape = cape()
with st.sidebar.beta_expander("Cape"):
    st.write(f"{cape.type}")
    st.write(f"Level: {cape.level}")
    st.write(f"{cape.stat}: {cape.stat_amount:.1f}")
    st.write(f"SF: {cape.sf}")
    st.write(f"Emblem: {cape.emblem}")
    st.write(f"Emblem Level: {cape.emblem_level}")
    st.write(f"Emblem Stat Amount: {cape.emblem_amount}")

st.header("Accessory Selections")
## Necklace
with st.beta_expander("Necklace"):
    necklaces = st.multiselect("Choose 2 Necklaces", ["Horntail Necklace (Unique)", "Horntail Necklace (Legendary)",
                                                      "Mu Lung Dojo Pendant (Epic)", "Mu Lung Dojo Pendant (Unique)",
                                                      "Ifia's Necklace", "Spigelmann's Necklace of Chaos"])
    if len(necklaces) == 2:
        _, neck1, _, neck2, _ = st.beta_columns([0.02, 0.47, 0.02, 0.47, 0.02])
        if necklaces[0] in ["Horntail Necklace (Unique)", "Horntail Necklace (Legendary)", "Ifia's Necklace"]:
            neck1_sf_level = neck1.slider(f"{necklaces[0]} SF Level", min_value=0, max_value=5)
            if neck1_sf_level == 5:
                neck1_emblem_stat = neck1.radio(f"Choose {necklaces[0]} Emblem Stat",
                                                ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                neck1_emblem_level = neck1.slider(f"{necklaces[0]} Emblem Level", min_value=1, max_value=5)
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
    rings = st.multiselect("Choose 4 Rings",
                           ["Cygnus Ring (Unique)", "Cygnus Ring (Legendary)", "Horntail Ring (Legendary)",
                            "Horntail Ring (Unique)", "Kerning Tower 50F Ring", "Kerning M Ring", "Attendance Ring",
                            "Ifia's Ring", "Noble Ifia's Ring", "Master Soul Ring SS"])
    if len(rings) == 4:
        _, ring1, _, ring2, _, ring3, _, ring4, _ = st.beta_columns(
            [0.02, 0.225, 0.02, 0.225, 0.02, 0.225, 0.02, 0.225, 0.02])
        if rings[0] in ["Cygnus Ring (Unique)", "Cygnus Ring (Legendary)", "Horntail Ring (Legendary)",
                        "Horntail Ring (Unique)", "Ifia's Ring", "Noble Ifia's Ring"]:
            ring1_sf_level = ring1.slider(f"{rings[0]} SF Level", min_value=0, max_value=5)
            if ring1_sf_level == 5:
                ring1_emblem_stat = ring1.radio(f"Choose {rings[0]} Emblem Stat",
                                                ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                ring1_emblem_level = ring1.slider(f"{rings[0]} Emblem Level", min_value=1, max_value=5)
        else:
            ring1.subheader(f"{rings[0]}")
        if rings[1] in ["Cygnus Ring (Unique)", "Cygnus Ring (Legendary)", "Horntail Ring (Legendary)",
                        "Horntail Ring (Unique)", "Ifia's Ring", "Noble Ifia's Ring"]:
            ring2_sf_level = ring2.slider(f"{rings[1]} SF Level", min_value=0, max_value=5)
            if ring2_sf_level == 5:
                ring2_emblem_stat = ring2.radio(f"Choose {rings[1]} Emblem Stat",
                                                ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                ring2_emblem_level = ring2.slider(f"{rings[1]} Emblem Level", min_value=1, max_value=5)
        else:
            ring2.subheader(f"{rings[1]}")
        if rings[2] in ["Cygnus Ring (Unique)", "Cygnus Ring (Legendary)", "Horntail Ring (Legendary)",
                        "Horntail Ring (Unique)", "Ifia's Ring", "Noble Ifia's Ring"]:
            ring3_sf_level = ring3.slider(f"{rings[2]} SF Level", min_value=0, max_value=5)
            if ring3_sf_level == 5:
                ring3_emblem_stat = ring3.radio(f"Choose {rings[2]} Emblem Stat",
                                                ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                ring3_emblem_level = ring3.slider(f"{rings[2]} Emblem Level", min_value=1, max_value=5)
        else:
            ring3.subheader(f"{rings[2]}")
        if rings[3] in ["Cygnus Ring (Unique)", "Cygnus Ring (Legendary)", "Horntail Ring (Legendary)",
                        "Horntail Ring (Unique)", "Ifia's Ring", "Noble Ifia's Ring"]:
            ring4_sf_level = ring4.slider(f"{rings[3]} SF Level", min_value=0, max_value=5)
            if ring4_sf_level == 5:
                ring4_emblem_stat = ring4.radio(f"Choose {rings[3]} Emblem Stat",
                                                ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                ring4_emblem_level = ring4.slider(f"{rings[3]} Emblem Level", min_value=1, max_value=5)
        else:
            ring4.subheader(f"{rings[3]}")
    else:
        st.write("Error: Please Select 4 Rings Only")
## Earring
with st.beta_expander("Earring"):
    _, earring1, _ = st.beta_columns([0.02, 0.96, 0.02])
    earring = earring1.selectbox("Choose Earring",
                                 ["Horntail Earring (Unique)", "Horntail Earring (Legendary)", "Ifia's Earring"])
    earring_sf_level = earring1.slider("Earring SF Level", min_value=0, max_value=5)
    if earring_sf_level == 5:
        earring_emblem_stat = earring1.radio("Choose Earring Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
        earring_emblem_level = earring1.slider("Earring Emblem Level", min_value=1, max_value=5)

## Title
with st.beta_expander("Title"):
    _, title1, _ = st.beta_columns([0.02, 0.96, 0.02])
    title = title1.selectbox("Choose Title", ["Holy Pink Beanity"])

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
                  "Fever Duration (Blaze Wizard)", "Drop (Night Walker)", "HP% (Thunder Breaker)",
                  "Fever Recharge (Aran)",
                  "Boss ATK (Evan)", "KBK RES (Corsair)", "Crit Rate (Shadower)", "EXP (Mercedes)",
                  "MP% (Ice Lightning Mage)",
                  "Phy DEF (Dark Knight)", "Phy ATK (Buccaneer)", "PEN (Paladin)", "Crit DMG (Phantom)",
                  "Mag ATK (Fire Poison Mage)",
                  "ACC (Marksman)", "Mag DMG (Luminous)", "Mag DEF (Dawn Warrior)", "Alive Chance (Shade)",
                  "Boss DEF (Hero)",
                  "Abnormal Status RES (Battle Mage, Wild Hunter & Mechanic)", "Boss ATK (Demon Slayer)",
                  "Phy DMG (Demon Avenger)",
                  "Party EXP (Bishop)"]

    _, links1, _ = st.beta_columns([0.02, 0.96, 0.02])
    links = links1.multiselect("Choose 12 Link Skills", linkskills)

equip_type_combination = st.radio("Equipment Combination",
                                  ["Full Empress", "Full Necro", "2 Piece Fafnir + Empress", "4 Piece Fafnir + Empress",
                                   "2 Piece Fafnir + Necro", "4 Piece Fafnir + Necro"])
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

stat_type_combination = st.radio("Exp Set", ["Normal", "Partial Exp", "Full Exp"])
if stat_type_combination == "Normal":
    stat_type = "1"
elif stat_type_combination == "Partial Exp":
    stat_type = "2"
else:
    stat_type = "3"

cash_type_combination = st.radio("Cash Set Combination", ["3+3 Set", "5 Set"])
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
firstppercentage = -(finalcalculations.bpoutput() - finalcalculations.bpoutput()) / finalcalculations.bpoutput() * 100
secondppercentage = -(finalcalculations.bpoutput() - finalcalculations.sbpoutput()) / finalcalculations.bpoutput() * 100
firstspercentage = -(finalcalculations.bsoutput() - finalcalculations.bsoutput()) / finalcalculations.bsoutput() * 100
secondspercentage = -(finalcalculations.bsoutput() - finalcalculations.sbsoutput()) / finalcalculations.bsoutput() * 100

atkflamestats = ['ATK', necalculations.atkflame, necalculations.atkflamebase, necalculations.atklinecount]
crflamestats = ["CR", necalculations.crflame, necalculations.crflamebase, necalculations.crlinecount]
cdflamestats = ["CD", necalculations.cdflame, necalculations.cdflamebase, necalculations.cdlinecount]
flamestatsdf = pd.DataFrame(columns=['Type', 'Amount', 'Base Used', 'Number of Lines'])
flamestatsdf.loc[0] = atkflamestats
flamestatsdf.loc[1] = crflamestats
flamestatsdf.loc[2] = cdflamestats

embstats = [int(finalcalculations.ncdemb), int(finalcalculations.natkpemb), int(finalcalculations.nbatkemb),
            finalcalculations.bpoutput()
    , firstppercentage, finalcalculations.bsoutput(), firstspercentage]
sembstats = [int(finalcalculations.secondncdemb), int(finalcalculations.secondnatkpemb),
             int(finalcalculations.secondnbatkemb),
             finalcalculations.sbpoutput(), secondppercentage, finalcalculations.sbsoutput(), secondspercentage]
atkstatsdf = pd.DataFrame(columns=["ATK", "ATK%", "DMG%", "BATK%", "CR%", "CD%", "FD%"])
atkstatsdf.loc[0] = atkstats

skillstatsdf = pd.DataFrame(columns=["Skill", "Boss Output", "Non-Boss Output"])
skillstatsdf.loc[0] = pskillstats
skillstatsdf.loc[1] = sskillstats

embstatsdf = pd.DataFrame(
    columns=["CD Emb", "ATK Emb", "BATK Emb", "Primary DMG", "Primary %", "Secondary DMG", "Secondary %"])
embstatsdf.loc[0] = embstats
embstatsdf.loc[1] = sembstats
skillstatsdf['Boss Output'] = skillstatsdf['Boss Output'].apply(lambda x: "{:,}".format(x))
skillstatsdf['Non-Boss Output'] = skillstatsdf['Non-Boss Output'].apply(lambda x: "{:,}".format(x))

embstatsdf['Primary DMG'] = embstatsdf['Primary DMG'].apply(lambda x: "{:,}".format(x))
embstatsdf['Secondary DMG'] = embstatsdf['Secondary DMG'].apply(lambda x: "{:,}".format(x))
embstatsdf['Primary %'] = embstatsdf['Primary %'].apply(lambda x: "{:.2f}".format(x))
embstatsdf['Secondary %'] = embstatsdf['Secondary %'].apply(lambda x: "{:.2f}".format(x))

st.dataframe(skillstatsdf)
st.dataframe(flamestatsdf)
st.dataframe(atkstatsdf)
st.dataframe(embstatsdf)
