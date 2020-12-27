import streamlit as st


class Earring:
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

        with st.beta_expander("Earrings"):
            earring_list = st.selectbox("Choose an Earring", ["Horntail Earring (Legendary)", "Horntail Earring (Unique)"])
            self.type = earring_list
            _, earring1, _ = st.beta_columns([0.02, 0.96, 0.02])
            if "Horntail Earring (Unique)" in [earring_list]:
                # Base
                self.hp += 120
                self.mp += 60
                self.cratk += 30
                self.cd += 1
                earring_sf_level = earring1.slider(f"Horntail Earring (Unique) SF Level", min_value=0, max_value=5)
                self.sf = earring_sf_level
                # SF
                self.hp += earring_sf_level * 120
                self.mp += earring_sf_level * 60
                self.cratk += earring_sf_level * 6
                self.cd += earring_sf_level * 0.2
                # Emblem
                if earring_sf_level == 5:
                    earring_emblem = earring1.radio(f"Choose Horntail Earring (Unique) Emblem Stat", ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                    earring_emblem_level = 1
                    self.emblem = earring_emblem
                    self.emblem_level = earring_emblem_level
                    self.unique_acc_emb += 1
                    # Emblem
                    if earring_emblem == "Crit DMG":
                        self.emblem_amount += emblem_cd_stats[earring_emblem_level]
                        self.emblem_cd += self.emblem_amount
                    elif earring_emblem == "Boss ATK":
                        self.emblem_amount += emblem_ba_stats[earring_emblem_level]
                        self.emblem_batk += self.emblem_amount
                    else:
                        self.emblem_amount += emblem_atk_stats[earring_emblem_level]
                        self.emblem_atkp += self.emblem_amount
                # Potential
                self.batk += 4.5
                # Set
                self.bosssetcount += 1
            elif "Horntail Earring (Legendary)" in [earring_list]:
                # Base
                self.hp += 230
                self.mp += 120
                self.cratk += 40
                self.cd += 1.2
                earring_sf_level = earring1.slider(f"Horntail Earring (Legendary) SF Level", min_value=0, max_value=5)
                self.sf = earring_sf_level
                # SF
                self.hp += earring_sf_level * 230
                self.mp += earring_sf_level * 120
                self.cratk += earring_sf_level * 8
                self.cd += earring_sf_level * 0.3
                # Emblem
                if earring_sf_level == 5:
                    earring_emblem = earring1.radio(f"Choose Horntail Earring (Legendary) Emblem Stat",
                                                    ["Crit DMG", "Boss ATK", "Phy/Mag ATK"])
                    earring_emblem_level = earring1.slider("Horntail Earring (Legendary) Emblem Level", min_value=1, max_value=5)
                    self.emblem = earring_emblem
                    self.emblem_level = earring_emblem_level
                    self.legendary_acc_emb += 1
                    # Emblem
                    if earring_emblem == "Crit DMG":
                        self.emblem_amount += emblem_cd_stats[earring_emblem_level]
                        self.emblem_cd += self.emblem_amount
                    elif earring_emblem == "Boss ATK":
                        self.emblem_amount += emblem_ba_stats[earring_emblem_level]
                        self.emblem_batk += self.emblem_amount
                    else:
                        self.emblem_amount += emblem_atk_stats[earring_emblem_level]
                        self.emblem_atkp += self.emblem_amount
                # Potential
                self.batk += 4.5
                # Set
                self.bosssetcount += 1
