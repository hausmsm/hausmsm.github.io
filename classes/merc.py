class merc:
    def __init__(self):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0
        self.spmulti = 0

        # Ishtar's Ring
        self.pname = "Ishtar's Ring"
        self.pskilldmg = 165
        self.phitcount = 2
        self.phatkp = 0
        self.phdmg = 0
        self.phbatk = 0
        self.phcr = 0
        self.phcd = 0
        self.phfd = 0

        # Final Attack: Dual Bowguns
        self.sname = "Final Attack: Dual Bowguns"
        self.sskilldmg = 64.4
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
        # Potential Power
        self.atkp += 15
        # Sharp Aim
        self.cr += 4

        # 2nd Job
        # Dual Bowguns Mastery
        self.dmg += 20
        # Spirit Surge
        self.cd += 18

        # 3rd Job
        # Unicorn Spike
        self.dmg += 10
        # Ignis Roar
        self.dmg += 50

        # 4th Job
        # Spikes Royale
        self.dmg += 15
        # Dual Bowguns Expert
        self.batk += 15
        # Defense Break
        self.atkp += 20

        # Hyper Buff
        # Heroic Memories
        self.cd += 30
        # Elvish Blessing
        self.atkp += 30
        self.dmg += 10

        # Hyper Skill
        # Ishtar's Ring - Reinforce
        self.phdmg += 20
        # Ishtar's Ring - Boss Rush
        self.phbatk += 20
        # Ishtar's Ring - Crit DMG
        self.phcd += 20
        # Ignis Roar - Reinforce

        # Spikes Royale - Armorbreak

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