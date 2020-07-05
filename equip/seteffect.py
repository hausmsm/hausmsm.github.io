class seteffect:
    def __init__(self,empsetcount,necrosetcount,fafsetcount,bosssetcount,cash_type):
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

        self.acc = 0
        self.accp = 0
        self.evd = 0
        self.evdp = 0
        self.penrate = 0
        self.block = 0
        self.abnormalstatres = 0

        self.hp = 0
        self.hpinc = 0
        self.mp = 0
        self.mpinc = 0

        self.spd = 0
        self.jmp = 0
        self.kbkres = 0

        self.exp = 0
        self.dr = 0
        self.meso = 0
        self.glincrease = 0
        self.partyexp = 0
        self.feverchargeinc = 0
        self.feverduration = 0
        self.maxfeverchance = 0
        self.spmulti = 0
        self.empsetcount = empsetcount
        self.necrosetcount = necrosetcount
        self.fafsetcount = fafsetcount
        self.bosssetcount = bosssetcount
        self.cash_type = cash_type
        self.threesetlist = {"1"}
        self.fivesetlist = {"2"}
        # Empress
        if self.empsetcount >= 3:
            self.hp += 1000
            self.pdef += 2500
            self.mdef += 2500
            if self.empsetcount >= 5:
                self.atk += 100
                self.evdp += 5
                if self.empsetcount >= 7:
                    self.atk += 1000
                    self.cr += 3
                    self.accp += 6

        # Necro
        if self.necrosetcount >= 3:
            self.hp += 1000
            self.atkp += 5
            self.dmg += 5
            if self.necrosetcount >= 5:
                self.batk += 10
                if self.necrosetcount >= 7:
                    self.atk += 1500

        # Fafnir
        if self.fafsetcount >= 2:
            self.batk += 2
            if self.fafsetcount >= 3:
                self.cr += 4
                if self.fafsetcount >= 4:
                    self.atk += 950
        # Boss Set
        if self.bosssetcount >= 2:
            self.atk += 50
            self.accp += 0.1
            if self.bosssetcount >= 3:
                self.atk += 50
                self.hp += 500
                self.mp += 500
                self.accp += 0.4
                if self.bosssetcount >= 4:
                    self.atk += 50
                    self.pdef += 500
                    self.mdef += 500
                    self.hp += 500
                    self.mp += 500
                    self.accp += 0.5
                    if self.bosssetcount >= 5:
                        self.atk += 50
                        self.pdef += 500
                        self.mdef += 500
                        self.hp += 500
                        self.mp += 500
                        self.cr += 3
                        self.accp += 0.5
                        self.spd += 0.5
                        if self.bosssetcount >= 6:
                            self.atk += 100
                            self.pdef += 500
                            self.mdef += 500
                            self.hp += 1000
                            self.mp += 1000
                            self.bdef += 2
                            self.cr += 1
                            self.cd += 2
                            self.accp += 0.5
                            self.spd += 0.5
                            if self.bosssetcount >= 7:
                                self.atk += 200
                                self.pdef += 1000
                                self.mdef += 1000
                                self.hp += 1000
                                self.mp += 1000
                                self.batk += 5
                                self.bdef += 3
                                self.cr += 1
                                self.cd += 3
                                self.accp += 1
                                self.spd += 0.5

        # Cash Set
        if self.cash_type in self.threesetlist:
            self.dmg += 10
            self.batk += 20
            self.pdefdec += 10
            self.mdefdec += 10
            self.bdef += 20

        elif self.cash_type in self.fivesetlist:
            self.dmg += 5
            self.batk += 10
            self.pdefdec += 5
            self.mdefdec += 5
            self.bdef += 10
            self.platk += 10
            self.pldef += 10
            self.cr += 10
            self.cd += 10
            self.spd += 25
            self.jmp += 25

        # M Label Pet Sets
        self.atk += 292 + 140 + 140
        self.pdef += 350 + 619 + 350
        self.mdef += 350 + 619 + 350
        self.hp += 938 + 938 + 1581
        self.mp += 224 + 224 + 224

        # M Label Pet Effect
        self.atk += 700
        self.accp += 3
        self.batk += 3
        self.bdef += 3
        self.dmg += 3
        self.cr += 3
        self.cd += 3

        # Soul Effect
        self.maxdmg += 1500000
        self.fd += 18
        self.atk += 200 + 900

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

    def empsetcount(self):
        empsetcount = self.empsetcount
        return empsetcount

    def necrosetcount(self):
        necrosetcount = self.necrosetcount
        return necrosetcount

    def fafsetcount(self):
        fafsetcount = self.fafsetcount
        return fafsetcount
