class Shad:
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

        # Assassinate
        self.pname = "Assassinate"
        self.pskilldmg = 275
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

        # Meso Explosion
        self.sname = "Meso Explosion"
        self.sskilldmg = 151.8
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

        # Shadow Veil
        self.tname = "Shadow Veil"
        self.tskilldmg = 400
        self.thitcount = 1
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
        # Dark Sigh
        # Haste
        self.spd += 20

        # Flash Jump
        # Nimble Body
        self.accp += 2
        self.evdp += 6
        self.cr += 2

    # 2nd Job
        # Meso Guard
        # Dagger Booster

        # Critical Growth
        self.cd += 17.5
        # Channel Karma
        self.pdefinc += 9
        self.mdefinc += 9
        # Dagger Mastery
        self.atkp += 9
        # Physical Training
        self.hprec += 55
        self.mprec += 22
        self.critdmgres += 10
        # Shield Mastery
        self.pdefdec += 8
        self.mdefdec += 8

    # 3rd Job
        # Shadow Partner
        self.spmulti += 35
        # Pickpocket

        # Gustav
        self.meso += 4
        # Venom
        # Enveloping Darkness
        self.hpinc += 20
        self.mpinc += 10
        # Advanced Dark Sight

    # 4th Job
        # Smokescreen
        self.cd += 15

        # Shadower Instinct
        self.atkp += 20
        # Shadow Shifter

        # Prime Critical
        self.cr += 2
        self.critres += 2
        # Toxic Venom
        # Dagger Expert
        self.cd += 10
        self.batk += 10
        self.platk += 4

    # Hyper Buff
        # Flip of the Coin
        self.atkp += 15
        self.cd += 15
        # Epic Adventure
        self.cd += 30

    # Hyper Skill
        # Assassinate - Reinforce
        self.pfd += 20
        # Assassinate - Boss Rush
        self.pbatk += 20
        # Assassinate - Critical Damage
        self.pcd += 20
        # Meso Explosion - Reinforce
        self.sfd += 20
        # Meso Explosion - Crit DMG
        self.scd += 20
