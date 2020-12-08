class aran:
    def __init__(self):
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

        # Beyond Blade
        self.pname = "Beyond Blade"
        self.pskilldmg = 283.6
        self.phitcount = 5
        self.phatkp = 0
        self.phdmg = 0
        self.phbatk = 0
        self.phcr = 0
        self.phcd = 0
        self.phfd = 0

        # Final Attack
        self.sname = "Final Attack"
        self.sskilldmg = 0
        self.shitcount = 0
        self.schance = 0
        self.shatkp = 0
        self.shdmg = 0
        self.shbatk = 0
        self.shcr = 0
        self.shcd = 0
        self.shfd = 0

        # Skills

        # 1st Job
        # Combo Ability
        self.cr += 3
        self.critres += 3

        # Polearm Booster

        # Body Pressure

        # 2nd Job
        # Polearm Mastery
        self.atkp += 20
        self.batk += 15
        self.platk += 15

        # Physical Training
        self.hpinc += 10
        self.mpinc += 10

        # Final Attack
        self.schance += 30
        self.sskilldmg += 72.7
        self.shitcount += 1

        # Command Mastery I
        self.pskilldmg += 17.5
        self.sskilldmg += 17.5

        # Swing Studies I

        # Drain
        self.atkp += 10

        # Snow Charge
        self.dmg += 17.5

        # 3rd Job
        # Advanced Combo Ability
        self.cd += 4
        self.critdmgres += 4

        # Cleaving Blows
        self.dmg += 10

        # Adrenaline Rush
        self.dmg += 10
        self.pdefdec += 10
        self.mdefdec += 10
        self.cr += 3
        self.cd += 15

        # Might
        self.kbkres += 31
        self.spd += 18
        self.jmp += 18

        # Maha's Blessing
        self.hpinc += 10
        self.mpinc += 10

        # 4th Job
        # High Mastery
        self.accp += 4
        self.evdp += 4
        self.penrate += 4

        # High Defense
        self.pdefinc += 10
        self.mdefinc += 10
        self.bdef += 5
        self.pldef += 5

        # Sudden Strike

        # Advanced Final Attack
        self.schance += 30
        self.sskilldmg += 66.2

        # Command Mastery II
        self.dmg += 14.2

        # Swing Studdies II

        # Hyper Buff
        # Adrenaline Burst

        # Heroic Memories
        self.cd += 30

        # Hyper Skill
        # Beyond Blade - Reinforce
        self.phdmg += 20

        # Beyond Blade - Crit DMG
        self.phcd += 20

        # Beyond Blade - Extra Strike
        self.phitcount += 1

        # Adrenaline Rush - Persist

        # Hunter's Prey Reinforce

    def atkp(self):
        atkp = self.atkp
        return atkp

    def dmg(self):
        dmg = self.dmg
        return dmg

    def batk(self):
        batk = self.batk
        return batk

    def cr(self):
        cr = self.cr
        return cr

    def cd(self):
        cd = self.cd
        return cd

    def fd(self):
        fd = self.fd
        return fd

    def pname(self):
        pname = self.pname
        return pname

    def pskilldmg(self):
        pskilldmg = self.pskilldmg
        return pskilldmg

    def phitcount(self):
        phitcount = self.phitcount
        return phitcount

    def phatkp(self):
        phatkp = self.phatkp
        return phatkp

    def phdmg(self):
        phdmg = self.phdmg
        return phdmg

    def phbatk(self):
        phbatk = self.phbatk
        return phbatk

    def phcr(self):
        phcr = self.phcr
        return phcr

    def phcd(self):
        phcd = self.phcd
        return phcd

    def phfd(self):
        phfd = self.phfd
        return phfd

    def sname(self):
        sname = self.sname
        return sname

    def sskilldmg(self):
        sskilldmg = self.sskilldmg
        return sskilldmg

    def shitcount(self):
        shitcount = self.shitcount
        return shitcount

    def schance(self):
        schance = self.schance
        return schance

    def shatkp(self):
        shatkp = self.shatkp
        return shatkp

    def shdmg(self):
        shdmg = self.shdmg
        return shdmg

    def shbatk(self):
        shbatk = self.shbatk
        return shbatk

    def shcr(self):
        shcr = self.shcr
        return shcr

    def shcd(self):
        shcd = self.shcd
        return shcd

    def shfd(self):
        shfd = self.shfd
        return shfd

    def spmulti(self):
        spmulti = self.spmulti
        return spmulti
