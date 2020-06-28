from common.mapletree import mapletree
from common.link import link
from classes.character_selection import character_selection

#Maple Tree Festival
tree = mapletree()
atkp = tree.atkp
dmg = tree.dmg
batk = tree.batk
cr = tree.cr
cd = tree.cd
fd = tree.fd

#Link Skills
link = link()
atkp += link.atkp
dmg += link.dmg
batk += link.batk
cr += link.cr
cd += link.cd
fd += link.fd

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
        from classes.dk import dk
        char = dk()

    elif character_class == "HERO":
        from classes.hero import hero
        char = hero()

    elif character_class == "PALA":
        from classes.pala import pala
        char = pala()

if character_type == "MAGE":
    mage = character_selection.mage()
    character_class = mage

if character_type == "ARCHER":
    archer = character_selection.archer()
    character_class = archer

if character_type == "THIEF":
    thief = character_selection.thief()
    character_class = thief

if character_type == "PIRATE":
    pirate = character_selection.pirate()
    character_class = pirate



atkp += char.atkp
dmg += char.dmg
batk += char.batk
cr += char.cr
cd += char.cd
fd += char.fd

pname = char.pname
sname = char.sname
print(atkp,dmg,batk,cr,cd,fd)
print(pname,sname)