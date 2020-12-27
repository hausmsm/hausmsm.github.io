class Bw:
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

        # Final Orbital Flame
        self.pname = "Final Orbital Flame"
        self.pskilldmg = 191
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

        # Blazing Extinction
        self.sname = "Blazing Extinction"
        self.sskilldmg = 440
        self.shitcount = 2
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

        # Ignition
        self.tname = "Ignition"
        self.tskilldmg = 276.3
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
        # Flame Elemental
        # Use Final Flame Elemental Instead
        # Fire Walk
        # Fire Repulsion
        # Natural Talent
        self.cr += 5
        self.critres += 5

    # 2nd Job
        # Ignition
        # Word of Fire

        # Greater Flame Elemental
        # Use Final Flame Elemental Instead
        # Spell Control
        self.pdefinc += 15
        self.mdefinc += 15
        self.pdefdec += 5
        self.mdefdec += 5

    # 3rd Job
        # Phoenix Run
        # Liberated Magic
        self.dmg += 30

        # Grand Flame Elemental
        # Use Final Flame Elemental Instead
        # Burning Focus
        self.cd += 10
        self.critdmgres += 10
        # Brilliant Enlightenment
        self.accp += 6
        self.penrate += 6
        self.atkp += 6

    # 4th Job
        # Towering Inferno
        self.dmg += 10
        # Burning Conduit
        self.atkp += 20
        self.dmg += 5

        # Fires of Creation
        self.kbkres += 25
        self.spd += 15
        self.jmp += 15
        # Flame Barrier
        self.evdp += 6

        # Final Flame Elemental
        self.atkp += 15
        self.dmg += 10
        self.batk += 5
        self.platk += 5
        self.cr += 5
        # Pure Magic
        self.atkp += 10
        self.hpinc += 10
        self.mpinc += 10
        # Wild Blaze

    # Hyper Buff
        # Glory Of The Guardians
        self.cd += 30

        # Hyper Skill
        # Orbital Flame- Boss Rush
        self.pbatk += 20
        # Orbital Flame - Crit DMG
        self.pcd += 20
        # Orbtial Flame - Split Attack
        self.pfd -= 10
        self.phitcount *= 2
        # Ignition - Max Extinction
        # Blazing Extinction - Max Extinction
