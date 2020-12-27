class Csr:
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

        # Rapid Fire
        self.pname = "Rapid Fire"
        self.pskilldmg = 379
        self.phitcount = 1
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

        # Brain Scrambler
        self.sname = "Brain Scrambler"
        self.sskilldmg = 384
        self.shitcount = 11
        self.schance = 100
        self.satkp = 0
        self.sdmg = 0
        self.sbatk = 0
        self.splatk = 0
        self.scr = 100
        self.scratk = 0
        self.scd = 0
        self.smaxdmg = 0
        self.sfd = 0

        # Majestic Presence
        self.tname = "Majestic Presence"
        self.tskilldmg = 0
        self.thitcount = 0
        self.tchance = 0
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
        # Octopush
        # Quick Motion
        self.kbkres += 26
        self.spd += 15
        # Shadow Heart
        self.cr += 4
        self.cd += 10
        # Dash
        # Wings

    # 2nd Job
        # Bullet Barrage
        self.critres += 5
        self.mprec += 24
        self.critdmgres += 20
        # Gun Booster

        # Gun Mastery
        self.accp += 6
        self.penrate += 4
        # Physical Training
        self.hprec += 100
        self.mprec += 50

    # 3rd Job
        # Cross Cut Blast
        self.pdefinc += 21
        self.atkp += 21
        self.mdefinc += 21
        # Luck of the Die
        # Use Double Down Instead

        # All Aboard
        # Outlaw's Code
        self.hpinc += 10
        self.mpinc += 10
        # Fullmetal Jacket
        self.cr += 6
        self.cd += 10

    # 4th Job
        # Parrotargetting
        self.dmg += 10

        # Jolly Roger
        self.pdefdec += 6
        self.mdefdec += 6
        self.bdef += 8
        self.pldef += 8

        # Counterattack
        self.atkp += 10
        self.batk += 10
        self.platk += 10
        # Double Down
        self.dmg += 10
        self.cd += 10
        # Ahoy Mateys
        self.atkp += 5
        self.pdefinc += 10
        self.mdefinc += 10
        self.hpinc += 10
        self.cd += 10
        # Majestic Presence
        self.tchance += 50
        self.thitcount += 2
        self.tskilldmg += 72
        # Quickdraw
        self.dmg += 15

    # Hyper Buff
        # Whaler's Potion
        self.atkp += 25
        self.dmg += 15
        self.abnormalstatres += 20
        # Epic Adventure
        self.cd += 30

    # Hyper Skill
        # Rapid Fire - Boss Rush
        self.pbatk += 20
        # Rapid Fire - Crit DMG
        self.pcd += 20
        # Rapid Fire - Reinforce
        self.pfd += 20
        # Brain Scrambler - Extra Strike
        self.shitcount += 1
        # Brain Scrambler - Boss Rush
        self.sbatk += 30