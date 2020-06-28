class pala:
    def __init__(self):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0
        self.hatkp = 0
        self.hdmg = 0
        self.hbatk = 0
        self.hcr = 0
        self.hcd = 0

        # Blast
        self.pname = "Blast"
        self.pskilldmg = 231
        self.phitcount = 9

        # Heaven's Hammer
        self.sname = "Heaven's Hammer"
        self.sskilldmg = 312.4
        self.shitcount = 10
        self.schance = 100

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
        self.hdmg += 20
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

    def fd(self):
        fd = self.fd
        return fd

    def hatkp(self):
        hatkp = self.hatkp
        return hatkp

    def hdmg(self):
        hdmg = self.hdmg
        return hdmg

    def hbatk(self):
        hbatk = self.hbatk
        return hbatk

    def hcr(self):
        hcr = self.hcr
        return hcr

    def hcd(self):
        hcd = self.hcd
        return hcd

    def pname(self):
        pname = self.pname
        return pname

    def pskilldmg(self):
        pskilldmg = self.pskilldmg
        return pskilldmg

    def phitcount(self):
        phitcount = self.phitcount
        return phitcount

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