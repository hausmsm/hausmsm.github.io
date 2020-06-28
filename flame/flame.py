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
        self.cr_on_ba = 0.06
        self.cr_on_cd = 0.014
        self.cr_on_exp = 0.06

    def calculation(self,flamestats):
        atk_on_hp = self.atk_on_hp * flamestats["HP"]
        atk_on_mp = self.atk_on_mp * flamestats["MP"]
        atk_on_batk = self.atk_on_batk * flamestats["BATK"]

        atkflame = max(atk_on_hp,atk_on_mp,atk_on_batk)
