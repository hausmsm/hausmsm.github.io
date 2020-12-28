import streamlit as st


class Glove:
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
                    self.acc += ((glove_level - 1) * (441/39) + 848)
                    self.stat_amount += self.acc
                elif glove_stat == "Crit ATK":
                    self.cratk += ((glove_level - 1) * (136/39) + 125)
                    self.stat_amount += self.cratk
                elif glove_stat == "Crit DMG":
                    self.cd += ((glove_level - 1) * (8.6/39) + 4.8)
                    self.stat_amount += self.cd
                else:
                    self.exp += ((glove_level - 1) * (0.8/39) + 0.7)
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
                self.hp += ((glove_level - 1) * (3990/49) + 6650)
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


        """print("\n")
        print(f"acc: {self.acc}")
        print(f"cratk: {self.cratk}")
        print(f"cd: {self.cd}")
        print(f"exp: {self.exp}")
        print(f"hp: {self.hp}")"""



