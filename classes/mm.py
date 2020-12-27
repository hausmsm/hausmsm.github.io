class Mm:
    def __init__(self):
        # Offensive Stats
        self.atk = 1578
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.platk = 0
        self.cr = 5.1
        self.cratk = 0
        self.cd = 12.6
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
        self.hp = 10272
        self.mp = 3171
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

        # Snipe
        self.pname = "Snipe"
        self.pskilldmg = 202.7
        self.phitcount = 9
        self.pchance = 100
        self.patkp = 0
        self.pdmg = 0
        self.pbatk = 0
        self.pplatk = 0
        self.pcr = 100
        self.pcratk = 0
        self.pcd = 0
        self.pmaxdmg = 0
        self.pfd = 0

        # High Speed Shot
        self.sname = "High Speed Shot"
        self.sskilldmg = 475
        self.shitcount = 13
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

        # Final Attack: Crossbow
        self.tname = "Final Attack: Crossbow"
        self.tskilldmg = 0
        self.thitcount = 1
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
        # Double Jump
        # Critical Shot
        self.cr += 2
        # Archer Mastery
        self.accp += 2
        self.kbkres += 26

    # 2nd Job
        # Soul Arrow: Crossbow
        self.atkp += 21
        # Crossbow Booster

        # Rangefinder
        self.fd += 15
        # Crossbow Mastery
        self.batk += 10
        self.platk += 8
        # Final Attack: Crossbow
        self.tchance += 50
        self.tskilldmg += 111.5
        # Physical Training
        self.hpinc += 20
        self.mpinc += 10

    # 3rd Job
        # Pain Killer
        # Reckless Hunt: Crossbow
        self.dmg += 15
        self.pdefdec -= 10
        self.mdefdec -= 10

        # Mortal Blow
        # Dodge
        self.evdp += 6
        self.critres += 2
        self.critdmgres += 10
        # Reverse Damage
        self.pdefdec += 30
        self.mdefdec += 30
        # Marksmanship
        self.penrate += 2
        self.pdefinc += 9
        self.mdefinc += 9

    # 4th Job
        # Sharp Eyes
        self.hprec += 229
        self.mprec += 92
        self.pdefdec += 6
        self.mdefdec += 6
        self.cd += 20
        self.spd += 20

        # Bolt Surplus
        self.fd += 15
        # Last Man Standing
        self.fd += 30
        # Vital Hunter
        self.cd += 14
        # Crossbow Expert
        self.dmg += 8
        # Illusion Step
        self.bdef += 4
        self.pldef += 4

    # Hyper Buff
        # Bullseye Shot
        self.atkp += 15
        self.cr += 15
        self.dmg += 15
        # Epic Adventure
        self.cd += 30

    # Hyper Skill
        # Sharp Eyes - Enhance
        self.atkp += 20
        # Sharp Eyes - Crit DMG
        self.cd += 15
        # Snipe - Reinforce
        self.pfd += 20
        # Snipe - Boss Rush
        self.pbatk += 20
        # Snipe - Cooldown Cutter
