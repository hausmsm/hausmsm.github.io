class Ds:
    def __init__(self):
        # Offensive Stats
        self.atk = 1577
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.platk = 0
        self.cr = 4.9
        self.cratk = 0
        self.cd = 7.4
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
        self.hp = 10285
        self.mp = 3169
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

        # Demon Impact
        self.pname = "Demon Impact"
        self.pskilldmg = 160
        self.phitcount = 8
        self.pchance = 100
        self.patkp = 0
        self.pdmg = 0
        self.pbatk = 0
        self.pplatk = 0
        self.pcr = 10
        self.pcratk = 0
        self.pcd = 0
        self.pmaxdmg = 0
        self.pfd = 0

        # Cerberus Chomp
        self.sname = "Cerberus Chomp"
        self.sskilldmg = 350
        self.shitcount = 10
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

        # Demon Cry
        self.tname = "Demon Cry"
        self.tskilldmg = 190
        self.thitcount = 7
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
        # Battle Pact

        # Demon Lash
        # Shadow Swiftness
        self.spd += 15
        self.jmp += 15
        # HP Increase
        self.hpinc += 3
        # Dark Winds
        # Demonic Blood
        self.kbkres += 35
        # Curse of Fury
        self.dmg += 100
        self.hprecp += 5

    # 2nd Job
        # Vengeance
        self.dmg += 10

        # Barbed Lash
        # Weapon Mastery
        self.accp += 3
        self.dmg += 10
        # Physical Training
        self.atkp += 10
        self.hpinc += 5
        # Outrage
        self.cr += 3
        self.atkp += 10

    # 3rd Job
        # Black-Hearted Strength
        self.critres += 5
        self.pdefinc += 10
        self.mdefinc += 10
        # Insult to Injury
        self.dmg += 10
        self.cr += 5
        self.cd += 15
        # Focused Fury
        self.atkp += 15
        # Possessed Aegis
        self.block += 10
        # Max Fury

    # 4th Job
        # Demon Cry
        self.dmg += 10

        # Dark Metamorphosis
        self.dmg += 15
        self.hpinc += 10
        # Boundless Rage
        self.fd += 15
        # Leech Aura
        self.batk += 15
        self.bdef += 15

        # Demon Thrash
        # Barricade Mastery
        self.dmg += 25
        self.cd += 15
        # Obsidian Skin
        self.pdefdec += 15
        self.mdefdec += 15

    # Hyper Buff
        # Blue Blood
        self.spmulti += 50
        # Demonic Fortitude
        self.cd += 30

        # Hyper Skill
        # Demon Impact - Reinforce
        self.pfd += 20
        # Demon Impact - Extra Strike
        self.phitcount += 1
        # Demon Impact - Reduce Fury
        # Dark Metamorphosis - Enhance
        # Demon Lash - Fury
