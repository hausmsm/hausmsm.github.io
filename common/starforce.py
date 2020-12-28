class Starforce:
    def __init__(self, sf_amount):
        # Emblem Visualization
        self.emblem = "None"
        self.emblem_amount = 0
        self.emblem_level = 0

        # Type of Emblem
        self.normal_emb = 0
        self.partial_emb = 0
        self.unique_acc_emb = 0
        self.legendary_acc_emb = 0

        # Emblem Stats
        self.emblem_cd = 0
        self.emblem_batk = 0
        self.emblem_atkp = 0

        # SF Stats
        self.sf = sf_amount

        # Equipment Type, Stat & Rank
        self.type = "None"
        self.stat = "None"
        self.stat_amount = 0
        self.rank = "None"

        # Offensive Stats
        self.atk = 0
        self.atkp = 0
        self.dmg = 0
        self.batk = 0
        self.platk = 0
        self.cr = 0
        self.cratk = 0
        self.cd = 0
        self.maxdmg = 0
        self.fd = 0

        # Defensive Stats
        self.pdef = 0
        self.pdefinc = 0
        self.pdefdec = 0
        self.mdef = 0
        self.mdefinc = 0
        self.mdefdec = 0
        self.bdef = 0
        self.pldef = 0
        self.critres = 0
        self.critdmgres = 0

        # Hit Miss Stats
        self.acc = 0
        self.accp = 0
        self.evd = 0
        self.evdp = 0
        self.penrate = 0
        self.block = 0
        self.abnormalstatres = 0
        self.ignore = 0

        # HP MP Stats
        self.hp = 0
        self.mp = 0
        self.hpinc = 0
        self.mpinc = 0
        self.hprec = 0
        self.mprec = 0
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

        # Set Stats
        self.mempsetcount = 0
        self.aempsetcount = 0
        self.necrosetcount = 0
        self.fafsetcount = 0
        self.bosssetcount = 0
        self.commandersetcount = 0

        # Flame Stats
        self.atklinecount = 0
        self.crlinecount = 0
        self.cdlinecount = 0

        if sf_amount >= 255:
            self.atk += 1500
            self.partyexp += 10
            self.maxfeverchance += 8
            self.maxdmg += 250000
        elif sf_amount >= 245:
            self.atk += 1440
            self.partyexp += 9.5
            self.maxfeverchance += 7
            self.maxdmg += 225000
        elif sf_amount >= 240:
            self.atk += 1380
            self.partyexp += 9
            self.maxfeverchance += 7
            self.maxdmg += 200000
        elif sf_amount >= 235:
            self.atk += 1320
            self.partyexp += 8.5
            self.maxfeverchance += 6
            self.maxdmg += 175000
        elif sf_amount >= 230:
            self.atk += 1260
            self.partyexp += 8
            self.maxfeverchance += 6
            self.maxdmg += 150000
        elif sf_amount >= 225:
            self.atk += 1200
            self.partyexp += 7.5
            self.maxfeverchance += 5
            self.maxdmg += 125000
        elif sf_amount >= 219:
            self.atk += 1140
            self.partyexp += 7
            self.maxfeverchance += 5
            self.maxdmg += 100000
        elif sf_amount >= 214:
            self.atk += 1080
            self.partyexp += 6.5
            self.maxfeverchance += 4
            self.maxdmg += 75000
        elif sf_amount >= 209:
            self.atk += 1020
            self.partyexp += 6
            self.maxfeverchance += 4
            self.maxdmg += 50000
        elif sf_amount >= 204:
            self.atk += 960
            self.partyexp += 5.5
            self.maxfeverchance += 3
            self.maxdmg += 25000
        elif sf_amount >= 198:
            self.atk += 900
            self.partyexp += 5
            self.maxfeverchance += 3
        elif sf_amount >= 192:
            self.atk += 840
            self.partyexp += 4.5
            self.maxfeverchance += 2
        elif sf_amount >= 186:
            self.atk += 780
            self.partyexp += 4
            self.maxfeverchance += 2
        elif sf_amount >= 179:
            self.atk += 720
            self.partyexp += 3.5
            self.maxfeverchance += 1
        elif sf_amount >= 172:
            self.atk += 660
            self.partyexp += 3
            self.maxfeverchance += 1
        elif sf_amount >= 164:
            self.atk += 600
            self.partyexp += 2.5
        elif sf_amount >= 157:
            self.atk += 540
            self.partyexp += 2
        elif sf_amount >= 149:
            self.atk += 480
            self.partyexp += 1.5
        elif sf_amount >= 140:
            self.atk += 420
            self.partyexp += 1
        elif sf_amount >= 132:
            self.atk += 360
            self.partyexp += 0.5
        elif sf_amount >= 124:
            self.atk += 300
        elif sf_amount >= 116:
            self.atk += 240
        elif sf_amount >= 108:
            self.atk += 180
        elif sf_amount >= 100:
            self.atk += 120
        elif sf_amount >= 95:
            self.atk += 60
