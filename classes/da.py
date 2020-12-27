class Da:
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

        # Exceed: Execution
        self.pname = "Exceed Execution"
        self.pskilldmg = 162
        self.phitcount = 11
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

        # Nether Shield
        self.sname = "Nether Shield"
        self.sskilldmg = 229
        self.shitcount = 2
        self.schance = 100
        self.satkp = 0
        self.sdmg = 0
        self.sbatk = 0
        self.splatk = 0
        self.scr = 0
        self.scratk = 0
        self.scd = 0
        self.smaxdmg = 0
        self.sfd = 0

        # Thousand Swords
        self.tname = "Thousand Swords"
        self.tskilldmg = 320
        self.thitcount = 18
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
        # Overload Release
        self.fd += 15
        self.hprecp += 100

        # Exceed
        # Life Sap
        self.hprecp += 1
        self.dmg += 2.5
        # Demonic Veracity
        self.cr += 3
        self.spd += 15
        self.jmp += 15
        # Dark Winds
        # Demonic Blood
        self.kbkres += 35
        # Hyper Potion Mastery
        self.hppotionrecp += 100
        # Star Force Conversion
        self.hpinc += 10
        # Blood Pact
        self.atkp += 60

    # 2nd Job
        # Battle Pact

        # Abyssal Connection
        self.atkp += 10
        self.cd += 10
        # Solid Wall
        self.block += 10
        self.pdefinc += 10
        self.mdefinc += 10
        # Desparado Mastery
        self.accp += 3
        self.dmg += 5
        # Rage Within
        self.atkp += 10
        self.hpinc += 8

    # 3rd Job
        # Ward Evil
        self.pdefdec += 10
        self.mdefdec += 10
        self.abnormalstatres += 10
        # Diabolic Recovery
        self.cr += 5
        self.hpinc += 10
        self.hprecp += 1

        # Pain Dampener
        self.fd += 10
        # Advanced Life Sap
        self.hprecp += 1
        self.dmg += 2.5

    # 4th Job
        # Nether Slice
        self.dmg += 10

        # Overwhelming Power
        self.cr += 5
        self.atkp += 15
        # Defense Expertise
        self.fd += 10
        self.cd += 10
        # Advanced Desperado Mastery
        self.dmg += 10
        self.cd += 15

    # Hyper Buff
        # Forbidden Contract
        self.dmg += 25
        self.hp += 15000
        # Demonic Fortitude
        self.cd += 30

        # Hyper Skill
        # Exceed - Reinforce
        self.pfd += 20
        # Exceed - Boss Rush
        self.pbatk += 20
        # Exceed - Deadly Crits
        self.pcd += 20
        # Exceed - Additional Reinforce
        self.fd += 5
        # Nethed Shield - Reinforce
        self.sfd += 20
