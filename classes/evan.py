class Evan:
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

        # Earth Dive
        self.pname = "Earth Dive"
        self.pskilldmg = 930.8
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

        # Mana Burst 4
        self.sname = "Mana Burst 4"
        self.sskilldmg = 96.9
        self.shitcount = 8
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

        # Dragon Master
        self.tname = "Dragon Master"
        self.tskilldmg = 335
        self.thitcount = 12
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

        # Dragon Soul
        self.spd += 18
        self.jmp += 18
        # Magic Link
        self.pdefdec += 9.6
        self.mdefdec += 9.6
        # Dragon Spark

    # 2nd Job
        # Magic Booster

        # Mana Burst 2
        # Use Mana Burst 4 Instead
        # Return Flash
        self.dmg += 15
        # High Wisdom
        self.accp += 4.8
        self.evdp += 14.4
        self.penrate += 4.8
        # Partners
        self.dmg += 14.4
        # Spell Mastery
        self.cr += 4.8
        # Support Mastery
        # Advanced Dragon Spark

    # 3rd Job
        # Elemental Decrease
        self.dmg += 14.4

        # Mana Burst 3
        # Use Mana Burst 4 Instead
        # Return Dive
        self.dmg += 15
        # Thunder Dive
        # Thunder Flash
        # Critical Magic
        self.cr += 4.8
        self.critres += 4.8
        # Magic Resistance
        self.bdef += 12
        self.pldef += 12
        # Magic Amplification
        self.dmg += 20
        # Dragon Potential
        self.atkp += 10.8

    # 4th Job
        # Blessing of the Onyx
        self.pdefinc += 13
        self.mdefinc += 13

        # Mana Burst 4
        # Wind Breath
        # Earth Breath
        # Return Flame
        # Enhanced Magic Debris
        # Magic Mastery
        self.cd += 18
        self.critdmgres += 18
        # Onyx Will
        self.kbkres += 31
        self.pdefdec += 9.6
        self.mdefdec += 9.6
        # Dragon Fury
        self.atkp += 15
        # High Dragon Potential
        self.batk += 9.6
        self.platk += 9.6

    # Hyper Buff
        # Heroic Memories
        self.cd += 30

    # Hyper Skill
        # Dragon Dive - Cooldown Reduction
        # Dragon Dive - Enhance Earth
        # Dragon Breath - Cooldown Reduction
        # Dragon Breath - Reinforce Wind
        # Dragon Breath - Affix Earth
