import streamlit as st


class Hat:
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
            1: 69,
            2: 141,
            3: 214,
            4: 290,
            5: 369,
            6: 450,
            7: 533,
            8: 619,
            9: 708,
            10: 800,
            11: 894,
            12: 993,
            13: 1094,
            14: 1200,
            15: 1309,
            16: 1422,
            17: 1539,
            18: 1661,
            19: 1788,
            20: 1920,
            21: 2057,
            22: 2200,
            23: 2349,
            24: 2504,
            25: 2666,
            26: 2836,
            27: 3014,
            28: 3200,
            29: 3395,
            30: 3600,
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

        with st.beta_expander("Hat"):
            _, hat1, _, hat2, _, hat3, _ = st.beta_columns([0.02, 0.303, 0.02, 0.303, 0.02, 0.303, 0.02])
            hat_type = hat1.selectbox("Choose Hat Type", ["Mythic Empress", "Ancient Empress", "Necro", "Fafnir"])
            self.type = hat_type
            if hat_type != "Fafnir":
                hat_stat = hat1.radio("Choose Hat Stat", ["Boss ATK", "Crit ATK", "Crit DMG", "EXP"])
            else:
                hat_stat = "None"
            if hat_type == "Mythic Empress":
                hat_level = hat2.slider('Hat Level', min_value=30, max_value=40)
            else:
                hat_level = hat2.slider('Hat Level', min_value=30, max_value=50)
            self.stat = hat_stat
            self.level = hat_level
            hat_sf_level = hat2.slider("Hat SF Level", min_value=0, max_value=30)
            self.sf = hat_sf_level
            if hat_type == "Mythic Empress":
                hat_refine_level = hat2.slider("Hat Refinement Level", min_value=1, max_value=10)
                # Base
                self.pdef += 860
                self.mdef += 860
                # Level
                self.pdef += ((hat_level-30)*31.5 + 630)
                self.mdef += ((hat_level-30)*31.5 + 630)
                self.hp += ((hat_level-30)*360.2 + 7205)
                # SF
                self.pdef += sfdefdict[hat_sf_level]
                self.mdef += sfdefdict[hat_sf_level]
                # Refinement
                self.pdef += ((hat_refine_level-1) * 32 + 160)
                self.mdef += ((hat_refine_level - 1) * 32 + 160)
                # Stat
                if hat_stat == "Boss ATK":
                    self.batk += ((hat_level-30)*0.14 + 1.6)
                    self.stat_amount += self.batk
                elif hat_stat == "Crit ATK":
                    self.cratk += ((hat_level-30)*5.4 + 108)
                    self.stat_amount += self.cratk
                elif hat_stat == "Crit DMG":
                    self.cd += ((hat_level-30)*0.67 + 6.7)
                    self.stat_amount += self.cd
                else:
                    self.exp += ((hat_level-30)*0.5 + 1)
                    self.stat_amount += self.exp
                self.mempsetcount += 1
            elif hat_type == "Ancient Empress":
                hat_refine_level = hat2.slider("Hat Refinement Level", min_value=1, max_value=10)
                # Base
                self.pdef += 2112
                self.mdef += 2112
                # Level
                self.pdef += ((hat_level-30)*22.45 + 651)
                self.mdef += ((hat_level-30)*22.45 + 651)
                self.hp += ((hat_level-30)*107.15 + 11857)
                # SF
                self.pdef += sfdefdict[hat_sf_level]
                self.mdef += sfdefdict[hat_sf_level]
                # Refinement
                self.pdef += ((hat_refine_level-1) * 32 + 160)
                self.mdef += ((hat_refine_level - 1) * 32 + 160)
                # Stat
                if hat_stat == "Boss ATK":
                    self.batk += ((hat_level-1)*0.048 + 1.6)
                    self.stat_amount += self.batk
                elif hat_stat == "Crit ATK":
                    self.cratk += ((hat_level-1)*1.8 + 110)
                    self.stat_amount += self.cratk
                elif hat_stat == "Crit DMG":
                    self.cd += ((hat_level-1)*0.182 + 6.9)
                    self.stat_amount += self.cd
                else:
                    self.exp += ((hat_level-1)*0.02 + 1)
                    self.stat_amount += self.exp
                self.aempsetcount += 1
            elif hat_type == "Fafnir":
                # Base
                self.pdef += 971
                self.mdef += 971
                # Level
                self.pdef += ((hat_level - 30) * 22.45 + 651)
                self.mdef += ((hat_level - 30) * 22.45 + 651)
                self.hp += ((hat_level - 30) * 107.15 + 8750)
                self.dmg += 0.1*hat_level
                # SF
                self.pdef += sfdefdict[hat_sf_level]
                self.mdef += sfdefdict[hat_sf_level]
                self.fafsetcount += 1
            elif hat_type == "Necro":
                # Base
                self.pdef += 2969
                self.mdef += 2969
                # Level
                self.pdef += ((hat_level - 1) * 27.3)
                self.mdef += ((hat_level - 1) * 27.3)
                self.hp += ((hat_level - 1) * 115.7 + 9450)
                # SF
                self.pdef += sfdefdict[hat_sf_level]
                self.mdef += sfdefdict[hat_sf_level]
                # Stat
                if hat_stat == "Boss ATK":
                    self.batk += ((hat_level - 1) * 0.048 + 1.6)
                    self.stat_amount += self.batk
                elif hat_stat == "Crit ATK":
                    self.cratk += ((hat_level - 1) * 1.8 + 110)
                    self.stat_amount += self.cratk
                elif hat_stat == "Crit DMG":
                    self.cd += ((hat_level - 1) * 0.182 + 6.9)
                    self.stat_amount += self.cd
                else:
                    self.exp += ((hat_level - 1) * 0.02 + 1)
                    self.stat_amount += self.exp
                self.necrosetcount += 1

            hat_emblem = hat3.radio("Choose Hat Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
            hat_emblem_level = hat3.slider("Hat Emblem Level", min_value=1, max_value=5)
            self.normal_emb += 1
            self.emblem = hat_emblem
            self.emblem_level = hat_emblem_level
            # Emblem
            if hat_emblem == "Crit DMG":
                self.emblem_amount += emblem_cd_stats[hat_emblem_level]
                self.emblem_cd += self.emblem_amount
            elif hat_emblem == "Boss ATK":
                self.emblem_amount += emblem_ba_stats[hat_emblem_level]
                self.emblem_batk += self.emblem_amount
            else:
                self.emblem_amount += emblem_atk_stats[hat_emblem_level]
                self.emblem_atkp += self.emblem_amount

        # Flame Stat
        self.cdlinecount += 2

        # Potential
        self.atkp += 6
