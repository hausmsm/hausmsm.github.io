class pala:
    def __init__(self):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0
        self.spmulti = 0

        # Blast
        self.pname = "Blast"
        self.pskilldmg = 231
        self.phitcount = 9
        self.phatkp = 0
        self.phdmg = 0
        self.phbatk = 0
        self.phcr = 0
        self.phcd = 0
        self.phfd = 0

        # Heaven's Hammer
        self.sname = "Heaven's Hammer"
        self.sskilldmg = 312.4
        self.shitcount = 10
        self.schance = 100
        self.shatkp = 0
        self.shdmg = 0
        self.shbatk = 20
        self.shcr = 0
        self.shcd = 0
        self.shfd = 0

        # Skills

        # 1st Job
        # Warrior Mastery
        self.atkp += 15

        # 2nd Job
        # Elemental Charge
        self.atkp += 20
        # Weapon Mastery
        self.dmg += 8

        # 3rd Job
        # Sheild Mastery
        self.atkp += 15
        # Parashock Guard
        self.atkp += 20
        # Combat Orders
        self.dmg += 15
        # Threaten
        self.cd += 16
        self.cr += 30

        # 4th Job
        # Elemental Force
        self.cd += 15
        # High Paladin
        self.cr += 2
        self.cd += 15
        # Advanced Charge

        # Hyper Buff
        # Smite Shield
        self.dmg += 20
        # Epic Adventure
        self.cd += 30
        # Sacrosanctity
        self.atkp += 40

        # Hyper Skill
        # Blast - Reinforce
        self.phdmg += 20
        # Blast - Extra Strike
        self.phitcount += 1

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
