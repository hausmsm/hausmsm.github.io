import streamlit as st


class weapon:
    def __init__(self, character_type, character_class):
        # Initialize
        self.character_type = character_type
        self.character_class = character_class
        self.stat_amount = 0
        self.emblem_amount = 0

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

        # Weapon SF Dict
        sfdict = {
            0: 0,
            1: 83,
            2: 178,
            3: 279,
            4: 384,
            5: 492,
            6: 602,
            7: 715,
            8: 829,
            9: 946,
            10: 1064,
            11: 1184,
            12: 1305,
            13: 1429,
            14: 1553,
            15: 1680,
            16: 1808,
            17: 1937,
            18: 2068,
            19: 2201,
            20: 2336,
            21: 2473,
            22: 2611,
            23: 2752,
            24: 2895,
            25: 3041,
            26: 3191,
            27: 3344,
            28: 3503,
            29: 3670,
            30: 3861,
            31: 4036
        }
        mythicdict = {
            30: 2048,
            31: 2252,
            32: 2457,
            33: 2662,
            34: 2867,
            35: 3072,
            36: 3276,
            37: 3481,
            38: 3686,
            39: 3891,
            40: 4096
        }

        ancientdict = {
            30: 3329,
            31: 3443,
            32: 3558,
            33: 3673,
            34: 3788,
            35: 3903,
            36: 4017,
            37: 4132,
            38: 4247,
            39: 4362,
            40: 4477,
            41: 4591,
            42: 4706,
            43: 4821,
            44: 4936,
            45: 5051,
            46: 5165,
            47: 5280,
            48: 5395,
            49: 5510,
            50: 5625
        }

        necrodict = {
            30: 3883,
            31: 4017,
            32: 4151,
            33: 4285,
            34: 4419,
            35: 4553,
            36: 4687,
            37: 4821,
            38: 4954,
            39: 5088,
            40: 5222,
            41: 5356,
            42: 5490,
            43: 5624,
            44: 5758,
            45: 5892,
            46: 6026,
            47: 6160,
            48: 6294,
            49: 6428,
            50: 6562
        }

        fafnirdict = {
            30: 4440,
            31: 4593,
            32: 4746,
            33: 4900,
            34: 5053,
            35: 5206,
            36: 5359,
            37: 5512,
            38: 5665,
            39: 5818,
            40: 5972,
            41: 6521,
            42: 7071,
            43: 7621,
            44: 8170,
            45: 8720,
            46: 9270,
            47: 9819,
            48: 10369,
            49: 10919,
            50: 11469
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

        # User Input
        with st.beta_expander("Weapon"):
            _, wep1, _, wep2, _, wep3, _ = st.beta_columns([0.02, 0.303, 0.02, 0.303, 0.02, 0.303, 0.02])
            weapon_type = wep1.selectbox("Choose Weapon Type", ["Mythic Empress", "Ancient Empress", "Necro", "Fafnir"])
            self.type = weapon_type
            if weapon_type == "Mythic Empress":
                weapon_level = wep2.slider("Choose Weapon Level", min_value=30, max_value=40)
            else:
                weapon_level = wep2.slider("Choose Weapon Level", min_value=30, max_value=50)
            weapon_sf_level = wep2.slider("Weapon SF Level", min_value=0, max_value=31)
            self.sf = weapon_sf_level
            self.level = weapon_level
            if weapon_type in ["Mythic Empress", "Ancient Empress"]:
                weapon_refine_level = wep2.slider("Weapon Refinement Level", min_value=1, max_value=10)
            if weapon_type != "Fafnir":
                weapon_stat = wep1.radio("Choose Weapon Stat", ["Boss ATK", "Crit DMG", "Crit Rate", "EXP"])
            else:
                weapon_stat = "Final DMG"
            self.stat = weapon_stat
            weapon_emblem = wep3.radio("Choose Weapon Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
            self.emblem = weapon_emblem
            weapon_emblem_level = wep3.slider("Weapon Emblem Level", min_value=1, max_value=5)
            self.emblem_level = weapon_emblem_level
            if character_type == "Warrior":
                if character_class in ["Paladin", "Demon Slayer", "Demon Avenger"]:
                    if weapon_type == "Mythic Empress":
                        # Base
                        self.atk += 5004
                        # Level
                        self.atk += mythicdict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_sf_level]
                        # Refinement
                        self.atk += ((weapon_refine_level - 1) * 50 + 250)
                        # Stats
                        if weapon_stat == "Boss ATK":
                            self.batk += ((weapon_level - 30) * 1.3 + 13)
                            self.stat_amount += self.batk
                        elif weapon_stat == "Crit DMG":
                            self.cd += ((weapon_level - 30) * 5.4 + 54)
                            self.stat_amount += self.cd
                        elif weapon_stat == "Crit Rate":
                            self.cr += ((weapon_level - 30) * 0.24 + 17.6)
                            self.stat_amount += self.cr
                        else:
                            if weapon_level in [30, 31]:
                                self.exp += ((weapon_level - 30) * 0.1 + 10.4)
                                self.stat_amount += self.exp
                            else:
                                self.exp += ((weapon_level - 32) * 0.5 + 11.0)
                                self.stat_amount += self.exp
                    elif weapon_type == "Ancient Empress":
                        # Base
                        self.atk += 9595
                        # Level
                        self.atk += ancientdict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_level]
                        # Refinement
                        if weapon_refine_level in [1, 2, 3, 4]:
                            self.atk += ((weapon_refine_level - 1) * 50 + 250)
                        else:
                            self.atk += ((weapon_refine_level - 4) * 100) + 400
                        # Stats
                        if weapon_stat == "Boss ATK":
                            self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                            self.stat_amount += self.batk
                        elif weapon_stat == "Crit DMG":
                            if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                                self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                                self.stat_amount += self.cd
                            else:
                                self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                                self.stat_amount += self.cd
                        elif weapon_stat == "Crit Rate":
                            self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                            self.stat_amount += self.cr
                        else:
                            self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                            self.stat_amount += self.exp
                    elif weapon_type == "Fafnir":
                        # Base
                        self.atk += 7179
                        # Level
                        self.atk += fafnirdict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_sf_level]
                        # Stats
                        self.fd += ((weapon_level - 30) * 0.4 + 12)
                        self.stat_amount += self.fd
                    else:
                        # Base
                        self.atk += 11696
                        # Level
                        self.atk += necrodict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_level]
                        # Stats
                        if weapon_stat == "Boss ATK":
                            self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                            self.stat_amount += self.batk
                        elif weapon_stat == "Crit DMG":
                            if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                                self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                                self.stat_amount += self.cd
                            else:
                                self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                                self.stat_amount += self.cd
                        elif weapon_stat == "Crit Rate":
                            self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                            self.stat_amount += self.cr
                        else:
                            self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                            self.stat_amount += self.exp
                else:
                    if weapon_type == "Mythic Empress":
                        # Base
                        self.atk += 4923
                        # Level
                        self.atk += mythicdict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_sf_level]
                        # Refinement
                        self.atk += ((weapon_refine_level - 1) * 50 + 250)
                        # Stats
                        if weapon_stat == "Boss ATK":
                            self.batk += ((weapon_level - 30) * 1.3 + 13)
                            self.stat_amount += self.batk
                        elif weapon_stat == "Crit DMG":
                            self.cd += ((weapon_level - 30) * 5.4 + 54)
                            self.stat_amount += self.cd
                        elif weapon_stat == "Crit Rate":
                            self.cr += ((weapon_level - 30) * 0.24 + 17.6)
                            self.stat_amount += self.cr
                        else:
                            if weapon_level in [30, 31]:
                                self.exp += ((weapon_level - 30) * 0.1 + 10.4)
                                self.stat_amount += self.exp
                            else:
                                self.exp += ((weapon_level - 32) * 0.5 + 11.0)
                                self.stat_amount += self.exp
                    elif weapon_type == "Ancient Empress":
                        # Base
                        self.atk += 9423
                        # Level
                        self.atk += ancientdict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_level]
                        # Refinement
                        if weapon_refine_level in [1, 2, 3, 4]:
                            self.atk += ((weapon_refine_level - 1) * 50 + 250)
                        else:
                            self.atk += ((weapon_refine_level - 4) * 100) + 400
                        # Stats
                        if weapon_stat == "Boss ATK":
                            self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                            self.stat_amount += self.batk
                        elif weapon_stat == "Crit DMG":
                            if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                                self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                                self.stat_amount += self.cd
                            else:
                                self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                                self.stat_amount += self.cd
                        elif weapon_stat == "Crit Rate":
                            self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                            self.stat_amount += self.cr
                        else:
                            self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                            self.stat_amount += self.exp
                    elif weapon_type == "Fafnir":
                        # Base
                        self.atk += 7179
                        # Level
                        self.atk += fafnirdict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_sf_level]
                        # Stats
                        self.fd += ((weapon_level - 30) * 0.4 + 12)
                        self.stat_amount += self.fd
                    else:
                        # Base
                        self.atk += 11487
                        # Level
                        self.atk += necrodict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_level]
                        # Stats
                        if weapon_stat == "Boss ATK":
                            self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                            self.stat_amount += self.batk
                        elif weapon_stat == "Crit DMG":
                            if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                                self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                                self.stat_amount += self.cd
                            else:
                                self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                                self.stat_amount += self.cd
                        elif weapon_stat == "Crit Rate":
                            self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                            self.stat_amount += self.cr
                        else:
                            self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                            self.stat_amount += self.exp
            elif character_type == "Archer":
                if weapon_type == "Mythic Empress":
                    # Base
                    self.atk += 5003
                    # Level
                    self.atk += mythicdict[weapon_level]
                    # SF
                    self.atk += sfdict[weapon_sf_level]
                    # Refinement
                    self.atk += ((weapon_refine_level - 1) * 50 + 250)
                    # Stats
                    if weapon_stat == "Boss ATK":
                        self.batk += ((weapon_level - 30) * 1.3 + 13)
                        self.stat_amount += self.batk
                    elif weapon_stat == "Crit DMG":
                        self.cd += ((weapon_level - 30) * 5.4 + 54)
                        self.stat_amount += self.cd
                    elif weapon_stat == "Crit Rate":
                        self.cr += ((weapon_level - 30) * 0.24 + 17.6)
                        self.stat_amount += self.cr
                    else:
                        if weapon_level in [30, 31]:
                            self.exp += ((weapon_level - 30) * 0.1 + 10.4)
                            self.stat_amount += self.exp
                        else:
                            self.exp += ((weapon_level - 32) * 0.5 + 11.0)
                            self.stat_amount += self.exp
                elif weapon_type == "Ancient Empress":
                    # Base
                    self.atk += 9594
                    # Level
                    self.atk += ancientdict[weapon_level]
                    # SF
                    self.atk += sfdict[weapon_sf_level]
                    # Refinement
                    if weapon_refine_level in [1, 2, 3, 4]:
                        self.atk += ((weapon_refine_level - 1) * 50 + 250)
                    else:
                        self.atk += ((weapon_refine_level - 4) * 100) + 400
                    # Stats
                    if weapon_stat == "Boss ATK":
                        self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                        self.stat_amount += self.batk
                    elif weapon_stat == "Crit DMG":
                        if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                            self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                            self.stat_amount += self.cd
                        else:
                            self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                            self.stat_amount += self.cd
                    elif weapon_stat == "Crit Rate":
                        self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                        self.stat_amount += self.cr
                    else:
                        self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                        self.stat_amount += self.exp
                elif weapon_type == "Fafnir":
                    # Base
                    self.atk += 7178
                    # Level
                    self.atk += fafnirdict[weapon_level]
                    # SF
                    self.atk += sfdict[weapon_sf_level]
                    # Stats
                    self.fd += ((weapon_level - 30) * 0.4 + 12)
                    self.stat_amount += self.fd
                else:
                    # Base
                    self.atk += 11694
                    # Level
                    self.atk += necrodict[weapon_level]
                    # SF
                    self.atk += sfdict[weapon_sf_level]
                    # Stats
                    if weapon_stat == "Boss ATK":
                        self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                        self.stat_amount += self.batk
                    elif weapon_stat == "Crit DMG":
                        if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                            self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                            self.stat_amount += self.cd
                        else:
                            self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                            self.stat_amount += self.cd
                    elif weapon_stat == "Crit Rate":
                        self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                        self.stat_amount += self.cr
                    else:
                        self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                        self.stat_amount += self.exp
            elif character_type == "Thief":
                if weapon_type == "Mythic Empress":
                    # Base
                    self.atk += 4981
                    # Level
                    self.atk += mythicdict[weapon_level]
                    # SF
                    self.atk += sfdict[weapon_sf_level]
                    # Refinement
                    self.atk += ((weapon_refine_level - 1) * 50 + 250)
                    # Stats
                    if weapon_stat == "Boss ATK":
                        self.batk += ((weapon_level - 30) * 1.3 + 13)
                        self.stat_amount += self.batk
                    elif weapon_stat == "Crit DMG":
                        self.cd += ((weapon_level - 30) * 5.4 + 54)
                        self.stat_amount += self.cd
                    elif weapon_stat == "Crit Rate":
                        self.cr += ((weapon_level - 30) * 0.24 + 17.6)
                        self.stat_amount += self.cr
                    else:
                        if weapon_level in [30, 31]:
                            self.exp += ((weapon_level - 30) * 0.1 + 10.4)
                            self.stat_amount += self.exp
                        else:
                            self.exp += ((weapon_level - 32) * 0.5 + 11.0)
                            self.stat_amount += self.exp
                elif weapon_type == "Ancient Empress":
                    # Base
                    self.atk += 9553
                    # Level
                    self.atk += ancientdict[weapon_level]
                    # SF
                    self.atk += sfdict[weapon_level]
                    # Refinement
                    if weapon_refine_level in [1, 2, 3, 4]:
                        self.atk += ((weapon_refine_level - 1) * 50 + 250)
                    else:
                        self.atk += ((weapon_refine_level - 4) * 100) + 400
                    # Stats
                    if weapon_stat == "Boss ATK":
                        self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                        self.stat_amount += self.batk
                    elif weapon_stat == "Crit DMG":
                        if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                            self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                            self.stat_amount += self.cd
                        else:
                            self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                            self.stat_amount += self.cd
                    elif weapon_stat == "Crit Rate":
                        self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                        self.stat_amount += self.cr
                    else:
                        self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                        self.stat_amount += self.exp
                elif weapon_type == "Fafnir":
                    # Base
                    self.atk += 7176
                    # Level
                    self.atk += fafnirdict[weapon_level]
                    # SF
                    self.atk += sfdict[weapon_sf_level]
                    # Stats
                    self.fd += ((weapon_level - 30) * 0.4 + 12)
                    self.stat_amount += self.fd
                else:
                    # Base
                    self.atk += 11645
                    # Level
                    self.atk += necrodict[weapon_level]
                    # SF
                    self.atk += sfdict[weapon_level]
                    # Stats
                    if weapon_stat == "Boss ATK":
                        self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                        self.stat_amount += self.batk
                    elif weapon_stat == "Crit DMG":
                        if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                            self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                            self.stat_amount += self.cd
                        else:
                            self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                            self.stat_amount += self.cd
                    elif weapon_stat == "Crit Rate":
                        self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                        self.stat_amount += self.cr
                    else:
                        self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                        self.stat_amount += self.exp
            elif character_type == "Mage":
                if weapon_type == "Mythic Empress":
                    # Base
                    self.atk += 4962
                    # Level
                    self.atk += mythicdict[weapon_level]
                    # SF
                    self.atk += sfdict[weapon_sf_level]
                    # Refinement
                    self.atk += ((weapon_refine_level - 1) * 50 + 250)
                    # Stats
                    if weapon_stat == "Boss ATK":
                        self.batk += ((weapon_level - 30) * 1.3 + 13)
                        self.stat_amount += self.batk
                    elif weapon_stat == "Crit DMG":
                        self.cd += ((weapon_level - 30) * 5.4 + 54)
                        self.stat_amount += self.cd
                    elif weapon_stat == "Crit Rate":
                        self.cr += ((weapon_level - 30) * 0.24 + 17.6)
                        self.stat_amount += self.cr
                    else:
                        if weapon_level in [30, 31]:
                            self.exp += ((weapon_level - 30) * 0.1 + 10.4)
                            self.stat_amount += self.exp
                        else:
                            self.exp += ((weapon_level - 32) * 0.5 + 11.0)
                            self.stat_amount += self.exp
                elif weapon_type == "Ancient Empress":
                    # Base
                    self.atk += 9503
                    # Level
                    self.atk += ancientdict[weapon_level]
                    # SF
                    self.atk += sfdict[weapon_level]
                    # Refinement
                    if weapon_refine_level in [1, 2, 3, 4]:
                        self.atk += ((weapon_refine_level - 1) * 50 + 250)
                    else:
                        self.atk += ((weapon_refine_level - 4) * 100) + 400
                    # Stats
                    if weapon_stat == "Boss ATK":
                        self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                        self.stat_amount += self.batk
                    elif weapon_stat == "Crit DMG":
                        if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                            self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                            self.stat_amount += self.cd
                        else:
                            self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                            self.stat_amount += self.cd
                    elif weapon_stat == "Crit Rate":
                        self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                        self.stat_amount += self.cr
                    else:
                        self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                        self.stat_amount += self.exp
                elif weapon_type == "Fafnir":
                    # Base
                    self.atk += 7173
                    # Level
                    self.atk += fafnirdict[weapon_level]
                    # SF
                    self.atk += sfdict[weapon_sf_level]
                    # Stats
                    self.fd += ((weapon_level - 30) * 0.4 + 12)
                    self.stat_amount += self.fd
                else:
                    # Base
                    self.atk += 11585
                    # Level
                    self.atk += necrodict[weapon_level]
                    # SF
                    self.atk += sfdict[weapon_level]
                    # Stats
                    if weapon_stat == "Boss ATK":
                        self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                        self.stat_amount += self.batk
                    elif weapon_stat == "Crit DMG":
                        if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                            self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                            self.stat_amount += self.cd
                        else:
                            self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                            self.stat_amount += self.cd
                    elif weapon_stat == "Crit Rate":
                        self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                        self.stat_amount += self.cr
                    else:
                        self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                        self.stat_amount += self.exp
            else:
                if character_class in ["Corsair", "Mechanic"]:
                    if weapon_type == "Mythic Empress":
                        # Base
                        self.atk += 5003
                        # Level
                        self.atk += mythicdict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_sf_level]
                        # Refinement
                        self.atk += ((weapon_refine_level - 1) * 50 + 250)
                        # Stats
                        if weapon_stat == "Boss ATK":
                            self.batk += ((weapon_level - 30) * 1.3 + 13)
                            self.stat_amount += self.batk
                        elif weapon_stat == "Crit DMG":
                            self.cd += ((weapon_level - 30) * 5.4 + 54)
                            self.stat_amount += self.cd
                        elif weapon_stat == "Crit Rate":
                            self.cr += ((weapon_level - 30) * 0.24 + 17.6)
                            self.stat_amount += self.cr
                        else:
                            if weapon_level in [30, 31]:
                                self.exp += ((weapon_level - 30) * 0.1 + 10.4)
                                self.stat_amount += self.exp
                            else:
                                self.exp += ((weapon_level - 32) * 0.5 + 11.0)
                                self.stat_amount += self.exp
                    elif weapon_type == "Ancient Empress":
                        # Base
                        self.atk += 9592
                        # Level
                        self.atk += ancientdict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_level]
                        # Refinement
                        if weapon_refine_level in [1, 2, 3, 4]:
                            self.atk += ((weapon_refine_level - 1) * 50 + 250)
                        else:
                            self.atk += ((weapon_refine_level - 4) * 100) + 400
                        # Stats
                        if weapon_stat == "Boss ATK":
                            self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                            self.stat_amount += self.batk
                        elif weapon_stat == "Crit DMG":
                            if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                                self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                                self.stat_amount += self.cd
                            else:
                                self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                                self.stat_amount += self.cd
                        elif weapon_stat == "Crit Rate":
                            self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                            self.stat_amount += self.cr
                        else:
                            self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                            self.stat_amount += self.exp
                    elif weapon_type == "Fafnir":
                        # Base
                        self.atk += 7176
                        # Level
                        self.atk += fafnirdict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_sf_level]
                        # Stats
                        self.fd += ((weapon_level - 30) * 0.4 + 12)
                        self.stat_amount += self.fd
                    else:
                        # Base
                        self.atk += 11693
                        # Level
                        self.atk += necrodict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_level]
                        # Stats
                        if weapon_stat == "Boss ATK":
                            self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                            self.stat_amount += self.batk
                        elif weapon_stat == "Crit DMG":
                            if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                                self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                                self.stat_amount += self.cd
                            else:
                                self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                                self.stat_amount += self.cd
                        elif weapon_stat == "Crit Rate":
                            self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                            self.stat_amount += self.cr
                        else:
                            self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                            self.stat_amount += self.exp
                else:
                    if weapon_type == "Mythic Empress":
                        # Base
                        self.atk += 4981
                        # Level
                        self.atk += mythicdict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_sf_level]
                        # Refinement
                        self.atk += ((weapon_refine_level - 1) * 50 + 250)
                        # Stats
                        if weapon_stat == "Boss ATK":
                            self.batk += ((weapon_level - 30) * 1.3 + 13)
                            self.stat_amount += self.batk
                        elif weapon_stat == "Crit DMG":
                            self.cd += ((weapon_level - 30) * 5.4 + 54)
                            self.stat_amount += self.cd
                        elif weapon_stat == "Crit Rate":
                            self.cr += ((weapon_level - 30) * 0.24 + 17.6)
                            self.stat_amount += self.cr
                        else:
                            if weapon_level in [30, 31]:
                                self.exp += ((weapon_level - 30) * 0.1 + 10.4)
                                self.stat_amount += self.exp
                            else:
                                self.exp += ((weapon_level - 32) * 0.5 + 11.0)
                                self.stat_amount += self.exp
                    elif weapon_type == "Ancient Empress":
                        # Base
                        self.atk += 9553
                        # Level
                        self.atk += ancientdict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_level]
                        # Refinement
                        if weapon_refine_level in [1, 2, 3, 4]:
                            self.atk += ((weapon_refine_level - 1) * 50 + 250)
                        else:
                            self.atk += ((weapon_refine_level - 4) * 100) + 400
                        # Stats
                        if weapon_stat == "Boss ATK":
                            self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                            self.stat_amount += self.batk
                        elif weapon_stat == "Crit DMG":
                            if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                                self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                                self.stat_amount += self.cd
                            else:
                                self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                                self.stat_amount += self.cd
                        elif weapon_stat == "Crit Rate":
                            self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                            self.stat_amount += self.cr
                        else:
                            self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                            self.stat_amount += self.exp
                    elif weapon_type == "Fafnir":
                        # Base
                        self.atk += 7176
                        # Level
                        self.atk += fafnirdict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_sf_level]
                        # Stats
                        self.fd += ((weapon_level - 30) * 0.4 + 12)
                        self.stat_amount += self.fd
                    else:
                        # Base
                        self.atk += 11645
                        # Level
                        self.atk += necrodict[weapon_level]
                        # SF
                        self.atk += sfdict[weapon_level]
                        # Stats
                        if weapon_stat == "Boss ATK":
                            self.batk += ((weapon_level - 30) * ((30 - 13.3) / 49) + 23.2)
                            self.stat_amount += self.batk
                        elif weapon_stat == "Crit DMG":
                            if weapon_level in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                                self.cd += ((weapon_level - 30) * 1.4 + 96.1)
                                self.stat_amount += self.cd
                            else:
                                self.cd += ((weapon_level - 40) * 0.99 + 110.1)
                                self.stat_amount += self.cd
                        elif weapon_stat == "Crit Rate":
                            self.cr += ((weapon_level - 30) * ((24 - 17.7) / 49) + 21.4285714286)
                            self.stat_amount += self.cr
                        else:
                            self.exp += ((weapon_level - 30) * 0.2 + 16.0)
                            self.stat_amount += self.exp
            # Emblem
            if weapon_emblem == "Crit DMG":
                self.emblem_amount += emblem_cd_stats[weapon_emblem_level]
                self.cd += self.emblem_amount
            elif weapon_emblem == "Boss ATK":
                self.emblem_amount += emblem_ba_stats[weapon_emblem_level]
                self.batk += self.emblem_amount
            else:
                self.emblem_amount += emblem_atk_stats[weapon_emblem_level]
                self.atkp += self.emblem_amount

            # Potential
            self.cd += 18

            # Flames
            self.atklinecount += 2

            # Set Effects
            if weapon_type == "Mythic Empress":
                self.mempsetcount += 1
            elif weapon_type == "Ancient Empress":
                self.aempsetcount += 1
            elif weapon_type == "Fafnir":
                self.fafsetcount += 1

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
