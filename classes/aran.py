class Aran:
    def __init__(self):
        # Offensive Stats
        self.atk = 1579
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.platk = 0
        self.cr = 0.1
        self.cratk = 0
        self.cd = 0
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
        self.hp = 10276
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

        # Beyond Blade - 1st Hit
        self.pname = "Beyond Blade - 1st Hit"
        self.pskilldmg = 287
        self.phitcount = 5
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

        # Beyond Blade - 2nd Hit
        self.sname = "Beyond Blade - 2nd Hit"
        self.sskilldmg = 300
        self.shitcount = 5
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

        # Beyond Blade - 3rd Hit
        self.tname = "Beyond Blade - 3rd Hit"
        self.tskilldmg = 314
        self.thitcount = 5
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
        # Polearm Booster
        # Body Pressure

        # Combo Ability
        self.cr += 3
        self.critres += 3
        # Combat Step
        # Smash Swing

    # 2nd Job
        # Drain
        self.atkp += 10
        # Snow Charge
        self.dmg += 17.5

        # Polearm Mastery
        self.atkp += 20
        self.batk += 15
        self.platk += 15
        # Physical Training
        self.hprec += 60
        self.mprec += 30
        self.hpinc += 10
        self.mpinc += 10
        # Final Attack
        # Command Mastery I
        self.pskilldmg += 17.5
        self.sskilldmg += 17.5
        self.tskilldmg += 17.5
        # Swing Studies I

    # 3rd Job
        # Maha's Blessing
        self.hpinc += 10
        self.mpinc += 10

        # Advanced Combo Ability
        self.cd += 20
        self.critdmgres += 20
        # Cleaving Blows
        self.dmg += 10
        # Adrenaline Rush
        self.dmg += 10
        self.pdefdec += 10
        self.mdefdec += 10
        self.cr += 3
        self.cd += 15
        # Aero Swing
        # Might
        self.kbkres += 31
        self.spd += 18
        self.jmp += 18

    # 4th Job
        # High Mastery
        self.accp += 4
        self.evdp += 4
        self.penrate += 4
        # High Defense
        self.pdefinc += 10
        self.mdefinc += 10
        self.bdef += 5
        self.pldef += 5
        # Sudden Strike
        # Advanced Final Attack
        # Command Mastery II
        self.pskilldmg += 14.2
        self.sskilldmg += 14.2
        self.tskilldmg += 14.2
        # Swing Studies II

    # Hyper Buff
        # Adrenaline Burst

        # Heroic Memories
        self.cd += 30

    # Hyper Skill
        # Beyond Blade - Reinforce
        self.pfd += 20
        self.sfd += 20
        self.tfd += 20
        # Beyond Blade - Crit DMG
        self.pcd += 20
        self.scd += 20
        self.tcd += 20
        # Beyond Blade - Extra Strike
        self.phitcount += 1
        self.shitcount += 1
        self.thitcount += 1
        # Adrenaline Rush - Persist
        # Hunter's Prey Reinforce
