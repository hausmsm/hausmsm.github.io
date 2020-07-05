from common.buffs import buffs
from common.link import link
from common.mapletree import mapletree

class commonsum:
    def __init__(self, type, character_class):
        buff = buffs(type, character_class)
        lk = link()
        mt = mapletree()

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

        # Buff
        self.atk += buff.atk
        self.atkp += buff.atkp
        self.dmg += buff.dmg
        self.batk += buff.batk
        self.platk += buff.platk
        self.cr += buff.cr
        self.cratk += buff.cratk
        self.cd += buff.cd
        self.maxdmg += buff.maxdmg
        self.fd += buff.fd

        self.pdef += buff.pdef
        self.pdefinc += buff.pdefinc
        self.pdefdec += buff.pdefdec
        self.mdef += buff.mdef
        self.mdefinc += buff.mdefinc
        self.mdefdec += buff.mdefdec
        self.bdef += buff.bdef
        self.pldef += buff.pldef
        self.critres += buff.critres
        self.critdmgres += buff.critdmgres

        self.acc += buff.acc
        self.accp += buff.accp
        self.evd += buff.evd
        self.evdp += buff.evdp
        self.penrate += buff.penrate
        self.block += buff.block
        self.abnormalstatres += buff.abnormalstatres

        self.hp += buff.hp
        self.hpinc += buff.hpinc
        self.mp += buff.mp
        self.mpinc += buff.mpinc

        self.spd += buff.spd
        self.jmp += buff.jmp
        self.kbkres += buff.kbkres

        self.exp += buff.exp
        self.dr += buff.dr
        self.meso += buff.meso
        self.glincrease += buff.glincrease
        self.partyexp += buff.partyexp
        self.feverchargeinc += buff.feverchargeinc
        self.feverduration += buff.feverduration
        self.maxfeverchance += buff.maxfeverchance
        self.spmulti += buff.spmulti
        self.empsetcount += buff.empsetcount
        self.necrosetcount += buff.necrosetcount
        self.fafsetcount += buff.fafsetcount

        # Link
        self.atk += lk.atk
        self.atkp += lk.atkp
        self.dmg += lk.dmg
        self.batk += lk.batk
        self.platk += lk.platk
        self.cr += lk.cr
        self.cratk += lk.cratk
        self.cd += lk.cd
        self.maxdmg += lk.maxdmg
        self.fd += lk.fd

        self.pdef += lk.pdef
        self.pdefinc += lk.pdefinc
        self.pdefdec += lk.pdefdec
        self.mdef += lk.mdef
        self.mdefinc += lk.mdefinc
        self.mdefdec += lk.mdefdec
        self.bdef += lk.bdef
        self.pldef += lk.pldef
        self.critres += lk.critres
        self.critdmgres += lk.critdmgres

        self.acc += lk.acc
        self.accp += lk.accp
        self.evd += lk.evd
        self.evdp += lk.evdp
        self.penrate += lk.penrate
        self.block += lk.block
        self.abnormalstatres += lk.abnormalstatres

        self.hp += lk.hp
        self.hpinc += lk.hpinc
        self.mp += lk.mp
        self.mpinc += lk.mpinc

        self.spd += lk.spd
        self.jmp += lk.jmp
        self.kbkres += lk.kbkres

        self.exp += lk.exp
        self.dr += lk.dr
        self.meso += lk.meso
        self.glincrease += lk.glincrease
        self.partyexp += lk.partyexp
        self.feverchargeinc += lk.feverchargeinc
        self.feverduration += lk.feverduration
        self.maxfeverchance += lk.maxfeverchance
        self.spmulti += lk.spmulti
        self.empsetcount += lk.empsetcount
        self.necrosetcount += lk.necrosetcount
        self.fafsetcount += lk.fafsetcount

        # Maple Tree
        self.atk += mt.atk
        self.atkp += mt.atkp
        self.dmg += mt.dmg
        self.batk += mt.batk
        self.platk += mt.platk
        self.cr += mt.cr
        self.cratk += mt.cratk
        self.cd += mt.cd
        self.maxdmg += mt.maxdmg
        self.fd += mt.fd

        self.pdef += mt.pdef
        self.pdefinc += mt.pdefinc
        self.pdefdec += mt.pdefdec
        self.mdef += mt.mdef
        self.mdefinc += mt.mdefinc
        self.mdefdec += mt.mdefdec
        self.bdef += mt.bdef
        self.pldef += mt.pldef
        self.critres += mt.critres
        self.critdmgres += mt.critdmgres

        self.acc += mt.acc
        self.accp += mt.accp
        self.evd += mt.evd
        self.evdp += mt.evdp
        self.penrate += mt.penrate
        self.block += mt.block
        self.abnormalstatres += mt.abnormalstatres

        self.hp += mt.hp
        self.hpinc += mt.hpinc
        self.mp += mt.mp
        self.mpinc += mt.mpinc

        self.spd += mt.spd
        self.jmp += mt.jmp
        self.kbkres += mt.kbkres

        self.exp += mt.exp
        self.dr += mt.dr
        self.meso += mt.meso
        self.glincrease += mt.glincrease
        self.partyexp += mt.partyexp
        self.feverchargeinc += mt.feverchargeinc
        self.feverduration += mt.feverduration
        self.maxfeverchance += mt.maxfeverchance
        self.spmulti += mt.spmulti
        self.empsetcount += mt.empsetcount
        self.necrosetcount += mt.necrosetcount
        self.fafsetcount += mt.fafsetcount

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