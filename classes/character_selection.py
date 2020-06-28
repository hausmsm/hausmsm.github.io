import pandas as pd
class character_selection:
    def __init__(self):
        self.warrior_list = {"DK", "HERO", "PALA", "DW", "ARAN"}
        self.mage_list = {"BSP", "ILM", "FPM", "BW", "EVAN", "LUMI", "BAM"}
        self.archer_list = {"BM", "MM", "WA", "MERC"}
        self.thief_list = {"NL", "SHAD", "NW", "PHAN"}
        self.pirate_list = {"CSR", "BUCC", "TB", "SHADE"}
        self.character_class = str

    def warrior(self):
        while True:
            self.character_class = str(input("Please enter your class:\n"
                                  "DK, HERO, PALA, DW, ARAN\n")).upper()
            if self.character_class not in self.warrior_list:
                continue
            else:
                return self.character_class

    def mage(self):
        while True:
            self.character_class = str(input("Please enter your class:\n"
                                  "BSP, ILM, FPM, BW, EVAN, LUMI, BAM\n")).upper()
            if self.character_class not in self.mage_list:
                continue
            else:
                return self.character_class

    def archer(self):
        while True:
            self.character_class = str(input("Please enter your class:\n"
                                  "BM, MM, WA, MERC\n")).upper()
            if self.character_class not in self.archer_list:
                continue
            else:
                return self.character_class

    def thief(self):
        while True:
            self.character_class = str(input("Please enter your class:\n"
                                  "NL, SHAD, NW, PHAN\n")).upper()
            if self.character_class not in self.thief_list:
                continue
            else:
                return self.character_class

    def pirate(self):
        while True:
            self.character_class = str(input("Please enter your class:\n"
                                  "CSR, BUCC, TB, SHADE\n")).upper()
            if self.character_class not in self.pirate_list:
                continue
            else:
                return self.character_class