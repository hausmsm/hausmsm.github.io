import streamlit as st


class Ring:
    def __init__(self):
        # Unique To Rings
        self.ring1 = "None"
        self.ring2 = "None"
        self.ring3 = "None"
        self.ring4 = "None"
        self.ring1_flag = 0
        self.ring2_flag = 0
        self.ring3_flag = 0

        # Emblem Visualization
        self.ring1_emblem = "None"
        self.ring1_emblem_amount = 0
        self.ring1_emblem_level = 0

        self.ring2_emblem = "None"
        self.ring2_emblem_amount = 0
        self.ring2_emblem_level = 0

        self.ring3_emblem = "None"
        self.ring3_emblem_amount = 0
        self.ring3_emblem_level = 0

        self.ring4_emblem = "None"
        self.ring4_emblem_amount = 0
        self.ring4_emblem_level = 0

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
        self.ring1_sf = 0
        self.ring2_sf = 0
        self.ring3_sf = 0
        self.ring4_sf = 0
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

        with st.beta_expander("Rings"):
            ring = st.multiselect("Choose 4 Rings", ["Cygnus Ring (Unique)", "Cygnus Ring (Legendary)",
                                                     "Horntail Ring (Legendary)", "Horntail Ring (Unique)",
                                                     "Kerning Tower 50F Ring", "Kerning M Ring", "Attendance Ring",
                                                     "Ifia's Ring", "Noble Ifia's Ring", "Master Soul Ring SS"])
            self.ring_amount = len(ring)
            if len(ring) == 4:
                _, ring1, _, ring2, _, ring3, _, ring4, _ = st.beta_columns([0.02, 0.235, 0.02, 0.235, 0.02, 0.235, 0.02, 0.235, 0.02])
# Cygnus Ring (Unique)
                if "Cygnus Ring (Unique)" in [ring[0], ring[1], ring[2], ring[3]]:
                    # Base
                    self.hp += 120
                    self.mp += 60
                    self.pdefdec += 1.2
                    self.mdefdec += 1.2
                    if self.ring1_flag == 0:
                        self.ring1 = "Cygnus Ring (Unique)"
                        ring1_sf_level = ring1.slider(f"Cygnus Ring (Unique) SF Level", min_value=0, max_value=5)
                        self.ring1_sf = ring1_sf_level
                        # SF
                        self.hp += ring1_sf_level * 120
                        self.mp += ring1_sf_level * 60
                        self.pdefdec += ring1_sf_level * 0.3
                        self.mdefdec += ring1_sf_level * 0.3
                        # Emblem
                        if ring1_sf_level == 5:
                            ring1_emblem = ring1.radio(f"Choose Cygnus Ring (Unique) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring1_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.ring1_emblem = ring1_emblem
                            self.ring1_emblem_level = ring1_emblem_level
                            # Emblem
                            if ring1_emblem == "Crit DMG":
                                self.ring1_emblem_amount += emblem_cd_stats[ring1_emblem_level]
                                self.emblem_cd += self.ring1_emblem_amount
                            elif ring1_emblem == "Boss ATK":
                                self.ring1_emblem_amount += emblem_ba_stats[ring1_emblem_level]
                                self.emblem_batk += self.ring1_emblem_amount
                            else:
                                self.ring1_emblem_amount += emblem_atk_stats[ring1_emblem_level]
                                self.emblem_atkp += self.ring1_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
                        self.ring1_flag = 1
                    elif self.ring2_flag == 0:
                        self.ring2 = "Cygnus Ring (Unique)"
                        ring2_sf_level = ring2.slider(f"Cygnus Ring (Unique) SF Level", min_value=0, max_value=5)
                        self.ring2_sf = ring2_sf_level
                        # SF
                        self.hp += ring2_sf_level * 120
                        self.mp += ring2_sf_level * 60
                        self.pdefdec += ring2_sf_level * 0.3
                        self.mdefdec += ring2_sf_level * 0.3
                        # Emblem
                        if ring2_sf_level == 5:
                            ring2_emblem = ring2.radio(f"Choose Cygnus Ring (Unique) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring2_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.ring2_emblem = ring2_emblem
                            self.ring2_emblem_level = ring2_emblem_level
                            # Emblem
                            if ring2_emblem == "Crit DMG":
                                self.ring2_emblem_amount += emblem_cd_stats[ring2_emblem_level]
                                self.emblem_cd += self.ring2_emblem_amount
                            elif ring2_emblem == "Boss ATK":
                                self.ring2_emblem_amount += emblem_ba_stats[ring2_emblem_level]
                                self.emblem_batk += self.ring2_emblem_amount
                            else:
                                self.ring2_emblem_amount += emblem_atk_stats[ring2_emblem_level]
                                self.emblem_atkp += self.ring2_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
                        self.ring2_flag = 1
                    elif self.ring3_flag == 0:
                        self.ring3 = "Cygnus Ring (Unique)"
                        ring3_sf_level = ring3.slider(f"Cygnus Ring (Unique) SF Level", min_value=0, max_value=5)
                        self.ring3_sf = ring3_sf_level
                        # SF
                        self.hp += ring3_sf_level * 120
                        self.mp += ring3_sf_level * 60
                        self.pdefdec += ring3_sf_level * 0.3
                        self.mdefdec += ring3_sf_level * 0.3
                        # Emblem
                        if ring3_sf_level == 5:
                            ring3_emblem = ring3.radio(f"Choose Cygnus Ring (Unique) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring3_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.ring3_emblem = ring3_emblem
                            self.ring3_emblem_level = ring3_emblem_level
                            # Emblem
                            if ring3_emblem == "Crit DMG":
                                self.ring3_emblem_amount += emblem_cd_stats[ring3_emblem_level]
                                self.emblem_cd += self.ring3_emblem_amount
                            elif ring3_emblem == "Boss ATK":
                                self.ring3_emblem_amount += emblem_ba_stats[ring3_emblem_level]
                                self.emblem_batk += self.ring3_emblem_amount
                            else:
                                self.ring3_emblem_amount += emblem_atk_stats[ring3_emblem_level]
                                self.emblem_atkp += self.ring3_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
                        self.ring3_flag = 1
                    else:
                        self.ring4 = "Cygnus Ring (Unique)"
                        ring4_sf_level = ring4.slider(f"Cygnus Ring (Unique) SF Level", min_value=0, max_value=5)
                        self.ring3_sf = ring4_sf_level
                        # SF
                        self.hp += ring4_sf_level * 120
                        self.mp += ring4_sf_level * 60
                        self.pdefdec += ring4_sf_level * 0.3
                        self.mdefdec += ring4_sf_level * 0.3
                        # Emblem
                        if ring4_sf_level == 5:
                            ring4_emblem = ring4.radio(f"Choose Cygnus Ring (Unique) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring4_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.ring4_emblem = ring4_emblem
                            self.ring4_emblem_level = ring4_emblem_level
                            # Emblem
                            if ring4_emblem == "Crit DMG":
                                self.ring4_emblem_amount += emblem_cd_stats[ring4_emblem_level]
                                self.emblem_cd += self.ring3_emblem_amount
                            elif ring4_emblem == "Boss ATK":
                                self.ring4_emblem_amount += emblem_ba_stats[ring4_emblem_level]
                                self.emblem_batk += self.ring3_emblem_amount
                            else:
                                self.ring4_emblem_amount += emblem_atk_stats[ring4_emblem_level]
                                self.emblem_atkp += self.ring4_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
# Cygnus Ring (Legendary)
                if "Cygnus Ring (Legendary)" in [ring[0], ring[1], ring[2], ring[3]]:
                    # Base
                    self.hp += 230
                    self.mp += 120
                    self.pdefdec += 1.6
                    self.mdefdec += 1.6
                    if self.ring1_flag == 0:
                        self.ring1 = "Cygnus Ring (Legendary)"
                        ring1_sf_level = ring1.slider(f"Cygnus Ring (Legendary) SF Level", min_value=0, max_value=5)
                        self.ring1_sf = ring1_sf_level
                        # SF
                        self.hp += ring1_sf_level * 230
                        self.mp += ring1_sf_level * 120
                        self.pdefdec += ring1_sf_level * 0.4
                        self.mdefdec += ring1_sf_level * 0.4
                        # Emblem
                        if ring1_sf_level == 5:
                            ring1_emblem = ring1.radio(f"Choose Cygnus Ring (Legendary) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring1_emblem_level = ring1.slider("Cygnus Ring (Legendary) Emblem Level",
                                                              min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.ring1_emblem = ring1_emblem
                            self.ring1_emblem_level = ring1_emblem_level
                            # Emblem
                            if ring1_emblem == "Crit DMG":
                                self.ring1_emblem_amount += emblem_cd_stats[ring1_emblem_level]
                                self.emblem_cd += self.ring1_emblem_amount
                            elif ring1_emblem == "Boss ATK":
                                self.ring1_emblem_amount += emblem_ba_stats[ring1_emblem_level]
                                self.emblem_batk += self.ring1_emblem_amount
                            else:
                                self.ring1_emblem_amount += emblem_atk_stats[ring1_emblem_level]
                                self.emblem_atkp += self.ring1_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
                        self.ring1_flag = 1
                    elif self.ring2_flag == 0:
                        self.ring2 = "Cygnus Ring (Legendary)"
                        ring2_sf_level = ring2.slider(f"Cygnus Ring (Legendary) SF Level", min_value=0, max_value=5)
                        self.ring2_sf = ring2_sf_level
                        # SF
                        self.hp += ring2_sf_level * 230
                        self.mp += ring2_sf_level * 120
                        self.pdefdec += ring2_sf_level * 0.4
                        self.mdefdec += ring2_sf_level * 0.4
                        # Emblem
                        if ring2_sf_level == 5:
                            ring2_emblem = ring2.radio(f"Choose Cygnus Ring (Legendary) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring2_emblem_level = ring2.slider(f"Cygnus Ring (Legendary) Emblem Level",
                                                              min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.ring2_emblem = ring2_emblem
                            self.ring2_emblem_level = ring2_emblem_level
                            # Emblem
                            if ring2_emblem == "Crit DMG":
                                self.ring2_emblem_amount += emblem_cd_stats[ring2_emblem_level]
                                self.emblem_cd += self.ring2_emblem_amount
                            elif ring2_emblem == "Boss ATK":
                                self.ring2_emblem_amount += emblem_ba_stats[ring2_emblem_level]
                                self.emblem_batk += self.ring2_emblem_amount
                            else:
                                self.ring2_emblem_amount += emblem_atk_stats[ring2_emblem_level]
                                self.emblem_atkp += self.ring2_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
                        self.ring2_flag = 1
                    elif self.ring3_flag == 0:
                        self.ring3 = "Cygnus Ring (Legendary)"
                        ring3_sf_level = ring3.slider(f"Cygnus Ring (Legendary) SF Level", min_value=0, max_value=5)
                        self.ring3_sf = ring3_sf_level
                        # SF
                        self.hp += ring3_sf_level * 240
                        self.mp += ring3_sf_level * 120
                        self.pdefdec += ring3_sf_level * 0.4
                        self.mdefdec += ring3_sf_level * 0.4
                        # Emblem
                        if ring3_sf_level == 5:
                            ring3_emblem = ring3.radio(f"Choose Cygnus Ring (Legendary) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring3_emblem_level = ring3.slider("Cygnus Ring (Legendary) Emblem Level",
                                                              min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.ring3_emblem = ring3_emblem
                            self.ring3_emblem_level = ring3_emblem_level
                            # Emblem
                            if ring3_emblem == "Crit DMG":
                                self.ring3_emblem_amount += emblem_cd_stats[ring3_emblem_level]
                                self.emblem_cd += self.ring3_emblem_amount
                            elif ring3_emblem == "Boss ATK":
                                self.ring3_emblem_amount += emblem_ba_stats[ring3_emblem_level]
                                self.emblem_batk += self.ring3_emblem_amount
                            else:
                                self.ring3_emblem_amount += emblem_atk_stats[ring3_emblem_level]
                                self.emblem_atkp += self.ring3_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
                        self.ring3_flag = 1
                    else:
                        self.ring4 = "Cygnus Ring (Legendary)"
                        ring4_sf_level = ring4.slider(f"Cygnus Ring (Legendary) SF Level", min_value=0, max_value=5)
                        self.ring3_sf = ring4_sf_level
                        # SF
                        self.hp += ring4_sf_level * 230
                        self.mp += ring4_sf_level * 120
                        self.pdefdec += ring4_sf_level * 0.4
                        self.mdefdec += ring4_sf_level * 0.4
                        # Emblem
                        if ring4_sf_level == 5:
                            ring4_emblem = ring4.radio(f"Choose Cygnus Ring (Legendary) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring4_emblem_level = ring4.slider("Cygnus Ring (Legendary) Emblem Level",
                                                              min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.ring4_emblem = ring4_emblem
                            self.ring4_emblem_level = ring4_emblem_level
                            # Emblem
                            if ring4_emblem == "Crit DMG":
                                self.ring4_emblem_amount += emblem_cd_stats[ring4_emblem_level]
                                self.emblem_cd += self.ring3_emblem_amount
                            elif ring4_emblem == "Boss ATK":
                                self.ring4_emblem_amount += emblem_ba_stats[ring4_emblem_level]
                                self.emblem_batk += self.ring3_emblem_amount
                            else:
                                self.ring4_emblem_amount += emblem_atk_stats[ring4_emblem_level]
                                self.emblem_atkp += self.ring4_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
# Horntail Ring (Unique)
                if "Horntail Ring (Unique)" in [ring[0], ring[1], ring[2], ring[3]]:
                    # Base
                    self.hp += 120
                    self.mp += 60
                    self.pdefdec += 1.2
                    self.mdefdec += 1.2
                    if self.ring1_flag == 0:
                        self.ring1 = "Horntail Ring (Unique)"
                        ring1_sf_level = ring1.slider(f"Horntail Ring (Unique) SF Level", min_value=0,
                                                      max_value=5)
                        self.ring1_sf = ring1_sf_level
                        # SF
                        self.hp += ring1_sf_level * 120
                        self.mp += ring1_sf_level * 60
                        self.pdefdec += ring1_sf_level * 0.3
                        self.mdefdec += ring1_sf_level * 0.3
                        # Emblem
                        if ring1_sf_level == 5:
                            ring1_emblem = ring1.radio(f"Choose Horntail Ring (Unique) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring1_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.ring1_emblem = ring1_emblem
                            self.ring1_emblem_level = ring1_emblem_level
                            # Emblem
                            if ring1_emblem == "Crit DMG":
                                self.ring1_emblem_amount += emblem_cd_stats[ring1_emblem_level]
                                self.emblem_cd += self.ring1_emblem_amount
                            elif ring1_emblem == "Boss ATK":
                                self.ring1_emblem_amount += emblem_ba_stats[ring1_emblem_level]
                                self.emblem_batk += self.ring1_emblem_amount
                            else:
                                self.ring1_emblem_amount += emblem_atk_stats[ring1_emblem_level]
                                self.emblem_atkp += self.ring1_emblem_amount
                                # Potential
                                self.atk += 69
                                # Set
                                self.bosssetcount += 1
                                self.ring1_flag = 1
                    elif self.ring2_flag == 0:
                        self.ring2 = "Horntail Ring (Unique)"
                        ring2_sf_level = ring2.slider(f"Horntail Ring (Unique) SF Level", min_value=0, max_value=5)
                        self.ring2_sf = ring2_sf_level
                        # SF
                        self.hp += ring2_sf_level * 120
                        self.mp += ring2_sf_level * 60
                        self.pdefdec += ring2_sf_level * 0.3
                        self.mdefdec += ring2_sf_level * 0.3
                        # Emblem
                        if ring2_sf_level == 5:
                            ring2_emblem = ring2.radio(f"Choose Horntail Ring (Unique) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring2_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.ring2_emblem = ring2_emblem
                            self.ring2_emblem_level = ring2_emblem_level
                            # Emblem
                            if ring2_emblem == "Crit DMG":
                                self.ring2_emblem_amount += emblem_cd_stats[ring2_emblem_level]
                                self.emblem_cd += self.ring2_emblem_amount
                            elif ring2_emblem == "Boss ATK":
                                self.ring2_emblem_amount += emblem_ba_stats[ring2_emblem_level]
                                self.emblem_batk += self.ring2_emblem_amount
                            else:
                                self.ring2_emblem_amount += emblem_atk_stats[ring2_emblem_level]
                                self.emblem_atkp += self.ring2_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
                        self.ring2_flag = 1
                    elif self.ring3_flag == 0:
                        self.ring3 = "Horntail Ring (Unique)"
                        ring3_sf_level = ring3.slider(f"Horntail Ring (Unique) SF Level", min_value=0, max_value=5)
                        self.ring3_sf = ring3_sf_level
                        # SF
                        self.hp += ring3_sf_level * 120
                        self.mp += ring3_sf_level * 60
                        self.pdefdec += ring3_sf_level * 0.3
                        self.mdefdec += ring3_sf_level * 0.3
                        # Emblem
                        if ring3_sf_level == 5:
                            ring3_emblem = ring3.radio(f"Choose Horntail Ring (Unique) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring3_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.ring3_emblem = ring3_emblem
                            self.ring3_emblem_level = ring3_emblem_level
                            # Emblem
                            if ring3_emblem == "Crit DMG":
                                self.ring3_emblem_amount += emblem_cd_stats[ring3_emblem_level]
                                self.emblem_cd += self.ring3_emblem_amount
                            elif ring3_emblem == "Boss ATK":
                                self.ring3_emblem_amount += emblem_ba_stats[ring3_emblem_level]
                                self.emblem_batk += self.ring3_emblem_amount
                            else:
                                self.ring3_emblem_amount += emblem_atk_stats[ring3_emblem_level]
                                self.emblem_atkp += self.ring3_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
                        self.ring3_flag = 1
                    else:
                        self.ring4 = "Horntail Ring (Unique)"
                        ring4_sf_level = ring4.slider(f"Horntail Ring (Unique) SF Level", min_value=0, max_value=5)
                        self.ring3_sf = ring4_sf_level
                        # SF
                        self.hp += ring4_sf_level * 120
                        self.mp += ring4_sf_level * 60
                        self.pdefdec += ring4_sf_level * 0.3
                        self.mdefdec += ring4_sf_level * 0.3
                        # Emblem
                        if ring4_sf_level == 5:
                            ring4_emblem = ring4.radio(f"Choose Horntail Ring (Unique) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring4_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.ring4_emblem = ring4_emblem
                            self.ring4_emblem_level = ring4_emblem_level
                            # Emblem
                            if ring4_emblem == "Crit DMG":
                                self.ring4_emblem_amount += emblem_cd_stats[ring4_emblem_level]
                                self.emblem_cd += self.ring3_emblem_amount
                            elif ring4_emblem == "Boss ATK":
                                self.ring4_emblem_amount += emblem_ba_stats[ring4_emblem_level]
                                self.emblem_batk += self.ring3_emblem_amount
                            else:
                                self.ring4_emblem_amount += emblem_atk_stats[ring4_emblem_level]
                                self.emblem_atkp += self.ring4_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
# Horntail Ring (Legendary)
                if "Horntail Ring (Legendary)" in [ring[0], ring[1], ring[2], ring[3]]:
                    # Base
                    self.hp += 230
                    self.mp += 120
                    self.pdefdec += 1.5
                    self.mdefdec += 1.5
                    if self.ring1_flag == 0:
                        self.ring1 = "Horntail Ring (Legendary)"
                        ring1_sf_level = ring1.slider(f"Horntail Ring (Legendary) SF Level", min_value=0, max_value=5)
                        self.ring1_sf = ring1_sf_level
                        # SF
                        self.hp += ring1_sf_level * 230
                        self.mp += ring1_sf_level * 120
                        self.pdefdec += ring1_sf_level * 0.3
                        self.mdefdec += ring1_sf_level * 0.3
                        # Emblem
                        if ring1_sf_level == 5:
                            ring1_emblem = ring1.radio(f"Choose Horntail Ring (Legendary) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring1_emblem_level = ring1.slider("Horntail Ring (Legendary) Emblem Level", min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.ring1_emblem = ring1_emblem
                            self.ring1_emblem_level = ring1_emblem_level
                            # Emblem
                            if ring1_emblem == "Crit DMG":
                                self.ring1_emblem_amount += emblem_cd_stats[ring1_emblem_level]
                                self.emblem_cd += self.ring1_emblem_amount
                            elif ring1_emblem == "Boss ATK":
                                self.ring1_emblem_amount += emblem_ba_stats[ring1_emblem_level]
                                self.emblem_batk += self.ring1_emblem_amount
                            else:
                                self.ring1_emblem_amount += emblem_atk_stats[ring1_emblem_level]
                                self.emblem_atkp += self.ring1_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
                        self.ring1_flag = 1
                    elif self.ring2_flag == 0:
                        self.ring2 = "Horntail Ring (Legendary)"
                        ring2_sf_level = ring2.slider(f"Horntail Ring (Legendary) SF Level", min_value=0,
                                                      max_value=5)
                        self.ring2_sf = ring2_sf_level
                        # SF
                        self.hp += ring2_sf_level * 230
                        self.mp += ring2_sf_level * 120
                        self.pdefdec += ring2_sf_level * 0.3
                        self.mdefdec += ring2_sf_level * 0.3
                        # Emblem
                        if ring2_sf_level == 5:
                            ring2_emblem = ring2.radio(f"Choose Horntail Ring (Legendary) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring2_emblem_level = ring2.slider(f"Horntail Ring (Legendary) Emblem Level",
                                                              min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.ring2_emblem = ring2_emblem
                            self.ring2_emblem_level = ring2_emblem_level
                            # Emblem
                            if ring2_emblem == "Crit DMG":
                                self.ring2_emblem_amount += emblem_cd_stats[ring2_emblem_level]
                                self.emblem_cd += self.ring2_emblem_amount
                            elif ring2_emblem == "Boss ATK":
                                self.ring2_emblem_amount += emblem_ba_stats[ring2_emblem_level]
                                self.emblem_batk += self.ring2_emblem_amount
                            else:
                                self.ring2_emblem_amount += emblem_atk_stats[ring2_emblem_level]
                                self.emblem_atkp += self.ring2_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
                        self.ring2_flag = 1
                    elif self.ring3_flag == 0:
                        self.ring3 = "Horntail Ring (Legendary)"
                        ring3_sf_level = ring3.slider(f"Horntail Ring (Legendary) SF Level", min_value=0,
                                                      max_value=5)
                        self.ring3_sf = ring3_sf_level
                        # SF
                        self.hp += ring3_sf_level * 240
                        self.mp += ring3_sf_level * 120
                        self.pdefdec += ring3_sf_level * 0.3
                        self.mdefdec += ring3_sf_level * 0.3
                        # Emblem
                        if ring3_sf_level == 5:
                            ring3_emblem = ring3.radio(f"Choose Horntail Ring (Legendary) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring3_emblem_level = ring3.slider("Cygnus Ring (Legendary) Emblem Level",
                                                              min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.ring3_emblem = ring3_emblem
                            self.ring3_emblem_level = ring3_emblem_level
                            # Emblem
                            if ring3_emblem == "Crit DMG":
                                self.ring3_emblem_amount += emblem_cd_stats[ring3_emblem_level]
                                self.emblem_cd += self.ring3_emblem_amount
                            elif ring3_emblem == "Boss ATK":
                                self.ring3_emblem_amount += emblem_ba_stats[ring3_emblem_level]
                                self.emblem_batk += self.ring3_emblem_amount
                            else:
                                self.ring3_emblem_amount += emblem_atk_stats[ring3_emblem_level]
                                self.emblem_atkp += self.ring3_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
                        self.ring3_flag = 1
                    else:
                        self.ring4 = "Horntail Ring (Legendary)"
                        ring4_sf_level = ring4.slider(f"Horntail Ring (Legendary) SF Level", min_value=0,
                                                      max_value=5)
                        self.ring3_sf = ring4_sf_level
                        # SF
                        self.hp += ring4_sf_level * 230
                        self.mp += ring4_sf_level * 120
                        self.pdefdec += ring4_sf_level * 0.3
                        self.mdefdec += ring4_sf_level * 0.3
                        # Emblem
                        if ring4_sf_level == 5:
                            ring4_emblem = ring4.radio(f"Choose Horntail Ring (Legendary) Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring4_emblem_level = ring4.slider("Horntail Ring (Legendary) Emblem Level",
                                                              min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.ring4_emblem = ring4_emblem
                            self.ring4_emblem_level = ring4_emblem_level
                            # Emblem
                            if ring4_emblem == "Crit DMG":
                                self.ring4_emblem_amount += emblem_cd_stats[ring4_emblem_level]
                                self.emblem_cd += self.ring3_emblem_amount
                            elif ring4_emblem == "Boss ATK":
                                self.ring4_emblem_amount += emblem_ba_stats[ring4_emblem_level]
                                self.emblem_batk += self.ring3_emblem_amount
                            else:
                                self.ring4_emblem_amount += emblem_atk_stats[ring4_emblem_level]
                                self.emblem_atkp += self.ring4_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.bosssetcount += 1
# Kerning Tower 50F Ring
                if "Kerning Tower 50F Ring" in [ring[0], ring[1], ring[2], ring[3]]:
                    # Base
                    self.dmg += 10
                    if self.ring1_flag == 0:
                        self.ring1 = "Kerning Tower 50F Ring"
                        ring1.write("Kerning Tower 50F Ring")
                        self.ring1_flag = 1
                    elif self.ring2_flag == 0:
                        self.ring2 = "Kerning Tower 50F Ring"
                        ring2.write("Kerning Tower 50F Ring")
                        self.ring2_flag = 1
                    elif self.ring3_flag == 0:
                        self.ring3 = "Kerning Tower 50F Ring"
                        ring3.write("Kerning Tower 50F Ring")
                        self.ring3_flag = 1
                    else:
                        self.ring4 = "Kerning Tower 50F Ring"
                        ring4.write("Kerning Tower 50F Ring")
# Kerning M Ring
                if "Kerning M Ring" in [ring[0], ring[1], ring[2], ring[3]]:
                    # Base
                    self.exp += 15
                    if self.ring1_flag == 0:
                        self.ring1 = "Kerning M Ring"
                        ring1.write("Kerning M Ring")
                        self.ring1_flag = 1
                    elif self.ring2_flag == 0:
                        self.ring2 = "Kerning M Ring"
                        ring2.write("Kerning M Ring")
                        self.ring2_flag = 1
                    elif self.ring3_flag == 0:
                        self.ring3 = "Kerning M Ring"
                        ring3.write("Kerning M Ring")
                        self.ring3_flag = 1
                    else:
                        self.ring4 = "Kerning M Ring"
                        ring4.write("Kerning M Ring")
# Attendance Ring
                if "Attendance Ring" in [ring[0], ring[1], ring[2], ring[3]]:
                    # Base
                    self.hp += 200
                    self.mp += 100
                    self.atk += 200
                    self.pdef += 400
                    self.mdef += 400
                    if self.ring1_flag == 0:
                        self.ring1 = "Attendance Ring"
                        ring1.write("Attendance Ring")
                        self.ring1_flag = 1
                    elif self.ring2_flag == 0:
                        self.ring2 = "Attendance Ring"
                        ring2.write("Attendance Ring")
                        self.ring2_flag = 1
                    elif self.ring3_flag == 0:
                        self.ring3 = "Attendance Ring"
                        ring3.write("Attendance Ring")
                        self.ring3_flag = 1
                    else:
                        self.ring4 = "Attendance Ring"
                        ring4.write("Attendance Ring")
# Master Soul SS Ring
                if "Master Soul SS Ring" in [ring[0], ring[1], ring[2], ring[3]]:
                    # Base
                    self.atk += 150
                    self.pdef += 300
                    self.mdef += 300
                    if self.ring1_flag == 0:
                        self.ring1 = "Master Soul SS Ring"
                        ring1.write("Master Soul SS Ring")
                        self.ring1_flag = 1
                    elif self.ring2_flag == 0:
                        self.ring2 = "Master Soul SS Ring"
                        ring2.write("Master Soul SS Ring")
                        self.ring2_flag = 1
                    elif self.ring3_flag == 0:
                        self.ring3 = "Master Soul SS Ring"
                        ring3.write("Master Soul SS Ring")
                        self.ring3_flag = 1
                    else:
                        self.ring4 = "Master Soul SS Ring"
                        ring4.write("Master Soul SS Ring")
                    # Potential
                    self.atk += 69
# Ifia's Ring
                if "Ifia's Ring" in [ring[0], ring[1], ring[2], ring[3]]:
                    # Base
                    self.atkp += 1
                    if self.ring1_flag == 0:
                        self.ring1 = "Ifia's Ring"
                        ring1_sf_level = ring1.slider(f"Ifia's Ring SF Level", min_value=0,
                                                      max_value=5)
                        self.ring1_sf = ring1_sf_level
                        # SF
                        self.atk += ring1_sf_level * 0.2
                        # Emblem
                        if ring1_sf_level == 5:
                            ring1_emblem = ring1.radio(f"Choose Ifia's Ring Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring1_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.ring1_emblem = ring1_emblem
                            self.ring1_emblem_level = ring1_emblem_level
                            # Emblem
                            if ring1_emblem == "Crit DMG":
                                self.ring1_emblem_amount += emblem_cd_stats[ring1_emblem_level]
                                self.emblem_cd += self.ring1_emblem_amount
                            elif ring1_emblem == "Boss ATK":
                                self.ring1_emblem_amount += emblem_ba_stats[ring1_emblem_level]
                                self.emblem_batk += self.ring1_emblem_amount
                            else:
                                self.ring1_emblem_amount += emblem_atk_stats[ring1_emblem_level]
                                self.emblem_atkp += self.ring1_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.ring1_flag = 1
                    elif self.ring2_flag == 0:
                        self.ring2 = "Ifia's Ring"
                        ring2_sf_level = ring2.slider(f"Ifia's Ring SF Level", min_value=0,
                                                      max_value=5)
                        self.ring2_sf = ring2_sf_level
                        # SF
                        self.atkp += ring2_sf_level * 0.2
                        # Emblem
                        if ring2_sf_level == 5:
                            ring2_emblem = ring2.radio(f"Choose Ifia's Ring Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring2_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.ring2_emblem = ring2_emblem
                            self.ring2_emblem_level = ring2_emblem_level
                            # Emblem
                            if ring2_emblem == "Crit DMG":
                                self.ring2_emblem_amount += emblem_cd_stats[ring2_emblem_level]
                                self.emblem_cd += self.ring2_emblem_amount
                            elif ring2_emblem == "Boss ATK":
                                self.ring2_emblem_amount += emblem_ba_stats[ring2_emblem_level]
                                self.emblem_batk += self.ring2_emblem_amount
                            else:
                                self.ring2_emblem_amount += emblem_atk_stats[ring2_emblem_level]
                                self.emblem_atkp += self.ring2_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.ring2_flag = 1
                    elif self.ring3_flag == 0:
                        self.ring3 = "Ifia's Ring"
                        ring3_sf_level = ring3.slider(f"Ifia's Ring SF Level", min_value=0,
                                                      max_value=5)
                        self.ring3_sf = ring3_sf_level
                        # SF
                        self.atkp += ring3_sf_level * 0.2
                        # Emblem
                        if ring3_sf_level == 5:
                            ring3_emblem = ring3.radio(f"Choose Ifia's Ring Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring3_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.ring3_emblem = ring3_emblem
                            self.ring3_emblem_level = ring3_emblem_level
                            # Emblem
                            if ring3_emblem == "Crit DMG":
                                self.ring3_emblem_amount += emblem_cd_stats[ring3_emblem_level]
                                self.emblem_cd += self.ring3_emblem_amount
                            elif ring3_emblem == "Boss ATK":
                                self.ring3_emblem_amount += emblem_ba_stats[ring3_emblem_level]
                                self.emblem_batk += self.ring3_emblem_amount
                            else:
                                self.ring3_emblem_amount += emblem_atk_stats[ring3_emblem_level]
                                self.emblem_atkp += self.ring3_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.ring3_flag = 1
                    else:
                        self.ring4 = "Ifia's Ring"
                        ring4_sf_level = ring4.slider(f"Ifia's Ring SF Level", min_value=0,
                                                      max_value=5)
                        self.ring3_sf = ring4_sf_level
                        # SF
                        self.atkp += ring4_sf_level * 0.2
                        # Emblem
                        if ring4_sf_level == 5:
                            ring4_emblem = ring4.radio(f"Choose Ifia's Ring Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring4_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.ring4_emblem = ring4_emblem
                            self.ring4_emblem_level = ring4_emblem_level
                            # Emblem
                            if ring4_emblem == "Crit DMG":
                                self.ring4_emblem_amount += emblem_cd_stats[ring4_emblem_level]
                                self.emblem_cd += self.ring3_emblem_amount
                            elif ring4_emblem == "Boss ATK":
                                self.ring4_emblem_amount += emblem_ba_stats[ring4_emblem_level]
                                self.emblem_batk += self.ring3_emblem_amount
                            else:
                                self.ring4_emblem_amount += emblem_atk_stats[ring4_emblem_level]
                                self.emblem_atkp += self.ring4_emblem_amount
                        # Potential
                        self.atk += 69
# Noble Ifia's Ring
                if "Noble Ifia's Ring" in [ring[0], ring[1], ring[2], ring[3]]:
                    # Base
                    self.atkp += 2
                    if self.ring1_flag == 0:
                        self.ring1 = "Noble Ifia's Ring"
                        ring1_sf_level = ring1.slider(f"Noble Ifia's Ring SF Level", min_value=0,
                                                      max_value=5)
                        self.ring1_sf = ring1_sf_level
                        # SF
                        self.atk += ring1_sf_level * 0.4
                        # Emblem
                        if ring1_sf_level == 5:
                            ring1_emblem = ring1.radio(f"Choose Noble Ifia's Ring Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring1_emblem_level = ring1.slider("Noble Ifia's Ring Emblem Level", min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.ring1_emblem = ring1_emblem
                            self.ring1_emblem_level = ring1_emblem_level
                            # Emblem
                            if ring1_emblem == "Crit DMG":
                                self.ring1_emblem_amount += emblem_cd_stats[ring1_emblem_level]
                                self.emblem_cd += self.ring1_emblem_amount
                            elif ring1_emblem == "Boss ATK":
                                self.ring1_emblem_amount += emblem_ba_stats[ring1_emblem_level]
                                self.emblem_batk += self.ring1_emblem_amount
                            else:
                                self.ring1_emblem_amount += emblem_atk_stats[ring1_emblem_level]
                                self.emblem_atkp += self.ring1_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.commandersetcount += 1
                        self.ring1_flag = 1
                    elif self.ring2_flag == 0:
                        self.ring2 = "Noble Ifia's Ring"
                        ring2_sf_level = ring2.slider(f"Noble Ifia's Ring SF Level", min_value=0,
                                                      max_value=5)
                        self.ring2_sf = ring2_sf_level
                        # SF
                        self.atkp += ring2_sf_level * 0.4
                        # Emblem
                        if ring2_sf_level == 5:
                            ring2_emblem = ring2.radio(f"Choose Noble Ifia's Ring Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring2_emblem_level = ring2.slider("Noble Ifia's Ring Emblem Level", min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.ring2_emblem = ring2_emblem
                            self.ring2_emblem_level = ring2_emblem_level
                            # Emblem
                            if ring2_emblem == "Crit DMG":
                                self.ring2_emblem_amount += emblem_cd_stats[ring2_emblem_level]
                                self.emblem_cd += self.ring2_emblem_amount
                            elif ring2_emblem == "Boss ATK":
                                self.ring2_emblem_amount += emblem_ba_stats[ring2_emblem_level]
                                self.emblem_batk += self.ring2_emblem_amount
                            else:
                                self.ring2_emblem_amount += emblem_atk_stats[ring2_emblem_level]
                                self.emblem_atkp += self.ring2_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.commandersetcount += 1
                        self.ring2_flag = 1
                    elif self.ring3_flag == 0:
                        self.ring3 = "Noble Ifia's Ring"
                        ring3_sf_level = ring3.slider(f"Noble Ifia's Ring SF Level", min_value=0,
                                                      max_value=5)
                        self.ring3_sf = ring3_sf_level
                        # SF
                        self.atkp += ring3_sf_level * 0.4
                        # Emblem
                        if ring3_sf_level == 5:
                            ring3_emblem = ring3.radio(f"Choose Noble Ifia's Ring Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring3_emblem_level = ring3.slider("Noble Ifia's Ring Emblem Level", min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.ring3_emblem = ring3_emblem
                            self.ring3_emblem_level = ring3_emblem_level
                            # Emblem
                            if ring3_emblem == "Crit DMG":
                                self.ring3_emblem_amount += emblem_cd_stats[ring3_emblem_level]
                                self.emblem_cd += self.ring3_emblem_amount
                            elif ring3_emblem == "Boss ATK":
                                self.ring3_emblem_amount += emblem_ba_stats[ring3_emblem_level]
                                self.emblem_batk += self.ring3_emblem_amount
                            else:
                                self.ring3_emblem_amount += emblem_atk_stats[ring3_emblem_level]
                                self.emblem_atkp += self.ring3_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.commandersetcount += 1
                        self.ring3_flag = 1
                    else:
                        self.ring4 = "Noble Ifia's Ring"
                        ring4_sf_level = ring4.slider(f"Noble Ifia's Ring SF Level", min_value=0,
                                                      max_value=5)
                        self.ring3_sf = ring4_sf_level
                        # SF
                        self.atkp += ring4_sf_level * 0.4
                        # Emblem
                        if ring4_sf_level == 5:
                            ring4_emblem = ring4.radio(f"Choose Noble Ifia's Ring Emblem Stat",
                                                       ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            ring4_emblem_level = ring4.slider("Noble Ifia's Ring Emblem Level", min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.ring4_emblem = ring4_emblem
                            self.ring4_emblem_level = ring4_emblem_level
                            # Emblem
                            if ring4_emblem == "Crit DMG":
                                self.ring4_emblem_amount += emblem_cd_stats[ring4_emblem_level]
                                self.emblem_cd += self.ring3_emblem_amount
                            elif ring4_emblem == "Boss ATK":
                                self.ring4_emblem_amount += emblem_ba_stats[ring4_emblem_level]
                                self.emblem_batk += self.ring3_emblem_amount
                            else:
                                self.ring4_emblem_amount += emblem_atk_stats[ring4_emblem_level]
                                self.emblem_atkp += self.ring4_emblem_amount
                        # Potential
                        self.atk += 69
                        # Set
                        self.commandersetcount += 1
                self.sf = self.ring1_sf + self.ring2_sf + self.ring3_sf + self.ring4_sf
            else:
                st.write("Error: Please Select 4 Rings Only")
            """print("\n")
            print(f"hp: {self.hp}")
            print(f"mp: {self.mp}")
            print(f"cratk: {self.cratk}")
            print(f"cd: {self.cd}")
            print(f"dmg: {self.dmg}")"""