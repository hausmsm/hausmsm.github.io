class shad:
    def __init__(self):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0
        self.spmulti = 0

        # Assassinate
        self.pname = "Assassinate"
        self.pskilldmg = 265
        self.phitcount = 4
        self.phatkp = 0
        self.phdmg = 0
        self.phbatk = 0
        self.phcr = 0
        self.phcd = 0
        self.phfd = 0

        # Meso Explosion
        self.sname = "Meso Explosion"
        self.sskilldmg = 151.8
        self.shitcount = 1
        self.schance = 100
        self.shatkp = 0
        self.shdmg = 0
        self.shbatk = 0
        self.shcr = 0
        self.shcd = 0
        self.shfd = 0

        # Skills

        # 1st Job
        # Nimble Body
        self.cr += 2

        # 2nd Job
        # Critical Growth
        self.cd += 17.5
        # Dagger Mastery
        self.atkp += 9

        # 3rd Job
        # Shadow Partner
        self.spmulti += 30

        # 4th Job
        # Prime Critical
        self.cr += 2
        # Dagger Expert
        self.batk += 10
        self.cd += 10
        # Shadower Instinct
        self.atkp += 20
        # Shadow Shifter
        self.dmg += 6
        # Smokescreen
        self.cd += 15

        # Hyper Buff
        # Flip of the Coin
        self.atkp += 15
        self.cd += 10
        # Epic Adventure
        self.cd += 30

        # Hyper Skill
        # Assassinate - Reinforce
        self.phdmg += 20
        # Assassinate - Boss Rush
        self.phbatk += 20
        # Assassinate - Critical Damage
        self.phcd += 20
        # Meso Explosion - Reinforce
        self.shdmg += 20
        # Meso Explosion - Crit DMG
        self.shcd += 20

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