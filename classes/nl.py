class Nl:
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

        # Quad Star
        self.pname = "Quad Star"
        self.pskilldmg = 355.7
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

        # Night Lord's Mark
        self.sname = "Night Lord's Mark"
        self.sskilldmg = 0
        self.shitcount = 1
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

        # Four Seasons
        self.tname = "Four Seasons"
        self.tskilldmg = 300
        self.thitcount = 10
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
        # Dark Sight

        # Side Step
        self.evdp += 10
        # Flash Jump
        # Nimble Body
        self.accp += 4
        self.evdp += 6
        self.cr += 4

    # 2nd Job
        # Haste
        self.spd += 20
        # Claw Booster

        # Assasin's Mark
        self.schance += 30
        self.sskilldmg += 35
        self.shitcount += 1
        # Claw Mastery
        self.pdefinc += 9
        self.mdefinc += 9
        # Physical Training
        self.hprec += 55
        self.mprec += 22
        self.critdmgres += 10
        # Critical Throw
        self.cr += 4
        self.cd += 10

    # 3rd Job
        # Shadow Stars
        self.dmg += 15
        # Shadow Partner
        self.spmulti += 35

        # Venom
        # Enveloping Darkness
        self.hpinc += 10
        self.mpinc += 5
        # Expert Throwing Star Technique
        self.atkp += 13

    # 4th Job
        # Frailty Curse
        self.dmg += 10

        # Shadow Shifter
        # Dark Serenity
        self.penrate += 5
        self.batk += 12
        self.platk += 12

        # Claw Expert
        self.pdefdec += 4
        self.mdefdec += 4
        self.bdef += 4
        self.pldef += 4
        self.hpinc += 10
        self.mpinc += 10
        # Toxic Venom
        # Night Lord's Mark
        self.shitcount += 2
        self.schance += 20
        self.sskilldmg += 45

    # Hyper Buff
        # Bleed Dart
        self.atkp += 15
        self.dmg += 15
        # Epic Adventure
        self.cd += 30

        # Frailty Curse - Enhance
        self.dmg += 20
        # Frailty Curse - Crit DMG
        self.cd += 20

        # Hyper Skill
        # Quad Star - Reinforce
        self.pfd += 20
        # Quad Star - Boss Rush
        self.pbatk += 20
        # Quad Star - Extra Strike
        self.phitcount += 1
