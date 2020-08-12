from flame.flame import flame


class nonemblemcalculations:
    def __init__(self, commonsum, equip):
        self.flame = flame(equip)
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
        self.empsetcount = 0
        self.necrosetcount = 0
        self.fafsetcount = 0
        self.atkflame = float
        self.atkflamebase = str
        self.crflame = float
        self.crflamebase = str
        self.cdflame = float
        self.cdflamebase = str

        # Common Sum
        self.atk += commonsum.atk
        self.atkp += commonsum.atkp
        self.dmg += commonsum.dmg
        self.batk += commonsum.batk
        self.platk += commonsum.platk
        self.cr += commonsum.cr
        self.cratk += commonsum.cratk
        self.cd += commonsum.cd
        self.maxdmg += commonsum.maxdmg
        self.fd += commonsum.fd

        self.pdef += commonsum.pdef
        self.pdefinc += commonsum.pdefinc
        self.pdefdec += commonsum.pdefdec
        self.mdef += commonsum.mdef
        self.mdefinc += commonsum.mdefinc
        self.mdefdec += commonsum.mdefdec
        self.bdef += commonsum.bdef
        self.pldef += commonsum.pldef
        self.critres += commonsum.critres
        self.critdmgres += commonsum.critdmgres

        self.acc += commonsum.acc
        self.accp += commonsum.accp
        self.evd += commonsum.evd
        self.evdp += commonsum.evdp
        self.penrate += commonsum.penrate
        self.block += commonsum.block
        self.abnormalstatres += commonsum.abnormalstatres

        self.hp += commonsum.hp
        self.hpinc += commonsum.hpinc
        self.mp += commonsum.mp
        self.mpinc += commonsum.mpinc

        self.spd += commonsum.spd
        self.jmp += commonsum.jmp
        self.kbkres += commonsum.kbkres

        self.exp += commonsum.exp
        self.dr += commonsum.dr
        self.meso += commonsum.meso
        self.glincrease += commonsum.glincrease
        self.partyexp += commonsum.partyexp
        self.feverchargeinc += commonsum.feverchargeinc
        self.feverduration += commonsum.feverduration
        self.maxfeverchance += commonsum.maxfeverchance
        self.spmulti += commonsum.spmulti
        self.empsetcount += commonsum.empsetcount
        self.necrosetcount += commonsum.necrosetcount
        self.fafsetcount += commonsum.fafsetcount

        # Equip
        self.atk += equip.atk
        self.atkp += equip.atkp
        self.dmg += equip.dmg
        self.batk += equip.batk
        self.platk += equip.platk
        self.cr += equip.cr
        self.cratk += equip.cratk
        self.cd += equip.cd
        self.maxdmg += equip.maxdmg
        self.fd += equip.fd

        self.pdef += equip.pdef
        self.pdefinc += equip.pdefinc
        self.pdefdec += equip.pdefdec
        self.mdef += equip.mdef
        self.mdefinc += equip.mdefinc
        self.mdefdec += equip.mdefdec
        self.bdef += equip.bdef
        self.pldef += equip.pldef
        self.critres += equip.critres
        self.critdmgres += equip.critdmgres

        self.acc += equip.acc
        self.accp += equip.accp
        self.evd += equip.evd
        self.evdp += equip.evdp
        self.penrate += equip.penrate
        self.block += equip.block
        self.abnormalstatres += equip.abnormalstatres

        self.hp += equip.hp
        self.hpinc += equip.hpinc
        self.mp += equip.mp
        self.mpinc += equip.mpinc

        self.spd += equip.spd
        self.jmp += equip.jmp
        self.kbkres += equip.kbkres

        self.exp += equip.exp
        self.dr += equip.dr
        self.meso += equip.meso
        self.glincrease += equip.glincrease
        self.partyexp += equip.partyexp
        self.feverchargeinc += equip.feverchargeinc
        self.feverduration += equip.feverduration
        self.maxfeverchance += equip.maxfeverchance
        self.spmulti += equip.spmulti
        self.empsetcount += equip.empsetcount
        self.necrosetcount += equip.necrosetcount
        self.fafsetcount += equip.fafsetcount

        # Flamestats
        atkflame = self.flame.fatk()
        self.atk += atkflame
        self.atkflame = atkflame
        atkflamebase = self.flame.fatkbase()
        self.atkflamebase = atkflamebase
        self.atklinecount = self.flame.fatklinecount()

        crflame = self.flame.fcr()
        self.cr += crflame
        self.crflame = crflame
        crflamebase = self.flame.fcrbase()
        self.crflamebase = crflamebase
        self.crlinecount = self.flame.fcrlinecount()

        cdflame = self.flame.fcd()
        self.cd += cdflame
        self.cdflame = cdflame
        cdflamebase = self.flame.fcdbase()
        self.cdflamebase = cdflamebase
        self.cdlinecount = self.flame.fcdlinecount()

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

        def atkflamebase(self):
            atkflamebase = self.atkflamebase
            return atkflamebase

        def crflamebase(self):
            crflamebase = self.crflamebase
            return crflamebase

        def cdflamebase(self):
            cdflamebase = self.cdflamebase
            return cdflamebase

        def atkflame(self):
            atkflame = self.atkflame
            return atkflame

        def crflame(self):
            crflame = self.crflame
            return crflame

        def cdflame(self):
            cdflame = self.cdflame
            return cdflame

        def atklinecount(self):
            atklinecount = self.atklinecount
            return atklinecount

        def crlinecount(self):
            crlinecount = self.crlinecount
            return crlinecount

        def cdlinecount(self):
            cdlinecount = self.cdlinecount
            return cdlinecount
