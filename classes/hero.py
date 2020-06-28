class hero:
    def __init__(self):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0

        # Raging Blow
        self.pname = "Raging Blow"
        self.pskilldmg = 225.6
        self.phitcount = 6
        self.phatkp = 0
        self.phdmg = 0
        self.phbatk = 0
        self.phcr = 0
        self.phcd = 0
        self.phfd = 0

        # Advanced Final Attack
        self.sname = "Advanced Final Attack"
        self.sskilldmg = 67.8
        self.shitcount = 1
        self.schance = 70
        self.shatkp = 0
        self.shdmg = 0
        self.shbatk = 0
        self.shcr = 0
        self.shcd = 0
        self.shfd = 0

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
        self.phdmg += 20
        # Chance Attack
        self.cd += 15
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
