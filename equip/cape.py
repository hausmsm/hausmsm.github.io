import streamlit as st


class cape:
    def __init__(self):
        # Initialize
        self.stat_amount = 0
        self.emblem_amount = 0
        self.emblem_cd = 0
        self.emblem_batk = 0
        self.emblem_atkp = 0
        self.normal_emb = 0
        self.unique_acc_emb = 0
        self.legendary_acc_emb = 0

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

        sfdefdict = {
            0: 0,
            1: 34,
            2: 70,
            3: 107,
            4: 145,
            5: 184,
            6: 225,
            7: 266,
            8: 309,
            9: 354,
            10: 400,
            11: 447,
            12: 496,
            13: 547,
            14: 600,
            15: 654,
            16: 711,
            17: 769,
            18: 830,
            19: 894,
            20: 960,
            21: 1028,
            22: 1100,
            23: 1174,
            24: 1252,
            25: 1333,
            26: 1418,
            27: 1507,
            28: 1600,
            29: 1697,
            30: 1800
        }

        emblem_cd_stats = {
            1: 5,
            2: 7,
            3: 10,
            4: 15,
            5: 20
        }

        emblem_ba_stats = {
            1: 3,
            2: 4,
            3: 5,
            4: 7,
            5: 10
        }

        emblem_atk_stats = {
            1: 3,
            2: 4,
            3: 5,
            4: 7,
            5: 10
        }

        with st.beta_expander("Cape"):
            _, cape1, _, cape2, _, cape3, _ = st.beta_columns([0.02, 0.303, 0.02, 0.303, 0.02, 0.303, 0.02])
            cape_type = cape1.selectbox("Choose Cape Type", ["Mythic Empress", "Ancient Empress", "Necro"])
            cape_stat = cape1.radio("Choose Cape Stat", ["Crit Rate", "EVD", "EXP", "Meso"])
            self.type = cape_type
            self.stat = cape_stat
            if cape_type == "Mythic Empress":
                cape_level = cape2.slider('Cape Level', min_value=30, max_value=40)
            else:
                cape_level = cape2.slider('Cape Level', min_value=30, max_value=50)
            self.level = cape_level
            cape_sf_level = cape2.slider("Cape SF Level", min_value=0, max_value=30)
            self.sf = cape_sf_level
            if cape_type == "Mythic Empress":
                cape_refine_level = cape2.slider("Cape Refinement Level", min_value=1, max_value=10)
                # Base
                self.pdef += 314
                self.mdef += 314
                # Level
                self.pdef += ((cape_level - 30) * 15.7)
                self.mdef += ((cape_level - 30) * 15.7)
                self.mp += ((cape_level - 30) * 154.7 + 3095)
                # SF
                self.pdef += sfdefdict[cape_sf_level]
                self.mdef += sfdefdict[cape_sf_level]
                # Refinement
                self.pdef += ((cape_refine_level - 1) * 16 + 80)
                self.mdef += ((cape_refine_level - 1) * 16 + 80)
                # Stat
                if cape_stat == "Crit Rate":
                    self.cr += ((cape_level - 30) * 0.1 + 1)
                    self.stat_amount += self.cr
                elif cape_stat == "EVD":
                    self.evd += ((cape_level - 30) * 28.1 + 563)
                    self.stat_amount += self.evd
                elif cape_stat == "EXP":
                    self.exp += ((cape_level - 30) * 0.05 + 0.9)
                    self.stat_amount += self.exp
                else:
                    self.meso += ((cape_level - 30) * 0.16 + 3.1)
                    self.stat_amount += self.meso
                self.mempsetcount += 1
            elif cape_type == "Ancient Empress":
                cape_refine_level = cape2.slider("Cape Refinement Level", min_value=1, max_value=10)
                # Base
                self.pdef += 1053
                self.mdef += 1053
                # Level
                self.pdef += ((cape_level - 1) * (548/49))
                self.mdef += ((cape_level - 1) * (548/49))
                self.mp += ((cape_level - 1) * (2258/49) + 3763)
                # SF
                self.pdef += sfdefdict[cape_sf_level]
                self.mdef += sfdefdict[cape_sf_level]
                # Refinement
                self.pdef += ((cape_refine_level - 1) * 16 + 80)
                self.mdef += ((cape_refine_level - 1) * 16 + 80)
                # Stat
                if cape_stat == "Crit Rate":
                    self.cr += ((cape_level - 1) * (2/49) + 1)
                    self.stat_amount += self.cr
                elif cape_stat == "EVD":
                    self.evd += ((cape_level - 1) * (428/49) + 572)
                    self.stat_amount += self.evd
                elif cape_stat == "EXP":
                    self.exp += ((cape_level - 1) * (1.7/49) + 0.9)
                    self.stat_amount += self.exp
                else:
                    self.meso += ((cape_level - 1) * (2.8/49) + 3.2)
                    self.stat_amount += self.meso
                self.aempsetcount += 1
            else:
                # Base
                self.pdef += 1478
                self.mdef += 1478
                # Level
                self.pdef += ((cape_level - 1) * (667/49))
                self.mdef += ((cape_level - 1) * (667/49))
                self.mp += ((cape_level - 1) * (2439/49) + 4064)
                # SF
                self.pdef += sfdefdict[cape_sf_level]
                self.mdef += sfdefdict[cape_sf_level]
                # Stat
                if cape_stat == "Crit Rate":
                    self.cr += ((cape_level - 1) * (2 / 49) + 1)
                    self.stat_amount += self.cr
                elif cape_stat == "EVD":
                    self.evd += ((cape_level - 1) * (428 / 49) + 572)
                    self.stat_amount += self.evd
                elif cape_stat == "EXP":
                    self.exp += ((cape_level - 1) * (1.7 / 49) + 0.9)
                    self.stat_amount += self.exp
                else:
                    self.meso += ((cape_level - 1) * (2.8 / 49) + 3.2)
                    self.stat_amount += self.meso
                self.necrosetcount += 1
            cape_emblem = cape3.radio("Choose Cape Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
            cape_emblem_level = cape3.slider("Cape Emblem Level", min_value=1, max_value=5)
            self.normal_emb += 1
            self.emblem = cape_emblem
            self.emblem_level = cape_emblem_level
            # Emblem
            if cape_emblem == "Crit DMG":
                self.emblem_amount += emblem_cd_stats[cape_emblem_level]
                self.emblem_cd += self.emblem_amount
            elif cape_emblem == "Boss ATK":
                self.emblem_amount += emblem_ba_stats[cape_emblem_level]
                self.emblem_batk += self.emblem_amount
            else:
                self.emblem_amount += emblem_atk_stats[cape_emblem_level]
                self.emblem_atkp += self.emblem_amount
        # Flame
        self.crlinecount += 2
        # Potential
        self.atkp += 9

    def normal_emb(self):
        normal_emb = self.normal_emb
        return normal_emb

    def unique_acc_emb(self):
        unique_acc_emb = self.unique_acc_emb
        return unique_acc_emb

    def legendary_acc_emb(self):
        legendary_acc_emb = self.legendary_acc_emb
        return legendary_acc_emb

    def emblem_cd(self):
        emblem_cd = self.emblem_cd
        return emblem_cd

    def emblem_batk(self):
        emblem_batk = self.emblem_batk
        return emblem_batk

    def emblem_atkp(self):
        emblem_atkp = self.emblem_atkp
        return emblem_atkp

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