import streamlit as st


class Cape:
    def __init__(self):
        # Emblem Visualization
        self.emblem = "None"
        self.emblem_amount = 0
        self.emblem_level = 0

        # Type of Emblem
        self.normal_emb = 0
        self.partial_emb = 0
        self.unique_acc_emb = 0
        self.legendary_acc_emb = 0

        # Emblem Stats
        self.emblem_cd = 0
        self.emblem_batk = 0
        self.emblem_atkp = 0

        # SF Stats
        self.sf = 0

        # Equipment Type, Stat & Rank
        self.type = "None"
        self.stat = "None"
        self.stat_amount = 0
        self.rank = "None"

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
        self.ignore = 0

        # HP MP Stats
        self.hp = 0
        self.mp = 0
        self.hpinc = 0
        self.mpinc = 0
        self.hprec = 0
        self.mprec = 0
        self.hprecp = 0
        self.mprecp = 0
        self.hppotionrecp = 0
        self.mppotionrecp = 0
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
        # Necro
        cape_level = 50
        cape_sf_level = 30
        cape_stat = "Crit Rate"
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
        cape_emblem = "Crit DMG"
        cape_emblem_level = 5
        self.normal_emb += 1
        self.emblem = cape_emblem
        self.emblem_level = cape_emblem_level
        # Emblem
        if cape_emblem == "Crit DMG":
            self.emblem_amount += emblem_cd_stats[cape_emblem_level]
            self.emblem_cd += self.emblem_amount
        # Flame
        self.crlinecount += 2
        # Potential
        self.atkp += 9

        """print("\n")
        print(f"evd: {self.evd}")
        print(f"cr: {self.cr}")
        print(f"meso: {self.meso}")
        print(f"exp: {self.exp}")
        print(f"mp: {self.mp}")"""
