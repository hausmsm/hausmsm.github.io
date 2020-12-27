import streamlit as st


class Soul:
    def __init__(self, character_type):
        # Initialize
        self.vonbonpierrecount = 0
        self.crimsonqueencount = 0
        self.vellumcount = 0
        self.vonleoncount = 0

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

        with st.beta_expander("Soul"):
            _, soul1, _, soul2, _ = st.beta_columns([0.02, 0.47, 0.02, 0.47, 0.02])
            weapon_soul = soul1.selectbox("Choose a Weapon Soul", ["Von Bon/Pierre", "Crimson Queen", "Vellum",
                                                                   "Von Leon"])
            weapon_type = soul2.selectbox("Choose a Weapon Soul Stat", ["Max DMG Cap", "HP%", "Phy DMG%", "Mag DMG%",
                                                                        "Boss ATK%", "Crit Rate%", "Crit DMG%",
                                                                        "Final DMG%"])
            self.weapon_soul = weapon_soul
            self.weapon_type = weapon_type
            if "Von Bon/Pierre" in [weapon_soul]:
                self.vonbonpierrecount += 1
                if "HP%" in [weapon_type]:
                    self.hpinc += 15
                elif "Phy DMG%" in [weapon_type]:
                    if character_type == "PHYSICAL":
                        self.dmg += 15
                elif "Mag DMG%" in [weapon_type]:
                    if character_type == "MAGICAL":
                        self.dmg += 15
                elif "Boss ATK%" in [weapon_type]:
                    self.batk += 15
                elif "Crit Rate%" in [weapon_type]:
                    self.cr += 15
                elif "Crit DMG%" in [weapon_type]:
                    self.cd += 15
                elif "Max DMG Cap" in [weapon_type]:
                    self.maxdmg += 1500000
                elif "Final DMG%" in [weapon_type]:
                    self.fd += 15
            elif "Crimson Queen" in [weapon_soul]:
                self.crimsonqueencount += 1
                if "HP%" in [weapon_type]:
                    self.hpinc += 15.5
                elif "Phy DMG%" in [weapon_type]:
                    if character_type == "PHYSICAL":
                        self.dmg += 15.5
                elif "Mag DMG%" in [weapon_type]:
                    if character_type == "MAGICAL":
                        self.dmg += 15.5
                elif "Boss ATK%" in [weapon_type]:
                    self.batk += 15.5
                elif "Crit Rate%" in [weapon_type]:
                    self.cr += 15.5
                elif "Crit DMG%" in [weapon_type]:
                    self.cd += 15.5
                elif "Max DMG Cap" in [weapon_type]:
                    self.maxdmg += 1500000
                elif "Final DMG%" in [weapon_type]:
                    self.fd += 16
            elif "Vellum" in [weapon_soul]:
                self.vellumcount += 1
                if "HP%" in [weapon_type]:
                    self.hpinc += 17
                elif "Phy DMG%" in [weapon_type]:
                    if character_type == "PHYSICAL":
                        self.dmg += 17
                elif "Mag DMG%" in [weapon_type]:
                    if character_type == "MAGICAL":
                        self.dmg += 17
                elif "Boss ATK%" in [weapon_type]:
                    self.batk += 17
                elif "Crit Rate%" in [weapon_type]:
                    self.cr += 17
                elif "Crit DMG%" in [weapon_type]:
                    self.cd += 17
                elif "Max DMG Cap" in [weapon_type]:
                    self.maxdmg += 1700000
                elif "Final DMG%" in [weapon_type]:
                    self.fd += 17
            elif "Von Leon" in [weapon_soul]:
                self.vonleoncount += 1
                if "HP%" in [weapon_type]:
                    self.hpinc += 13
                elif "Phy DMG%" in [weapon_type]:
                    if character_type == "PHYSICAL":
                        self.dmg += 13
                elif "Mag DMG%" in [weapon_type]:
                    if character_type == "MAGICAL":
                        self.dmg += 13
                elif "Boss ATK%" in [weapon_type]:
                    self.batk += 13
                elif "Crit Rate%" in [weapon_type]:
                    self.cr += 13
                elif "Crit DMG%" in [weapon_type]:
                    self.cd += 13
                elif "Max DMG Cap" in [weapon_type]:
                    self.maxdmg += 1300000
                elif "Final DMG%" in [weapon_type]:
                    self.fd += 13
            swep_soul = soul1.selectbox("Choose Secondary Weapon Soul", ["Von Bon/Pierre", "Crimson Queen", "Vellum",
                                                                         "Von Leon"])
            swep_type = soul2.selectbox("Choose Secondary Weapon Soul Stat", ["Final DMG%", "EXP%", "Fever Buff Duration",
                                                                              "Item Drop%", "Phy ATK%", "Mag ATK%"])
            self.swep_soul = swep_soul
            self.swep_type = swep_type
            if "Von Bon/Pierre" in [swep_soul]:
                self.vonbonpierrecount += 1
                if "EXP%" in [swep_type]:
                    self.exp += 4.2
                elif "Phy ATK%" in [swep_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 3.8
                elif "Mag ATK%" in [swep_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 3.8
                elif "Item Drop%" in [swep_type]:
                    self.dr += 3.8
                elif "Fever Buff Duration" in [swep_type]:
                    self.feverduration += 3
                elif "Final DMG%" in [swep_type]:
                    self.fd += 4.5
            elif "Crimson Queen" in [swep_soul]:
                self.crimsonqueencount += 1
                if "EXP%" in [swep_type]:
                    self.exp += 4.4
                elif "Phy ATK%" in [swep_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 4
                elif "Mag ATK%" in [swep_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 4
                elif "Item Drop%" in [swep_type]:
                    self.dr += 4
                elif "Fever Buff Duration" in [swep_type]:
                    self.feverduration += 3.2
                elif "Final DMG%" in [swep_type]:
                    self.fd += 4.5
            elif "Vellum" in [swep_soul]:
                self.vellumcount += 1
                if "EXP%" in [swep_type]:
                    self.exp += 4.7
                elif "Phy ATK%" in [swep_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 34.3
                elif "Mag ATK%" in [swep_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 4.3
                elif "Item Drop%" in [swep_type]:
                    self.dr += 4.3
                elif "Fever Buff Duration" in [swep_type]:
                    self.feverduration += 3.5
                elif "Final DMG%" in [swep_type]:
                    self.fd += 5
            elif "Von Leon" in [swep_soul]:
                self.vonleoncount += 1
                if "EXP%" in [swep_type]:
                    self.exp += 3.7
                elif "Phy ATK%" in [swep_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 3.3
                elif "Mag ATK%" in [swep_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 3.3
                elif "Item Drop%" in [swep_type]:
                    self.dr += 3
                elif "Fever Buff Duration" in [swep_type]:
                    self.feverduration += 2.2
                elif "Final DMG%" in [swep_type]:
                    self.fd += 3.8
            shoulder_soul = soul1.selectbox("Choose Shoulder Soul", ["Von Bon/Pierre", "Crimson Queen", "Vellum",
                                                                     "Von Leon"])
            shoulder_type = soul2.selectbox("Choose Shoulder Soul Stat", ["Final DMG%", "EXP%", "Fever Buff Duration",
                                                                          "Item Drop%", "Phy ATK%", "Mag ATK%"])
            self.shoulder_soul = shoulder_soul
            self.shoulder_type = shoulder_type
            if "Von Bon/Pierre" in [shoulder_soul]:
                self.vonbonpierrecount += 1
                if "EXP%" in [shoulder_type]:
                    self.exp += 4.2
                elif "Phy ATK%" in [shoulder_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 3.8
                elif "Mag ATK%" in [shoulder_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 3.8
                elif "Item Drop%" in [shoulder_type]:
                    self.dr += 3.8
                elif "Fever Buff Duration" in [shoulder_type]:
                    self.feverduration += 3
                elif "Final DMG%" in [shoulder_type]:
                    self.fd += 4.5
            elif "Crimson Queen" in [shoulder_soul]:
                self.crimsonqueencount += 1
                if "EXP%" in [shoulder_type]:
                    self.exp += 4.4
                elif "Phy ATK%" in [shoulder_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 4
                elif "Mag ATK%" in [shoulder_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 4
                elif "Item Drop%" in [shoulder_type]:
                    self.dr += 4
                elif "Fever Buff Duration" in [shoulder_type]:
                    self.feverduration += 3.2
                elif "Final DMG%" in [shoulder_type]:
                    self.fd += 4.5
            elif "Vellum" in [shoulder_soul]:
                self.vellumcount += 1
                if "EXP%" in [shoulder_type]:
                    self.exp += 4.7
                elif "Phy ATK%" in [shoulder_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 34.3
                elif "Mag ATK%" in [shoulder_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 4.3
                elif "Item Drop%" in [shoulder_type]:
                    self.dr += 4.3
                elif "Fever Buff Duration" in [shoulder_type]:
                    self.feverduration += 3.5
                elif "Final DMG%" in [shoulder_type]:
                    self.fd += 5
            elif "Von Leon" in [shoulder_soul]:
                self.vonleoncount += 1
                if "EXP%" in [shoulder_type]:
                    self.exp += 3.7
                elif "Phy ATK%" in [shoulder_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 3.3
                elif "Mag ATK%" in [shoulder_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 3.3
                elif "Item Drop%" in [shoulder_type]:
                    self.dr += 3
                elif "Fever Buff Duration" in [shoulder_type]:
                    self.feverduration += 2.2
                elif "Final DMG%" in [shoulder_type]:
                    self.fd += 3.8
            belt_soul = soul1.selectbox("Choose Belt Soul", ["Von Bon/Pierre", "Crimson Queen", "Vellum", "Von Leon"])
            belt_type = soul2.selectbox("Choose Belt Soul Stat", ["Final DMG%", "EXP%", "Fever Buff Duration",
                                                                  "Item Drop%", "Phy ATK%", "Mag ATK%"])
            self.belt_soul = belt_soul
            self.belt_type = belt_type
            if "Von Bon/Pierre" in [belt_soul]:
                self.vonbonpierrecount += 1
                if "EXP%" in [belt_type]:
                    self.exp += 4.2
                elif "Phy ATK%" in [belt_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 3.8
                elif "Mag ATK%" in [belt_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 3.8
                elif "Item Drop%" in [belt_type]:
                    self.dr += 3.8
                elif "Fever Buff Duration" in [belt_type]:
                    self.feverduration += 3
                elif "Final DMG%" in [belt_type]:
                    self.fd += 4.5
            elif "Crimson Queen" in [belt_soul]:
                self.crimsonqueencount += 1
                if "EXP%" in [belt_type]:
                    self.exp += 4.4
                elif "Phy ATK%" in [belt_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 4
                elif "Mag ATK%" in [belt_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 4
                elif "Item Drop%" in [belt_type]:
                    self.dr += 4
                elif "Fever Buff Duration" in [belt_type]:
                    self.feverduration += 3.2
                elif "Final DMG%" in [belt_type]:
                    self.fd += 4.5
            elif "Vellum" in [belt_soul]:
                self.vellumcount += 1
                if "EXP%" in [belt_type]:
                    self.exp += 4.7
                elif "Phy ATK%" in [belt_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 34.3
                elif "Mag ATK%" in [belt_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 4.3
                elif "Item Drop%" in [belt_type]:
                    self.dr += 4.3
                elif "Fever Buff Duration" in [belt_type]:
                    self.feverduration += 3.5
                elif "Final DMG%" in [belt_type]:
                    self.fd += 5
            elif "Von Leon" in [belt_soul]:
                self.vonleoncount += 1
                if "EXP%" in [belt_type]:
                    self.exp += 3.7
                elif "Phy ATK%" in [belt_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 3.3
                elif "Mag ATK%" in [belt_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 3.3
                elif "Item Drop%" in [belt_type]:
                    self.dr += 3
                elif "Fever Buff Duration" in [belt_type]:
                    self.feverduration += 2.2
                elif "Final DMG%" in [belt_type]:
                    self.fd += 3.8
            cape_soul = soul1.selectbox("Choose Cape Soul", ["Von Bon/Pierre", "Crimson Queen", "Vellum", "Von Leon"])
            cape_type = soul2.selectbox("Choose Cape Soul Stat", ["Final DMG%", "EXP%", "Fever Buff Duration",
                                                                  "Item Drop%", "Phy ATK%", "Mag ATK%"])
            self.cape_soul = cape_soul
            self.cape_type = cape_type
            if "Von Bon/Pierre" in [cape_soul]:
                self.vonbonpierrecount += 1
                if "EXP%" in [cape_type]:
                    self.exp += 4.2
                elif "Phy ATK%" in [cape_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 3.8
                elif "Mag ATK%" in [cape_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 3.8
                elif "Item Drop%" in [cape_type]:
                    self.dr += 3.8
                elif "Fever Buff Duration" in [cape_type]:
                    self.feverduration += 3
                elif "Final DMG%" in [cape_type]:
                    self.fd += 4.5
            elif "Crimson Queen" in [cape_soul]:
                self.crimsonqueencount += 1
                if "EXP%" in [cape_type]:
                    self.exp += 4.4
                elif "Phy ATK%" in [cape_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 4
                elif "Mag ATK%" in [cape_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 4
                elif "Item Drop%" in [cape_type]:
                    self.dr += 4
                elif "Fever Buff Duration" in [cape_type]:
                    self.feverduration += 3.2
                elif "Final DMG%" in [cape_type]:
                    self.fd += 4.5
            elif "Vellum" in [cape_soul]:
                self.vellumcount += 1
                if "EXP%" in [cape_type]:
                    self.exp += 4.7
                elif "Phy ATK%" in [cape_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 34.3
                elif "Mag ATK%" in [cape_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 4.3
                elif "Item Drop%" in [cape_type]:
                    self.dr += 4.3
                elif "Fever Buff Duration" in [cape_type]:
                    self.feverduration += 3.5
                elif "Final DMG%" in [cape_type]:
                    self.fd += 5
            elif "Von Leon" in [cape_soul]:
                self.vonleoncount += 1
                if "EXP%" in [cape_type]:
                    self.exp += 3.7
                elif "Phy ATK%" in [cape_type]:
                    if character_type == "PHYSICAL":
                        self.atkp += 3.3
                elif "Mag ATK%" in [cape_type]:
                    if character_type == "MAGICAL":
                        self.atkp += 3.3
                elif "Item Drop%" in [cape_type]:
                    self.dr += 3
                elif "Fever Buff Duration" in [cape_type]:
                    self.feverduration += 2.2
                elif "Final DMG%" in [cape_type]:
                    self.fd += 3.8

            if "Von Bon/Pierre" in [weapon_soul]:
                if self.vonbonpierrecount == 5:
                    self.atk += 900
                elif self.vonbonpierrecount == 4:
                    self.atk += 720
                elif self.vonbonpierrecount == 3:
                    self.atk += 540
                elif self.vonbonpierrecount == 2:
                    self.atk += 360
                elif self.vonbonpierrecount == 1:
                    self.atk += 180
            elif "Crimson Queen" in [weapon_soul]:
                if self.vonbonpierrecount == 5:
                    self.atk += 900
                elif self.vonbonpierrecount == 4:
                    self.atk += 720
                elif self.vonbonpierrecount == 3:
                    self.atk += 540
                elif self.vonbonpierrecount == 2:
                    self.atk += 360
                elif self.vonbonpierrecount == 1:
                    self.atk += 180
            elif "Vellum" in [weapon_soul]:
                if self.vonbonpierrecount == 5:
                    self.atk += 900
                elif self.vonbonpierrecount == 4:
                    self.atk += 720
                elif self.vonbonpierrecount == 3:
                    self.atk += 540
                elif self.vonbonpierrecount == 2:
                    self.atk += 360
                elif self.vonbonpierrecount == 1:
                    self.atk += 180
            elif "Von Leon" in [weapon_soul]:
                if self.vonbonpierrecount == 5:
                    self.atk += 750
                elif self.vonbonpierrecount == 4:
                    self.atk += 600
                elif self.vonbonpierrecount == 3:
                    self.atk += 450
                elif self.vonbonpierrecount == 2:
                    self.atk += 300
                elif self.vonbonpierrecount == 1:
                    self.atk += 150
