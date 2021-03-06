import streamlit as st


class Secweapon:
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

        # User Input
        with st.beta_expander("Secondary Weapon"):
            _, swep1, _, swep2, _ = st.beta_columns([0.02, 0.47, 0.02, 0.47, 0.02])
            swep_type = swep1.selectbox("Choose Secondary Weapon Type", ["Normal Class Specific", "Longinus Spear"])
            swep_rank = swep2.selectbox("Choose Secondary Weapon Rank", ["Unique", "Legendary", "Mythic"])
            self.type = swep_type
            self.rank = swep_rank
            _, swep3, _ = st.beta_columns([0.02, 0.96, 0.02])
            if swep_type == "Longinus Spear":
                swep_level = swep3.slider('Sharenian Ability', min_value=1, max_value=10)
                self.swep_level = swep_level
            if swep_rank == "Unique":
                # Base
                self.atk += 502
                # SF
                swep_sf_level = swep3.slider("SWep SF Level", min_value=0, max_value=10)
                self.sf += swep_sf_level
                self.atk += int((swep_sf_level/10)*214)
                # Refinement
                if swep_type == "Longinus Spear":
                    self.atk += swep_level*1
                    if swep_level in [8, 9]:
                        self.fd += 1
                    if swep_level == 10:
                        self.fd += 1.5
                    if swep_level != 10:
                        self.batk += ((swep_level-1)*0.2 + 3)
                    else:
                        self.batk += 5

            elif swep_rank == "Legendary":
                # Base
                self.atk += 831
                # SF
                swep_sf_level = swep3.slider("SWep SF Level", min_value=0, max_value=12)
                self.sf += swep_sf_level
                self.atk += int((swep_sf_level/12) * 448)
                # Refinement
                if swep_type == "Longinus Spear":
                    self.atk += swep_level*5
                    if swep_level in [1, 2]:
                        self.fd += 0
                    elif swep_level in [3, 5]:
                        self.fd += 1
                    elif swep_level in [6, 7]:
                        self.fd += 1.5
                    elif swep_level in [8, 9]:
                        self.fd += 2
                    else:
                        self.fd += 3
                    if swep_level in [1, 2, 3, 4, 5, 6, 7]:
                        self.batk += ((swep_level-1)*0.5 + 4)
                    else:
                        self.batk += swep_level
            else:
                # Base
                self.atk += 1510
                # SF
                swep_sf_level = swep3.slider("SWep SF Level", min_value=0, max_value=15)
                self.sf += swep_sf_level
                self.atk += int((swep_sf_level/15) * 981)
                # Refinement
                if swep_type == "Longinus Spear":
                    self.atk += swep_level * 10
                    if swep_level in [1, 2]:
                        self.fd += 0
                    elif swep_level in [3, 5]:
                        self.fd += 2
                    elif swep_level in [6, 7]:
                        self.fd += 3
                    elif swep_level in [8, 9]:
                        self.fd += 4
                    else:
                        self.fd += 5
                    if swep_level in [1, 2, 3]:
                        self.batk += ((swep_level - 1) * 0.7 + 6)
                    elif swep_level in [4, 5]:
                        self.batk += ((swep_level - 3) * 0.8 + 7.4)
                    elif swep_level in [6]:
                        self.batk += 9.7
                    else:
                        self.batk += ((swep_level - 7) * 1.5 + 10.5)

            # Flame Stats
            self.atklinecount += 2

            # Potential
            if swep_rank == "Mythic":
                self.cd += 18
            else:
                self.cd += 15
            """print("\n")
            print(f"batk: {self.batk}")
            print(f"fd: {self.fd}")
            print(f"cd: {self.cd}")"""
