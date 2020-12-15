# Equipment + Set
# Soul + Soul Set
# Jewel + Jewel Set
# Style + Style Set
# Potential Options

class flame:
    def __init__(self,equip):
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
        self.hp = equip.hp
        self.mp = equip.mp
        self.batk = equip.batk
        self.cr = equip.cr
        self.cd = equip.cd
        self.exp = equip.exp
        self.atklinecount = equip.atklinecount
        self.crlinecount = equip.crlinecount
        self.cdlinecount = equip.cdlinecount

        self.f_atk_on_hp = self.atk_on_hp * self.hp
        self.f_atk_on_mp = self.atk_on_mp * self.mp
        self.f_atk_on_batk = self.atk_on_batk * self.batk
        self.f_atk_on_cr = self.atk_on_cr * self.cr
        self.f_atk_on_cd = self.atk_on_cd * self.cd
        self.f_atk_on_exp = self.atk_on_exp * self.exp
        self.f_atkflame = max(self.f_atk_on_hp,self.f_atk_on_mp,self.f_atk_on_batk,self.f_atk_on_cr,self.f_atk_on_cd,
                              self.f_atk_on_exp)* self.atklinecount
        if self.f_atk_on_hp > self.f_atk_on_mp and self.f_atk_on_hp > self.f_atk_on_batk and self.f_atk_on_hp > self.f_atk_on_cr \
                and self.f_atk_on_hp > self.f_atk_on_cd and self.f_atk_on_hp > self.f_atk_on_exp:
            self.f_atkflamebase = "HP"
        elif self.f_atk_on_mp > self.f_atk_on_hp and self.f_atk_on_mp > self.f_atk_on_batk and self.f_atk_on_mp > self.f_atk_on_cr \
                and self.f_atk_on_mp > self.f_atk_on_cd and self.f_atk_on_mp > self.f_atk_on_exp:
            self.f_atkflamebase = "MP"
        elif self.f_atk_on_batk > self.f_atk_on_hp and self.f_atk_on_batk > self.f_atk_on_mp and self.f_atk_on_batk > self.f_atk_on_cr \
                and self.f_atk_on_batk > self.f_atk_on_cd and self.f_atk_on_batk > self.f_atk_on_exp:
            self.f_atkflamebase = "BATK"
        elif self.f_atk_on_cr > self.f_atk_on_hp and self.f_atk_on_cr > self.f_atk_on_mp and self.f_atk_on_cr > self.f_atk_on_batk \
                and self.f_atk_on_cr > self.f_atk_on_cd and self.f_atk_on_cr > self.f_atk_on_exp:
            self.f_atkflamebase = "CR"
        elif self.f_atk_on_cd > self.f_atk_on_hp and self.f_atk_on_cd > self.f_atk_on_mp and self.f_atk_on_cd > self.f_atk_on_batk \
                and self.f_atk_on_cd > self.f_atk_on_cr and self.f_atk_on_hp > self.f_atk_on_exp:
            self.f_atkflamebase = "CD"
        else:
            self.f_atkflamebase = "EXP"

        self.f_cr_on_batk = self.cr_on_batk * self.batk
        self.f_cr_on_cd = self.cr_on_cd * self.cd
        self.f_cr_on_exp = self.cr_on_exp * self.exp
        self.f_crflame = max(self.f_cr_on_batk,self.f_cr_on_cd,self.f_cr_on_exp)* self.crlinecount
        if self.f_cr_on_batk > self.f_cr_on_cd and self.f_cr_on_batk > self.f_cr_on_exp:
            self.f_crflamebase = "BATK"
        elif self.f_cr_on_cd > self.f_cr_on_batk and self.f_cr_on_cd > self.f_cr_on_exp:
            self.f_crflamebase = "CD"
        else:
            self.f_crflamebase = "EXP"

        self.f_cd_on_batk = self.cd_on_batk * self.batk
        self.f_cd_on_cr = self.cd_on_cr * self.cr
        self.f_cd_on_exp = self.cd_on_exp * self.exp
        self.f_cdflame = max(self.f_cd_on_batk,self.f_cd_on_cr,self.f_cd_on_exp)* self.cdlinecount
        if self.f_cd_on_batk > self.f_cd_on_cr and self.f_cd_on_batk > self.f_cd_on_exp:
            self.f_cdflamebase = "BATK"
        elif self.f_cd_on_cr > self.f_cd_on_batk and self.f_cd_on_cr > self.f_cd_on_exp:
            self.f_cdflamebase = "CR"
        else:
            self.f_cdflamebase = "EXP"

    def fatk(self):
        atkflame = self.f_atkflame
        return atkflame

    def fcr(self):
        crflame = self.f_crflame
        return crflame

    def fcd(self):
        cdflame = self.f_cdflame
        return cdflame

    def fatkbase(self):
        atkbase = self.f_atkflamebase
        return atkbase

    def fcrbase(self):
        crbase = self.f_crflamebase
        return crbase

    def fcdbase(self):
        cdbase = self.f_cdflamebase
        return cdbase

    def fatklinecount(self):
        atklinecount = self.atklinecount
        return atklinecount

    def fcrlinecount(self):
        crlinecount = self.crlinecount
        return crlinecount

    def fcdlinecount(self):
        cdlinecount = self.cdlinecount
        return cdlinecount
