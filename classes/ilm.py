class ilm:
    def __init__(self):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0
        self.spmulti = 0

        # Chain Lightning
        self.pname = "Chain Lightning"
        self.pskilldmg = 180
        self.phitcount = 8
        self.phatkp = 0
        self.phdmg = 0
        self.phbatk = 0
        self.phcr = 20
        self.phcd = 0
        self.phfd = 0

        # Frozen Orb
        self.sname = "Frozen Orb"
        self.sskilldmg = 195.8
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

        # 2nd Job
        # Freezing Crush
        self.cd += 5
        self.fd += 5
        # High Wisdom
        self.dmg += 4
        # Meditation
        self.dmg += 10

        # 3rd Job
        # Elemental Decrease
        self.dmg += 12
        # Elemental Amplification
        self.dmg += 15
        # Magic Dominance
        self.cr += 2
        self.cd += 10
        # Shatter
        self.atkp += 13.5
        # Extreme Magic
        self.dmg += 10

        # 4th Job
        # Infinity
        self.batk += 8
        # Frost Clutch
        self.cd += 5
        self.fd += 5
        # Arcane Aim
        self.atkp += 15

        # Hyper Buff
        # Epic Adventure
        self.cd += 30

        # Hyper Skill
        # Chain Lightning - Reinforce
        self.phdmg += 20
        # Chain Lightning - Extra Strike
        self.phitcount += 1
        # Chain Lightning - Spread

        # Frozen Orb - Reinforce
        self.shdmg += 20
        # Frozen Orb - Critical Damge
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