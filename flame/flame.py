class Flame:
    def __init__(self, flamestats):
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

        self.fatk = 0
        self.fcr = 0
        self.fcd = 0
        self.fatkbase = str
        self.fcrbase = str
        self.fcdbase = str

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
        self.hp += int(round(flamestats.hp, 0))
        self.mp += int(round(flamestats.mp, 0))
        self.batk += float(round(flamestats.batk, 1))
        self.cr += float(round(flamestats.cr, 1))
        self.cd += float(round(flamestats.cd, 1))
        self.exp += float(round(flamestats.exp, 1))
        self.fatklinecount = flamestats.atklinecount
        self.fcrlinecount = flamestats.crlinecount
        self.fcdlinecount = flamestats.cdlinecount

        self.f_atk_on_hp = self.atk_on_hp * self.hp
        self.f_atk_on_mp = self.atk_on_mp * self.mp
        self.f_atk_on_batk = self.atk_on_batk * self.batk
        self.f_atk_on_cr = self.atk_on_cr * self.cr
        self.f_atk_on_cd = self.atk_on_cd * self.cd
        self.f_atk_on_exp = self.atk_on_exp * self.exp
        self.f_atkflame = int(round((max(self.f_atk_on_hp, self.f_atk_on_mp, self.f_atk_on_batk, self.f_atk_on_cr, self.f_atk_on_cd,
                              self.f_atk_on_exp) * self.fatklinecount), 0))
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
        self.f_crflame = float(round((max(self.f_cr_on_batk, self.f_cr_on_cd, self.f_cr_on_exp) * self.fcrlinecount), 1))
        if self.f_cr_on_batk > self.f_cr_on_cd and self.f_cr_on_batk > self.f_cr_on_exp:
            self.f_crflamebase = "BATK"
        elif self.f_cr_on_cd > self.f_cr_on_batk and self.f_cr_on_cd > self.f_cr_on_exp:
            self.f_crflamebase = "CD"
        else:
            self.f_crflamebase = "EXP"

        self.f_cd_on_batk = self.cd_on_batk * self.batk
        self.f_cd_on_cr = self.cd_on_cr * self.cr
        self.f_cd_on_exp = self.cd_on_exp * self.exp
        self.f_cdflame = float(round((max(self.f_cd_on_batk, self.f_cd_on_cr, self.f_cd_on_exp) * self.fcdlinecount), 1))
        if self.f_cd_on_batk > self.f_cd_on_cr and self.f_cd_on_batk > self.f_cd_on_exp:
            self.f_cdflamebase = "BATK"
        elif self.f_cd_on_cr > self.f_cd_on_batk and self.f_cd_on_cr > self.f_cd_on_exp:
            self.f_cdflamebase = "CR"
        else:
            self.f_cdflamebase = "EXP"
