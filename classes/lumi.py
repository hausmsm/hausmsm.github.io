class Lumi:
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

        # Ender
        self.pname = "Ender"
        self.pskilldmg = 309.8
        self.phitcount = 9
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

        # Reflection
        self.sname = "Reflection"
        self.sskilldmg = 247.9
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

        # Armageddon
        self.tname = "Armageddon"
        self.tskilldmg = 500
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
        # Ordinary Magic Guard
        self.pdefdec += 9.6
        self.mdefdec += 9.6
        # Light/ Dark Affinity
        self.fd += 10
        # Mana Well
        self.kbkres += 31

    # 2nd Job
        # Magic Booster

        # Bless Of Darkness
        self.atkp += 32.4
        # Spell Mastery
        self.cr += 4.8
        self.hpinc += 10
        self.mpinc += 20
        # High Wisdom
        self.accp += 4.8
        self.evdp += 14.4
        self.penrate += 4.8

    # 3rd Job
        # Shadow Shell
        # Dusk Guard
        self.ignore += 20
        # Photic Meditation (Party)
        self.atkp += 21.6

        # Lunar Tide
        self.cd += 15

    # 4th Job
        # Dark Crescendo
        self.cd += 20
        self.atkp += 15
        # Arcane Pitch
        self.batk += 15
        self.platk += 15

        # Magic Mastery
        self.cd += 18
        self.critdmgres += 18
        # Darkness Mastery

    # Hyper Buff
        # Heroic Memories
        self.cd += 30

    # Hyper Skill
        # Ender - Reinforce
        self.pfd += 20
        # Ender - Crit DMG
        self.pcd += 20
        # Reflection - Reinforce
        self.sfd += 20
        # Apocalypse - Reinforce
        # Apocalypse - Recharge
