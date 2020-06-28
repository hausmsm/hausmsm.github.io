class phan:
    def __init__(self):
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.cr = 0
        self.cd = 0
        self.fd = 0
        self.spmulti = 0

        # Mille Aiguilles
        self.pname = "Mille Aiguilles"
        self.pskilldmg = 235
        self.phitcount = 1
        self.phatkp = 0
        self.phdmg = 0
        self.phbatk = 0
        self.phcr = 0
        self.phcd = 0
        self.phfd = 0

        # Carte Noire
        self.sname = "Carte Noire"
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

        # 2nd Job
        # Impeccable Memory 2 - Unmanaged Anger
        self.atkp += 21
        # Judgement Draw
        self.cd += 12
        self.schance += 60
        # Carte Blanc
        self.sskilldmg += 70
        # Cane Mastery
        self.atkp += 20
        # Devil's Luck
        self.cr += 5

        # 3rd Job
        # Impeccable Memory 3 - Combat Orders
        self.dmg += 15
        # Clair de Lune
        self.dmg += 25
        # Piercing Vision
        self.cr += 3
        self.cd += 15

        # 4th Job
        # Aria Armour
        self.dmg += 15
        self.atkp += 15
        # Carte Noire
        self.sskilldmg += 145
        self.schance += 40
        # Cane Expert
        self.atkp += 15
        self.dmg += 15

        # Hyper Buff
        # Impeccable Memory H - Cry Valhalla
        self.atkp += 25
        self.fd += 10
        # Heroic Memores
        self.cd += 30
        # Bad Luck Ward
        self.atkp += 20

        # Hyper Skill
        # Mille Aiguilles - Reinforce
        self.phdmg += 20
        # Mille Aiguilles - Crit DMG
        self.phcd += 15
        # Tempest - Reinforce

        # Tempest - Cooldown Cutter

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