from scipy.optimize import minimize

class emblemcalculations:
    def __init__(self, necalculations, char):
        self.cdemb = 20
        self.batkemb = 10
        self.atkpemb = 10

        self.atk = necalculations.atk
        self.atkp = necalculations.atkp
        self.dmg = necalculations.dmg
        self.batk = necalculations.batk
        self.platk = necalculations.platk
        self.cr = necalculations.cr
        self.cratk = necalculations.cratk
        self.cd = necalculations.cd
        self.maxdmg = necalculations.maxdmg
        self.fd = necalculations.fd

        self.pdef = necalculations.pdef
        self.pdefinc = necalculations.pdefinc
        self.pdefdec = necalculations.pdefdec
        self.mdef = necalculations.mdef
        self.mdefinc = necalculations.mdefinc
        self.mdefdec = necalculations.mdefdec
        self.bdef = necalculations.bdef
        self.pldef = necalculations.pldef
        self.critres = necalculations.critres
        self.critdmgres = necalculations.critdmgres

        self.acc = necalculations.acc
        self.accp = necalculations.accp
        self.evd = necalculations.evd
        self.evdp = necalculations.evdp
        self.penrate = necalculations.penrate
        self.block = necalculations.block
        self.abnormalstatres = necalculations.abnormalstatres

        self.hp = necalculations.hp
        self.hpinc = necalculations.hpinc
        self.mp = necalculations.mp
        self.mpinc = necalculations.mpinc

        self.spd = necalculations.spd
        self.jmp = necalculations.jmp
        self.kbkres = necalculations.kbkres

        self.exp = necalculations.exp
        self.dr = necalculations.dr
        self.meso = necalculations.meso
        self.glincrease = necalculations.glincrease
        self.partyexp = necalculations.partyexp
        self.feverchargeinc = necalculations.feverchargeinc
        self.feverduration = necalculations.feverduration
        self.maxfeverchance = necalculations.maxfeverchance
        self.spmulti = necalculations.spmulti
        self.empsetcount = necalculations.empsetcount
        self.necrosetcount = necalculations.necrosetcount
        self.fafsetcount = necalculations.fafsetcount

        self.pname = char.pname
        self.pskilldmg = char.pskilldmg
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

        self.pname = char.pname
        self.sname = char.sname

        print(self.cd)

        if self.cr >= 90:
            self.croverflow = 90.0
        else:
            self.croverflow = self.cr

        def objective(x):
            cd = x[0] * self.cdemb
            atkp = x[1] * self.atkpemb
            batk = x[2] * self.batkemb
            obj = -((1 + ((self.atkp + atkp)/ 100) + (((self.pskilldmg / 100) + (self.phbatk / 100)) * ((self.batk + batk) / 100))) \
                   * (1 + ((self.cd + cd) / 100) + (self.phcd / 100) + 0.2))
            return obj

        def constraint1(x):
            sum = 8
            sum = sum - x[0] - x[1] - x[2]
            return sum


        x0 =[0,0,0]
        bound = (0,8)
        bnds = (bound,bound,bound)
        cons = {'type': 'eq', 'fun': constraint1}
        sol = minimize(objective,x0, method ='SLSQP',bounds=bnds,constraints=cons)

        ncdemb = int(round(sol.x[0]))
        natkpemb = int(round(sol.x[1]))
        nbatkemb = int(round(sol.x[2]))

        self.ncdemb = ncdemb
        self.natkpemb = natkpemb
        self.nbatkemb = nbatkemb

        self.embatkp = (self.atkpemb * self.natkpemb)
        self.embbatk = (self.batkemb * self.nbatkemb)
        self.embcd = (self.cdemb * self.ncdemb)

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
                             * (1 + self.spmulti/100)
        # Non Boss Crit
        self.nb_c_poutput = self.atk \
                            * (1 + (self.dmg / 100)) \
                            * (1 + ((self.atkp + self.embatkp) / 100)) \
                            * (1 + ((self.dmg / 100) * (self.phdmg / 100))) \
                            * (1 + ((self.cd + self.embcd) / 100) + (self.phcd / 100) + 0.2) \
                            * (self.pskilldmg / 100) \
                            * self.phitcount \
                            * (1 + (self.fd / 100)) \
                            * (1 + self.spmulti/100)
        # Non Boss Average
        self.nb_poutput = int(round((((self.nb_c_poutput * self.croverflow) + ((100.0 - self.croverflow) * self.nb_nc_poutput)) / 100), 0))
        # Boss Non Crit
        self.b_nc_poutput = self.atk \
                            * (1 + (self.dmg / 100)) \
                            * (1 + ((self.atkp + self.embatkp) / 100) + (((self.pskilldmg / 100) + (self.phbatk / 100)) * ((self.batk + self.embbatk) / 100))) \
                            * (1 + ((self.dmg / 100) * (self.phdmg / 100))) \
                            * (self.pskilldmg / 100) \
                            * self.phitcount \
                            * (1 + (self.fd / 100)) \
                            * (1 + self.spmulti/100)
        # Boss Crit
        self.b_c_poutput = self.atk \
                           * (1 + (self.dmg / 100)) \
                           * (1 + ((self.atkp + self.embatkp) / 100) + (((self.pskilldmg / 100) + (self.phbatk / 100)) * ((self.batk + self.embbatk) / 100))) \
                           * (1 + ((self.dmg / 100) * (self.phdmg / 100))) \
                           * (1 + ((self.cd + self.embcd) / 100) + (self.phcd / 100) + 0.2) \
                           * (self.pskilldmg / 100) \
                           * self.phitcount \
                           * (1 + (self.fd / 100)) \
                           * (1 + self.spmulti/100)

        self.b_poutput = int(round((((self.b_c_poutput * self.croverflow) + ((100.0 - self.croverflow) * self.b_nc_poutput)) / 100), 0))

        # Secondary Skill
        # Non Boss Non Crit
        self.nb_nc_soutput = self.atk \
                             * (1 + (self.dmg / 100)) \
                             * (1 + ((self.atkp + self.embatkp) / 100)) \
                             * (1 + ((self.dmg / 100) * (self.shdmg / 100))) \
                             * (self.sskilldmg / 100) \
                             * self.shitcount \
                             * (1 + (self.fd / 100)) \
                             * (1 + self.spmulti/100)
        # Non Boss Crit
        self.nb_c_soutput = self.atk \
                            * (1 + (self.dmg / 100)) \
                            * (1 + ((self.atkp + self.embatkp) / 100)) \
                            * (1 + ((self.dmg / 100) * (self.shdmg / 100))) \
                            * (1 + ((self.cd + self.embcd) / 100) + (self.shcd / 100) + 0.2) \
                            * (self.sskilldmg / 100) \
                            * self.shitcount \
                            * (1 + (self.fd / 100)) \
                            * (1 + self.spmulti/100)
        # Non Boss Average
        self.nb_soutput = int(round((((self.nb_c_soutput * self.croverflow) + ((100.0 - self.croverflow) * self.nb_nc_soutput)) / 100), 0))

        # Boss Non Crit
        self.b_nc_soutput = self.atk \
                            * (1 + (self.dmg / 100)) \
                            * (1 + ((self.atkp + self.embatkp) / 100) + (((self.sskilldmg / 100) + (self.shbatk / 100)) * ((self.batk + self.embbatk)/ 100))) \
                            * (1 + ((self.dmg / 100) * (self.shdmg / 100))) \
                            * (self.sskilldmg / 100) \
                            * self.shitcount \
                            * (1 + (self.fd / 100)) \
                            * (1 + self.spmulti/100)
        # Boss Crit
        self.b_c_soutput = self.atk \
                           * (1 + (self.dmg / 100)) \
                           * (1 + ((self.atkp + self.embatkp) / 100) + (((self.sskilldmg / 100) + (self.shbatk / 100)) * ((self.batk + self.embbatk) / 100))) \
                           * (1 + ((self.dmg / 100) * (self.shdmg / 100))) \
                           * (1 + ((self.cd + self.embcd) / 100) + (self.shcd / 100) + 0.2) \
                           * (self.sskilldmg / 100) \
                           * self.shitcount \
                           * (1 + (self.fd / 100)) \
                           * (1 + self.spmulti/100)

        self.b_soutput = int(round((((self.b_c_soutput * self.croverflow) + ((100.0 - self.croverflow) * self.b_nc_soutput)) / 100 \
                         * (self.schance/100)), 0))

        self.secondncdemb = ncdemb - 1
        self.secondnbatkemb = nbatkemb + 1
        self.secondnatkpemb = natkpemb

        self.sembatkp = (self.atkpemb * self.secondnatkpemb)
        self.sembbatk = (self.batkemb * self.secondnbatkemb)
        self.sembcd = (self.cdemb * self.secondncdemb)

        # SECOND EMBLEM COMBINATION
        # Primary Skill
        # Non Boss Non Crit
        self.snb_nc_poutput = self.atk \
                             * (1 + (self.dmg / 100)) \
                             * (1 + ((self.atkp + self.sembatkp) / 100)) \
                             * (1 + ((self.dmg / 100) * (self.phdmg / 100))) \
                             * (self.pskilldmg / 100) \
                             * self.phitcount \
                             * (1 + (self.fd / 100)) \
                             * (1 + self.spmulti / 100)
        # Non Boss Crit
        self.snb_c_poutput = self.atk \
                            * (1 + (self.dmg / 100)) \
                            * (1 + ((self.atkp + self.sembatkp) / 100)) \
                            * (1 + ((self.dmg / 100) * (self.phdmg / 100))) \
                            * (1 + ((self.cd + self.sembcd) / 100) + (self.phcd / 100) + 0.2) \
                            * (self.pskilldmg / 100) \
                            * self.phitcount \
                            * (1 + (self.fd / 100)) \
                            * (1 + self.spmulti / 100)
        # Non Boss Average
        self.snb_poutput = int(
            round((((self.snb_c_poutput * self.croverflow) + ((100.0 - self.croverflow) * self.snb_nc_poutput)) / 100),
                  0))
        # Boss Non Crit
        self.sb_nc_poutput = self.atk \
                            * (1 + (self.dmg / 100)) \
                            * (1 + ((self.atkp + self.sembatkp) / 100) + (
                    ((self.pskilldmg / 100) + (self.phbatk / 100)) * ((self.batk + self.sembbatk) / 100))) \
                            * (1 + ((self.dmg / 100) * (self.phdmg / 100))) \
                            * (self.pskilldmg / 100) \
                            * self.phitcount \
                            * (1 + (self.fd / 100)) \
                            * (1 + self.spmulti / 100)
        # Boss Crit
        self.sb_c_poutput = self.atk \
                           * (1 + (self.dmg / 100)) \
                           * (1 + ((self.atkp + self.sembatkp) / 100) + (
                    ((self.pskilldmg / 100) + (self.phbatk / 100)) * ((self.batk + self.sembbatk) / 100))) \
                           * (1 + ((self.dmg / 100) * (self.phdmg / 100))) \
                           * (1 + ((self.cd + self.sembcd) / 100) + (self.phcd / 100) + 0.2) \
                           * (self.pskilldmg / 100) \
                           * self.phitcount \
                           * (1 + (self.fd / 100)) \
                           * (1 + self.spmulti / 100)

        self.sb_poutput = int(
            round((((self.sb_c_poutput * self.croverflow) + ((100.0 - self.croverflow) * self.sb_nc_poutput)) / 100), 0))

        # Secondary Skill
        # Non Boss Non Crit
        self.snb_nc_soutput = self.atk \
                             * (1 + (self.dmg / 100)) \
                             * (1 + ((self.atkp + self.sembatkp) / 100)) \
                             * (1 + ((self.dmg / 100) * (self.shdmg / 100))) \
                             * (self.sskilldmg / 100) \
                             * self.shitcount \
                             * (1 + (self.fd / 100)) \
                             * (1 + self.spmulti / 100)
        # Non Boss Crit
        self.snb_c_soutput = self.atk \
                            * (1 + (self.dmg / 100)) \
                            * (1 + ((self.atkp + self.sembatkp) / 100)) \
                            * (1 + ((self.dmg / 100) * (self.shdmg / 100))) \
                            * (1 + ((self.cd + self.sembcd) / 100) + (self.shcd / 100) + 0.2) \
                            * (self.sskilldmg / 100) \
                            * self.shitcount \
                            * (1 + (self.fd / 100)) \
                            * (1 + self.spmulti / 100)
        # Non Boss Average
        self.snb_soutput = int(
            round((((self.snb_c_soutput * self.croverflow) + ((100.0 - self.croverflow) * self.snb_nc_soutput)) / 100),
                  0))

        # Boss Non Crit
        self.sb_nc_soutput = self.atk \
                            * (1 + (self.dmg / 100)) \
                            * (1 + ((self.atkp + self.sembatkp) / 100) + (
                    ((self.sskilldmg / 100) + (self.shbatk / 100)) * ((self.batk + self.sembbatk) / 100))) \
                            * (1 + ((self.dmg / 100) * (self.shdmg / 100))) \
                            * (self.sskilldmg / 100) \
                            * self.shitcount \
                            * (1 + (self.fd / 100)) \
                            * (1 + self.spmulti / 100)
        # Boss Crit
        self.sb_c_soutput = self.atk \
                           * (1 + (self.dmg / 100)) \
                           * (1 + ((self.atkp + self.sembatkp) / 100) + (
                    ((self.sskilldmg / 100) + (self.shbatk / 100)) * ((self.batk + self.sembbatk) / 100))) \
                           * (1 + ((self.dmg / 100) * (self.shdmg / 100))) \
                           * (1 + ((self.cd + self.sembcd) / 100) + (self.shcd / 100) + 0.2) \
                           * (self.sskilldmg / 100) \
                           * self.shitcount \
                           * (1 + (self.fd / 100)) \
                           * (1 + self.spmulti / 100)

        self.sb_soutput = int(
            round((((self.sb_c_soutput * self.croverflow) + ((100.0 - self.croverflow) * self.sb_nc_soutput)) / 100 \
                   * (self.schance / 100)), 0))

        self.atkp += self.embatkp
        self.batk += self.embbatk
        self.cd += self.embcd

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

    def nbpoutput(self):
        nbpoutput = self.nb_poutput
        return nbpoutput

    def bpoutput(self):
        bpoutput = self.b_poutput
        return bpoutput

    def nbsoutput(self):
        nbsoutput = self.nb_soutput
        return nbsoutput

    def bsoutput(self):
        bsoutput = self.b_soutput
        return bsoutput

    def snbpoutput(self):
        snbpoutput = self.snb_poutput
        return snbpoutput

    def sbpoutput(self):
        sbpoutput = self.sb_poutput
        return sbpoutput

    def snbsoutput(self):
        snbsoutput = self.snb_soutput
        return snbsoutput

    def sbsoutput(self):
        sbsoutput = self.sb_soutput
        return sbsoutput

    def pname(self):
        pname = self.pname
        return pname

    def sname(self):
        sname = self.sname
        return sname


