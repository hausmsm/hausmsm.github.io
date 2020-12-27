class Dw:
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

        # Moon Dancer
        self.pname = "Moon Dancer"
        self.pskilldmg = 125
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

        # Speeding Sunset
        self.sname = "Speeding Sunset"
        self.sskilldmg = 250
        self.shitcount = 4
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

        # Styx Crossing
        self.tname = "Styx Crossing"
        self.tskilldmg = 365
        self.thitcount = 18
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
        # Soul Elemental

        # Hand of Light
        self.atkp += 8
        # Inner Voice
        self.spd += 15
        self.jmp += 15
        # Elemental Shift

    # 2nd Job
        # Falling Moon
        # Use Equinox Cycle Instead
        # Soul Speed

        # Divine Hand
        self.pdefinc += 15
        self.mdefinc += 15
        # Sword Mastery
        self.dmg += 6
        # Inner Harmony
        self.kbkres += 30
        self.pdefdec += 10
        self.mdefdec += 10

    # 3rd Job
        # Rising Sun
        # Use Equinox Cycle Instead
        # True Sight
        self.atkp += 15
        self.bdef += 10
        self.pldef += 10

        # Soul of the Guardian
        self.hprec += 150
        self.mprec += 50
        self.hpinc += 30
        self.mpinc += 10
        # Will of Steel
        self.hprecp += 10
        # Inner Shout
        self.accp += 6
        self.penrate += 6

    # 4th Job
        # Equinox Cycle
        self.cr += 10
        self.cd += 15
        self.fd += 20

        # Soul Pledge
        self.cr += 4
        # Student of the Blade
        self.cd += 10
        self.critdmgres += 10
        # Unpredictable
        self.batk += 10
        self.platk += 10
        # Master of the Sword
        self.pskilldmg += 10
        self.sskilldmg += 15

    # Hyper Buff
        # Soul Forge
        self.atkp += 25
        self.dmg += 15
        # Glory of the Guardians
        self.cd += 30

    # Hyper Skill
        # Student of the Blade - Reinforce
        self.cd += 10
        # Unpredictable - Reinforce
        self.batk += 10
        # Careening Dance - Reinforce
        self.pfd += 10
        self.sfd += 10
        # Careening Dance - Extra Strike
        self.phitcount += 2
        self.shitcount += 1
        # Careening Dance - Boss Rush
        self.pbatk += 10
        self.sbatk += 10
