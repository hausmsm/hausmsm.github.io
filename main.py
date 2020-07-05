from common.commonsum import commonsum
from classes.character_selection import character_selection
from equip.equip_selection import equip_selection

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

commonsum = commonsum(type, character_class)

# Non Flame Stats
nfatk = commonsum.atk + char.atk
nfatkp = commonsum.atkp + char.atkp
nfdmg = commonsum.dmg + char.dmg
nfbatk = commonsum.batk + char.batk
nfplatk = commonsum.platk + char.platk
nfcr = commonsum.cr + char.cr
nfcatk = commonsum.cratk + char.cratk
nfcd = commonsum.cd + char.cd
nfmaxdmg = commonsum.maxdmg + char.maxdmg
nffd = commonsum.fd + char.fd

nfpdef = commonsum.pdef + char.pdef
nfpdefinc = commonsum.pdefinc + char.pdefinc
nfpdefdec = commonsum.pdefdec + char.pdefdec
nfmdef = commonsum.mdef + char.mdef
nfmdefinc = commonsum.mdefinc + char.mdefinc
nfmdefdec = commonsum.mdefdec + char.mdefdec
nfbdef = commonsum.bdef + char.bdef
nfpldef = commonsum.pldef + char.pldef
nfcritres = commonsum.critres + char.critres
nfcritdmgres = commonsum.critdmgres + char.critdmgres

nfacc = commonsum.acc + char.acc
nfaccp = commonsum.accp + char.accp
nfevd = commonsum.evd + char.evd
nfevdp = commonsum.evdp + char.evdp
nfpenrate = commonsum.penrate + char.penrate
nfblock = commonsum.block + char.block
nfabnormalstatres = commonsum.abnormalstatres + char.abnormalstatres

nfhp = commonsum.hp + char.hp
nfhpinc = commonsum.hpinc + char.hpinc
nfmp = commonsum.mp + char.mp
nfmpinc = commonsum.mpinc + char.mpinc

nfspd = commonsum.spd + char.spd
nfjmp = commonsum.jmp + char.jmp
nfkbkres = commonsum.kbkres + char.kbkres

nfexp = commonsum.exp + char.exp
nfdr = commonsum.dr + char.dr
nfmeso = commonsum.meso + char.meso
nfglincrease = commonsum.glincrease + char.glincrease
nfpartyexp = commonsum.partyexp + char.partyexp
nffeverchargeinc = commonsum.feverchargeinc + char.feverchargeinc
nffeverduration = commonsum.feverduration + char.feverduration
nfmaxfeverchance = commonsum.maxfeverchance + char.maxfeverchance
nfspmulti = commonsum.spmulti + char.spmulti

# Character Skill Specific
pname = char.pname
pskilldmg = char.pskilldmg
phitcount = char.phitcount
phatkp = char.phatkp
phdmg = char.phdmg
phbatk = char.phbatk
phcr = char.phcr
phcd = char.phcd
phfd = char.phfd

sname = char.sname
sskilldmg = char.sskilldmg
shitcount = char.shitcount
schance = char.schance
shatkp = char.shatkp
shdmg = char.shdmg
shbatk = char.shbatk
shcr = char.shcr
shcd = char.shcd
shfd = char.shfd

pname = char.pname
sname = char.sname

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
equip = equip_selection(equip_type, stat_type, character_class, cash_type)
atk = equip.atk
print(atk)
print(nfatkp, nfdmg, nfbatk, nfcr, nfcd, nffd)
print(pname, sname)
