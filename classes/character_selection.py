import streamlit as st


class Character_selection:
    def __init__(self):
        with st.beta_expander("Class"):
            self.character_type = st.selectbox("Choose Class Type", ["Warrior", "Mage", "Archer", "Thief", "Pirate"])
            if self.character_type == "Warrior":
                self.character_class = st.selectbox("Choose Class",
                                               ["Dark Knight", "Hero", "Paladin", "Dawn Warrior", "Aran", "Demon Slayer",
                                                "Demon Avenger"])
                if self.character_class == "Dark Knight":
                    self.type = "PHYSICAL"
                    from classes.dk import Dk
                    self.char = Dk()

                elif self.character_class == "Hero":
                    self.type = "PHYSICAL"
                    from classes.hero import Hero
                    self.char = Hero()

                elif self.character_class == "Paladin":
                    self.type = "PHYSICAL"
                    from classes.pala import Pala
                    self.char = Pala()

                elif self.character_class == "Dawn Warrior":
                    self.type = "PHYSICAL"
                    from classes.dw import Dw
                    self.char = Dw()

                elif self.character_class == "Aran":
                    self.type = "PHYSICAL"
                    from classes.aran import Aran
                    self.char = Aran()

                elif self.character_class == "Demon Slayer":
                    self.type = "PHYSICAL"
                    from classes.ds import Ds
                    self.char = Ds()

                elif self.character_class == "Demon Avenger":
                    self.type = "PHYSICAL"
                    from classes.da import Da
                    self.char = Da()

            elif self.character_type == "Mage":
                self.character_class = st.selectbox("Choose Class",
                                               ["Bishop", "Ice Lightning Mage", "Fire Poison Mage", "Blaze Wizard",
                                                "Evan",
                                                "Luminous", "Battle Mage"])
                if self.character_class == "Bishop":
                    self.type = "MAGICAL"
                    from classes.bsp import Bsp
                    self.char = Bsp()

                elif self.character_class == "Ice Lightning Mage":
                    self.type = "MAGICAL"
                    from classes.ilm import Ilm
                    self.char = Ilm()

                elif self.character_class == "Fire Poison Mage":
                    self.type = "MAGICAL"
                    from classes.fpm import Fpm
                    self.char = Fpm()

                elif self.character_class == "Blaze Wizard":
                    self.type = "MAGICAL"
                    from classes.bw import Bw
                    self.char = Bw()

                elif self.character_class == "Evan":
                    self.type = "MAGICAL"
                    from classes.evan import Evan
                    self.char = Evan()

                elif self.character_class == "Luminous":
                    self.type = "MAGICAL"
                    from classes.lumi import Lumi
                    self.char = Lumi()

                elif self.character_class == "Battle Mage":
                    self.type = "MAGICAL"
                    from classes.bam import Bam
                    self.char = Bam()

            elif self.character_type == "Archer":
                self.character_class = st.selectbox("Choose Class",
                                               ["Bow Master", "Marksman", "Wind Archer", "Mercedes", "Wild Hunter"])
                if self.character_class == "Bow Master":
                    self.type = "PHYSICAL"
                    from classes.bm import Bm
                    self.char = Bm()

                elif self.character_class == "Marksman":
                    self.type = "PHYSICAL"
                    from classes.mm import Mm
                    self.char = Mm()

                elif self.character_class == "Wind Archer":
                    self.type = "PHYSICAL"
                    from classes.wa import Wa
                    self.char = Wa()

                elif self.character_class == "Mercedes":
                    self.type = "PHYSICAL"
                    from classes.merc import Merc
                    self.char = Merc()

                elif self.character_class == "Wild Hunter":
                    self.type = "PHYSICAL"
                    from classes.wh import Wh
                    self.char = Wh()

            elif self.character_type == "Thief":
                self.character_class = st.selectbox("Choose Class", ["Night Lord", "Shadower", "Night Walker", "Phantom"])
                if self.character_class == "Night Lord":
                    self.type = "PHYSICAL"
                    from classes.nl import Nl
                    self.char = Nl()

                elif self.character_class == "Shadower":
                    self.type = "PHYSICAL"
                    from classes.shad import Shad
                    self.char = Shad()

                elif self.character_class == "Night Walker":
                    self.type = "PHYSICAL"
                    from classes.nw import Nw
                    self.char = Nw()

                elif self.character_class == "Phantom":
                    self.type = "PHYSICAL"
                    from classes.phan import Phan
                    self.char = Phan()

            elif self.character_type == "Pirate":
                self.character_class = st.selectbox("Choose Class",
                                               ["Corsair", "Buccaneer", "Thunder Breaker", "Shade", "Mechanic"])
                if self.character_class == "Corsair":
                    self.type = "MAGICAL"
                    from classes.csr import Csr
                    self.char = Csr()

                elif self.character_class == "Buccaneer":
                    self.type = "PHYSICAL"
                    from classes.bucc import Bucc
                    self.char = Bucc()

                elif self.character_class == "Thunder Breaker":
                    self.type = "PHYSICAL"
                    from classes.tb import Tb
                    self.char = Tb()

                elif self.character_class == "Shade":
                    self.type = "PHYSICAL"
                    from classes.shade import Shade
                    self.char = Shade()

                elif self.character_class == "Mechanic":
                    self.type = "MAGICAL"
                    from classes.mech import Mech
                    self.char = Mech()

