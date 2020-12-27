import streamlit as st


class Tbo:
    def __init__(self):
        # Emblem Visualization
        self.emblem = "None"
        self.emblem_amount = 0
        self.emblem_level = 0
        self.top_emblem = "None"
        self.top_emblem_amount = 0
        self.top_emblem_level = 0
        self.btm_emblem = "None"
        self.btm_emblem_amount = 0
        self.btm_emblem_level = 0

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
        self.top_sf = 0
        self.btm_sf = 0
        self.sf = 0

        # Equipment Type, Stat & Rank
        self.type = "None"
        self.stat = "None"
        self.stat_amount = 0
        self.top_type = "None"
        self.top_stat = "None"
        self.top_stat_amount = 0
        self.btm_type = "None"
        self.btm_stat = "None"
        self.btm_stat_amount = 0
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

        o_sfdefdict = {
            0: 0,
            1: 173,
            2: 352,
            3: 537,
            4: 727,
            5: 923,
            6: 1125,
            7: 1333,
            8: 1548,
            9: 1770,
            10: 2000,
            11: 2237,
            12: 2482,
            13: 2736,
            14: 3000,
            15: 3272,
            16: 3555,
            17: 3849,
            18: 4154,
            19: 4470,
            20: 4800,
            21: 5143,
            22: 5500,
            23: 5872,
            24: 6261,
            25: 6667,
            26: 7091,
            27: 7535,
            28: 8000,
            29: 8488,
            30: 9000
        }
        o_emblem_cd_stats = {
            1: 5,
            2: 7,
            3: 10,
            4: 15,
            5: 20
        }

        o_emblem_ba_stats = {
            1: 3,
            2: 4,
            3: 5,
            4: 7,
            5: 10
        }

        o_emblem_atk_stats = {
            1: 3,
            2: 4,
            3: 5,
            4: 7,
            5: 10
        }
        tb_emblem_cd_stats = {
            1: 2.5,
            2: 3.5,
            3: 5,
            4: 7.5,
            5: 10
        }

        tb_emblem_ba_stats = {
            1: 1.5,
            2: 2,
            3: 2.5,
            4: 3.5,
            5: 5
        }

        tb_emblem_atk_stats = {
            1: 1.5,
            2: 2,
            3: 2.5,
            4: 3.5,
            5: 5
        }
        with st.beta_expander("Top+Bottom/Outfit"):
            tbo_type = st.selectbox("Choose Combination", ["Top+Bottom", "Outfit"])
            self.tbo_type = tbo_type
            if tbo_type == "Outfit":
                _, outfit1, _, outfit2, _, outfit3, _ = st.beta_columns([0.02, 0.303, 0.02, 0.303, 0.02, 0.303, 0.02])
                outfit_type = outfit1.selectbox("Choose Outfit Type", ["Mythic Empress", "Ancient Empress", "Necro"])
                outfit_stat = outfit1.radio("Choose Outfit Stat", ["Crit ATK", "EVD", "MP Rec", "EXP"])
                self.type = outfit_type
                self.stat = outfit_stat
                if outfit_type == "Mythic Empress":
                    outfit_level = outfit2.slider('Outfit Level', min_value=30, max_value=40)
                else:
                    outfit_level = outfit2.slider('Outfit Level', min_value=30, max_value=50)
                self.level = outfit_level
                outfit_sf_level = outfit2.slider("Outfit SF Level", min_value=0, max_value=30)
                self.sf = outfit_sf_level
                if outfit_type == "Mythic Empress":
                    outfit_refine_level = outfit2.slider("Outfit Refinement Level", min_value=1, max_value=10)
                    # Base
                    self.pdef += 2048
                    self.mdef += 2048
                    # Level
                    self.pdef += (outfit_level - 30) * 78.8
                    self.mdef += (outfit_level - 30) * 78.8
                    self.hp += ((outfit_level - 30) * 540.3 + 10807)
                    # SF
                    self.pdef += o_sfdefdict[outfit_sf_level]
                    self.mdef += o_sfdefdict[outfit_sf_level]
                    # Refinement
                    self.pdef += ((outfit_refine_level - 1) * 82 + 410)
                    self.mdef += ((outfit_refine_level - 1) * 82 + 410)
                    # Stat
                    if outfit_stat == "Crit ATK":
                        self.batk += ((outfit_level - 30) * 5.4 + 108)
                        self.stat_amount += self.batk
                    elif outfit_stat == "EVD":
                        self.cratk += ((outfit_level - 30) * 18.8 + 375)
                        self.stat_amount += self.cratk
                    elif outfit_stat == "MP Rec":
                        self.mprec += ((outfit_level - 30) * 0.2 + 3)
                        self.stat_amount += self.mprec
                    else:
                        self.exp += ((outfit_level - 30) * 0.04 + 1.1)
                        self.stat_amount += self.exp
                    # Emblem
                    outfit_emblem = outfit3.radio("Choose Outfit Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                    outfit_emblem_level = outfit3.slider("Outfit Emblem Level", min_value=1, max_value=5)
                    self.normal_emb += 1
                    self.emblem = outfit_emblem
                    self.emblem_level = outfit_emblem_level
                    if outfit_emblem == "Crit DMG":
                        self.emblem_amount += o_emblem_cd_stats[outfit_emblem_level]
                        self.emblem_cd += self.emblem_amount
                    elif outfit_emblem == "Boss ATK":
                        self.emblem_amount += o_emblem_ba_stats[outfit_emblem_level]
                        self.emblem_batk += self.emblem_amount
                    else:
                        self.emblem_amount += o_emblem_atk_stats[outfit_emblem_level]
                        self.emblem_atkp += self.emblem_amount
                    self.mempsetcount += 1
                    self.crlinecount += 2
                    self.atk += 450
                elif outfit_type == "Ancient Empress":
                    outfit_refine_level = outfit2.slider("Outfit Refinement Level", min_value=1, max_value=10)
                    # Base
                    self.pdef += 5287
                    self.mdef += 5287
                    # Level
                    self.pdef += (outfit_level - 1) * (2750/49)
                    self.mdef += (outfit_level - 1) * (2750/49)
                    self.hp += ((outfit_level - 1) * (7770/49) + 12950)
                    # SF
                    self.pdef += o_sfdefdict[outfit_sf_level]
                    self.mdef += o_sfdefdict[outfit_sf_level]
                    # Refinement
                    self.pdef += ((outfit_refine_level - 1) * 82 + 410)
                    self.mdef += ((outfit_refine_level - 1) * 82 + 410)
                    # Stat
                    if outfit_stat == "Crit ATK":
                        self.batk += ((outfit_level - 1) * (90/49) + 110)
                        self.stat_amount += self.batk
                    elif outfit_stat == "EVD":
                        self.cratk += ((outfit_level - 1) * (299/49) + 381)
                        self.stat_amount += self.cratk
                    elif outfit_stat == "MP Rec":
                        self.mprec += ((outfit_level - 1) * (3/49) + 3)
                        self.stat_amount += self.mprec
                    else:
                        self.exp += ((outfit_level - 1) * (0.9/49) + 1.1)
                        self.stat_amount += self.exp
                    # Emblem
                    outfit_emblem = outfit3.radio("Choose Outfit Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                    outfit_emblem_level = outfit3.slider("Outfit Emblem Level", min_value=1, max_value=5)
                    self.normal_emb += 1
                    self.emblem = outfit_emblem
                    self.emblem_level = outfit_emblem_level
                    if outfit_emblem == "Crit DMG":
                        self.emblem_amount += o_emblem_cd_stats[outfit_emblem_level]
                        self.emblem_cd += self.emblem_amount
                    elif outfit_emblem == "Boss ATK":
                        self.emblem_amount += o_emblem_ba_stats[outfit_emblem_level]
                        self.emblem_batk += self.emblem_amount
                    else:
                        self.emblem_amount += o_emblem_atk_stats[outfit_emblem_level]
                        self.emblem_atkp += self.emblem_amount
                    self.aempsetcount += 1
                    self.crlinecount += 2
                    self.atk += 450
                else:
                    # Base
                    self.pdef += 7427
                    self.mdef += 7427
                    # Level
                    self.pdef += (outfit_level - 1) * (3347/49)
                    self.mdef += (outfit_level - 1) * (3347/49)
                    self.hp += ((outfit_level - 1) * (8391/49) + 13986)
                    # SF
                    self.pdef += o_sfdefdict[outfit_sf_level]
                    self.mdef += o_sfdefdict[outfit_sf_level]
                    # Stat
                    if outfit_stat == "Crit ATK":
                        self.batk += ((outfit_level - 1) * (90 / 49) + 110)
                        self.stat_amount += self.batk
                    elif outfit_stat == "EVD":
                        self.cratk += ((outfit_level - 1) * (299 / 49) + 381)
                        self.stat_amount += self.cratk
                    elif outfit_stat == "MP Rec":
                        self.mprec += ((outfit_level - 1) * (3 / 49) + 3)
                        self.stat_amount += self.mprec
                    else:
                        self.exp += ((outfit_level - 1) * (0.9 / 49) + 1.1)
                        self.stat_amount += self.exp
                    # Emblem
                    outfit_emblem = outfit3.radio("Choose Outfit Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                    outfit_emblem_level = outfit3.slider("Outfit Emblem Level", min_value=1, max_value=5)
                    self.normal_emb += 1
                    self.emblem = outfit_emblem
                    self.emblem_level = outfit_emblem_level
                    if outfit_emblem == "Crit DMG":
                        self.emblem_amount += o_emblem_cd_stats[outfit_emblem_level]
                        self.emblem_cd += self.emblem_amount
                    elif outfit_emblem == "Boss ATK":
                        self.emblem_amount += o_emblem_ba_stats[outfit_emblem_level]
                        self.emblem_batk += self.emblem_amount
                    else:
                        self.emblem_amount += o_emblem_atk_stats[outfit_emblem_level]
                        self.emblem_atkp += self.emblem_amount
                    self.necrosetcount += 1
                    self.crlinecount += 2
                    self.atk += 450
            else:
                _, tb1, _, tb2, _ = st.beta_columns([0.02, 0.47, 0.02, 0.47, 0.02])
                top_level = tb1.slider("Top Level", min_value=30, max_value=50)
                top_sf_level = tb1.slider("Top SF Level", min_value=0, max_value=20)
                self.top_level = top_level
                self.top_sf = top_sf_level
                # Base
                self.pdef += 1211
                self.mdef += 1211
                # Level
                self.pdef += (top_level - 1) * 29.326
                self.mdef += (top_level - 1) * 29.326
                self.hp += ((top_level - 1) * (3092 / 39) + 6475)
                self.dmg += 0.1*top_level
                # SF
                self.pdef += o_sfdefdict[top_sf_level] * (923/1333)
                self.mdef += o_sfdefdict[top_sf_level] * (923/1333)
                top_emblem = tb1.radio("Choose Top Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                top_emblem_level = tb1.slider("Top Emblem Level", min_value=1, max_value=5)
                self.partial_emb += 1
                self.top_emblem = top_emblem
                self.top_emblem_level = top_emblem_level
                # Emblem
                if top_emblem == "Crit DMG":
                    self.top_emblem_amount += tb_emblem_cd_stats[top_emblem_level]
                    self.emblem_cd += self.top_emblem_amount
                elif top_emblem == "Boss ATK":
                    self.top_emblem_amount += tb_emblem_ba_stats[top_emblem_level]
                    self.emblem_batk += self.top_emblem_amount
                else:
                    self.top_emblem_amount += tb_emblem_atk_stats[top_emblem_level]
                    self.emblem_atkp += self.top_emblem_amount
                self.fafsetcount += 1
                self.atklinecount += 2
                self.atk += 450

                btm_level = tb2.slider("Bottom Level", min_value=30, max_value=50)
                btm_sf_level = tb2.slider("Bottom SF Level", min_value=0, max_value=20)
                self.btm_level = btm_level
                self.btm_sf = btm_sf_level
                # Base
                self.pdef += 1211
                self.mdef += 1211
                # Level
                self.pdef += (btm_level - 1) * 29.326
                self.mdef += (btm_level - 1) * 29.326
                self.hp += ((btm_level - 1) * (3092 / 39) + 6475)
                self.dmg += 0.1*btm_level
                # SF
                self.pdef += o_sfdefdict[btm_sf_level] * (923 / 799)
                self.mdef += o_sfdefdict[btm_sf_level] * (923 / 799)
                btm_emblem = tb2.radio("Choose Bottom Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                btm_emblem_level = tb2.slider("Bottom Emblem Level", min_value=1, max_value=5)
                self.partial_emb += 1
                self.btm_emblem = btm_emblem
                self.btm_emblem_level = btm_emblem_level
                # Emblem
                if btm_emblem == "Crit DMG":
                    self.btm_emblem_amount += tb_emblem_cd_stats[btm_emblem_level]
                    self.emblem_cd += self.btm_emblem_amount
                elif btm_emblem == "Boss ATK":
                    self.btm_emblem_amount += tb_emblem_ba_stats[btm_emblem_level]
                    self.emblem_batk += self.btm_emblem_amount
                else:
                    self.btm_emblem_amount += tb_emblem_atk_stats[btm_emblem_level]
                    self.emblem_atkp += self.btm_emblem_amount
                self.fafsetcount += 1
                self.atklinecount += 2
                self.atk += 450
                self.sf += self.top_sf + self.btm_sf
