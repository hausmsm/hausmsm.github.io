import streamlit as st


class Belt:
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

        with st.beta_expander("Belt"):
            _, belt1, _, belt2, _, belt3, _ = st.beta_columns([0.02, 0.303, 0.02, 0.303, 0.02, 0.303, 0.02])
            belt_type = belt1.selectbox("Choose Belt Type", ["Mythic", "Ancient", "Necro"])
            belt_stat = belt1.radio("Choose Belt Stat", ["ACC", "Crit Rate", "Drop", "EXP"])
            self.type = belt_type
            self.stat = belt_stat
            if belt_type == "Mythic":
                belt_level = belt2.slider('Belt Level', min_value=30, max_value=40)
            else:
                belt_level = belt2.slider('Belt Level', min_value=30, max_value=50)
            self.level = belt_level
            belt_sf_level = belt2.slider("Belt SF Level", min_value=0, max_value=30)
            self.sf = belt_sf_level
            if belt_type == "Mythic":
                # Base
                self.pdef += 945
                self.mdef += 945
                # Level
                self.pdef += ((belt_level - 30) * 47.2)
                self.mdef += ((belt_level - 30) * 47.2)
                self.mp += ((belt_level - 30) * 77.3 + 1547)
                # SF
                self.pdef += sfdefdict[belt_sf_level]
                self.mdef += sfdefdict[belt_sf_level]
                # Stat
                if belt_stat == "ACC":
                    self.acc += ((belt_level - 30) * 58.8 + 1175)
                    self.stat_amount += self.acc
                elif belt_stat == "Crit Rate":
                    self.cr += ((belt_level - 30) * 0.1 + 1)
                    self.stat_amount += self.cr
                elif belt_stat == "Drop":
                    self.dr += ((belt_level - 30) * 0.16 + 3.1)
                    self.stat_amount += self.dr
                else:
                    self.exp += ((belt_level - 30) * 0.03 + 0.6)
                    self.stat_amount += self.exp
            elif belt_type == "Ancient":
                # Base
                self.pdef += 3169
                self.mdef += 3169
                # Level
                self.pdef += ((belt_level - 1) * (1647/49))
                self.mdef += ((belt_level - 1) * (1647/49))
                self.mp += ((belt_level - 1) * (1129/49) + 1881)
                # SF
                self.pdef += sfdefdict[belt_sf_level]
                self.mdef += sfdefdict[belt_sf_level]
                # Stat
                if belt_stat == "ACC":
                    self.acc += ((belt_level - 1) * (1004/49) + 1196)
                    self.stat_amount += self.acc
                elif belt_stat == "Crit Rate":
                    self.cr += ((belt_level - 1) * (2/49) + 1)
                    self.stat_amount += self.cr
                elif belt_stat == "Drop":
                    self.dr += ((belt_level - 1) * (2.8/49) + 3.2)
                    self.stat_amount += self.dr
                else:
                    self.exp += ((belt_level - 1) * (1.3/49) + 0.6)
                    self.stat_amount += self.exp
            else:
                # Base
                self.pdef += 4449
                self.mdef += 4449
                # Level
                self.pdef += ((belt_level - 1) * (2005/49))
                self.mdef += ((belt_level - 1) * (2005/49))
                self.mp += ((belt_level - 1) * (1219/49) + 2032)
                # SF
                self.pdef += sfdefdict[belt_sf_level]
                self.mdef += sfdefdict[belt_sf_level]
                # Stat
                if belt_stat == "ACC":
                    self.acc += ((belt_level - 1) * (1004 / 49) + 1196)
                    self.stat_amount += self.acc
                elif belt_stat == "Crit Rate":
                    self.cr += ((belt_level - 1) * (2 / 49) + 1)
                    self.stat_amount += self.cr
                elif belt_stat == "Drop":
                    self.dr += ((belt_level - 1) * (2.8 / 49) + 3.2)
                    self.stat_amount += self.dr
                else:
                    self.exp += ((belt_level - 1) * (1.3 / 49) + 0.6)
                    self.stat_amount += self.exp
                self.necrosetcount += 1
            belt_emblem = belt3.radio("Choose Belt Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
            belt_emblem_level = belt3.slider("Belt Emblem Level", min_value=1, max_value=5)
            self.normal_emb += 1
            self.emblem = belt_emblem
            self.emblem_level = belt_emblem_level
            # Emblem
            if belt_emblem == "Crit DMG":
                self.emblem_amount += emblem_cd_stats[belt_emblem_level]
                self.emblem_cd += self.emblem_amount
            elif belt_emblem == "Boss ATK":
                self.emblem_amount += emblem_ba_stats[belt_emblem_level]
                self.emblem_batk += self.emblem_amount
            else:
                self.emblem_amount += emblem_atk_stats[belt_emblem_level]
                self.emblem_atkp += self.emblem_amount
        # Flame
        self.crlinecount += 2
        # Potential
        self.atkp += 9
