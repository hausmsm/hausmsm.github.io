import streamlit as st


class seteffect:
    def __init__(self, badge,belt,cash,cape,earring,eye,face,glove,hat,necklace,ring,shoe,shoulder,tbo,weapon,pet):
        # Initialize
        self.emblem = "None"
        self.emblem_amount = 0
        self.normal_emb = 0
        self.unique_acc_emb = 0
        self.legendary_acc_emb = 0
        self.emblem_cd = 0
        self.emblem_batk = 0
        self.emblem_atkp = 0

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

        emblem_cd_stats = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5
        }

        emblem_ba_stats = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5
        }

        emblem_atk_stats = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5
        }

        self.mempsetcount += badge.mempsetcount
        self.aempsetcount += badge.aempsetcount
        self.necrosetcount += badge.necrosetcount
        self.fafsetcount += badge.fafsetcount
        self.bosssetcount += badge.bosssetcount
        self.commandersetcount += badge.commandersetcount

        self.mempsetcount += belt.mempsetcount
        self.aempsetcount += belt.aempsetcount
        self.necrosetcount += belt.necrosetcount
        self.fafsetcount += belt.fafsetcount
        self.bosssetcount += belt.bosssetcount
        self.commandersetcount += belt.commandersetcount

        self.mempsetcount += cape.mempsetcount
        self.aempsetcount += cape.aempsetcount
        self.necrosetcount += cape.necrosetcount
        self.fafsetcount += cape.fafsetcount
        self.bosssetcount += cape.bosssetcount
        self.commandersetcount += cape.commandersetcount

        self.mempsetcount += earring.mempsetcount
        self.aempsetcount += earring.aempsetcount
        self.necrosetcount += earring.necrosetcount
        self.fafsetcount += earring.fafsetcount
        self.bosssetcount += earring.bosssetcount
        self.commandersetcount += earring.commandersetcount

        self.mempsetcount += eye.mempsetcount
        self.aempsetcount += eye.aempsetcount
        self.necrosetcount += eye.necrosetcount
        self.fafsetcount += eye.fafsetcount
        self.bosssetcount += eye.bosssetcount
        self.commandersetcount += eye.commandersetcount

        self.mempsetcount += face.mempsetcount
        self.aempsetcount += face.aempsetcount
        self.necrosetcount += face.necrosetcount
        self.fafsetcount += face.fafsetcount
        self.bosssetcount += face.bosssetcount
        self.commandersetcount += face.commandersetcount

        self.mempsetcount += glove.mempsetcount
        self.aempsetcount += glove.aempsetcount
        self.necrosetcount += glove.necrosetcount
        self.fafsetcount += glove.fafsetcount
        self.bosssetcount += glove.bosssetcount
        self.commandersetcount += glove.commandersetcount

        self.mempsetcount += hat.mempsetcount
        self.aempsetcount += hat.aempsetcount
        self.necrosetcount += hat.necrosetcount
        self.fafsetcount += hat.fafsetcount
        self.bosssetcount += hat.bosssetcount
        self.commandersetcount += hat.commandersetcount

        self.mempsetcount += necklace.mempsetcount
        self.aempsetcount += necklace.aempsetcount
        self.necrosetcount += necklace.necrosetcount
        self.fafsetcount += necklace.fafsetcount
        self.bosssetcount += necklace.bosssetcount
        self.commandersetcount += necklace.commandersetcount

        self.mempsetcount += ring.mempsetcount
        self.aempsetcount += ring.aempsetcount
        self.necrosetcount += ring.necrosetcount
        self.fafsetcount += ring.fafsetcount
        self.bosssetcount += ring.bosssetcount
        self.commandersetcount += ring.commandersetcount

        self.mempsetcount += shoe.mempsetcount
        self.aempsetcount += shoe.aempsetcount
        self.necrosetcount += shoe.necrosetcount
        self.fafsetcount += shoe.fafsetcount
        self.bosssetcount += shoe.bosssetcount
        self.commandersetcount += shoe.commandersetcount

        self.mempsetcount += shoulder.mempsetcount
        self.aempsetcount += shoulder.aempsetcount
        self.necrosetcount += shoulder.necrosetcount
        self.fafsetcount += shoulder.fafsetcount
        self.bosssetcount += shoulder.bosssetcount
        self.commandersetcount += shoulder.commandersetcount

        self.mempsetcount += tbo.mempsetcount
        self.aempsetcount += tbo.aempsetcount
        self.necrosetcount += tbo.necrosetcount
        self.fafsetcount += tbo.fafsetcount
        self.bosssetcount += tbo.bosssetcount
        self.commandersetcount += tbo.commandersetcount

        self.mempsetcount += weapon.mempsetcount
        self.aempsetcount += weapon.aempsetcount
        self.necrosetcount += weapon.necrosetcount
        self.fafsetcount += weapon.fafsetcount
        self.bosssetcount += weapon.bosssetcount
        self.commandersetcount += weapon.commandersetcount

        self.normal_emb += pet.normal_emb
        self.unique_acc_emb += pet.unique_acc_emb
        self.legendary_acc_emb += pet.legendary_acc_emb
        self.emblem_cd += pet.emblem_cd
        self.emblem_batk += pet.emblem_batk
        self.emblem_atkp += pet.emblem_atkp

        self.normal_emb += cash.normal_emb
        self.unique_acc_emb += cash.unique_acc_emb
        self.legendary_acc_emb += cash.legendary_acc_emb
        self.emblem_cd += cash.emblem_cd
        self.emblem_batk += cash.emblem_batk
        self.emblem_atkp += cash.emblem_atkp

        # SF Stats
        self.sf += cash.sf

        # Offensive Stats
        self.atk += cash.atk
        self.atkp += cash.atkp
        self.dmg += cash.dmg
        self.batk += cash.batk
        self.platk += cash.platk
        self.cr += cash.cr
        self.cratk += cash.cratk
        self.cd += cash.cd
        self.maxdmg += cash.maxdmg
        self.fd += cash.fd

        # Defensive Stats
        self.pdef += cash.pdef
        self.pdefinc += cash.pdefinc
        self.pdefdec += cash.pdefdec
        self.mdef += cash.mdef
        self.mdefinc += cash.mdefinc
        self.mdefdec += cash.mdefdec
        self.bdef += cash.bdef
        self.pldef += cash.pldef
        self.critres += cash.critres
        self.critdmgres += cash.critdmgres

        # Hit Miss Stats
        self.acc += cash.acc
        self.accp += cash.accp
        self.evd += cash.evd
        self.evdp += cash.evdp
        self.penrate += cash.penrate
        self.block += cash.block
        self.abnormalstatres += cash.abnormalstatres

        # HP MP Stats
        self.hp += cash.hp
        self.mp += cash.mp
        self.hpinc += cash.hpinc
        self.mpinc += cash.mpinc
        self.hprec += cash.hprec
        self.mprec += cash.mprec
        self.buffdurationinc += cash.buffdurationinc

        # Mobility Stats
        self.spd += cash.spd
        self.jmp += cash.jmp
        self.kbkres += cash.kbkres

        # Misc Stats
        self.exp += cash.exp
        self.dr += cash.dr
        self.meso += cash.meso
        self.glincrease += cash.glincrease
        self.partyexp += cash.partyexp
        self.feverchargeinc += cash.feverchargeinc
        self.feverduration += cash.feverduration
        self.maxfeverchance += cash.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += cash.spmulti

        # Set Stats
        self.mempsetcount += cash.mempsetcount
        self.aempsetcount += cash.aempsetcount
        self.necrosetcount += cash.necrosetcount
        self.fafsetcount += cash.fafsetcount
        self.bosssetcount += cash.bosssetcount
        self.commandersetcount += cash.commandersetcount

        # Flame Stats
        self.atklinecount += cash.atklinecount
        self.crlinecount += cash.crlinecount
        self.cdlinecount += cash.cdlinecount

        # SF Stats
        self.sf += pet.sf

        # Offensive Stats
        self.atk += pet.atk
        self.atkp += pet.atkp
        self.dmg += pet.dmg
        self.batk += pet.batk
        self.platk += pet.platk
        self.cr += pet.cr
        self.cratk += pet.cratk
        self.cd += pet.cd
        self.maxdmg += pet.maxdmg
        self.fd += pet.fd

        # Defensive Stats
        self.pdef += pet.pdef
        self.pdefinc += pet.pdefinc
        self.pdefdec += pet.pdefdec
        self.mdef += pet.mdef
        self.mdefinc += pet.mdefinc
        self.mdefdec += pet.mdefdec
        self.bdef += pet.bdef
        self.pldef += pet.pldef
        self.critres += pet.critres
        self.critdmgres += pet.critdmgres

        # Hit Miss Stats
        self.acc += pet.acc
        self.accp += pet.accp
        self.evd += pet.evd
        self.evdp += pet.evdp
        self.penrate += pet.penrate
        self.block += pet.block
        self.abnormalstatres += pet.abnormalstatres

        # HP MP Stats
        self.hp += pet.hp
        self.mp += pet.mp
        self.hpinc += pet.hpinc
        self.mpinc += pet.mpinc
        self.hprec += pet.hprec
        self.mprec += pet.mprec
        self.buffdurationinc += pet.buffdurationinc

        # Mobility Stats
        self.spd += pet.spd
        self.jmp += pet.jmp
        self.kbkres += pet.kbkres

        # Misc Stats
        self.exp += pet.exp
        self.dr += pet.dr
        self.meso += pet.meso
        self.glincrease += pet.glincrease
        self.partyexp += pet.partyexp
        self.feverchargeinc += pet.feverchargeinc
        self.feverduration += pet.feverduration
        self.maxfeverchance += pet.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += pet.spmulti

        # Set Stats
        self.mempsetcount += pet.mempsetcount
        self.aempsetcount += pet.aempsetcount
        self.necrosetcount += pet.necrosetcount
        self.fafsetcount += pet.fafsetcount
        self.bosssetcount += pet.bosssetcount
        self.commandersetcount += pet.commandersetcount

        # Flame Stats
        self.atklinecount += pet.atklinecount
        self.crlinecount += pet.crlinecount
        self.cdlinecount += pet.cdlinecount

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
        # Mythic Empress Set
        if self.mempsetcount >= 3:
            self.pdef += 2443
            self.mdef += 2443
            self.hp += 189
            if self.mempsetcount >= 5:
                self.atk += 49
                self.evdp += 5
                self.pdef += 2443
                self.mdef += 2443
                self.hp += 189
                if self.mempsetcount >= 7:
                    self.cr += 2
                    self.accp += 5
                    self.atk += 49
                    self.evdp += 5
                    self.pdef += 2443
                    self.mdef += 2443
                    self.hp += 189
        # Ancient Empress Set
        if self.aempsetcount >= 3:
            self.pdef += 2500
            self.mdef += 2500
            self.hp += 1000
            if self.aempsetcount >= 5:
                self.atk += 100
                self.evdp += 5
                self.pdef += 2500
                self.mdef += 2500
                self.hp += 1000
                if self.aempsetcount >= 7:
                    self.atk += 1000
                    self.cr += 3
                    self.accp += 6
                    self.atk += 100
                    self.evdp += 5
                    self.pdef += 2500
                    self.mdef += 2500
                    self.hp += 1000
        # Fafnir
        if self.fafsetcount >= 2:
            self.batk += 2
            if self.fafsetcount >= 3:
                self.cr += 4
                if self.fafsetcount >= 4:
                    self.atk += 950
        # Necro
        if self.necrosetcount >= 3:
            self.hp += 1000
            self.atkp += 5
            self.dmg += 5
            if self.necrosetcount >= 5:
                self.batk += 10
                if self.necrosetcount >= 7:
                    self.atk += 1500

    def normal_emb(self):
        normal_emb = self.normal_emb
        return normal_emb

    def unique_acc_emb(self):
        unique_acc_emb = self.unique_acc_emb
        return unique_acc_emb

    def legendary_acc_emb(self):
        legendary_acc_emb = self.legendary_acc_emb
        return legendary_acc_emb

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