# Equipment + Set
# Soul + Soul Set
# Jewel + Jewel Set
# Style + Style Set
# Potential Options
# Pet Set

class flame:
    def __init__(self, flamestats):
        # Initialize
        self.normal_emb = 0
        self.emblem_cd = 0
        self.emblem_batk = 0
        self.emblem_atkp = 0
        self.unique_acc_emb = 0
        self.legendary_acc_emb = 0

        # SF Stats
        self.sf = 0

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

        # HP MP Stats
        self.hp = 0
        self.mp = 0
        self.hpinc = 0
        self.mpinc = 0
        self.hprec = 0
        self.mprec = 0
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
        self.hp += flamestats.hp
        self.mp += flamestats.mp
        self.batk += flamestats.batk
        self.cr += flamestats.cr
        self.cd += flamestats.cd
        self.exp += flamestats.exp
        self.fatklinecount = flamestats.atklinecount
        self.fcrlinecount = flamestats.crlinecount
        self.fcdlinecount = flamestats.cdlinecount

        self.f_atk_on_hp = self.atk_on_hp * self.hp
        self.f_atk_on_mp = self.atk_on_mp * self.mp
        self.f_atk_on_batk = self.atk_on_batk * self.batk
        self.f_atk_on_cr = self.atk_on_cr * self.cr
        self.f_atk_on_cd = self.atk_on_cd * self.cd
        self.f_atk_on_exp = self.atk_on_exp * self.exp
        self.f_atkflame = max(self.f_atk_on_hp,self.f_atk_on_mp,self.f_atk_on_batk,self.f_atk_on_cr,self.f_atk_on_cd,
                              self.f_atk_on_exp)* self.fatklinecount
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
        self.f_crflame = max(self.f_cr_on_batk,self.f_cr_on_cd,self.f_cr_on_exp)* self.fcrlinecount
        if self.f_cr_on_batk > self.f_cr_on_cd and self.f_cr_on_batk > self.f_cr_on_exp:
            self.f_crflamebase = "BATK"
        elif self.f_cr_on_cd > self.f_cr_on_batk and self.f_cr_on_cd > self.f_cr_on_exp:
            self.f_crflamebase = "CD"
        else:
            self.f_crflamebase = "EXP"

        self.f_cd_on_batk = self.cd_on_batk * self.batk
        self.f_cd_on_cr = self.cd_on_cr * self.cr
        self.f_cd_on_exp = self.cd_on_exp * self.exp
        self.f_cdflame = max(self.f_cd_on_batk,self.f_cd_on_cr,self.f_cd_on_exp)* self.fcdlinecount
        if self.f_cd_on_batk > self.f_cd_on_cr and self.f_cd_on_batk > self.f_cd_on_exp:
            self.f_cdflamebase = "BATK"
        elif self.f_cd_on_cr > self.f_cd_on_batk and self.f_cd_on_cr > self.f_cd_on_exp:
            self.f_cdflamebase = "CR"
        else:
            self.f_cdflamebase = "EXP"

    def f_atkflame(self):
        f_atkflame = self.f_atkflame
        return f_atkflame

    def f_crflame(self):
        f_crflame = self.f_crflame
        return f_crflame

    def f_cdflame(self):
        f_cdflame = self.f_cdflame
        return f_cdflame

    def f_atkflamebase(self):
        f_atkflamebase = self.f_atkflamebase
        return f_atkflamebase

    def f_crflamebase(self):
        f_crflamebase = self.f_crflamebase
        return f_crflamebase

    def f_cdflamebase(self):
        f_cdflamebase = self.f_cdflamebase
        return f_cdflamebase

    def atklinecount(self):
        atklinecount = self.atklinecount
        return atklinecount

    def crlinecount(self):
        crlinecount = self.crlinecount
        return crlinecount

    def cdlinecount(self):
        cdlinecount = self.cdlinecount
        return cdlinecount

    def normal_emb(self):
        normal_emb = self.normal_emb
        return normal_emb

    def unique_acc_emb(self):
        unique_acc_emb = self.unique_acc_emb
        return unique_acc_emb

    def legendary_acc_emb(self):
        legendary_acc_emb = self.legendary_acc_emb
        return legendary_acc_emb

    def emblem_cd(self):
        emblem_cd = self.emblem_cd
        return emblem_cd

    def emblem_batk(self):
        emblem_batk = self.emblem_batk
        return emblem_batk

    def emblem_atkp(self):
        emblem_atkp = self.emblem_atkp
        return emblem_atkp

    def emblem(self):
        emblem = self.emblem
        return emblem

    def emblem_level(self):
        emblem_level = self.emblem_level
        return emblem_level

    def emblem_amount(self):
        emblem_amount = self.emblem_amount
        return emblem_amount

    def type(self):
        type = self.type
        return type

    def sf(self):
        sf = self.sf
        return sf

    def stat(self):
        stat = self.stat
        return stat

    def stat_amount(self):
        stat_amount = self.stat_amount
        return stat_amount

    def level(self):
        level = self.level
        return level

    def atk(self):
        atk = self.atk
        return atk

    def atkp(self):
        atkp = self.atkp
        return atkp

    def dmg(self):
        dmg = self.dmg
        return dmg

    def batk(self):
        batk = self.batk
        return batk

    def platk(self):
        platk = self.platk
        return platk

    def cr(self):
        cr = self.cr
        return cr

    def cratk(self):
        cratk = self.cratk
        return cratk

    def cd(self):
        cd = self.cd
        return cd

    def maxdmg(self):
        maxdmg = self.maxdmg
        return maxdmg

    def fd(self):
        fd = self.fd
        return fd

    def pdef(self):
        pdef = self.pdef
        return pdef

    def pdefinc(self):
        pdefinc = self.pdefinc
        return pdefinc

    def pdefdec(self):
        pdefdec = self.pdefdec
        return pdefdec

    def mdef(self):
        mdef = self.mdef
        return mdef

    def mdefinc(self):
        mdefinc = self.mdefinc
        return mdefinc

    def mdefdec(self):
        mdefdec = self.mdefdec
        return mdefdec

    def bdef(self):
        bdef = self.bdef
        return bdef

    def pldef(self):
        pldef = self.pldef
        return pldef

    def critres(self):
        critres = self.critres
        return critres

    def critdmgres(self):
        critdmgres = self.critdmgres
        return critdmgres

    def acc(self):
        acc = self.acc
        return acc

    def accp(self):
        accp = self.accp
        return accp

    def evd(self):
        evd = self.evd
        return evd

    def evdp(self):
        evdp = self.evdp
        return evdp

    def penrate(self):
        penrate = self.penrate
        return penrate

    def block(self):
        block = self.block
        return block

    def abnormalstatres(self):
        abnormalstatres = self.abnormalstatres
        return abnormalstatres

    def hp(self):
        hp = self.hp
        return hp

    def hpinc(self):
        hpinc = self.hpinc
        return hpinc

    def mp(self):
        mp = self.mp
        return mp

    def mpinc(self):
        mpinc = self.mpinc
        return mpinc

    def hprec(self):
        hprec = self.hprec
        return hprec

    def mprec(self):
        mprec = self.mprec
        return mprec

    def spd(self):
        spd = self.spd
        return spd

    def jmp(self):
        jmp = self.jmp
        return jmp

    def kbkres(self):
        kbkres = self.kbkres
        return kbkres

    def exp(self):
        exp = self.exp
        return exp

    def dr(self):
        dr = self.dr
        return dr

    def meso(self):
        meso = self.meso
        return meso

    def glincrease(self):
        glincrease = self.glincrease
        return glincrease

    def partyexp(self):
        partyexp = self.partyexp
        return partyexp

    def feverchargeinc(self):
        feverchargeinc = self.feverchargeinc
        return feverchargeinc

    def feverduration(self):
        feverduration = self.feverduration
        return feverduration

    def maxfeverchance(self):
        maxfeverchance = self.maxfeverchance
        return maxfeverchance

    def spmulti(self):
        spmulti = self.spmulti
        return spmulti

    def mempsetcount(self):
        mempsetcount = self.mempsetcount
        return mempsetcount

    def aempsetcount(self):
        aempsetcount = self.aempsetcount
        return aempsetcount

    def necrosetcount(self):
        necrosetcount = self.necrosetcount
        return necrosetcount

    def fafsetcount(self):
        fafsetcount = self.fafsetcount
        return fafsetcount

    def bosssetcount(self):
        bosssetcount = self.bosssetcount
        return bosssetcount

    def commandersetcount(self):
        commandersetcount = self.commandersetcount
        return commandersetcount

    def atklinecount(self):
        atklinecount = self.atklinecount
        return atklinecount

    def crlinecount(self):
        crlinecount = self.crlinecount
        return crlinecount

    def cdlinecount(self):
        cdlinecount = self.cdlinecount
        return cdlinecount
