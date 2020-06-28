class flame:
    def __init__(self):
        self.atk_on_hp = 0.01
        self.atk_on_mp = 0.035
        self.atk_on_batk = 11.3
        self.atk_on_cr = 16.63
        self.atk_on_cd = 2.75
        self.atk_on_exp = 11.0
        self.cd_on_batk = 0.06
        self.cd_on_cr = 0.11
        self.cd_on_exp = 0.12
        self.cr_on_batk = 0.06
        self.cr_on_cd = 0.014
        self.cr_on_exp = 0.06

    def atkcalculation(self,hp,mp,batk,cr,cd,exp,lines):
        atk_on_hp = self.atk_on_hp * hp
        atk_on_mp = self.atk_on_mp * mp
        atk_on_batk = self.atk_on_batk * batk
        atk_on_cr = self.atk_on_cr * cr
        atk_on_cd = self.atk_on_cd * cd
        atk_on_exp = self.atk_on_exp * exp
        atkflame = max(atk_on_hp,atk_on_mp,atk_on_batk,atk_on_cr,atk_on_cd,atk_on_exp)*lines
        if atk_on_hp > atk_on_mp and atk_on_hp > atk_on_batk and atk_on_hp > atk_on_cr and atk_on_hp > atk_on_cd \
                and atk_on_hp > atk_on_exp:
            atkflamebase = "HP"
        elif atk_on_mp > atk_on_hp and atk_on_mp > atk_on_batk and atk_on_mp > atk_on_cr and atk_on_mp > atk_on_cd \
                and atk_on_mp > atk_on_exp:
            atkflamebase = "MP"
        elif atk_on_batk > atk_on_hp and atk_on_batk > atk_on_mp and atk_on_batk > atk_on_cr and atk_on_batk > atk_on_cd \
                and atk_on_batk > atk_on_exp:
            atkflamebase = "BATK"
        elif atk_on_cr > atk_on_hp and atk_on_cr > atk_on_mp and atk_on_cr > atk_on_batk and atk_on_cr > atk_on_cd \
                and atk_on_cr > atk_on_exp:
            atkflamebase = "CR"
        elif atk_on_cd > atk_on_hp and atk_on_cd > atk_on_mp and atk_on_cd > atk_on_batk and atk_on_cd > atk_on_cr \
                and atk_on_hp > atk_on_exp:
            atkflamebase = "CD"
        else:
            atkflamebase = "EXP"
        return atkflame, atkflamebase

    def crcalculation(self,batk,cd,exp,lines):
        cr_on_batk = self.cr_on_batk * batk
        cr_on_cd = self.cr_on_cd * cd
        cr_on_exp = self.cr_on_exp * exp
        crflame = max(cr_on_batk,cr_on_cd,cr_on_exp)*lines
        if cr_on_batk > cr_on_cd and cr_on_batk > cr_on_exp:
            crflamebase = "BATK"
        elif cr_on_cd > cr_on_batk and cr_on_cd > cr_on_exp:
            crflamebase = "CD"
        else:
            crflamebase = "EXP"
        return crflame, crflamebase

    def cdcalculation(self,batk,cr,exp,lines):
        cd_on_batk = self.cd_on_batk * batk
        cd_on_cr = self.cd_on_cr * cr
        cd_on_exp = self.cd_on_exp * exp
        cdflame = max(cd_on_batk,cd_on_cr,cd_on_exp)*lines
        if cd_on_batk > cd_on_cr and cd_on_batk > cd_on_exp:
            cdflamebase = "BATK"
        elif cd_on_cr > cd_on_batk and cd_on_cr > cd_on_exp:
            cdflamebase = "CR"
        else:
            cdflamebase = "EXP"
        return cdflame, cdflamebase