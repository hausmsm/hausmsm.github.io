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

wep = weapon(char.character_type, char.character_class)
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
from equip.necklace import necklace

necklace = necklace()
with st.sidebar.beta_expander("Necklaces"):
    if necklace.neck_amount == 2:
        st.write(f"{necklace.neck1}")
        st.write(f"SF: {necklace.neck1_sf}")
        if necklace.neck1_emblem != "None":
            st.write(f"Emblem: {necklace.neck1_emblem}")
            st.write(f"Emblem Level: {necklace.neck1_emblem_level}")
            st.write(f"Emblem Stat Amount: {necklace.neck1_emblem_amount}")
            st.write("\n")
        st.write(f"{necklace.neck2}")
        st.write(f"SF: {necklace.neck2_sf}")
        if necklace.neck2_emblem != "None":
            st.write(f"Emblem: {necklace.neck2_emblem}")
            st.write(f"Emblem Level: {necklace.neck2_emblem_level}")
            st.write(f"Emblem Stat Amount: {necklace.neck2_emblem_amount}")
    else:
        st.write("Error: Please Select 2 Necklaces Only")

## Ring
from equip.ring import ring

ring = ring()
with st.sidebar.beta_expander("Rings"):
    if ring.ring_amount == 4:
        st.write(f"{ring.ring1}")
        st.write(f"SF: {ring.ring1_sf}")
        if ring.ring1_emblem != "None":
            st.write(f"Emblem: {ring.ring1_emblem}")
            st.write(f"Emblem Level: {ring.ring1_emblem_level}")
            st.write(f"Emblem Stat Amount: {ring.ring1_emblem_amount}")
            st.write("\n")
        st.write(f"{ring.ring2}")
        st.write(f"SF: {ring.ring2_sf}")
        if ring.ring2_emblem != "None":
            st.write(f"Emblem: {ring.ring2_emblem}")
            st.write(f"Emblem Level: {ring.ring2_emblem_level}")
            st.write(f"Emblem Stat Amount: {ring.ring2_emblem_amount}")
            st.write("\n")
        st.write(f"{ring.ring3}")
        st.write(f"SF: {ring.ring3_sf}")
        if ring.ring3_emblem != "None":
            st.write(f"Emblem: {ring.ring3_emblem}")
            st.write(f"Emblem Level: {ring.ring3_emblem_level}")
            st.write(f"Emblem Stat Amount: {ring.ring3_emblem_amount}")
            st.write("\n")
        st.write(f"{ring.ring4}")
        st.write(f"SF: {ring.ring4_sf}")
        if ring.ring4_emblem != "None":
            st.write(f"Emblem: {ring.ring4_emblem}")
            st.write(f"Emblem Level: {ring.ring4_emblem_level}")
            st.write(f"Emblem Stat Amount: {ring.ring4_emblem_amount}")
    else:
        st.write("Error: Please Select 4 Rings Only")

## Earring
from equip.earring import earring

earrings = earring()
with st.sidebar.beta_expander("Earrings"):
    st.write(f"{earrings.type}")
    st.write(f"SF: {earrings.sf}")
    if earrings.sf == 5:
        st.write(f"Emblem: {earrings.emblem}")
        st.write(f"Emblem Level: {earrings.emblem_level}")
        st.write(f"Emblem Stat Amount: {earrings.emblem_amount}")

## Title
from equip.title import title

title = title()
with st.sidebar.beta_expander("Title"):
    st.write(f"{title.type}")

## Badge
from equip.badge import badge

badge = badge()
with st.sidebar.beta_expander("Badge"):
    st.write(f"{badge.type}")

## Medal
from equip.medal import medal

medal = medal()
with st.sidebar.beta_expander("Medal"):
    st.write(f"{medal.type}")

## Face Accessory
from equip.face import face

face = face()
with st.sidebar.beta_expander("Face Accessory"):
    st.write(f"{face.type}")

## Eye Accessory
from equip.eye import eye

eye = eye()
with st.sidebar.beta_expander("Eye Accessory"):
    st.write(f"{eye.type}")

## Common Stats Stuff
from common.link import link

link = link(char.character_class, char.type)
with st.sidebar.beta_expander("Link Skills"):
    if len(link.links) == 12:
        st.write(f"Link 1:{link.links[0]}")
        st.write(f"Link 2:{link.links[1]}")
        st.write(f"Link 3:{link.links[2]}")
        st.write(f"Link 4:{link.links[3]}")
        st.write(f"Link 5:{link.links[4]}")
        st.write(f"Link 6:{link.links[5]}")
        st.write(f"Link 7:{link.links[6]}")
        st.write(f"Link 8:{link.links[7]}")
        st.write(f"Link 9:{link.links[8]}")
        st.write(f"Link 10:{link.links[9]}")
        st.write(f"Link 11:{link.links[10]}")
        st.write(f"Link 12:{link.links[11]}")
    elif len(link.links) > 12:
        st.write(f"Above Link Skill Limit. Currently {len(link.links)}/12")
    else:
        st.write(f"Only {len(link.links)}/12")

from equip.jewel import jewel

jewel = jewel(char.type)
with st.sidebar.beta_expander("Jewels"):
    st.write(f"Rank: {jewel.rank}")
    st.write(f"Stat: {jewel.stat}")

from common.buffs import buffs

buffs = buffs(char.character_class, char.type)
with st.sidebar.beta_expander("Buffs"):
    if len(buffs.buffs) != 0:
        for i in buffs.buffs:
            st.write(f"{i}")

from equip.cash import cash

cash = cash()
with st.sidebar.beta_expander("Cash Set"):
    st.write(f"{cash.type}")

from common.soul import soul

soul = soul(char.character_type)
with st.sidebar.beta_expander("Soul"):
    st.write("Weapon")
    st.write(f"Soul: {soul.weapon_soul}")
    st.write(f"Soul Stat: {soul.weapon_type}")
    st.write("\n")
    st.write("Secondary Weapon")
    st.write(f"Soul: {soul.swep_soul}")
    st.write(f"Soul Stat: {soul.swep_type}")
    st.write("\n")
    st.write("Shoulder")
    st.write(f"Soul: {soul.shoulder_soul}")
    st.write(f"Soul Stat: {soul.shoulder_type}")
    st.write("\n")
    st.write("Belt")
    st.write(f"Soul: {soul.belt_soul}")
    st.write(f"Soul Stat: {soul.belt_type}")
    st.write("\n")
    st.write("Cape")
    st.write(f"Soul: {soul.cape_soul}")
    st.write(f"Soul Stat: {soul.cape_type}")

from common.pet import pet
pet = pet()
with st.sidebar.beta_expander("Pets"):
    st.write(f"Pet Type: {pet.type}")

from common.petstats import petstats
petstats = petstats(pet.type)

from equip.seteffect import seteffect
seteffect = seteffect(badge,belt,cash,cape,earrings,eye,face,glove,hat,necklace,ring,shoes,shoulder,tbo,wep,pet)
with st.sidebar.beta_expander("Set Effect"):
    st.write(f"Mythic Empress Set Count: {seteffect.mempsetcount}")
    st.write(f"Ancient Empress Set Count: {seteffect.aempsetcount}")
    st.write(f"Necro Set Count: {seteffect.necrosetcount}")
    st.write(f"Fafnir Set Count: {seteffect.fafsetcount}")
    st.write(f"Boss Accessory Set Count: {seteffect.bosssetcount}")
    st.write(f"Commander Accessory Set Count: {seteffect.commandersetcount}")

from common.flamestats import flamestats
flamestats = flamestats(badge,belt,cape,earrings,eye,face,glove,hat,jewel,medal,necklace,ring,seteffect,shoes,shoulder,
                 tbo,title,wep)
with st.sidebar.beta_expander("Flame Stats"):
    st.write(f"ATK: {flamestats.atk}")
    st.write(f"ATK%: {flamestats.atkp}")
    st.write(f"DMG%: {flamestats.dmg}")
    st.write(f"Boss ATK%: {flamestats.batk}")
    st.write(f"Crit Rate%: {flamestats.cr}")
    st.write(f"Crit DMG%: {flamestats.cd}")
    st.write(f"Final DMG%: {flamestats.fd}")
    st.write(f"Max DMG Inc: {flamestats.maxdmg}")

from common.hyperstats import hyperstats

hs = hyperstats(char.character_type)
with st.sidebar.beta_expander("Hyper Stats"):
    length = len(hs.hyperstatlist)
    for i in range(0, length):
        st.write(f"{hs.hyperstatlist[i]}: {hs.hyperstatamountlist[i]}")

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

# commonsum = commonsum(type, character_class)
# equip = equip_selection(equip_type, stat_type, character_class, cash_type)
# necalculations = nonemblemcalculations(commonsum, equip)

# finalcalculations = emblemcalculations(necalculations, char)

# atkstats = [finalcalculations.atk, finalcalculations.atkp, finalcalculations.dmg, finalcalculations.batk,
#            finalcalculations.cr, finalcalculations.cd, finalcalculations.fd]

# pskillstats = [finalcalculations.pname, finalcalculations.bpoutput(), finalcalculations.nbpoutput()]
##sskillstats = [finalcalculations.sname, finalcalculations.bsoutput(), finalcalculations.nbsoutput()]
# firstppercentage = -(finalcalculations.bpoutput() - finalcalculations.bpoutput()) / finalcalculations.bpoutput() * 100
# secondppercentage = -(finalcalculations.bpoutput() - finalcalculations.sbpoutput()) / finalcalculations.bpoutput() * 100
# firstspercentage = -(finalcalculations.bsoutput() - finalcalculations.bsoutput()) / finalcalculations.bsoutput() * 100
# secondspercentage = -(finalcalculations.bsoutput() - finalcalculations.sbsoutput()) / finalcalculations.bsoutput() * 100

# atkflamestats = ['ATK', necalculations.atkflame, necalculations.atkflamebase, necalculations.atklinecount]
# crflamestats = ["CR", necalculations.crflame, necalculations.crflamebase, necalculations.crlinecount]
# cdflamestats = ["CD", necalculations.cdflame, necalculations.cdflamebase, necalculations.cdlinecount]
# flamestatsdf = pd.DataFrame(columns=['Type', 'Amount', 'Base Used', 'Number of Lines'])
# flamestatsdf.loc[0] = atkflamestats
# flamestatsdf.loc[1] = crflamestats
# flamestatsdf.loc[2] = cdflamestats

# embstats = [int(finalcalculations.ncdemb), int(finalcalculations.natkpemb), int(finalcalculations.nbatkemb),
#            finalcalculations.bpoutput()
#    , firstppercentage, finalcalculations.bsoutput(), firstspercentage]
###sembstats = [int(finalcalculations.secondncdemb), int(finalcalculations.secondnatkpemb),
#             int(finalcalculations.secondnbatkemb),
#             finalcalculations.sbpoutput(), secondppercentage, finalcalculations.sbsoutput(), secondspercentage]
# atkstatsdf = pd.DataFrame(columns=["ATK", "ATK%", "DMG%", "BATK%", "CR%", "CD%", "FD%"])
# atkstatsdf.loc[0] = atkstats#
#
# skillstatsdf = pd.DataFrame(columns=["Skill", "Boss Output", "Non-Boss Output"])
# skillstatsdf.loc[0] = pskillstats
# skillstatsdf.loc[1] = sskillstats

# embstatsdf = pd.DataFrame(
#    columns=["CD Emb", "ATK Emb", "BATK Emb", "Primary DMG", "Primary %", "Secondary DMG", "Secondary %"])
# embstatsdf.loc[0] = embstats
# embstatsdf.loc[1] = sembstats
# skillstatsdf['Boss Output'] = skillstatsdf['Boss Output'].apply(lambda x: "{:,}".format(x))
# skillstatsdf['Non-Boss Output'] = skillstatsdf['Non-Boss Output'].apply(lambda x: "{:,}".format(x))

# embstatsdf['Primary DMG'] = embstatsdf['Primary DMG'].apply(lambda x: "{:,}".format(x))
# embstatsdf['Secondary DMG'] = embstatsdf['Secondary DMG'].apply(lambda x: "{:,}".format(x))
# embstatsdf['Primary %'] = embstatsdf['Primary %'].apply(lambda x: "{:.2f}".format(x))
# embstatsdf['Secondary %'] = embstatsdf['Secondary %'].apply(lambda x: "{:.2f}".format(x))

##st.dataframe(skillstatsdf)
# st.dataframe(flamestatsdf)
# st.dataframe(atkstatsdf)
# st.dataframe(embstatsdf)
