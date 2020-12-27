class Merc:
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

        # Ishtar's Ring
        self.pname = "Ishtar's Ring"
        self.pskilldmg = 221
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

        # Advanced Final Attack
        self.sname = "Advanced Final Attack"
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

        # Wrath of Enlil
        self.tname = "Wrath of Enlil"
        self.tskilldmg = 325
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
        # Potential Power
        self.atkp += 15
        self.pdefinc += 10
        self.mdefinc += 10
        # Sharp Aim
        self.cr += 4
        self.critres += 4
        # Updraft
        # Glide Blast

    # 2nd Job
        # Dual Bowguns Boost

        # Dual Bowguns Mastery
        self.dmg += 20
        # Final Attack: Dual Bowguns
        self.schance += 30
        self.sskilldmg += 35
        # Physical Training
        self.hprec += 50
        self.mprec += 20
        self.hpinc += 10
        self.mpinc += 10
        # Spirit Surge
        self.cd += 18
        self.critdmgres += 18

    # 3rd Job
        # Unicorn Spike
        self.dmg += 10

        # Ignis Roar
        self.dmg += 40

        # Water Shield
        self.kbkres += 31
        self.pdefdec += 9.6
        self.mdefdec += 9.6
        self.spd += 20
        self.jmp += 18

    # 4th Job
        # Spikes Royale
        self.dmg += 10

        # Ancient Warding
        self.accp += 6
        self.evdp += 12
        self.penrate += 6
        self.hpinc += 5

        # Staggering Strikes
        # Dual Bowguns Expert
        self.batk += 15
        self.bdef += 9.6
        self.platk += 15
        self.pldef += 9.6
        # Defense Break
        self.atkp += 20
        # Advanced Final Attack
        self.schance += 30
        self.sskilldmg += 29.4

    # Hyper Buff
        # Elvish Blessing
        self.atkp += 25
        self.dmg += 15
        # Heroic Memories
        self.cd += 30

    # Hyper Skill
        # Ishtar's Ring - Reinforce
        self.pfd += 20
        # Ishtar's Ring - Boss Rush
        self.pbatk += 20
        # Ishtar's Ring - Crit DMG
        self.pcd += 20
        # Ignis Roar - Reinforce
        self.dmg += 10
        # Spikes Royale - Armorbreak
        self.dmg += 10
