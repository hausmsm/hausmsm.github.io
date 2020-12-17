import streamlit as st


class soul:
    def __init__(self,type):
        # Initialize
        self.emblem = "None"
        self.emblem_amount = 0
        self.vonbonpierrecount = 0
        self.crimsonqueencount = 0
        self.vellumcount = 0
        self.vonleoncount = 0

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

        emblem_cd_stats = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5
        }

        emblem_ba_stats = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5
        }

        emblem_atk_stats = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5
        }
        with st.beta_expander("Soul"):
            _, soul1, _, soul2, _ = st.beta_columns([0.02, 0.47, 0.02, 0.47, 0.02])
            weapon_soul = soul1.selectbox("Choose a Weapon Soul", ["Von Bon/Pierre", "Crimson Queen", "Vellum",
                                                                   "Von Leon"])
            weapon_type = soul2.selectbox("Choose a Weapon Soul Stat", ["Max DMG Cap", "HP%", "Phy DMG%", "Mag DMG%",
                                                                        "Boss ATK%", "Crit Rate%", "Crit DMG%",
                                                                        "Final DMG%"])
            self.weapon_soul = weapon_soul
            self.weapon_type = weapon_type
            if "Von Bon/Pierre" in [weapon_soul]:
                self.vonbonpierrecount += 1
                if "HP%" in [weapon_type]:
                    self.hpinc += 15
                elif "Phy DMG%" in [weapon_type]:
                    if type == "PHYSICAL":
                        self.dmg += 15
                elif "Mag DMG%" in [weapon_type]:
                    if type == "MAGICAL":
                        self.dmg += 15
                elif "Boss ATK%" in [weapon_type]:
                    self.batk += 15
                elif "Crit Rate%" in [weapon_type]:
                    self.cr += 15
                elif "Crit DMG%" in [weapon_type]:
                    self.cd += 15
                elif "Max DMG Cap" in [weapon_type]:
                    self.maxdmg += 1500000
                elif "Final DMG%" in [weapon_type]:
                    self.fd += 15
            elif "Crimson Queen" in [weapon_soul]:
                self.crimsonqueencount += 1
                if "HP%" in [weapon_type]:
                    self.hpinc += 15.5
                elif "Phy DMG%" in [weapon_type]:
                    if type == "PHYSICAL":
                        self.dmg += 15.5
                elif "Mag DMG%" in [weapon_type]:
                    if type == "MAGICAL":
                        self.dmg += 15.5
                elif "Boss ATK%" in [weapon_type]:
                    self.batk += 15.5
                elif "Crit Rate%" in [weapon_type]:
                    self.cr += 15.5
                elif "Crit DMG%" in [weapon_type]:
                    self.cd += 15.5
                elif "Max DMG Cap" in [weapon_type]:
                    self.maxdmg += 1500000
                elif "Final DMG%" in [weapon_type]:
                    self.fd += 16
            elif "Vellum" in [weapon_soul]:
                self.vellumcount += 1
                if "HP%" in [weapon_type]:
                    self.hpinc += 17
                elif "Phy DMG%" in [weapon_type]:
                    if type == "PHYSICAL":
                        self.dmg += 17
                elif "Mag DMG%" in [weapon_type]:
                    if type == "MAGICAL":
                        self.dmg += 17
                elif "Boss ATK%" in [weapon_type]:
                    self.batk += 17
                elif "Crit Rate%" in [weapon_type]:
                    self.cr += 17
                elif "Crit DMG%" in [weapon_type]:
                    self.cd += 17
                elif "Max DMG Cap" in [weapon_type]:
                    self.maxdmg += 1700000
                elif "Final DMG%" in [weapon_type]:
                    self.fd += 17
            elif "Von Leon" in [weapon_soul]:
                self.vonleoncount += 1
                if "HP%" in [weapon_type]:
                    self.hpinc += 13
                elif "Phy DMG%" in [weapon_type]:
                    if type == "PHYSICAL":
                        self.dmg += 13
                elif "Mag DMG%" in [weapon_type]:
                    if type == "MAGICAL":
                        self.dmg += 13
                elif "Boss ATK%" in [weapon_type]:
                    self.batk += 13
                elif "Crit Rate%" in [weapon_type]:
                    self.cr += 13
                elif "Crit DMG%" in [weapon_type]:
                    self.cd += 13
                elif "Max DMG Cap" in [weapon_type]:
                    self.maxdmg += 1300000
                elif "Final DMG%" in [weapon_type]:
                    self.fd += 13
            swep_soul = soul1.selectbox("Choose Secondary Weapon Soul", ["Von Bon/Pierre", "Crimson Queen", "Vellum",
                                                                         "Von Leon"])
            swep_type = soul2.selectbox("Choose Secondary Weapon Soul Stat", ["Final DMG%","EXP%", "Fever Buff Duration",
                                                                  "Item Drop%", "Phy ATK%", "Mag ATK%"])
            self.swep_soul = swep_soul
            self.swep_type = swep_type
            if "Von Bon/Pierre" in [swep_soul]:
                self.vonbonpierrecount += 1
                if "EXP%" in [swep_type]:
                    self.exp += 4.2
                elif "Phy ATK%" in [swep_type]:
                    if type == "PHYSICAL":
                        self.atkp += 3.8
                elif "Mag ATK%" in [swep_type]:
                    if type == "MAGICAL":
                        self.atkp += 3.8
                elif "Item Drop%" in [swep_type]:
                    self.dr += 3.8
                elif "Fever Buff Duration" in [swep_type]:
                    self.feverduration += 3
                elif "Final DMG%" in [swep_type]:
                    self.fd += 4.5
            elif "Crimson Queen" in [swep_soul]:
                self.crimsonqueencount += 1
                if "EXP%" in [swep_type]:
                    self.exp += 4.4
                elif "Phy ATK%" in [swep_type]:
                    if type == "PHYSICAL":
                        self.atkp += 4
                elif "Mag ATK%" in [swep_type]:
                    if type == "MAGICAL":
                        self.atkp += 4
                elif "Item Drop%" in [swep_type]:
                    self.dr += 4
                elif "Fever Buff Duration" in [swep_type]:
                    self.feverduration += 3.2
                elif "Final DMG%" in [swep_type]:
                    self.fd += 4.5
            elif "Vellum" in [swep_soul]:
                self.vellumcount += 1
                if "EXP%" in [swep_type]:
                    self.exp += 4.7
                elif "Phy ATK%" in [swep_type]:
                    if type == "PHYSICAL":
                        self.atkp += 34.3
                elif "Mag ATK%" in [swep_type]:
                    if type == "MAGICAL":
                        self.atkp += 4.3
                elif "Item Drop%" in [swep_type]:
                    self.dr += 4.3
                elif "Fever Buff Duration" in [swep_type]:
                    self.feverduration += 3.5
                elif "Final DMG%" in [swep_type]:
                    self.fd += 5
            elif "Von Leon" in [swep_soul]:
                self.vonleoncount += 1
                if "EXP%" in [swep_type]:
                    self.exp += 3.7
                elif "Phy ATK%" in [swep_type]:
                    if type == "PHYSICAL":
                        self.atkp += 3.3
                elif "Mag ATK%" in [swep_type]:
                    if type == "MAGICAL":
                        self.atkp += 3.3
                elif "Item Drop%" in [swep_type]:
                    self.dr += 3
                elif "Fever Buff Duration" in [swep_type]:
                    self.feverduration += 2.2
                elif "Final DMG%" in [swep_type]:
                    self.fd += 3.8
            shoulder_soul = soul1.selectbox("Choose Shoulder Soul", ["Von Bon/Pierre", "Crimson Queen", "Vellum",
                                                                     "Von Leon"])
            shoulder_type = soul2.selectbox("Choose Shoulder Soul Stat", ["Final DMG%","EXP%", "Fever Buff Duration",
                                                                  "Item Drop%", "Phy ATK%", "Mag ATK%"])
            self.shoulder_soul = shoulder_soul
            self.shoulder_type = shoulder_type
            if "Von Bon/Pierre" in [shoulder_soul]:
                self.vonbonpierrecount += 1
                if "EXP%" in [shoulder_type]:
                    self.exp += 4.2
                elif "Phy ATK%" in [shoulder_type]:
                    if type == "PHYSICAL":
                        self.atkp += 3.8
                elif "Mag ATK%" in [shoulder_type]:
                    if type == "MAGICAL":
                        self.atkp += 3.8
                elif "Item Drop%" in [shoulder_type]:
                    self.dr += 3.8
                elif "Fever Buff Duration" in [shoulder_type]:
                    self.feverduration += 3
                elif "Final DMG%" in [shoulder_type]:
                    self.fd += 4.5
            elif "Crimson Queen" in [shoulder_soul]:
                self.crimsonqueencount += 1
                if "EXP%" in [shoulder_type]:
                    self.exp += 4.4
                elif "Phy ATK%" in [shoulder_type]:
                    if type == "PHYSICAL":
                        self.atkp += 4
                elif "Mag ATK%" in [shoulder_type]:
                    if type == "MAGICAL":
                        self.atkp += 4
                elif "Item Drop%" in [shoulder_type]:
                    self.dr += 4
                elif "Fever Buff Duration" in [shoulder_type]:
                    self.feverduration += 3.2
                elif "Final DMG%" in [shoulder_type]:
                    self.fd += 4.5
            elif "Vellum" in [shoulder_soul]:
                self.vellumcount += 1
                if "EXP%" in [shoulder_type]:
                    self.exp += 4.7
                elif "Phy ATK%" in [shoulder_type]:
                    if type == "PHYSICAL":
                        self.atkp += 34.3
                elif "Mag ATK%" in [shoulder_type]:
                    if type == "MAGICAL":
                        self.atkp += 4.3
                elif "Item Drop%" in [shoulder_type]:
                    self.dr += 4.3
                elif "Fever Buff Duration" in [shoulder_type]:
                    self.feverduration += 3.5
                elif "Final DMG%" in [shoulder_type]:
                    self.fd += 5
            elif "Von Leon" in [shoulder_soul]:
                self.vonleoncount += 1
                if "EXP%" in [shoulder_type]:
                    self.exp += 3.7
                elif "Phy ATK%" in [shoulder_type]:
                    if type == "PHYSICAL":
                        self.atkp += 3.3
                elif "Mag ATK%" in [shoulder_type]:
                    if type == "MAGICAL":
                        self.atkp += 3.3
                elif "Item Drop%" in [shoulder_type]:
                    self.dr += 3
                elif "Fever Buff Duration" in [shoulder_type]:
                    self.feverduration += 2.2
                elif "Final DMG%" in [shoulder_type]:
                    self.fd += 3.8
            belt_soul = soul1.selectbox("Choose Belt Soul", ["Von Bon/Pierre", "Crimson Queen", "Vellum", "Von Leon"])
            belt_type = soul2.selectbox("Choose Belt Soul Stat", ["Final DMG%","EXP%", "Fever Buff Duration",
                                                                  "Item Drop%", "Phy ATK%", "Mag ATK%"])
            self.belt_soul = belt_soul
            self.belt_type = belt_type
            if "Von Bon/Pierre" in [belt_soul]:
                self.vonbonpierrecount += 1
                if "EXP%" in [belt_type]:
                    self.exp += 4.2
                elif "Phy ATK%" in [belt_type]:
                    if type == "PHYSICAL":
                        self.atkp += 3.8
                elif "Mag ATK%" in [belt_type]:
                    if type == "MAGICAL":
                        self.atkp += 3.8
                elif "Item Drop%" in [belt_type]:
                    self.dr += 3.8
                elif "Fever Buff Duration" in [belt_type]:
                    self.feverduration += 3
                elif "Final DMG%" in [belt_type]:
                    self.fd += 4.5
            elif "Crimson Queen" in [belt_soul]:
                self.crimsonqueencount += 1
                if "EXP%" in [belt_type]:
                    self.exp += 4.4
                elif "Phy ATK%" in [belt_type]:
                    if type == "PHYSICAL":
                        self.atkp += 4
                elif "Mag ATK%" in [belt_type]:
                    if type == "MAGICAL":
                        self.atkp += 4
                elif "Item Drop%" in [belt_type]:
                    self.dr += 4
                elif "Fever Buff Duration" in [belt_type]:
                    self.feverduration += 3.2
                elif "Final DMG%" in [belt_type]:
                    self.fd += 4.5
            elif "Vellum" in [belt_soul]:
                self.vellumcount += 1
                if "EXP%" in [belt_type]:
                    self.exp += 4.7
                elif "Phy ATK%" in [belt_type]:
                    if type == "PHYSICAL":
                        self.atkp += 34.3
                elif "Mag ATK%" in [belt_type]:
                    if type == "MAGICAL":
                        self.atkp += 4.3
                elif "Item Drop%" in [belt_type]:
                    self.dr += 4.3
                elif "Fever Buff Duration" in [belt_type]:
                    self.feverduration += 3.5
                elif "Final DMG%" in [belt_type]:
                    self.fd += 5
            elif "Von Leon" in [belt_soul]:
                self.vonleoncount += 1
                if "EXP%" in [belt_type]:
                    self.exp += 3.7
                elif "Phy ATK%" in [belt_type]:
                    if type == "PHYSICAL":
                        self.atkp += 3.3
                elif "Mag ATK%" in [belt_type]:
                    if type == "MAGICAL":
                        self.atkp += 3.3
                elif "Item Drop%" in [belt_type]:
                    self.dr += 3
                elif "Fever Buff Duration" in [belt_type]:
                    self.feverduration += 2.2
                elif "Final DMG%" in [belt_type]:
                    self.fd += 3.8
            cape_soul = soul1.selectbox("Choose Cape Soul", ["Von Bon/Pierre", "Crimson Queen", "Vellum", "Von Leon"])
            cape_type = soul2.selectbox("Choose Cape Soul Stat", ["Final DMG%","EXP%", "Fever Buff Duration",
                                                                  "Item Drop%", "Phy ATK%", "Mag ATK%"])
            self.cape_soul = cape_soul
            self.cape_type = cape_type
            if "Von Bon/Pierre" in [cape_soul]:
                self.vonbonpierrecount += 1
                if "EXP%" in [cape_type]:
                    self.exp += 4.2
                elif "Phy ATK%" in [cape_type]:
                    if type == "PHYSICAL":
                        self.atkp += 3.8
                elif "Mag ATK%" in [cape_type]:
                    if type == "MAGICAL":
                        self.atkp += 3.8
                elif "Item Drop%" in [cape_type]:
                    self.dr += 3.8
                elif "Fever Buff Duration" in [cape_type]:
                    self.feverduration += 3
                elif "Final DMG%" in [cape_type]:
                    self.fd += 4.5
            elif "Crimson Queen" in [cape_soul]:
                self.crimsonqueencount += 1
                if "EXP%" in [cape_type]:
                    self.exp += 4.4
                elif "Phy ATK%" in [cape_type]:
                    if type == "PHYSICAL":
                        self.atkp += 4
                elif "Mag ATK%" in [cape_type]:
                    if type == "MAGICAL":
                        self.atkp += 4
                elif "Item Drop%" in [cape_type]:
                    self.dr += 4
                elif "Fever Buff Duration" in [cape_type]:
                    self.feverduration += 3.2
                elif "Final DMG%" in [cape_type]:
                    self.fd += 4.5
            elif "Vellum" in [cape_soul]:
                self.vellumcount += 1
                if "EXP%" in [cape_type]:
                    self.exp += 4.7
                elif "Phy ATK%" in [cape_type]:
                    if type == "PHYSICAL":
                        self.atkp += 34.3
                elif "Mag ATK%" in [cape_type]:
                    if type == "MAGICAL":
                        self.atkp += 4.3
                elif "Item Drop%" in [cape_type]:
                    self.dr += 4.3
                elif "Fever Buff Duration" in [cape_type]:
                    self.feverduration += 3.5
                elif "Final DMG%" in [cape_type]:
                    self.fd += 5
            elif "Von Leon" in [cape_soul]:
                self.vonleoncount += 1
                if "EXP%" in [cape_type]:
                    self.exp += 3.7
                elif "Phy ATK%" in [cape_type]:
                    if type == "PHYSICAL":
                        self.atkp += 3.3
                elif "Mag ATK%" in [cape_type]:
                    if type == "MAGICAL":
                        self.atkp += 3.3
                elif "Item Drop%" in [cape_type]:
                    self.dr += 3
                elif "Fever Buff Duration" in [cape_type]:
                    self.feverduration += 2.2
                elif "Final DMG%" in [cape_type]:
                    self.fd += 3.8

            if "Von Bon/Pierre" in [weapon_soul]:
                if self.vonbonpierrecount == 5:
                    self.atk += 900
                elif self.vonbonpierrecount == 4:
                    self.atk += 720
                elif self.vonbonpierrecount == 3:
                    self.atk += 540
                elif self.vonbonpierrecount == 2:
                    self.atk += 360
                elif self.vonbonpierrecount == 1:
                    self.atk += 180
            elif "Crimson Queen" in [weapon_soul]:
                if self.vonbonpierrecount == 5:
                    self.atk += 900
                elif self.vonbonpierrecount == 4:
                    self.atk += 720
                elif self.vonbonpierrecount == 3:
                    self.atk += 540
                elif self.vonbonpierrecount == 2:
                    self.atk += 360
                elif self.vonbonpierrecount == 1:
                    self.atk += 180
            elif "Vellum" in [weapon_soul]:
                if self.vonbonpierrecount == 5:
                    self.atk += 900
                elif self.vonbonpierrecount == 4:
                    self.atk += 720
                elif self.vonbonpierrecount == 3:
                    self.atk += 540
                elif self.vonbonpierrecount == 2:
                    self.atk += 360
                elif self.vonbonpierrecount == 1:
                    self.atk += 180
            elif "Von Leon" in [weapon_soul]:
                if self.vonbonpierrecount == 5:
                    self.atk += 750
                elif self.vonbonpierrecount == 4:
                    self.atk += 600
                elif self.vonbonpierrecount == 3:
                    self.atk += 450
                elif self.vonbonpierrecount == 2:
                    self.atk += 300
                elif self.vonbonpierrecount == 1:
                    self.atk += 150

    def weapon_soul(self):
        weapon_soul = self.weapon_soul
        return weapon_soul

    def weapon_type(self):
        weapon_type = self.weapon_type
        return weapon_type

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
