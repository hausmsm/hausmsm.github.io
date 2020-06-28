class dk:
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

        # Gungnir's Descent
        self.pname = "Gungnir's Descent"
        self.pskilldmg = 226.6
        self.phitcount = 10

        # Nightshade Explosion
        self.sname = "Nightshade Explosion"
        self.sskilldmg = 320.1
        self.shitcount = 10
        self.schance = 100

        # Skills

        # 1st Job
        # Warrior Mastery
        self.atkp += 12

        # 2nd Job
        # Weapon Mastery
        self.dmg += 6

        # 3rd Job
        # Cross Surge
        self.atkp += 15
        self.dmg += 10
        #Lord of Darkness
        self.cr += 4
        self.cd += 10

        # 4th Job
        # Advanced Weapon Mastery
        self.batk += 6
        # Final Pact
        self.atkp += 5

        # Hyper Buff
        # Beholder - Reinforce
        self.atkp += 20
        # Beholder - Sacrifice

        #Dark Thirst
        self.atkp += 30
        # Epic Adventure
        self.cd += 30

        # Hyper Skill
        # Gungnir's Descent - Reinforce
        self.hdmg += 20
        # Gungnir's Descent - Boss Rush
        self.hbatk += 20
        # Gungnir's Descent - Extra Strike
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