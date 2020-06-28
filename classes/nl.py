class nl:
    def __init__(self):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0
        self.spmulti = 0

        # Quad Star
        self.pname = "Quad Star"
        self.pskilldmg = 355.7
        self.phitcount = 4
        self.phatkp = 0
        self.phdmg = 0
        self.phbatk = 0
        self.phcr = 0
        self.phcd = 0
        self.phfd = 0

        # Night Lord's Mark
        self.sname = "Night Lord's Mark"
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
        # Nimble Body
        self.cr += 4

        # 2nd Job
        # Critical Throw
        self.cr += 4
        self.cd += 10
        # Assassin's Mark
        self.sskilldmg += 35
        self.schance += 30
        self.shitcount += 1

        # 3rd Job
        # Shadow Stars
        self.dmg += 15
        # Expert Throwing Star Technique
        self.atkp += 13
        # Shadow Partner
        self.spmulti += 30

        # 4th Job
        # Frailty Curse
        self.dmg += 10
        # Dark Serenity
        self.batk += 11
        # Shadow Shifter
        self.dmg += 6
        # Night Lord's Mark
        self.schance += 20
        self.sskilldmg += 45

        # Hyper Buff
        # Bleed Dart
        self.atkp += 25
        # Epic Adventure
        self.cd += 30
        # Frailty Curse - Enhance
        self.dmg += 20
        # Frailty Curse - Crit DMG
        self.cd += 30

        # Hyper Skill
        # Quad Star - Reinforce
        self.phdmg += 20
        # Quad Star - Boss Rush
        self.phbatk += 20
        # Quad Star - Extra Strike
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