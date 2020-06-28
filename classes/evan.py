class evan:
    def __init__(self):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0
        self.spmulti = 0

        # Earth Dive
        self.pname = "Earth Dive"
        self.pskilldmg = 930.8
        self.phitcount = 6
        self.phatkp = 0
        self.phdmg = 0
        self.phbatk = 0
        self.phcr = 0
        self.phcd = 0
        self.phfd = 0

        # Magic Debris
        self.sname = "Magic Debris"
        self.sskilldmg = 72.3
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

        # 2nd Job
        # Return Flash
        self.dmg += 15
        # Partners
        self.dmg += 14.4
        # Spell Mastery
        self.cr += 4.8

        # 3rd Job
        # Elemental Decrease
        self.dmg += 14.4
        # Return Dive
        self.dmg += 15
        # Critical Magic
        self.cr += 4.8
        # Magic Amplification
        self.dmg += 20
        # Dragon Potential
        self.atkp += 10.8

        # 4th Job
        # Magic Mastery
        self.cd += 8
        # Dragon Fury
        self.atkp += 15
        # High Dragon Potential
        self.batk += 9.6

        # Hyper Buff
        # Heroic Memories
        self.cd += 30

        # Hyper Skill
        # Dragon Dive - Cooldown Reduction

        # Dragon Dive - Enhance Earth

        # Dragon Breath - Cooldown Reduction

        # Dragon Breath - Reinforce Wind

        # Dragon Breath - Affix Earth

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