class Tb:
    def __init__(self):
        # Offensive Stats
        self.atk = 1578
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
        self.hp = 10280
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

        # Annihilate
        self.pname = "Annihilate"
        self.pskilldmg = 163
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

        # Thunderbolt
        self.sname = "Thunderbolt"
        self.sskilldmg = 178
        self.shitcount = 7
        self.schance = 100
        self.satkp = 0
        self.sdmg = 0
        self.sbatk = 0
        self.splatk = 0
        self.scr = 100
        self.scratk = 0
        self.scd = 0
        self.smaxdmg = 0
        self.sfd = 0

        # Deep Rising
        self.tname = "Deep Rising"
        self.tskilldmg = 500
        self.thitcount = 12
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
        # Lightning Elemental
        self.atkp += 5

        # Electrify
        self.spd += 15
        self.jmp += 15
        # Elemental Shift

    # 2nd Job
        # Knuckle Booster
        # Knuckle Mastery
        self.atkp += 5
        self.dmg += 4
        # Gains
        self.accp += 6
        self.penrate += 6
        # Lightning Boost

    # 3rd Job
        # Seawall
        self.dmg += 4
        self.pdefdec += 10
        self.mdefdec += 10
        # Ironclad
        self.kbkres += 30
        self.pdefinc += 15
        self.mdefinc += 15
        self.bdef += 5
        self.pldef += 5
        # Link Mastery
        self.pskilldmg += 18
        self.sskilldmg += 18
        # Lightning Lord

    # 4th Job
        # Typhoon
        self.dmg += 25

        # Arc Charger
        self.spmulti += 30
        # Speed Infusion
        self.batk += 9.6
        self.platk += 9.6

        # Knuckle Expert
        self.cr += 4
        self.critres += 4
        # Electrify
        self.hprec += 200
        self.mprec += 50
        self.hpinc += 20
        self.mpinc += 10
        # Thunder God
        self.cd += 15
        self.critres += 15

    # Hyper Buff
        # Primal Bolt
        self.atkp += 25
        self.dmg += 15
        # Glory Of The Guardians
        self.cd += 30

    # Hyper Skill
        # Annihilate - Boss Rush
        self.pbatk += 20
        # Annihilate - Crit DMG
        self.pcd += 20
        # Annihilate - Reinforce
        self.pfd += 20
        # Thunderbolt - Reinforce
        self.sfd += 20
        # Thunderbolt - Extra Strike
        self.shitcount += 1
