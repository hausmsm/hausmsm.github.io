class hero:
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

        # Raging Blow
        self.pname = "Raging Blow"
        self.pskilldmg = 225.6
        self.phitcount = 6

        # Advanced Final Attack
        self.sname = "Advanced Final Attack"
        self.sskilldmg = 67.8
        self.shitcount = 1
        self.schance = 70

        # Skills

        # 1st Job
        # Warrior Mastery
        self.atkp += 9

        # 2nd Job
        # Unmanaged Anger
        self.atkp += 21
        # Weapon Mastery
        self.dmg += 4

        # 3rd Job
        # Combo Synergy
        self.cr += 2

        # 4th Job
        # Enrage
        self.fd += 25
        # Advanced Combo Attack
        self.fd += 20
        # Combat Mastery
        self.batk += 4

        # Hyper Buff
        # Cry Valhalla
        self.fd += 10
        self.atkp += 25
        # Epic Adventure
        self.cd += 30
        # Advanced Combo Attack - Reinforce
        self.fd += 10
        # Advanced Combo Attack - Boss Rush
        self.batk += 20

        # Hyper Skill
        # Raging Blow - Reinforce
        self.hdmg += 20
        # Chance Attack
        self.hcd += 15
        # Raging Blow - Extra Strike
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