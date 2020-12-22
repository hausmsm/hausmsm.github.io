class Nw:
    def __init__(self):
        # Offensive Stats
        self.atk = 1579
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
        self.hp = 10272
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

        # Quintuple Star - Normal Strike
        self.pname = "Quintuple Star - Normal Strike"
        self.pskilldmg = 309.4
        self.phitcount = 4
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

        # Quintuple Star - Last Strike
        self.sname = "Quintuple Star - Last Strike"
        self.sskilldmg = 371.1
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

        # Shadow Bat
        self.tname = "Shadow Bat"
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
        # Dark Elemental
        # Haste
        self.spd += 20
        self.jmp += 15
        # Dark Sight

        # Shadow Jump
        # Shadow Bat
        self.tchance += 18
        self.thitcount += 1
        self.tskilldmg += 50

    # 2nd Job
        # Throwing Booster

        # Throwing Mastery
        self.accp += 6
        self.penrate += 6
        # Critical Throw
        self.cr += 5
        # Physical Training
        self.hpinc += 10
        self.mpinc += 10
        # Adoptive Darkness
        # Bat Affinity
        self.tchance += 7
        self.thitcount += 1
        self.tskilldmg += 6

    # 3rd Job
        # Dark Servant
        # Use Hyper Skill Instead
        # Spirit Projection
        self.atkp += 25
        self.dmg += 6
        self.batk += 6
        self.platk += 6
        # Darkness Ascending

        # Enveloping Darkness
        self.pdefinc += 10
        self.mdefinc += 10
        self.pdefdec += 5
        self.mdefdec += 5
        # Alchemic Adrenaline
        self.hppotionrecp += 10
        self.mppotionrecp += 10
        # Adaptive Darkness II
        # Bat Affinity II
        self.tchance += 7
        self.thitcount += 1
        self.tskilldmg += 11

    # 4th Job
        # Throwing Expert
        self.cr += 5
        self.cd += 10
        self.critdmgres += 10
        # Dark Blessing
        self.batk += 5
        self.platk += 5
        # Adaptive Darkness III
        # Bat Affinity III
        self.tchance += 7
        self.thitcount += 1
        self.tskilldmg += 16
        # Vitality Siphon
        self.hpinc += 50
        # Shadow Slip
        self.evdp += 6
        self.bdef += 4
        self.pldef += 4

    # Hyper Buff
        # Dominion
        self.atkp += 25
        self.kbkres += 10

        # Shadow Illusion
        self.spmulti += 75
        # Glory of the Guardians
        self.cd += 30

        # Darkness Ascending - Enhance
        self.atkp += 30
        # Darkness Ascending - Crit DMG
        self.cd += 20

    # Hyper Skill
        # Quintuple Star - Reinforce
        self.pfd += 20
        self.sfd += 20
        # Quintuple Star - Boss Rush
        self.pbatk += 20
        self.sbatk += 20
        # Quintuple Star - Crit DMG
        self.pcd += 20
        self.scd += 20
