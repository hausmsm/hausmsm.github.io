class Bam:
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

        # Finishing Blow
        self.pname = "Finishing Blow"
        self.pskilldmg = 210
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

        # Dark Genesis - Main Attack
        self.sname = "Dark Genesis - Main Attack"
        self.sskilldmg = 270
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

        # Dark Genesis - Lightning Explosion
        self.tname = "Dark Genesis - Lightning Explosion"
        self.tskilldmg = 110
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
        # Hasty Aura
        self.spd += 15
        self.jmp += 15

        # Staff Artist
        self.cr += 4
        self.critres += 4
        self.batk += 8
        self.platk += 8

    # 2nd Job
        # Staff Boost
        # Draining Aura

        # Ordinary Conversion
        self.hprecp += 7.5
        self.hpinc += 20
        self.mpinc += 20
        # Grim Contract
        # Staff Mastery
        self.atkp += 15
        # High Wisdom
        self.dmg += 10

    # 3rd Job
        # Dark Shock
        # Blue Aura
        self.pdefinc += 15
        self.mdefinc += 15

        # Battle Mastery
        self.cd += 10
        self.critdmgres += 10
        self.bdef += 4
        self.pldef += 4
        # Power Stance
        self.kbkres += 26
        # Dark Conditioning
        self.accp += 3
        self.evdp += 9
        # Grim Contract II

    # 4th Job
        # Battle Rage
        self.fd += 25
        self.cd += 10
        # Dark Aura
        self.dmg += 20

        # Staff Expert
        self.cd += 15
        self.atkp += 25
        # Spell Boost
        self.dmg += 25
        # Grim Contract III

    # Hyper Buff
        # Master of Death
        self.dmg += 15
        # For Liberty
        self.cd += 30

    # Hyper Skill
        # Dark Aura - Boss Rush
        self.batk += 10
        # Party Shield - Cooldown Cutter
        # Party Shield - Persist
        # Dark Genesis - Cooldown Cutter
        # Dark Genesis - Additional Reinforce
        self.tfd += 20
