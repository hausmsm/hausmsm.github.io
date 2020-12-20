from scipy.optimize import minimize


class emblemcalculations:
    def __init__(self, nec, character):
        self.nb_poutput = 0
        self.b_poutput = 0
        self.nb_soutput = 0
        self.b_soutput = 0

        char = character.char

        self.cd_normalemb = 20
        self.batk_normalemb = 10
        self.atkp_normalemb = 10

        self.cd_uniqueemb = 1
        self.batk_uniqueemb = 1
        self.atkp_uniqueemb = 1

        self.cd_legendaryemb = 5
        self.batk_legendaryemb = 5
        self.atkp_legendaryemb = 5

        self.ncdnormalemb = 0
        self.natkpnormalemb = 0
        self.nbatknormalemb = 0

        self.stat_amount = 0
        self.emblem_amount = 0
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

        self.normal_emb += nec.normal_emb
        self.unique_acc_emb += nec.unique_acc_emb
        self.legendary_acc_emb += nec.legendary_acc_emb
        self.emblem_cd += nec.emblem_cd
        self.emblem_batk += nec.emblem_batk
        self.emblem_atkp += nec.emblem_atkp

        # SF Stats
        self.sf += nec.sf

        # Offensive Stats
        self.atk += nec.atk
        self.atkp += nec.atkp
        self.dmg += nec.dmg
        self.batk += nec.batk
        self.platk += nec.platk
        self.cr += nec.cr
        self.cratk += nec.cratk
        self.cd += nec.cd
        self.maxdmg += nec.maxdmg
        self.fd += nec.fd

        # Defensive Stats
        self.pdef += nec.pdef
        self.pdefinc += nec.pdefinc
        self.pdefdec += nec.pdefdec
        self.mdef += nec.mdef
        self.mdefinc += nec.mdefinc
        self.mdefdec += nec.mdefdec
        self.bdef += nec.bdef
        self.pldef += nec.pldef
        self.critres += nec.critres
        self.critdmgres += nec.critdmgres

        # Hit Miss Stats
        self.acc += nec.acc
        self.accp += nec.accp
        self.evd += nec.evd
        self.evdp += nec.evdp
        self.penrate += nec.penrate
        self.block += nec.block
        self.abnormalstatres += nec.abnormalstatres

        # HP MP Stats
        self.hp += nec.hp
        self.mp += nec.mp
        self.hpinc += nec.hpinc
        self.mpinc += nec.mpinc
        self.hprec += nec.hprec
        self.mprec += nec.mprec
        self.buffdurationinc += nec.buffdurationinc

        # Mobility Stats
        self.spd += nec.spd
        self.jmp += nec.jmp
        self.kbkres += nec.kbkres

        # Misc Stats
        self.exp += nec.exp
        self.dr += nec.dr
        self.meso += nec.meso
        self.glincrease += nec.glincrease
        self.partyexp += nec.partyexp
        self.feverchargeinc += nec.feverchargeinc
        self.feverduration += nec.feverduration
        self.maxfeverchance += nec.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += nec.spmulti

        # Set Stats
        self.mempsetcount += nec.mempsetcount
        self.aempsetcount += nec.aempsetcount
        self.necrosetcount += nec.necrosetcount
        self.fafsetcount += nec.fafsetcount
        self.bosssetcount += nec.bosssetcount
        self.commandersetcount += nec.commandersetcount

        # Flame Stats
        self.atklinecount += nec.atklinecount
        self.crlinecount += nec.crlinecount
        self.cdlinecount += nec.cdlinecount

        self.pname = char.pname
        self.pskilldmg = char.sskilldmg
        self.phitcount = char.phitcount
        self.phatkp = char.phatkp
        self.phdmg = char.phdmg
        self.phbatk = char.phbatk
        self.phcr = char.phcr
        self.phcd = char.phcd
        self.phfd = char.phfd

        self.sname = char.sname
        self.sskilldmg = char.sskilldmg
        self.shitcount = char.shitcount
        self.schance = char.schance
        self.shatkp = char.shatkp
        self.shdmg = char.shdmg
        self.shbatk = char.shbatk
        self.shcr = char.shcr
        self.shcd = char.shcd
        self.shfd = char.shfd

        if self.cr >= 90:
            self.croverflow = 90.0
        else:
            self.croverflow = self.cr

        def objective(x):
            cd = x[0] * self.cd_normalemb + x[3]*self.cd_uniqueemb + x[6]*self.cd_legendaryemb
            atkp = x[1] * self.atkp_normalemb + x[4]*self.atkp_uniqueemb + x[7]*self.atkp_legendaryemb
            batk = x[2] * self.batk_normalemb + x[5]*self.batk_uniqueemb + x[8]*self.batk_legendaryemb
            obj = -((1 + ((self.atkp + atkp) / 100) + (
                    ((self.pskilldmg / 100) + (self.phbatk / 100)) * ((self.batk + batk) / 100))) \
                    * (1 + ((self.cd + cd) / 100) + (self.phcd / 100) + 0.2))
            return obj

        def constraint1(x):
            sum = self.normal_emb
            sum = sum - x[0] - x[1] - x[2]
            return sum

        def constraint2(x):
            sum = self.unique_acc_emb
            sum = sum - x[3] - x[4] - x[5]
            return sum

        def constraint3(x):
            sum = self.legendary_acc_emb
            sum = sum - x[6] - x[7] - x[8]
            return sum

        cd_normalamount = self.normal_emb * 20
        cd_uniqueamount = self.unique_acc_emb * 1
        cd_legendaryamount = self.legendary_acc_emb * 5
        atkp_normalamount = self.normal_emb * 10
        atkp_uniqueamount = self.unique_acc_emb * 1
        atkp_legendaryamount = self.legendary_acc_emb * 5
        batk_normalamount = self.normal_emb * 10
        batk_uniqueamount = self.unique_acc_emb * 1
        batk_legendaryamount = self.legendary_acc_emb * 5

        x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        cd_normalbound = (0, cd_normalamount)
        atkp_normalbound = (0, atkp_normalamount)
        batk_normalbound = (0, batk_normalamount)
        cd_uniquebound = (0, cd_uniqueamount)
        atkp_uniquebound = (0, atkp_uniqueamount)
        batk_uniquebound = (0, batk_uniqueamount)
        cd_legendarybound = (0, cd_legendaryamount)
        atkp_legendarybound = (0, atkp_legendaryamount)
        batk_legendarybound = (0, batk_legendaryamount)
        bnds = (cd_normalbound, atkp_normalbound, batk_normalbound, cd_uniquebound, atkp_uniquebound, batk_uniquebound,
                cd_legendarybound, atkp_legendarybound, batk_legendarybound)
        cons = [{'type': 'eq', 'fun': constraint1}, {'type': 'eq', 'fun': constraint2}, {'type': 'eq', 'fun': constraint3}]
        sol = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)

        ncdnormalemb = int(round(sol.x[0]))
        natkpnormalemb = int(round(sol.x[1]))
        nbatknormalemb = int(round(sol.x[2]))
        ncduniqueemb = int(round(sol.x[3]))
        natkpuniqueemb = int(round(sol.x[4]))
        nbatkuniqueemb = int(round(sol.x[5]))
        ncdlegendaryemb = int(round(sol.x[6]))
        natkplegendaryemb = int(round(sol.x[7]))
        nbatklegendaryemb = int(round(sol.x[8]))

        self.ncdnormalemb = ncdnormalemb
        self.natkpnormalemb = natkpnormalemb
        self.nbatknormalemb = nbatknormalemb

        self.ncduniqueemb = ncduniqueemb
        self.natkpuniqueemb = natkpuniqueemb
        self.nbatkuniqueemb = nbatkuniqueemb

        self.ncdlegendaryemb = ncdlegendaryemb
        self.natkplegendaryemb = natkplegendaryemb
        self.nbatklegendaryemb = nbatklegendaryemb

        self.embatkp = (self.atkp_normalemb * self.natkpnormalemb) + (self.atkp_uniqueemb * self.natkpuniqueemb) + \
                       (self.atkp_legendaryemb * self.natkplegendaryemb)
        self.embbatk = (self.batk_normalemb * self.nbatknormalemb) + (self.batk_uniqueemb * self.nbatkuniqueemb) + \
                       (self.batk_legendaryemb * self.nbatklegendaryemb)
        self.embcd = (self.cd_normalemb * self.ncdnormalemb) + (self.cd_uniqueemb * self.ncduniqueemb) + \
                     (self.cd_legendaryemb * self.ncdlegendaryemb)

        # FIRST EMBLEM COMBINATION
        # Primary Skill
        # Non Boss Non Crit
        self.nb_nc_poutput = self.atk \
                             * (1 + (self.dmg / 100)) \
                             * (1 + ((self.atkp + self.embatkp) / 100)) \
                             * (1 + ((self.dmg / 100) * (self.phdmg / 100))) \
                             * (self.pskilldmg / 100) \
                             * self.phitcount \
                             * (1 + (self.fd / 100)) \
                             * (1 + (self.spmulti / 100))
        # Non Boss Crit
        self.nb_c_poutput = self.atk \
                            * (1 + (self.dmg / 100)) \
                            * (1 + ((self.atkp + self.embatkp) / 100)) \
                            * (1 + ((self.dmg / 100) * (self.phdmg / 100))) \
                            * (1 + ((self.cd + self.embcd) / 100) + (self.phcd / 100) + 0.2) \
                            * (self.pskilldmg / 100) \
                            * self.phitcount \
                            * (1 + (self.fd / 100)) \
                            * (1 + (self.spmulti / 100))
        # Non Boss Average
        self.nb_poutput = int(
            round((((self.nb_c_poutput * self.croverflow) + ((100.0 - self.croverflow) * self.nb_nc_poutput)) / 100),
                  0))
        # Boss Non Crit
        self.b_nc_poutput = self.atk \
                            * (1 + (self.dmg / 100)) \
                            * (1 + ((self.atkp + self.embatkp) / 100) + (
                ((self.pskilldmg / 100) + (self.phbatk / 100)) * ((self.batk + self.embbatk) / 100))) \
                            * (1 + ((self.dmg / 100) * (self.phdmg / 100))) \
                            * (self.pskilldmg / 100) \
                            * self.phitcount \
                            * (1 + (self.fd / 100)) \
                            * (1 + (self.spmulti / 100))
        # Boss Crit
        self.b_c_poutput = self.atk \
                           * (1 + (self.dmg / 100)) \
                           * (1 + ((self.atkp + self.embatkp) / 100) + (
                ((self.pskilldmg / 100) + (self.phbatk / 100)) * ((self.batk + self.embbatk) / 100))) \
                           * (1 + ((self.dmg / 100) * (self.phdmg / 100))) \
                           * (1 + ((self.cd + self.embcd) / 100) + (self.phcd / 100) + 0.2) \
                           * (self.pskilldmg / 100) \
                           * self.phitcount \
                           * (1 + (self.fd / 100)) \
                           * (1 + (self.spmulti / 100))

        self.b_poutput = int(
            round((((self.b_c_poutput * self.croverflow) + ((100.0 - self.croverflow) * self.b_nc_poutput)) / 100), 0))

        # Secondary Skill
        # Non Boss Non Crit
        self.nb_nc_soutput = self.atk \
                             * (1 + (self.dmg / 100)) \
                             * (1 + ((self.atkp + self.embatkp) / 100)) \
                             * (1 + ((self.dmg / 100) * (self.shdmg / 100))) \
                             * (self.sskilldmg / 100) \
                             * self.shitcount \
                             * (1 + (self.fd / 100)) \
                             * (1 + (self.spmulti / 100))
        # Non Boss Crit
        self.nb_c_soutput = self.atk \
                            * (1 + (self.dmg / 100)) \
                            * (1 + ((self.atkp + self.embatkp) / 100)) \
                            * (1 + ((self.dmg / 100) * (self.shdmg / 100))) \
                            * (1 + ((self.cd + self.embcd) / 100) + (self.shcd / 100) + 0.2) \
                            * (self.sskilldmg / 100) \
                            * self.shitcount \
                            * (1 + (self.fd / 100)) \
                            * (1 + (self.spmulti / 100))
        # Non Boss Average
        self.nb_soutput = int(round(((((self.nb_c_soutput * self.croverflow) + ((100.0 - self.croverflow) * self.nb_nc_soutput)) / 100)
                                     * (self.schance / 100)), 0))

        # Boss Non Crit
        self.b_nc_soutput = self.atk \
                            * (1 + (self.dmg / 100)) \
                            * (1 + ((self.atkp + self.embatkp) / 100) + (
                ((self.sskilldmg / 100) + (self.shbatk / 100)) * ((self.batk + self.embbatk) / 100))) \
                            * (1 + ((self.dmg / 100) * (self.shdmg / 100))) \
                            * (self.sskilldmg / 100) \
                            * self.shitcount \
                            * (1 + (self.fd / 100)) \
                            * (1 + (self.spmulti / 100))

        # Boss Crit
        self.b_c_soutput = self.atk \
                           * (1 + (self.dmg / 100)) \
                           * (1 + ((self.atkp + self.embatkp) / 100) + (
                ((self.sskilldmg / 100) + (self.shbatk / 100)) * ((self.batk + self.embbatk) / 100))) \
                           * (1 + ((self.dmg / 100) * (self.shdmg / 100))) \
                           * (1 + ((self.cd + self.embcd) / 100) + (self.shcd / 100) + 0.2) \
                           * (self.sskilldmg / 100) \
                           * self.shitcount \
                           * (1 + (self.fd / 100)) \
                           * (1 + self.spmulti / 100)

        self.b_soutput = int(
            round((((self.b_c_soutput * self.croverflow) + ((100.0 - self.croverflow) * self.b_nc_soutput)) / 100 \
                   * (self.schance / 100)), 0))

        self.secondncdnormalemb = ncdnormalemb - 1
        self.secondnbatknormalemb = nbatknormalemb + 1
        self.secondnatkpnormalemb = natkpnormalemb

        self.sembatkp = (self.atkp_normalemb * self.secondnatkpnormalemb) + (self.atkp_uniqueemb * self.natkpuniqueemb) + \
                       (self.atkp_legendaryemb * self.natkplegendaryemb)
        self.sembbatk = (self.batk_normalemb * self.secondnbatknormalemb) + (self.batk_uniqueemb * self.nbatkuniqueemb) + \
                       (self.batk_legendaryemb * self.nbatklegendaryemb)
        self.sembcd = (self.cd_normalemb * self.secondncdnormalemb) + (self.cd_uniqueemb * self.ncduniqueemb) + \
                     (self.cd_legendaryemb * self.ncdlegendaryemb)

        self.atkp += self.embatkp
        self.batk += self.embbatk
        self.cd += self.embcd

    def ncdnormalemb(self):
        ncdnormalemb = self.ncdnormalemb
        return ncdnormalemb

    def natkpnormalemb(self):
        natkpnormalemb = self.natkpnormalemb
        return natkpnormalemb

    def nbatknormalemb(self):
        nbatknormalemb = self.nbatknormalemb
        return nbatknormalemb

    def ncduniqueemb(self):
        ncduniqueemb = self.ncduniqueemb
        return ncduniqueemb

    def natkpuniqueemb(self):
        natkpuniqueemb = self.natkpuniqueemb
        return natkpuniqueemb

    def nbatkuniqueemb(self):
        nbatkuniqueemb = self.nbatkuniqueemb
        return nbatkuniqueemb

    def ncdlegendaryemb(self):
        ncdlegendaryemb = self.ncdlegendaryemb
        return ncdlegendaryemb

    def natkplegendaryemb(self):
        natkplegendaryemb = self.natkplegendaryemb
        return natkplegendaryemb

    def nbatklegendaryemb(self):
        nbatklegendaryemb = self.nbatklegendaryemb
        return nbatklegendaryemb

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

    def nb_poutput(self):
        nb_poutput = self.nb_poutput
        return nb_poutput

    def b_poutput(self):
        b_poutput = self.b_poutput
        return b_poutput

    def nbsoutput(self):
        nb_soutput = self.nb_soutput
        return nb_soutput

    def b_soutput(self):
        b_soutput = self.b_soutput
        return b_soutput

    def pname(self):
        pname = self.pname
        return pname

    def sname(self):
        sname = self.sname
        return sname
