class Pala:
    def __init__(self):
        # Offensive Stats
        self.atk = 1577
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.platk = 0
        self.cr = 4.9
        self.cratk = 0
        self.cd = 7.4
        self.maxdmg = 3999999
        self.fd = 0

        # Defensive Stats
        self.pdef = 10
        self.pdefinc = 0
        self.pdefdec = 0
        self.mdef = 10
        self.mdefinc = 0
        self.mdefdec = 0
        self.bdef = 0
        self.pldef = 0
        self.critres = 0
        self.critdmgres = 0

        # Hit Miss Stats
        self.acc = 2251
        self.accp = 0
        self.evd = 1125
        self.evdp = 0
        self.penrate = 0
        self.block = 0
        self.abnormalstatres = 0
        self.ignore = 0

        # HP MP Stats
        self.hp = 10285
        self.mp = 3169
        self.hpinc = 0
        self.mpinc = 0
        self.hprec = 1
        self.mprec = 1
        self.hprecp = 0
        self.mprecp = 0
        self.hppotionrecp = 0
        self.mppotionrecp = 0
        self.buffdurationinc = 0

        # Mobility Stats
        self.spd = 0
        self.jmp = 0
        self.kbkres = 0

        # Misc Stats
        self.exp = 0
        self.dr = 0
        self.meso = 0
        self.glincrease = 0
        self.partyexp = 0
        self.feverchargeinc = 0
        self.feverduration = 0
        self.maxfeverchance = 0

        # Shadow Partner Stats
        self.spmulti = 0

        # Blast
        self.pname = "Blast"
        self.pskilldmg = 231
        self.phitcount = 9
        self.pchance = 100
        self.patkp = 0
        self.pdmg = 0
        self.pbatk = 0
        self.pplatk = 0
        self.pcr = 0
        self.pcratk = 0
        self.pcd = 0
        self.pmaxdmg = 0
        self.pfd = 0

        # Heaven's Hammer
        self.sname = "Heaven's Hammer"
        self.sskilldmg = 295
        self.shitcount = 11
        self.schance = 100
        self.satkp = 0
        self.sdmg = 0
        self.sbatk = 30
        self.splatk = 0
        self.scr = 0
        self.scratk = 0
        self.scd = 0
        self.smaxdmg = 0
        self.sfd = 0

        # Smite Shield
        self.tname = "Smite Shield"
        self.tskilldmg = 315
        self.thitcount = 12
        self.tchance = 100
        self.tatkp = 0
        self.tdmg = 0
        self.tbatk = 0
        self.tplatk = 0
        self.tcr = 0
        self.tcratk = 0
        self.tcd = 0
        self.tmaxdmg = 0
        self.tfd = 0

# Skills
    # 1st Job
        # Warrior Leap
        # Iron Body
        self.pdefinc += 9
        self.mdefinc += 9
        self.hpinc += 30
        self.mpinc += 10
        # Warrior Mastery
        self.atkp += 15

    # 2nd Job
        # Weapon Booster

        # Elemental Charge
        self.atkp += 20
        self.pdefinc += 15
        self.mdefinc += 15
        # Weapon Mastery
        self.dmg += 8
        # Final Attack
        # Physical Training
        self.accp += 2
        self.evdp += 6
        self.spd += 15

    # 3rd Job
        # Threaten
        self.cr += 30
        self.cd += 16

        # Parashock Guard (Party)
        self.atkp += 20 # Self Only
        self.pdefdec -= 10
        self.mdefdec -= 10
        # Combat Orders (Party)
        self.dmg += 15

        # Shield Mastery
        self.atkp += 10
        self.block += 10
        self.block += 5
        # Achilles
        self.pdefinc += 20
        self.mdefinc += 20
        self.batk += 15
        self.bdef += 15
        # Divine Shield
        self.pdefdec += 30
        self.mdefdec += 30

    # 4th Job
        # Elemental Force
        self.cd += 15

        # KBK RES
        self.kbkres += 26
        # High Paladin
        self.cr += 2
        self.cd += 15
        # Advanced Charge
        self.fd += 15

    # Hyper Buff
        # Smite Shield
        self.dmg += 20

        # Sacrosanctity
        self.atkp += 25
        self.dmg += 15
        # Epic Adventure
        self.cd += 30

    # Hyper Skill
        # Threaten - Persist
        # Threaten - Opportunity
        # Threaten - Enhance
        self.cr += 30
        # Blast - Reinforce
        self.pfd += 20
        # Blast - Extra Strike
        self.phitcount += 1
