class Shade:
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

        # Spirit Claw
        self.pname = "Spirit Claw"
        self.pskilldmg = 118.2
        self.phitcount = 8
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

        # Fox Spirits
        self.sname = "Fox Spirits"
        self.sskilldmg = 0
        self.shitcount = 0
        self.schance = 0
        self.satkp = 0
        self.sdmg = 0
        self.sbatk = 0
        self.splatk = 0
        self.scr = 0
        self.scratk = 0
        self.scd = 0
        self.smaxdmg = 0
        self.sfd = 0

        # Spirit Incarnation
        self.tname = "Spirit Incarnation"
        self.tskilldmg = 425
        self.thitcount = 6
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
        # Vulpes Leap
        # Cosmic Balance
        self.pdefinc += 10.8
        self.mdefinc += 10.8
        # Spirit Bond 1
        self.kbkres += 31
        self.hprecp += 5

    # 2nd Job
        # Fox Spirits

        # Knuckle Mastery
        self.atkp += 15
        self.dmg += 8
        # Spirit Bond 2
        self.spd += 15
        self.jmp += 15
        # Strength Training
        self.cd += 10
        self.critdmgres += 10
        # Fox Spirit Mastery
        # Use Fire Fox Spirit Mastery Instead

    # 3rd Job
        # Spirit Redemption

        # Spirit Bond 3
        self.dmg += 15
        # Harmonious Defence
        self.pdefdec += 8
        self.mdefdec += 8
        self.abnormalstatres += 10
        # Weaken
        self.dmg += 10

    # 4th Job
        # Soul Splitter

        # Shielding Spirit Ward

        # Fire Fox Spirit Mastery
        self.sskilldmg += 251.4
        self.shitcount += 1
        self.schance += 10
        # Spirit Bond 4
        self.block += 6
        self.evdp += 6
        self.batk += 15
        self.platk += 15
        # Advanced Knuckle Mastery
        self.accp += 4
        self.penrate += 4
        self.cr += 8
        self.critres += 8
        # Critical Insight
        self.fd += 20

    # Hyper Buff
        # True Spirit Bond
        self.atkp += 15
        self.dmg += 15
        self.batk += 15
        # Heroic Memories
        self.cd += 30

    # Hyper Skill
        # Spirit Claw - Reinforce
        self.pfd += 15
        # Spirit Claw - Boss Rush
        self.pbatk += 15
        # Spirit Claw - Extra Strike
        self.phitcount += 1
        # Fire Fox Spirits - Repeat Attack Chance
        # Fire Fox Spirits - Summon Chance
        self.schance += 10
