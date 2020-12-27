import streamlit as st


class Link:
    def __init__(self, character_class, character_type):
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

        joblink = {
            # Warrior
            "Dark Knight": "Phy DEF (Dark Knight)",
            "Hero": "Boss DEF (Hero)",
            "Paladin": "PEN Rate (Paladin)",
            "Dawn Warrior": "Mag DEF (Dawn Warrior)",
            "Aran": "Fever Recharge (Aran)",
            "Demon Slayer": "Boss ATK (Demon Slayer)",
            "Demon Avenger": "Phy DMG (Demon Avenger)",
            # Mage
            "Bishop": "Party EXP (Bishop)",
            "Ice Lightning Mage": "MP% (Ice Lightning Mage)",
            "Fire Poison Mage": "Mag ATK (Fire Poison Mage)",
            "Blaze Wizard": "Fever Duration (Blaze Wizard)",
            "Evan": "Boss ATK (Evan)",
            "Luminous": "Mag DMG (Luminous)",
            "Battle Mage": "Abnormal Status RES (Battle Mage, Wild Hunter & Mechanic)",
            # Archer
            "Bow Master": "Gold Leaf (Bow Master)",
            "Marksman": "ACC (Marksman)",
            "Wind Archer": "HP/MP Rec (Wind Archer)",
            "Mercedes": "EXP (Mercedes)",
            "Wild Hunter": "Abnormal Status RES (Battle Mage, Wild Hunter & Mechanic)",
            # Thief
            "Night Lord": "Meso (Night Lord)",
            "Shadower": "Crit Rate (Shadower)",
            "Night Walker": "Drop (Night Walker)",
            "Phantom": "Crit DMG (Phantom)",
            # Pirate
            "Corsair": "KBK RES (Corsair)",
            "Buccaneer": "Phy ATK (Buccaneer)",
            "Thunder Breaker": "HP% (Thunder Breaker)",
            "Shade": "Survival Chance (Shade)",
            "Mechanic": "Abnormal Status RES (Battle Mage, Wild Hunter & Mechanic)"
        }
        linkskills = ["Phy DEF (Dark Knight)", "Boss DEF (Hero)", "PEN Rate (Paladin)", "Mag DEF (Dawn Warrior)",
                      "Fever Recharge (Aran)", "Boss ATK (Demon Slayer)", "Phy DMG (Demon Avenger)",
                      "Party EXP (Bishop)", "MP% (Ice Lightning Mage)", "Mag ATK (Fire Poison Mage)",
                      "Fever Duration (Blaze Wizard)", "Boss ATK (Evan)", "Mag DMG (Luminous)",
                      "Abnormal Status RES (Battle Mage, Wild Hunter & Mechanic)", "Gold Leaf (Bow Master)",
                      "ACC (Marksman)", "HP/MP Rec (Wind Archer)", "EXP (Mercedes)", "Meso (Night Lord)",
                      "Crit Rate (Shadower)", "Drop (Night Walker)", "Crit DMG (Phantom)", "KBK RES (Corsair)",
                      "Phy ATK (Buccaneer)", "HP% (Thunder Breaker)", "Survival Chance (Shade)"]

        linkskills.remove(joblink[character_class])
        with st.beta_expander("Link Skills"):
            st.write("Note: Character Innate Link Skill Already Included")
            link_list = st.multiselect("Choose 12 Link Skills", linkskills)
            self.links = link_list
            _, link1, _, link2, _ = st.beta_columns([0.02, 0.47, 0.02, 0.47, 0.02])
            if len(link_list) == 12:
                link1.write(link_list[0])
                link1.write(link_list[1])
                link1.write(link_list[2])
                link1.write(link_list[3])
                link1.write(link_list[4])
                link1.write(link_list[5])
                link2.write(link_list[6])
                link2.write(link_list[7])
                link2.write(link_list[8])
                link2.write(link_list[9])
                link2.write(link_list[10])
                link2.write(link_list[11])
                if "Phy DEF (Dark Knight)" in link_list:
                    self.pdefinc += 4
                if "Boss DEF (Hero)" in link_list:
                    self.bdef += 4
                if "PEN Rate (Paladin)" in link_list:
                    self.penrate += 4
                if "Mag DEF (Dawn Warrior)" in link_list:
                    self.mdefinc += 4
                if "Fever Recharge (Aran)" in link_list:
                    self.feverchargeinc += 4
                if "Boss ATK (Demon Slayer)" in link_list:
                    self.batk += 4
                if "Phy DMG (Demon Avenger)" in link_list:
                    if character_type == "PHYSICAL":
                        self.dmg += 4
                if "Party EXP (Bishop)" in link_list:
                    self.partyexp += 4
                if "MP% (Ice Lightning Mage)" in link_list:
                    self.mpinc += 4
                if "Mag ATK (Fire Poison Mage)" in link_list:
                    if character_type == "MAGICAL":
                        self.atkp += 4
                if "Fever Duration (Blaze Wizard)" in link_list:
                    self.feverduration += 5
                if "Boss ATK (Evan)" in link_list:
                    self.batk += 5
                if "Mag DMG (Luminous)" in link_list:
                    if character_type == "MAGICAL":
                        self.dmg += 4
                if "Abnormal Status RES (Battle Mage, Wild Hunter & Mechanic)" in link_list:
                    self.abnormalstatres += 6
                if "Gold Leaf (Bow Master)" in link_list:
                    self.glincrease += 4
                if "ACC (Marksman)" in link_list:
                    self.accp += 4
                if "HP/MP Rec (Wind Archer)" in link_list:
                    self.hprec += 100
                    self.mprec += 100
                if "EXP (Mercedes)" in link_list:
                    self.exp += 4
                if "Meso (Night Lord)" in link_list:
                    self.meso += 4
                if "Crit Rate (Shadower)" in link_list:
                    self.cr += 4
                if "Drop (Night Walker)" in link_list:
                    self.dr += 4
                if "Crit DMG (Phantom)" in link_list:
                    self.cd += 4
                if "KBK RES (Corsair)" in link_list:
                    self.kbkres += 10
                if "Phy ATK (Buccaneer)" in link_list:
                    if character_type == "PHYSICAL":
                        self.atkp += 4
                if "HP% (Thunder Breaker)" in link_list:
                    self.hpinc += 4
                if "Survival Chance (Shade)" in link_list:
                    pass
            elif len(link_list) > 12:
                st.write(f"Above Link Skill Limit. Currently {len(link_list)}/12.")
            else:
                st.write(f"Only {len(link_list)}/12")
