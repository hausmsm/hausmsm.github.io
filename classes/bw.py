class bw:
    def __init__(self):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0

        # Final Orbital Flame
        self.pname = "Final Orbital Flame"
        self.pskilldmg = 190
        self.phitcount = 2
        self.phatkp = 0
        self.phdmg = 0
        self.phbatk = 0
        self.phcr = 0
        self.phcd = 0
        self.phfd = 0

        # Blazing Extinction
        self.sname = "Blazing Extinction"
        self.sskilldmg = 433.8
        self.shitcount = 2
        self.schance = 100
        self.shatkp = 0
        self.shdmg = 0
        self.shbatk = 0
        self.shcr = 0
        self.shcd = 0
        self.shfd = 0

        # Skills

        # 1st Job
        # Natural Talent
        self.cr += 5

        # 2nd Job

        # 3rd Job
        # Liberated Magic
        self.dmg += 30
        # Burning Focus
        self.cd += 10
        # Brilliant Enlightenment
        self.atkp += 6

        # 4th Job
        # Final Flame Elemental
        self.atkp += 15
        self.dmg += 10
        self.batk += 5
        self.cr += 5
        # Burning Conduit
        self.atkp += 20
        self.dmg += 5
        # Pure Magic
        self.atkp += 10

        # Hyper Buff
        # Glory Of The Guardians
        self.cd += 30

        # Hyper Skill
        # Orbital Flame- Boss Rush
        self.phbatk += 20
        # Orbital Flame - Crit DMG
        self.phcd += 20
        # Orbtial Flame - Split Attack
        self.phfd -= 10
        self.phitcount += 2
        # Blazing Extinction - Reinforce
        self.shdmg += 25
        # Blazing Extinction - Max Extinction

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
