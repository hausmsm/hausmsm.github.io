class bm:
    def __init__(self):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0

        # Hurricane
        self.pname = "Hurricane"
        self.pskilldmg = 215
        self.phitcount = 1
        self.phatkp = 0
        self.phdmg = 0
        self.phbatk = 0
        self.phcr = 0
        self.phcd = 0
        self.phfd = 0

        # Advanced Final Attack
        self.sname = "Advanced Final Attack"
        self.sskilldmg = 42.3
        self.shitcount = 1
        self.schance = 60
        self.shatkp = 0
        self.shdmg = 0
        self.shbatk = 0
        self.shcr = 0
        self.shcd = 0
        self.shfd = 0

        # Skills

        # 1st Job
        # Critical Shot
        self.cr += 4

        # 2nd Job
        # Soul Arrow: Bow
        self.atkp += 21
        # Bow Mastery
        self.batk += 10

        # 3rd Job
        # Reckless Hunt: Bow
        self.dmg += 30
        # Focused Fury
        self.atkp += 20

        # 4th Job
        # Sharp Eyes
        self.cd += 20
        # Armor Break
        self.dmg += 10
        # Bow Expert
        self.dmg += 4

        # Hyper Buff
        # Concentration
        self.atkp += 25
        # Epic Adventure
        self.cd += 30
        # Sharp Eyes - Enhance
        self.atkp += 20

        # Hyper Skill
        # Hurricane - Reinforce
        self.phdmg += 20
        # Hurricane - Boss Rush
        self.phbatk += 20
        # Hurricane - Split Attack
        self.phfd -= 40
        self.phitcount += 1
        # Hurricane - Maintain

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
