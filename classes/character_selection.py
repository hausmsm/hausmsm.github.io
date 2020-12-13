import streamlit as st
class character_selection:
    def __init__(self):
        with st.beta_expander("Class"):
            self.character_type = st.selectbox("Choose Class Type", ["Warrior", "Mage", "Archer", "Thief", "Pirate"])
            if self.character_type == "Warrior":
                self.character_class = st.selectbox("Choose Class",
                                               ["Dark Knight", "Hero", "Paladin", "Dawn Warrior", "Aran"])
                if self.character_class == "Dark Knight":
                    type = "PHYSICAL"
                    from classes.dk import dk
                    self.char = dk()

                elif self.character_class == "Hero":
                    type = "PHYSICAL"
                    from classes.hero import hero
                    self.char = hero()

                elif self.character_class == "Paladin":
                    type = "PHYSICAL"
                    from classes.pala import pala
                    self.char = pala()

                elif self.character_class == "Dawn Warrior":
                    type = "PHYSICAL"
                    from classes.dw import dw
                    self.char = dw()

                elif self.character_class == "Aran":
                    type = "PHYSICAL"
                    from classes.aran import aran
                    self.char = aran()

            elif self.character_type == "Mage":
                self.character_class = st.selectbox("Choose Class",
                                               ["Bishop", "Ice Lightning Mage", "Fire Poison Mage", "Blaze Wizard",
                                                "Evan",
                                                "Luminous", "Battle Mage"])
                if self.character_class == "Bishop":
                    type = "MAGICAL"
                    from classes.bsp import bsp
                    self.char = bsp()

                elif self.character_class == "Ice Lightning Mage":
                    type = "MAGICAL"
                    from classes.ilm import ilm
                    self.char = ilm()

                elif self.character_class == "Fire Poison Mage":
                    type = "MAGICAL"
                    from classes.fpm import fpm
                    self.char = fpm()

                elif self.character_class == "Blaze Wizard":
                    type = "MAGICAL"
                    from classes.bw import bw
                    self.char = bw()

                elif self.character_class == "Evan":
                    type = "MAGICAL"
                    from classes.evan import evan
                    self.char = evan()

                elif self.character_class == "Luminous":
                    type = "MAGICAL"
                    from classes.lumi import lumi
                    self.char = lumi()

                elif self.character_class == "Battle Mage":
                    type = "MAGICAL"
                    from classes.bam import bam
                    self.char = bam()

            elif self.character_type == "Archer":
                self.character_class = st.selectbox("Choose Class",
                                               ["Bow Master", "Marksman", "Wind Archer", "Mercedes", "Wild Hunter"])
                if self.character_class == "Bow Master":
                    type = "PHYSICAL"
                    from classes.bm import bm
                    self.char = bm()

                elif self.character_class == "Marksman":
                    type = "PHYSICAL"
                    from classes.mm import mm
                    self.char = mm()

                elif self.character_class == "Wind Archer":
                    type = "PHYSICAL"
                    from classes.wa import wa
                    self.char = wa()

                elif self.character_class == "Mercedes":
                    type = "PHYSICAL"
                    from classes.merc import merc
                    self.char = merc()

                elif self.character_class == "Wild Hunter":
                    type = "PHYSICAL"
                    from classes.wh import wh
                    self.char = wh()

            elif self.character_type == "Thief":
                self.character_class = st.selectbox("Choose Class", ["Night Lord", "Shadower", "Night Walker", "Phantom"])
                if self.character_class == "Night Lord":
                    type = "PHYSICAL"
                    from classes.nl import nl
                    self.char = nl()

                elif self.character_class == "Shadower":
                    type = "PHYSICAL"
                    from classes.shad import shad
                    self.char = shad()

                elif self.character_class == "Night Walker":
                    type = "PHYSICAL"
                    from classes.nw import nw
                    self.char = nw()

                elif self.character_class == "Phantom":
                    type = "PHYSICAL"
                    from classes.phan import phan
                    self.char = phan()

            elif self.character_type == "Pirate":
                self.character_class = st.selectbox("Choose Class",
                                               ["Corsair", "Buccaneer", "Thunder Breaker", "Shade", "Mechanic"])
                if self.character_class == "Corsair":
                    type = "MAGICAL"
                    from classes.csr import csr
                    self.char = csr()

                elif self.character_class == "Buccaneer":
                    type = "PHYSICAL"
                    from classes.bucc import bucc
                    self.char = bucc()

                elif self.character_class == "Thunder Breaker":
                    type = "PHYSICAL"
                    from classes.tb import tb
                    self.char = tb()

                elif self.character_class == "Shade":
                    type = "PHYSICAL"
                    from classes.shade import shade
                    self.char = shade()

                elif self.character_class == "Mechanic":
                    type = "MAGICAL"
                    from classes.mech import mech
                    self.char = mech()

    def char(self):
        char = self.char
        return char

    def character_class(self):
        character_class = self.character_class
        return character_class

    def character_type(self):
        character_type = self.character_type
        return character_type

    def type(self):
        type = self.type
        return type
