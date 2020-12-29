class Hero:
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

        # Raging Blow
        self.pname = "Raging Blow"
        self.pskilldmg = 210
        self.phitcount = 7
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
        self.shitcount = 0
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

        # Rising Rage
        self.tname = "Rising Rage"
        self.tskilldmg = 325
        self.thitcount = 15
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
        self.pdefinc += 18
        self.mdefinc += 18
        # Warrior Mastery
        self.atkp += 9

        # 2nd Job
        # Combo Attack
        # Weapon Booster
        # Unmanaged Anger
        self.atkp += 21
        # Weapon Mastery
        self.dmg += 4
        # Final Attack
        self.schance += 20
        self.sskilldmg += 33.7
        # Physical Training
        self.accp += 6
        self.evdp += 6
        self.spd += 15

        # 3rd Job
        # Combo Synergy
        self.cr += 2
        # Self Recovery
        self.hprec += 229
        self.mprec += 92
        self.bdef += 4
        self.pldef += 4
        # Chance Attack
        self.cd += 15
        # Endure
        self.critdmgres += 10

        # 4th Job
        # Puncture
        self.cd += 10

        # Enrage
        self.fd += 25

        # KBK RES
        self.kbkres += 26
        # Advanced Combo Attack
        self.fd += 20
        # Combat Mastery
        self.batk += 4
        self.platk += 4
        # Advanced Final Attack
        self.schance += 20
        self.sskilldmg += 33.9

    # Hyper Buff
        # Cry Valhalla
        self.fd += 15
        self.atkp += 15
        # Epic Adventure
        self.cd += 30

    # Hyper Skill
        # Advanced Combo Attack - Reinforce
        self.fd += 10
        # Advanced Combo Attack - Boss Rush
        self.batk += 20
        # Advanced Final Attack - Opportunity
        self.schance += 30
        # Raging Blow - Reinforce
        self.pfd += 20
        # Raging Blow - Extra Strike
        self.phitcount += 1
