class Wa:
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

        # Song of Heaven - Normal Arrow
        self.pname = "Song of Heaven - Normal Arrow"
        self.pskilldmg = 305
        self.phitcount = 2
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

        # Song of Heaven - Third Arrow
        self.sname = "Song of Heaven - Third Arrow"
        self.sskilldmg = 425
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

        # Trifling Wind
        self.tname = "Trifling Wind"
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
        # Storm Elemental
        self.atkp += 15

        # Elemental Shift
        # Whispers of the Wind
        self.kbkres += 30
        self.spd += 20
        self.jmp += 15

    # 2nd Job
        # Bow Booster
        # Slyvan Aid
        self.pdefinc += 15
        self.mdefinc += 15
        # Trifling Wind I
        self.tchance += 15
        self.tskilldmg += 100
        self.thitcount += 1
        # Bow Mastery
        self.accp += 6
        self.penrate += 6
        # Physical Training
        self.hprec += 50
        self.mprec += 20
        self.hpinc += 10
        self.mpinc += 10

    # 3rd Job
        # Emerald Flower
        # Use Emerald Dust instead

        # Albatross
        # Use Albatross Max Instead

        # Trifling Wind II
        self.tchance += 5
        self.thitcount += 1
        self.tskilldmg += 15
        # Featherweight
        self.critres += 10
        self.critdmgres += 15
        # Second Wind
        self.evdp += 6
        self.batk += 8
        self.platk += 8

    # 4th Job
        # Emerald Dust
        self.dmg += 20

        # Touch of the Wind
        self.bdef += 8
        self.pldef += 8
        # Sharp Eyes
        self.dmg += 6
        self.pdefdec += 4
        self.mdefdec += 4
        # Albatross Max
        self.cr += 5
        self.atkp += 15
        self.cd += 25

        # Trifling Wind III
        self.tchance += 10
        self.thitcount += 2
        self.tskilldmg += 30
        # Bow Expert
        self.batk += 6
        self.platk += 6

    # Hyper Buff
        # Storm Bringer
        self.dmg += 15
        # Glory Of The Guardians
        self.cd += 30

    # Hyper Skill
        # Song Of Heaven - Reinforce
        self.pskilldmg += 20
        self.sskilldmg += 20
        # Song Of Heaven - Boss Rush
        self.pbatk += 20
        self.sbatk += 20
        # Song Of Heaven - Crit DMG
        self.pcd += 20
        self.scd += 20
        # Trifling Wind - Enhance
        self.tchance += 40
        self.thitcount += 4
        # Trifling Wind - Double Chance
        self.tfd -= 40
        self.thitcount *= 2
