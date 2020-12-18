import streamlit as st


class glove:
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
            1: 104,
            2: 211,
            3: 322,
            4: 436,
            5: 553,
            6: 675,
            7: 799,
            8: 928,
            9: 1062,
            10: 1200,
            11: 1342,
            12: 1489,
            13: 1642,
            14: 1800,
            15: 1963,
            16: 2133,
            17: 2309,
            18: 2492,
            19: 2682,
            20: 2880,
            21: 3085,
            22: 3300,
            23: 3523,
            24: 3756,
            25: 4000,
            26: 4254,
            27: 4521,
            28: 4800,
            29: 5092,
            30: 5400
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
        with st.beta_expander("Gloves"):
            _, glove1, _, glove2, _, glove3, _ = st.beta_columns([0.02, 0.303, 0.02, 0.303, 0.02, 0.303, 0.02])
            glove_type = glove1.selectbox("Choose Glove Type", ["Mythic Empress", "Ancient Empress", "Necro"])
            glove_stat = glove1.radio("Choose Glove Stat", ["ACC", "Crit ATK", "Crit DMG", "EXP"])
            self.type = glove_type
            self.stat = glove_stat
            if glove_type == "Mythic Empress":
                glove_level = glove2.slider('Glove Level', min_value=30, max_value=40)
            else:
                glove_level = glove2.slider('Glove Level', min_value=30, max_value=50)
            self.level = glove_level
            glove_sf_level = glove2.slider("Glove SF Level", min_value=0, max_value=30)
            self.sf = glove_sf_level
            if glove_type == "Mythic Empress":
                glove_refine_level = glove2.slider("Glove Refinement Level", min_value=1, max_value=10)
                # Base
                self.pdef += 1350
                self.mdef += 1350
                # Level
                self.pdef += ((glove_level - 30) * 47.2 + 945)
                self.mdef += ((glove_level - 30) * 47.2 + 945)
                self.hp += ((glove_level - 30) * 270.1 + 5403)
                # SF
                self.pdef += sfdefdict[glove_sf_level]
                self.mdef += sfdefdict[glove_sf_level]
                # Refinement
                self.pdef += ((glove_refine_level - 1) * 50 + 250)
                self.mdef += ((glove_refine_level - 1) * 50 + 250)
                # Stat
                if glove_stat == "ACC":
                    self.acc += ((glove_level - 30) * 11.4 + 1175)
                    self.stat_amount += self.acc
                elif glove_stat == "Crit ATK":
                    self.cratk += ((glove_level - 30) * 8.7 + 174)
                    self.stat_amount += self.cratk
                elif glove_stat == "Crit DMG":
                    self.cd += ((glove_level - 30) * 0.67 + 6.7)
                    self.stat_amount += self.cd
                else:
                    self.exp += ((glove_level - 30) * 0.5 + 1)
                    self.stat_amount += self.exp
                self.mempsetcount += 1
            elif glove_type == "Ancient Empress":
                glove_refine_level = glove2.slider("Glove Refinement Level", min_value=1, max_value=10)
                # Base
                self.pdef += 3170
                self.mdef += 3170
                # Level
                self.pdef += (glove_level - 1) * 32.96
                self.mdef += (glove_level - 1) * 32.96
                self.hp += ((glove_level - 1) * (3990/49)+ 6650)
                # SF
                self.pdef += sfdefdict[glove_sf_level]
                self.mdef += sfdefdict[glove_sf_level]
                # Refinement
                self.pdef += ((glove_refine_level - 1) * 50 + 250)
                self.mdef += ((glove_refine_level - 1) * 50 + 250)
                # Stat
                if glove_stat == "ACC":
                    self.acc += ((glove_level - 1) * (281/49) + 1181)
                    self.stat_amount += self.acc
                elif glove_stat == "Crit ATK":
                    self.cratk += ((glove_level - 1) * (153/49) + 177)
                    self.stat_amount += self.cratk
                elif glove_stat == "Crit DMG":
                    self.cd += ((glove_level - 1) * (9.1/49) + 6.9)
                    self.stat_amount += self.cd
                else:
                    self.exp += ((glove_level - 1) * (1/49) + 1)
                    self.stat_amount += self.exp
                self.aempsetcount += 1
            else:
                # Base
                self.pdef += 4452
                self.mdef += 4452
                # Level
                self.pdef += (glove_level - 1) * (2007/49)
                self.mdef += (glove_level - 1) * (2007/49)
                self.hp += ((glove_level - 1) * (4309 / 49) + 7182)
                # SF
                self.pdef += sfdefdict[glove_sf_level]
                self.mdef += sfdefdict[glove_sf_level]
                # Stat
                if glove_stat == "ACC":
                    self.acc += ((glove_level - 1) * (281 / 49) + 1181)
                    self.stat_amount += self.acc
                elif glove_stat == "Crit ATK":
                    self.cratk += ((glove_level - 1) * (153 / 49) + 177)
                    self.stat_amount += self.cratk
                elif glove_stat == "Crit DMG":
                    self.cd += ((glove_level - 1) * (9.1 / 49) + 6.9)
                    self.stat_amount += self.cd
                else:
                    self.exp += ((glove_level - 1) * (1 / 49) + 1)
                    self.stat_amount += self.exp
                self.necrosetcount += 1
            glove_emblem = glove3.radio("Choose Glove Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
            glove_emblem_level = glove3.slider("Glove Emblem Level", min_value=1, max_value=5)
            self.normal_emb += 1
            self.emblem = glove_emblem
            self.emblem_level = glove_emblem_level
            # Emblem
            if glove_emblem == "Crit DMG":
                self.emblem_amount += emblem_cd_stats[glove_emblem_level]
                self.emblem_cd += self.emblem_amount
            elif glove_emblem == "Boss ATK":
                self.emblem_amount += emblem_ba_stats[glove_emblem_level]
                self.emblem_batk += self.emblem_amount
            else:
                self.emblem_amount += emblem_atk_stats[glove_emblem_level]
                self.emblem_atkp += self.emblem_amount

        # Flame
        self.cdlinecount += 2

        # Potential
        self.dmg += 6

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