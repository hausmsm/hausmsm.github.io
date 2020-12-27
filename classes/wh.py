class Wh:
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

        # Wild Arrow Blast
        self.pname = "Wild Arrow Blast"
        self.pskilldmg = 192
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

        # Jaguar Rampage
        self.sname = "Jaguar Rampage"
        self.sskilldmg = 400
        self.shitcount = 12
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

        # Advanced Final Attack
        self.tname = "Advanced Final Attack"
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
        # Summon Jaguar
        self.atkp += 15
        self.dmg += 15

        # Double Jump
        # Resistance Auto Crank
        self.atkp += 13.5
        self.spd += 15
        self.jmp += 15
        # Nature's Wrath
        self.cr += 4
        self.critres += 4

    # 2nd Job
        # Soul Arrow: Crossbow
        self.atkp += 21
        # Call of the Wild (Party)
        self.atkp += 14.7
        # Crossbow Booster

        # Crossbow Mastery
        self.batk += 8
        self.platk += 8
        # Final Attack
        self.tchance += 30
        self.tskilldmg += 50
        # Physical Training
        self.hpinc += 5
        self.mpinc += 2.5
        # Jaguar Mastery
        self.kbkres += 26
        self.spd += 15
        self.jmp += 15

    # 3rd Job
        # Feline Berserk
        self.dmg += 12
        self.hpinc += 10
        self.mpinc += 5
        # Backstep
        self.batk += 8
        self.bdef += 8
        self.platk += 8
        self.pldef += 8

        # Flurry
        self.accp += 4
        self.block += 12
        self.evdp += 12
        self.penrate += 4
        # Jaguar Link
        self.dmg += 30

    # 4th Job
        # Sharp Eyes
        self.hprec += 229
        self.mprec += 92
        self.pdefdec += 6
        self.cd += 20
        self.mdefdec += 6

        # Extended Magazine
        self.cd += 10
        self.critdmgres += 10
        # Crossbow Expert
        self.cd += 10
        self.dmg += 10
        # Wild Instinct
        self.pdefinc += 9
        self.pdefdec += 6
        self.mdefinc += 9
        self.mdefdec += 6
        # Advanced Final Attack
        self.tchance += 40
        self.tskilldmg += 100
        # Natural Force
        self.abnormalstatres += 10

    # Hyper Buff
        # Silent Rampage
        self.fd += 15
        # For Liberty
        self.cd += 30

    # Hyper Skill
        # Feline Berserk - Reinforce
        self.dmg += 15
        # Wild Arrow Blast - Reinforce
        self.pfd += 20
        # Wild Arrow Blast - Crit DMG
        self.pcd += 20
        # Wild Arrow Blast - Boss Rush
        self.pbatk += 20
        # Summon Jaguar - Cooldown Cutter