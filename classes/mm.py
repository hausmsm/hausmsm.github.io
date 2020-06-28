class mm:
    def __init__(self):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0
        self.spmulti = 0

        # Snipe
        self.pname = "Snipe"
        self.pskilldmg = 187.9
        self.phitcount = 1
        self.phatkp = 0
        self.phdmg = 0
        self.phbatk = 0
        self.phcr = 0
        self.phcd = 0
        self.phfd = 0

        # Arrow Illusion
        self.sname = "Arrow Illusion"
        self.sskilldmg = 85
        self.shitcount = 3
        self.schance = 100
        self.shatkp = 0
        self.shdmg = 0
        self.shbatk = 0
        self.shcr = 0
        self.shcd = 0
        self.shfd = 0

        # Skills

        # 1st Job
        # Critical Shot
        self.cr += 2

        # 2nd Job
        # Soul Arrow: Crossbow
        self.atkp += 21
        # Rangefinder
        self.fd += 15
        # Crossbow Mastery
        self.batk += 10

        # 3rd Job
        # Reckless Hunt: Crossbow
        self.dmg += 15

        # 4th Job
        # Sharp Eyes
        self.cd += 20
        # Bolt Surplus
        self.fd += 15
        # Last Man Standing
        self.fd += 30
        # Vital Hunter
        self.cd += 14
        # Crossbow Expert
        self.dmg += 8

        # Hyper Buff
        # Bullseye Shot
        self.atkp += 10
        self.cr += 10
        self.dmg += 10
        # Epic Adventure
        self.cd += 30
        # Sharp Eyes - Enhance
        self.atkp += 20
        # Sharp Eyes - Crit DMG
        self.cd += 15

        # Hyper Skill
        # Snipe - Reinforce
        self.phdmg += 20
        # Snipe - Boss Rush
        self.phbatk += 20
        # Snipe - Cooldown Cutter

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