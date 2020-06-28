class nw:
    def __init__(self):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0
        self.spmulti = 0

        # Quintuple Star
        self.pname = "Quintuple Star"
        self.pskilldmg = 371.8
        self.phitcount = 5
        self.phatkp = 0
        self.phdmg = 0
        self.phbatk = 0
        self.phcr = 0
        self.phcd = 0
        self.phfd = 0

        # Shadow Bat
        self.sname = "Shadow Bat"
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
        # Shadow Bat
        self.schance += 18
        self.shitcount += 1
        self.sskilldmg += 50

        # 2nd Job
        # Critical Throw
        self.cr += 5
        # Bat Affinity
        self.sskilldmg += 6
        self.schance += 7

        # 3rd Job
        # Spirit Projection
        self.atkp += 25
        self.dmg += 6
        self.batk += 6
        # Bat Affinity II
        self.sskilldmg += 11
        self.schance += 7

        # 4th Job
        # Throwing Expert
        self.cr += 5
        self.cd += 10
        # Dark Blessing
        self.batk += 5
        # Bat Affinity III
        self.schance += 7
        self.sskilldmg += 16

        # Hyper Buff
        # Dominion
        self.atkp += 25
        # Shadow Illusion
        self.spmulti += 45
        # Glory of the Guardians
        self.cd += 30
        # Darkness Ascending - Enhance
        self.atkp += 30
        # Darkness Ascending - Crit DMG
        self.cd += 20

        # Hyper Skill
        # Quintuple Star - Reinforce
        self.phdmg += 20
        # Quintuple Star - Boss Rush
        self.phbatk += 20
        # Quintuple Star - Crit DMG
        self.phcd += 20

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