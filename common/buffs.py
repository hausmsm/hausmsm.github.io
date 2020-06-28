class buffs:
    def __init__(self,type,character_class):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0

        #Bishop
        if character_class != "BSP":
            self.atkp += 35
            self.batk += 15

        #Wild Hunter (STILL UNKNOWN)
        if character_class != "WH":
            self.dmg += 10

        #Mage
        if type == "MAGICAL":
            if character_class != "FPM" and character_class != "ILM":
                self.dmg += 10

        #Paladin
        if character_class != "PALA":
            if character_class != "PHAN":
                self.dmg += 15

        #Buccaneer
        if character_class != "BUCC":
            if character_class != "TB":
                self.batk += 9.6

        #Luminous
        if type == "MAGICAL":
            if character_class != "LUMI":
                self.atkp += 21.6

        #Hero
        if type == "PHYSICAL":
            if character_class != "HERO" and character_class != "PHAN":
                self.atkp += 21

        #Evan
        if character_class != "EVAN":
            self.dmg += 15

        #Cash Buffs
        self.atkp += 30
        self.dmg += 30
        self.batk += 30
        self.cr += 30
        self.cd += 30

        #Tangyoon Buffs
        self.dmg += 20
        self.batk += 20
        self.cr += 20

        #Fever
        self.atkp += 10
        self.cr += 10
        self.cd += 20

    def atkp(self):
        atkp = self.atkp
        return atkp

    def dmg(self):
        dmg = self.dmg
        return dmg

    def batk(self):
        batk = self.batk
        return batk

    def cr(self):
        cr = self.cr
        return cr

    def fd(self):
        fd = self.fd
        return fd
