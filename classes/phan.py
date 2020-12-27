class Phan:
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

        # Mille Aiguilles
        self.pname = "Mille Aiguilles"
        self.pskilldmg = 240
        self.phitcount = 1
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

        # Tempest
        self.sname = "Tempest"
        self.sskilldmg = 290
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

        # Carte Noire
        self.tname = "Carte Noire"
        self.tskilldmg = 0
        self.thitcount = 1
        self.tchance = 0
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
        # Phantom Swiftness
        # Quick Dodge
        self.block += 5
        self.evdp += 5

    # 2nd Job
        # Impeccable Memory 2 - Unmanaged Anger
        self.atkp += 21

        # Cane Booster

        # Judgement Draw
        self.cd += 12
        self.tchance += 60
        # Carte Blanc
        self.tskilldmg += 80
        # Cane Mastery
        self.atkp += 20
        # Devil's Luck
        self.cr += 5
        self.critres += 5

     # 3rd Job
        # Impeccable Memory 3 - Combat Orders
        self.dmg += 15

        # Final Feint
        # Bad Luck Ward
        self.pdefinc += 10
        self.mdefinc += 10
        self.hpinc += 15
        self.mpinc += 10

        # Mist Mask
        self.ignore += 5
        self.spd += 18
        self.jmp += 18
        # Clair de Lune
        self.dmg += 25
        # Piercing Vision
        self.cr += 3
        self.cd += 15

    # 4th Job
        # Aria Armour
        self.atkp += 15
        self.dmg += 15

        # Carte Noire
        self.tskilldmg += 175
        self.tchance += 40
        # Cane Expert
        self.accp += 4.8
        self.penrate += 6
        self.atkp += 15
        self.dmg += 15

    # Hyper Buff
        # Impeccable Memory H - Cry Valhalla
        self.kbkres += 32
        self.atkp += 15
        self.fd += 15

        # Heroic Memores
        self.cd += 30

    # Hyper Skill
        # Bad Luck Ward
        self.atkp += 20
        # Mille Aiguilles - Reinforce
        self.pfd += 20
        # Mille Aiguilles - Crit DMG
        self.pcd += 15
        # Tempest - Reinforce
        self.sfd += 20
        # Tempest - Cooldown Cutter
