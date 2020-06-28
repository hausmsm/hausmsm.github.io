from common.mapletree import mapletree
from common.link import link
from common.buffs import buffs
from classes.character_selection import character_selection

#Maple Tree Festival
tree = mapletree()
nfatkp = tree.atkp
nfdmg = tree.dmg
nfbatk = tree.batk
nfcr = tree.cr
nfcd = tree.cd
nffd = tree.fd

#Link Skills
link = link()
nfatkp += link.atkp
nfdmg += link.dmg
nfbatk += link.batk
nfcr += link.cr
nfcd += link.cd
nffd += link.fd

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

if character_type == "MAGE":
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

if character_type == "ARCHER":
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

if character_type == "THIEF":
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

if character_type == "PIRATE":
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

#Buffs
buff = buffs(type,character_class)

nfatkp += (char.atkp + buff.atkp)
nfdmg += (char.dmg + buff.dmg)
nfbatk += (char.batk + buff.batk)
nfcr += (char.cr + buff.cr)
nfcd += (char.cd + buff.cd)
nffd += (char.fd + buff.fd)

pname = char.pname
sname = char.sname
print(nfatkp,nfdmg,nfbatk,nfcr,nfcd,nffd)
print(pname,sname)