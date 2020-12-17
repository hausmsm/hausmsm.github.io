import streamlit as st
import math
import pandas as pd


class buffs:
    def __init__(self, character_class, type):
        # Initialize
        self.emblem = "None"
        self.emblem_amount = 0
        self.character_class = character_class
        self.type = type
        self.buffs = list

        # SF Stats
        self.sf = 0

        # Offensive Stats
        self.atk = 0
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.platk = 0
        self.cr = 0
        self.cratk = 0
        self.cd = 0
        self.maxdmg = 0
        self.fd = 0

        # Defensive Stats
        self.pdef = 0
        self.pdefinc = 0
        self.pdefdec = 0
        self.mdef = 0
        self.mdefinc = 0
        self.mdefdec = 0
        self.bdef = 0
        self.pldef = 0
        self.critres = 0
        self.critdmgres = 0

        # Hit Miss Stats
        self.acc = 0
        self.accp = 0
        self.evd = 0
        self.evdp = 0
        self.penrate = 0
        self.block = 0
        self.abnormalstatres = 0

        # HP MP Stats
        self.hp = 0
        self.mp = 0
        self.hpinc = 0
        self.mpinc = 0
        self.hprec = 0
        self.mprec = 0
        self.buffdurationinc = 0

        # Mobility Stats
        self.spd = 0
        self.jmp = 0
        self.kbkres = 0

        # Misc Stats
        self.exp = 0
        self.dr = 0
        self.meso = 0
        self.glincrease = 0
        self.partyexp = 0
        self.feverchargeinc = 0
        self.feverduration = 0
        self.maxfeverchance = 0

        # Shadow Partner Stats
        self.spmulti = 0

        # Set Stats
        self.mempsetcount = 0
        self.aempsetcount = 0
        self.necrosetcount = 0
        self.fafsetcount = 0
        self.bosssetcount = 0
        self.commandersetcount = 0

        # Flame Stats
        self.atklinecount = 0
        self.crlinecount = 0
        self.cdlinecount = 0

        jobbuff = {
            # Warrior
            "Dark Knight": ["Hyper Body (Phy DMG Reduction, Mag DMG Reduction)", "Iron Will (Boss DEF%, Player DEF%)"],
            "Hero": ["Unmanaged Anger (Phy ATK%)"],
            "Paladin": ["Combat Orders (Phy DMG%, Mag DMG%)", "Parashock Guard (Phy DMG Reduction, Mag DMG Reduction)"],
            "Dawn Warrior": [],
            "Aran": ["Maha's Blessing (HP, MP)"],
            "Demon Slayer": [],
            "Demon Avenger": [],
            # Mage
            "Bishop": ["Advanced Blessing (Phy ATK%, Mag ATK%, ACC%, EVD%)", "Holy Shell (HP%, MP%, HP, MP)",
                       "Holy Symbol (EXP, KBK Res)"],
            "Ice Lightning Mage": ["Meditation (Mag DMG%)", "Absolute Zero Aura (KBK RES, Abnormal Status RES)"],
            "Fire Poison Mage": ["Meditation (Mag DMG%)"],
            "Blaze Wizard": ["Burning Conduit (Phy ATK%, Mag ATK%, Phy DMG%, Mag DMG%)"],
            "Evan": ["Return Dive (Phy DMG%, Mag DMG%)"],
            "Luminous": ["Photic Meditation (Mag ATK%)"],
            "Battle Mage": ["Dark Aura (Phy DMG%, Mag DMG%)"],
            # Archer
            "Bow Master": [],
            "Marksman": [],
            "Wind Archer": [],
            "Mercedes": [],
            "Wild Hunter": ["Call of the Wild (Phy ATK%, Mag ATK%)"],
            # Thief
            "Night Lord": [],
            "Shadower": [],
            "Night Walker": [],
            "Phantom": ["Unmanaged Anger (Phy ATK%)", "Combat Orders (Phy DMG%, Mag DMG%)"],
            # Pirate
            "Corsair": [],
            "Buccaneer": ["Speed Infusion (Boss ATK%, Player ATK%)"],
            "Thunder Breaker": ["Speed Infusion (Boss ATK%, Player ATK%)"],
            "Shade": [],
            "Mechanic": ["Support Unit: H-EX (Phy DMG%, Mag DMG%, FD%)"]
        }
        buffs_list = ["Hyper Body (Phy DMG Reduction, Mag DMG Reduction)", "Iron Will (Boss DEF%, Player DEF%)",
                      "Unmanaged Anger (Phy ATK%)", "Combat Orders (Phy DMG%, Mag DMG%)",
                      "Parashock Guard (Phy DMG Reduction, Mag DMG Reduction)", "Maha's Blessing (HP, MP)",
                      "Advanced Blessing (Phy ATK%, Mag ATK%, ACC%, EVD%)", "Holy Shell (HP%, MP%, HP, MP)",
                      "Holy Symbol (EXP, KBK Res)", "Meditation (Mag DMG%)",
                      "Absolute Zero Aura (KBK RES, Abnormal Status RES)",
                      "Burning Conduit (Phy ATK%, Mag ATK%, Phy DMG%, Mag DMG%)", "Return Dive (Phy DMG%, Mag DMG%)",
                      "Photic Meditation (Mag ATK%)", "Dark Aura (Phy DMG%, Mag DMG%)",
                      "Call of the Wild (Phy ATK%, Mag ATK%)", "Speed Infusion (Boss ATK%, Player ATK%)",
                      "Support Unit: H-EX (Phy DMG%, Mag DMG%, FD%)"
                      ]

        cash_buffs_list = ["Fried Shrimp (50% Boss ATK)", "Baby Chick Cookie (30% Boss ATK)",
                           "Fruity Yoghurt (50% Phy ATK)", "Grape Juice (50% Mag ATK)",
                           "Buttery Roasted Squid (30% Mag ATK)", "Chestnut (30% Crit DMG)",
                           "Carrot Juice (30% Crit Rate)", "Candy Basket (30% Phy DMG)", "Candy Cane (30% Mag DMG)",
                           "Buckwheat Paste (30% Phy ATK)", "Fruity Candy (30% ACC)", "Dumpling (30% SPD)",
                           "Cafe Latte (30% Phy DEF)", "Cake (30% Mag DEF)", "Coconut (300 HP)", "Cookie (300 MP)",
                           "Electrolyte Drink (300 HP Rec)", "Corn Stick (300 MP Rec)",
                           "Cotton Candy on a Stick (30% EXP)", "Cronos's Egg (30% Meso)", "Cup of Coffee (30% Drop)",
                           "Egg (30% JMP)", "Berzerker Bon-Bons (30% Boss DEF)", "Halloween Candy (50% Phy DEF)",
                           "Hamburger (50% Mag DEF)", "Wedding Cake (50% Boss DEF)", "Snake Soup (40% EXP)"
                           ]

        character_buff = jobbuff[character_class]
        for i in character_buff:
            buffs_list.remove(i)

        buffdf = pd.DataFrame(columns=["1", "2"])
        with st.beta_expander("Buffs"):
            st.write("Note: Character Innate Party Buffs Already Included")
            buff_list = st.multiselect("Choose Party Buffs To Be Applied", buffs_list)
            self.buffs = buff_list
            _, buff1, _ = st.beta_columns([0.02, 0.96, 0.02])
            length = len(buff_list)
            if length != 0:
                for i in range(0, length, 2):
                    if i+1 == length:
                        buffrow = [buff_list[i], ""]
                        buffdf.loc[len(buffdf)] = buffrow
                    else:
                        buffrow = [buff_list[i], buff_list[i + 1]]
                        buffdf.loc[len(buffdf)] = buffrow
                buff1.table(buffdf)

        # Warriors
            # Dark Knight
            if "Hyper Body (Phy DMG Reduction, Mag DMG Reduction)" in buff_list:
                self.pdefdec += 9
                self.mdefdec += 9
            if "Iron Will (Boss DEF%, Player DEF%)" in buff_list:
                self.bdef += 12
                self.pldef += 12
            # Hero
            if "Unmanaged Anger (Phy ATK%)" in buff_list:
                if type == "PHYSICAL":
                    self.atkp += 21
            # Paladin
            if "Parashock Guard (Phy DMG Reduction, Mag DMG Reduction)" in buff_list:
                self.pdefdec += 20
                self.mdefdec += 20
            if "Combat Orders (Phy DMG%, Mag DMG%)" in buff_list:
                self.dmg += 15
            # Aran
            if "Maha's Blessing (HP, MP)" in buff_list:
                self.hpinc += 10
                self.mpinc += 10
        # Mages
            # Bishop
            if "Advanced Blessing (Phy ATK%, Mag ATK%, ACC%, EVD%)" in buff_list:
                self.atkp += 35
                self.batk += 15
                self.accp += 10
                self.evd += 15
            if "Holy Shell (HP%, MP%, HP, MP)" in buff_list:
                self.hpinc += 10
                self.mpinc += 10
                self.hp += 7808
                self.mp += 3124
            if "Holy Symbol (EXP, KBK Res)" in buff_list:
                self.exp += 20
                self.kbkres += 13
            # FPM + ILM
            if "Meditation (Mag DMG%)" in buff_list:
                if type == "MAGICAL":
                    self.dmg += 10
            # ILM
            if "Absolute Zero Aura (KBK RES, Abnormal Status RES)" in buff_list:
                self.kbkres += 10
                self.abnormalstatres += 10
            # Blaze Wizard
            if "Burning Conduit (Phy ATK%, Mag ATK%, Phy DMG%, Mag DMG%)" in buff_list:
                self.atkp += 20
                self.dmg += 5
            # Evan
            if "Return Dive (Phy DMG%, Mag DMG%)" in buff_list:
                self.dmg += 15
            # Luminous
            if "Photic Meditation (Mag ATK%)" in buff_list:
                if type == "MAGICAL":
                    self.atkp += 21.6
            # Battle Mage
            if "Dark Aura (Phy DMG%, Mag DMG%)" in buff_list:
                self.dmg += 20
        # Archers
            # Wild Hunter
            if "Call of the Wild (Phy ATK%, Mag ATK%)" in buff_list:
                self.atkp += 14.7
        # Thieves
        # Pirates
            # Buccaneer/ Thunder Breaker
            if "Speed Infusion (Boss ATK%, Player ATK%)" in buff_list:
                self.batk += 9.6
                self.platk += 9.6
            # Mechanic
            if "Support Unit: H-EX (Phy DMG%, Mag DMG%, FD%)" in buff_list:
                self.dmg += 10
                self.fd += 5

            st.write("Cash Buff Selection")
            buff_choice = st.selectbox("Choose Manual/Automatic Buff Selection", ["Automatic", "Manual"])
            if buff_choice == "Manual":
                _, buff2, _, buff3, _ = st.beta_columns([0.02, 0.47, 0.02, 0.47, 0.02])
                self.atkp += buff2.selectbox("Choose Amount of PHY/MAG ATK Buff", [0, 10, 30, 50])
                self.dmg += buff3.selectbox("Choose Amount of PHY/MAG DMG Buff", [0, 10, 30])
                self.batk += buff2.selectbox("Choose Amount of Boss ATK Buff", [0, 10, 30, 50])
                self.bdef += buff3.selectbox("Choose Amount of Boss DEF Buff", [0, 10, 30, 50])
                self.cr += buff2.selectbox("Choose Amount of Crit Rate Buff", [0, 10, 30])
                self.cd += buff3.selectbox("Choose Amount of Crit DMG Buff", [0, 30])
                self.pdefinc += buff2.selectbox("Choose Amount of Phy DEF Buff", [0, 10, 30, 50])
                self.mdefinc += buff3.selectbox("Choose Amount of Mag DEF Buff", [0, 10, 30, 50])
                self.critres += buff2.selectbox("Choose Amount of Crit Res Buff", [0, 10])
                self.accp += buff3.selectbox("Choose Amount of ACC Buff", [0, 10, 30])
                self.hp += buff2.selectbox("Choose Amount of HP Buff", [0, 300])
                self.mp += buff3.selectbox("Choose Amount of MP Buff", [0, 300])
                self.hprec += buff2.selectbox("Choose Amount of HP Rec Buff", [0, 300])
                self.mprec += buff3.selectbox("Choose Amount of MP Rec Buff", [0, 300])
                self.spd += buff2.selectbox("Choose Amount of SPD Buff", [0, 10, 30])
                self.jmp += buff3.selectbox("Choose Amount of JMP Buff", [0, 10, 30])
                exp = buff2.multiselect("Choose Amount of EXP Buff", [10, 30, 40, 50])
                for i in exp:
                    self.exp += i
                self.dr += buff3.selectbox("Choose Amount of Drop Buff", [0, 10, 30])
                self.meso += buff2.selectbox("Choose Amount of Meso Buff", [0, 10, 30])
            if buff_choice == "Automatic":
                buff_choice_amount = st.selectbox("Choose Amount of Buff", [0, 10, 30, 50])
                if buff_choice_amount == 10:
                    self.atkp += 10
                    self.dmg += 10
                    self.batk += 10
                    self.bdef += 10
                    self.cr += 10
                    self.cd += 0
                    self.pdefinc += 10
                    self.mdefinc += 10
                    self.critres += 10
                    self.accp += 10
                    self.hp += 0
                    self.mp += 0
                    self.hprec += 0
                    self.mprec += 0
                    self.spd += 10
                    self.jmp += 10
                    self.exp += 70
                    self.dr += 10
                    self.meso += 10
                elif buff_choice_amount == 30:
                    self.atkp += 30
                    self.dmg += 30
                    self.batk += 30
                    self.bdef += 30
                    self.cr += 30
                    self.cd += 30
                    self.pdefinc += 30
                    self.mdefinc += 30
                    self.critres += 10
                    self.accp += 30
                    self.hp += 300
                    self.mp += 300
                    self.hprec += 300
                    self.mprec += 300
                    self.spd += 30
                    self.jmp += 30
                    self.exp += 70
                    self.dr += 30
                    self.meso += 30
                elif buff_choice_amount == 50:
                    self.atkp += 50
                    self.dmg += 30
                    self.batk += 50
                    self.bdef += 50
                    self.cr += 30
                    self.cd += 30
                    self.pdefinc += 50
                    self.mdefinc += 50
                    self.critres += 10
                    self.accp += 30
                    self.hp += 300
                    self.mp += 300
                    self.hprec += 300
                    self.mprec += 300
                    self.spd += 30
                    self.jmp += 30
                    self.exp += 70
                    self.dr += 30
                    self.meso += 30
            st.write("Tangyoon Selection")
            tangyoon = st.selectbox("Choose Tangyoon Selection", ["No", "Yes"])
            if tangyoon == "Yes":
                if type == "PHYSICAL":
                    self.dmg += 20
                    self.pdefinc += 20
                    self.bdef += 20
                    self.batk += 20
                    self.cr += 20
                    self.accp += 20
                if type == "MAGICAL":
                    self.dmg += 20
                    self.mdefinc += 20
                    self.bdef += 20
                    self.batk += 20
                    self.cr += 20
                    self.accp += 20
            fever = st.selectbox("Choose Fever Selection", ["None", "Normal", "Max"])
            if fever == "Normal":
                self.atkp += 10
                self.cr += 10
                self.cd += 20
                self.pdefinc += 10
                self.mdefinc += 10
                self.hprec += 200
                self.mprec += 200
                self.spd += 10
                self.jmp += 20
                self.exp += 20
                self.meso += 20
            elif fever == "Max":
                self.atkp += 15
                self.cr += 15
                self.cd += 30
                self.pdefinc += 15
                self.mdefinc += 15
                self.hprec += 300
                self.mprec += 300
                self.spd += 15
                self.jmp += 30
                self.exp += 30
                self.meso += 30

    def buffs(self):
        buffs = self.buffs
        return buffs

    def emblem(self):
        emblem = self.emblem
        return emblem

    def emblem_level(self):
        emblem_level = self.emblem_level
        return emblem_level

    def emblem_amount(self):
        emblem_amount = self.emblem_amount
        return emblem_amount

    def type(self):
        type = self.type
        return type

    def sf(self):
        sf = self.sf
        return sf

    def stat(self):
        stat = self.stat
        return stat

    def stat_amount(self):
        stat_amount = self.stat_amount
        return stat_amount

    def level(self):
        level = self.level
        return level

    def atk(self):
        atk = self.atk
        return atk

    def atkp(self):
        atkp = self.atkp
        return atkp

    def dmg(self):
        dmg = self.dmg
        return dmg

    def batk(self):
        batk = self.batk
        return batk

    def platk(self):
        platk = self.platk
        return platk

    def cr(self):
        cr = self.cr
        return cr

    def cratk(self):
        cratk = self.cratk
        return cratk

    def cd(self):
        cd = self.cd
        return cd

    def maxdmg(self):
        maxdmg = self.maxdmg
        return maxdmg

    def fd(self):
        fd = self.fd
        return fd

    def pdef(self):
        pdef = self.pdef
        return pdef

    def pdefinc(self):
        pdefinc = self.pdefinc
        return pdefinc

    def pdefdec(self):
        pdefdec = self.pdefdec
        return pdefdec

    def mdef(self):
        mdef = self.mdef
        return mdef

    def mdefinc(self):
        mdefinc = self.mdefinc
        return mdefinc

    def mdefdec(self):
        mdefdec = self.mdefdec
        return mdefdec

    def bdef(self):
        bdef = self.bdef
        return bdef

    def pldef(self):
        pldef = self.pldef
        return pldef

    def critres(self):
        critres = self.critres
        return critres

    def critdmgres(self):
        critdmgres = self.critdmgres
        return critdmgres

    def acc(self):
        acc = self.acc
        return acc

    def accp(self):
        accp = self.accp
        return accp

    def evd(self):
        evd = self.evd
        return evd

    def evdp(self):
        evdp = self.evdp
        return evdp

    def penrate(self):
        penrate = self.penrate
        return penrate

    def block(self):
        block = self.block
        return block

    def abnormalstatres(self):
        abnormalstatres = self.abnormalstatres
        return abnormalstatres

    def hp(self):
        hp = self.hp
        return hp

    def hpinc(self):
        hpinc = self.hpinc
        return hpinc

    def mp(self):
        mp = self.mp
        return mp

    def mpinc(self):
        mpinc = self.mpinc
        return mpinc

    def hprec(self):
        hprec = self.hprec
        return hprec

    def mprec(self):
        mprec = self.mprec
        return mprec

    def spd(self):
        spd = self.spd
        return spd

    def jmp(self):
        jmp = self.jmp
        return jmp

    def kbkres(self):
        kbkres = self.kbkres
        return kbkres

    def exp(self):
        exp = self.exp
        return exp

    def dr(self):
        dr = self.dr
        return dr

    def meso(self):
        meso = self.meso
        return meso

    def glincrease(self):
        glincrease = self.glincrease
        return glincrease

    def partyexp(self):
        partyexp = self.partyexp
        return partyexp

    def feverchargeinc(self):
        feverchargeinc = self.feverchargeinc
        return feverchargeinc

    def feverduration(self):
        feverduration = self.feverduration
        return feverduration

    def maxfeverchance(self):
        maxfeverchance = self.maxfeverchance
        return maxfeverchance

    def spmulti(self):
        spmulti = self.spmulti
        return spmulti

    def mempsetcount(self):
        mempsetcount = self.mempsetcount
        return mempsetcount

    def aempsetcount(self):
        aempsetcount = self.aempsetcount
        return aempsetcount

    def necrosetcount(self):
        necrosetcount = self.necrosetcount
        return necrosetcount

    def fafsetcount(self):
        fafsetcount = self.fafsetcount
        return fafsetcount

    def bosssetcount(self):
        bosssetcount = self.bosssetcount
        return bosssetcount

    def commandersetcount(self):
        commandersetcount = self.commandersetcount
        return commandersetcount

    def atklinecount(self):
        atklinecount = self.atklinecount
        return atklinecount

    def crlinecount(self):
        crlinecount = self.crlinecount
        return crlinecount

    def cdlinecount(self):
        cdlinecount = self.cdlinecount
        return cdlinecount
