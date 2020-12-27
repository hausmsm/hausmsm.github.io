import streamlit as st


class Necklace:
    def __init__(self):
        # Initialize
        self.neck1_flag = 0

        # Emblem Visualization
        self.neck1_emblem = "None"
        self.neck1_emblem_amount = 0
        self.neck1_emblem_level = 0

        self.neck2_emblem = "None"
        self.neck2_emblem_amount = 0
        self.neck2_emblem_level = 0

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
        self.neck1_sf = 0
        self.neck2_sf = 0
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

        with st.beta_expander("Necklace"):
            necklaces = st.multiselect("Choose 2 Necklaces",
                                       ["Horntail Necklace (Unique)", "Horntail Necklace (Legendary)",
                                        "Mu Lung Dojo Pendant (Epic)", "Mu Lung Dojo Pendant (Unique)",
                                        "Ifia's Necklace", "Spigelmann's Necklace of Chaos"])
            self.neck_amount = len(necklaces)
            if len(necklaces) == 2:
                _, neck1, _, neck2, _ = st.beta_columns([0.02, 0.47, 0.02, 0.47, 0.02])
                if "Horntail Necklace (Unique)" in [necklaces[0], necklaces[1]]:
                    # Base
                    self.hp += 120
                    self.mp += 60
                    self.cratk += 45
                    self.cd += 2
                    if self.neck1_flag == 0:
                        self.neck1 = "Horntail Necklace (Unique)"
                        neck1_sf_level = neck1.slider(f"Horntail Necklace (Unique) SF Level", min_value=0, max_value=5)
                        self.neck1_sf = neck1_sf_level
                        # SF
                        self.hp += neck1_sf_level * 120
                        self.mp += neck1_sf_level * 60
                        self.cratk += neck1_sf_level * 9
                        self.cd += neck1_sf_level * 0.4
                        # Emblem
                        if neck1_sf_level == 5:
                            neck1_emblem = neck1.radio(f"Choose Horntail Necklace (Unique) Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            neck1_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.neck1_emblem = neck1_emblem
                            self.neck1_emblem_level = neck1_emblem_level
                            # Emblem
                            if neck1_emblem == "Crit DMG":
                                self.neck1_emblem_amount += emblem_cd_stats[neck1_emblem_level]
                                self.emblem_cd += self.neck1_emblem_amount
                            elif neck1_emblem == "Boss ATK":
                                self.neck1_emblem_amount += emblem_ba_stats[neck1_emblem_level]
                                self.emblem_batk += self.neck1_emblem_amount
                            else:
                                self.neck1_emblem_amount += emblem_atk_stats[neck1_emblem_level]
                                self.emblem_atkp += self.neck1_emblem_amount
                        # Potential
                        self.batk += 4.5
                        # Set
                        self.bosssetcount += 1
                        self.neck1_flag = 1
                    else:
                        self.neck2 = "Horntail Necklace (Unique)"
                        neck2_sf_level = neck2.slider(f"Horntail Necklace (Unique) SF Level", min_value=0, max_value=5)
                        self.neck2_sf = neck2_sf_level
                        # SF
                        self.hp += neck2_sf_level * 120
                        self.mp += neck2_sf_level * 60
                        self.cratk += neck2_sf_level * 9
                        self.cd += neck2_sf_level * 0.4
                        # Emblem
                        if neck2_sf_level == 5:
                            neck2_emblem = neck2.radio(f"Choose Horntail Necklace (Unique) Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            neck2_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.neck2_emblem = neck2_emblem
                            self.neck2_emblem_level = neck2_emblem_level
                            # Emblem
                            if neck2_emblem == "Crit DMG":
                                self.neck2_emblem_amount += emblem_cd_stats[neck2_emblem_level]
                                self.emblem_cd += self.neck2_emblem_amount
                            elif neck2_emblem == "Boss ATK":
                                self.neck2_emblem_amount += emblem_ba_stats[neck2_emblem_level]
                                self.emblem_batk += self.neck2_emblem_amount
                            else:
                                self.neck2_emblem_amount += emblem_atk_stats[neck2_emblem_level]
                                self.emblem_atkp += self.neck2_emblem_amount

                        # Potential
                        self.batk += 4.5
                        # Set
                        self.bosssetcount += 1
                if "Horntail Necklace (Legendary)" in [necklaces[0], necklaces[1]]:
                    # Base
                    self.hp += 230
                    self.mp += 120
                    self.cratk += 60
                    self.cd += 2.5
                    if self.neck1_flag == 0:
                        self.neck1 = "Horntail Necklace (Legendary)"
                        neck1_sf_level = neck1.slider(f"Horntail Necklace (Legendary) SF Level", min_value=0, max_value=5)
                        self.neck1_sf = neck1_sf_level
                        # SF
                        self.hp += neck1_sf_level * 230
                        self.mp += neck1_sf_level * 120
                        self.cratk += neck1_sf_level * 12
                        self.cd += neck1_sf_level * 0.5
                        # Emblem
                        if neck1_sf_level == 5:
                            neck1_emblem = neck1.radio(f"Choose Horntail Necklace (Legendary) Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            neck1_emblem_level = neck1.slider(f"Horntail Necklace (Legendary) Emblem Level", min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.neck1_emblem = neck1_emblem
                            self.neck1_emblem_level = neck1_emblem_level
                            # Emblem
                            if neck1_emblem == "Crit DMG":
                                self.neck1_emblem_amount += emblem_cd_stats[neck1_emblem_level]
                                self.emblem_cd += self.neck1_emblem_amount
                            elif neck1_emblem == "Boss ATK":
                                self.neck1_emblem_amount += emblem_ba_stats[neck1_emblem_level]
                                self.emblem_batk += self.neck1_emblem_amount
                            else:
                                self.neck1_emblem_amount += emblem_atk_stats[neck1_emblem_level]
                                self.emblem_atkp += self.neck1_emblem_amount
                        # Potential
                        self.batk += 4.5
                        # Set
                        self.bosssetcount += 1
                        self.neck1_flag = 1
                    else:
                        self.neck2 = "Horntail Necklace (Legendary)"
                        neck2_sf_level = neck2.slider(f"Horntail Necklace (Legendary) SF Level", min_value=0, max_value=5)
                        self.neck2_sf = neck2_sf_level
                        # SF
                        self.hp += neck2_sf_level * 230
                        self.mp += neck2_sf_level * 120
                        self.cratk += neck2_sf_level * 12
                        self.cd += neck2_sf_level * 0.5
                        # Emblem
                        if neck2_sf_level == 5:
                            neck2_emblem = neck2.radio(f"Choose Horntail Necklace (Legendary) Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            neck2_emblem_level = neck2.slider(f"Horntail Necklace (Legendary) Emblem Level", min_value=1, max_value=5)
                            self.legendary_acc_emb += 1
                            self.neck2_emblem = neck2_emblem
                            self.neck2_emblem_level = neck2_emblem_level
                            # Emblem
                            if neck2_emblem == "Crit DMG":
                                self.neck2_emblem_amount += emblem_cd_stats[neck2_emblem_level]
                                self.emblem_cd += self.neck2_emblem_amount
                            elif neck2_emblem == "Boss ATK":
                                self.neck2_emblem_amount += emblem_ba_stats[neck2_emblem_level]
                                self.emblem_batk += self.neck2_emblem_amount
                            else:
                                self.neck2_emblem_amount += emblem_atk_stats[neck2_emblem_level]
                                self.emblem_atkp += self.neck2_emblem_amount
                        # Potential
                        self.batk += 4.5
                        # Set
                        self.bosssetcount += 1
                if "Mu Lung Dojo Pendant (Epic)" in [necklaces[0], necklaces[1]]:
                    # Base
                    self.hp += 5
                    self.mp += 5
                    self.exp += 10
                    if self.neck1_flag == 0:
                        self.neck1 = "Mu Lung Dojo Pendant (Epic)"
                        self.neck1_flag = 1
                    else:
                        self.neck2 = "Mu Lung Dojo Pendant (Epic)"
                if "Mu Lung Dojo Pendant (Unique)" in [necklaces[0], necklaces[1]]:
                    # Base
                    self.hp += 5
                    self.mp += 5
                    self.exp += 15
                    if self.neck1_flag == 0:
                        self.neck1 = "Mu Lung Dojo Pendant (Unique)"
                        self.neck1_flag = 1
                    else:
                        self.neck2 = "Mu Lung Dojo Pendant (Unique)"
                if "Ifia's Necklace" in [necklaces[0], necklaces[1]]:
                    # Base
                    self.atkp += 1
                    if self.neck1_flag == 0:
                        self.neck1 = "Ifia's Necklace"
                        neck1_sf_level = neck1.slider(f"Ifia's Necklace SF Level", min_value=0, max_value=5)
                        self.neck1_sf = neck1_sf_level
                        # SF
                        self.atkp += neck1_sf_level * 0.2
                        # Emblem
                        if neck1_sf_level == 5:
                            neck1_emblem = neck1.radio(f"Choose Ifia's Necklace Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            neck1_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.neck1_emblem = neck1_emblem
                            self.neck1_emblem_level = neck1_emblem_level
                            # Emblem
                            if neck1_emblem == "Crit DMG":
                                self.neck1_emblem_amount += emblem_cd_stats[neck1_emblem_level]
                                self.emblem_cd += self.neck1_emblem_amount
                            elif neck1_emblem == "Boss ATK":
                                self.neck1_emblem_amount += emblem_ba_stats[neck1_emblem_level]
                                self.emblem_batk += self.neck1_emblem_amount
                            else:
                                self.neck1_emblem_amount += emblem_atk_stats[neck1_emblem_level]
                                self.emblem_atkp += self.neck1_emblem_amount
                        # Potential
                        self.batk += 4.5

                        self.neck1_flag = 1
                    else:
                        self.neck2 = "Ifia's Necklace"
                        neck2_sf_level = neck2.slider(f"Ifia's Necklace SF Level", min_value=0, max_value=5)
                        self.neck2_sf = neck2_sf_level
                        # SF
                        self.atkp += neck2_sf_level * 0.2
                        # Emblem
                        if neck2_sf_level == 5:
                            neck2_emblem = neck2.radio(f"Choose Ifia's Necklace Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                            neck2_emblem_level = 1
                            self.unique_acc_emb += 1
                            self.neck2_emblem = neck2_emblem
                            self.neck2_emblem_level = neck2_emblem_level
                            # Emblem
                            if neck2_emblem == "Crit DMG":
                                self.neck2_emblem_amount += emblem_cd_stats[neck2_emblem_level]
                                self.emblem_cd += self.neck2_emblem_amount
                            elif neck2_emblem == "Boss ATK":
                                self.neck2_emblem_amount += emblem_ba_stats[neck2_emblem_level]
                                self.emblem_batk += self.neck2_emblem_amount
                            else:
                                self.neck2_emblem_amount += emblem_atk_stats[neck2_emblem_level]
                                self.emblem_atkp += self.neck2_emblem_amount
                        # Potential
                        self.batk += 4.5

                if "Spiegelmann's Necklace of Chaos" in [necklaces[0], necklaces[1]]:
                    # Base
                    self.hp += 120
                    self.mp += 60
                    self.cd += 3
                    if self.neck1_flag == 0:
                        self.neck1 = "Spiegelmann's Necklace of Chaos"
                        self.neck1_flag = 1
                    else:
                        self.neck2 = "Spiegelmann's Necklace of Chaos"
                    # Potential
                    self.batk += 4.5
                self.sf = self.neck1_sf + self.neck2_sf
            else:
                st.write("Error: Please Select 2 Necklaces Only")
