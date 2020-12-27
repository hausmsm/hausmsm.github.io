class Mech:
    def __init__(self):
        # Offensive Stats
        self.atk = 1578
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.platk = 0
        self.cr = 5
        self.cratk = 0
        self.cd = 10
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
        self.hp = 10280
        self.mp = 3167
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

        # AP Salvo Plus
        self.pname = "AP Salvo Plus"
        self.pskilldmg = 152.9
        self.phitcount = 6
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

        # Homing Beacon
        self.sname = "Homing Beacon"
        self.sskilldmg = 112
        self.shitcount = 1
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

        # Giant Robot SG-88
        self.tname = "Giant Robot SG-88"
        self.tskilldmg = 495.2
        self.thitcount = 3
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
        # Humanoid Mech
        # Use Tank Mech Instead

        # Hidden Peace
        self.pdefinc += 13.5
        self.atkp += 13.5
        self.mdefinc += 13.5

    # 2nd Job
        # Mechanic Rage
        # Perfect Armor
        self.accp += 4
        self.block += 15
        self.evd += 12
        self.penrate += 5

        # Mechanic Mastery
        self.atkp += 10
        self.dmg += 10
        # Physical Training
        self.batk += 6
        self.bdef += 6
        self.platk += 6
        self.pldef += 6

    # 3rd Job
        # Support Unit: H-EX
        self.dmg += 10

        # Tank Mech
        self.cr += 10
        self.cd += 10
        # Luck of the Die
        # Use Double Down Instead

        # Advanced Homing Beacon
        self.sskilldmg += 91
        # Mechanised Defence System
        self.block += 6
        self.evd += 6
        self.hpinc += 10
        self.mpinc += 5
        # Battle Program Prep
        self.kbkres += 26
        self.spd += 15
        self.jmp += 15
        # Overclock
        self.cr += 4
        self.critres += 4
        self.cd += 10
        self.critdmgres += 10

    # 4th Job
        # Extreme Mech
        self.pdefinc += 9
        self.atkp += 9
        self.mdefinc += 9
        self.hpinc += 10
        self.mpinc += 5
        # Mech Alloy Research
        self.block += 6
        self.evdp += 6
        self.pdefdec += 12
        self.mdefdec += 12
        # Enhanced Support Unit
        self.fd += 10
        # Homing Beacon Research
        self.sskilldmg += 154
        # Robot Mastery
        self.fd += 30
        # Double Down
        self.cd += 10
        self.dmg += 10

    # Hyper Buff
        # Full Spread
        self.dmg += 15
        self.batk += 15
        # For Liberty
        self.cd += 30

    # Hyper Skill
        # Support Unit: H-EX - Party Reinforce
        self.fd += 5
        # Support Unit: H-EX - Persist
        # Rock 'n Shock - Persist
        # Heavy Salvo - Reinforce
        self.pfd += 20
        # AP Salvo PLus - Extra Strike
        self.phitcount += 7
