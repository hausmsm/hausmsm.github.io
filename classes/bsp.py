class Bsp:
    def __init__(self):
        # Offensive Stats
        self.atk = 1580
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.platk = 0
        self.cr = 5.1
        self.cratk = 0
        self.cd = 11.3
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
        self.hp = 10267
        self.mp = 3173
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

        # Angel Ray
        self.pname = "Angel Ray"
        self.pskilldmg = 175.5
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

        # Genesis
        self.sname = "Genesis"
        self.sskilldmg = 327.7
        self.shitcount = 6
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

        # Heaven's Door
        self.tname = "Heaven's Door"
        self.tskilldmg = 455
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
        # Magic Guard

        # Magic Armor
        self.pdefinc += 9
        self.mdefinc += 9
        # MP Increase
        self.mprec += 7
        self.mpinc += 30

    # 2nd Job
        # Bless
        # Use Advanced Bless Instead
        # Magic Booster

        # MP Eater
        self.mprecp += 1
        # Invincible
        self.pdefdec += 4
        self.mdefdec += 4
        # Spell Mastery
        self.hprec += 53
        self.hpinc += 10
        # Blessed Ensemble
        self.atkp += 9
        # Final Damage Replaced By Blessed Harmony
        # High Wisdom
        self.dmg += 4
        self.spd += 15

    # 3rd Job
        # Holy Symbol (Party)
        self.exp += 10
        self.kbkres += 13
        # Holy Magic Shell (Party)
        self.hpinc += 10
        self.mpinc += 10
        # Teleport Mastery
        # Divine Protection

        # Holy Focus
        self.critres += 4
        self.critdmgres += 10
        # Arcane Overdrive
        self.cr += 4
        self.cd += 10

    # 4th Job
        # Advanced Blessing (Party)
        self.accp += 10
        self.evd += 15
        self.atkp += 20
        # Infinity
        self.penrate += 5
        self.batk += 8
        self.platk += 8

        # Buff Mastery
        self.pdefdec += 4
        self.mdefdec += 4
        self.bdef += 10
        self.pldef += 10
        # Arcane Aim
        self.atkp += 15
        # Blessed Harmony
        self.atkp += 9
        self.fd += 20

    # Hyper Buff
        # Righteously Indignant
        self.atkp += 25
        self.dmg += 15
        self.pskilldmg += 20.5
        self.phitcount += 5
        # Epic Adventure
        self.cd += 30

    # Hyper Skill
        # Advanced Blessing - Bonus Damage
        self.atkp += 15
        # Advanced Blessing - Boss Rush
        self.batk += 15
        # Infinity - Reinforce
        self.batk += 20
        # Holy Magic Shell - Reinforce
        self.hp += 7808
        self.mp += 3124
        # Holy Symbol - Experience
        self.exp += 10
