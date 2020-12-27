class Dk:
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

        # Gungnir's Descent
        self.pname = "Gungnir's Descent"
        self.pskilldmg = 226.7
        self.phitcount = 10
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

        # Nightshade Explosion
        self.sname = "Nightshade Explosion"
        self.sskilldmg = 335
        self.shitcount = 18
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

        # Revenge of the Evil Eye
        self.tname = "Revenge of the Evil Eye"
        self.tskilldmg = 267.9
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
        # Warrior Leap
        # Iron Body
        self.pdefinc += 20
        self.mdefinc += 20
        self.hpinc += 30
        self.mpinc += 20
        # Warrior Mastery
        self.atkp += 12

    # 2nd Job
        # Beholder
        self.hprec += 5000

        # Iron Will (Party)
        self.bdef += 12
        self.pldef += 12
        # Hyper Body (Party)
        self.pdefdec += 9
        self.mdefdec += 9
        # Weapon Booster

        # Weapon Mastery
        self.dmg += 6
        # Physical Training
        self.accp += 6
        self.evdp += 6
        self.spd += 15
        # Final Attack

    # 3rd Job
        # Cross Surge
        self.atkp += 15
        self.dmg += 10

        # Beholder Shock
        # Lord of Darkness
        self.cr += 4
        self.cd += 10
        # Beholder's Buff
        self.mprec += 48
        # Endure
        self.critdmgres += 10

    # 4th Job
        # Sacrifice
        # Final Pact
        self.atkp += 5

        # KBK RES
        self.kbkres += 26
        # Advanced Weapon Mastery
        self.penrate += 2
        self.batk += 6
        self.platk += 6
        # Revenge of the Evil Eye

    # Hyper Buff
        # Dark Thirst
        self.atkp += 25
        self.dmg += 15
        self.hprecp += 1
        # Epic Adventure
        self.cd += 30

        # Beholder - Reinforce
        self.atkp += 20
        # Beholder - Sacrifice

    # Hyper Skill
        # Gungnir's Descent - Reinforce
        self.pfd += 20
        # Gungnir's Descent - Boss Rush
        self.pbatk += 20
        # Gungnir's Descent - Extra Strike
        self.phitcount += 1
