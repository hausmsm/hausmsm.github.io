class Seteffect:
    def __init__(self, badge, belt, cape, earring, eye, face, glove, hat, medal, necklace, ring, swep, shoe, shoulder, tbo, title, weapon):
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
        self.sf = 0

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

# Badge
        self.mempsetcount += badge.mempsetcount
        self.aempsetcount += badge.aempsetcount
        self.necrosetcount += badge.necrosetcount
        self.fafsetcount += badge.fafsetcount
        self.bosssetcount += badge.bosssetcount
        self.commandersetcount += badge.commandersetcount

# Belt
        self.mempsetcount += belt.mempsetcount
        self.aempsetcount += belt.aempsetcount
        self.necrosetcount += belt.necrosetcount
        self.fafsetcount += belt.fafsetcount
        self.bosssetcount += belt.bosssetcount
        self.commandersetcount += belt.commandersetcount

# Cape
        self.mempsetcount += cape.mempsetcount
        self.aempsetcount += cape.aempsetcount
        self.necrosetcount += cape.necrosetcount
        self.fafsetcount += cape.fafsetcount
        self.bosssetcount += cape.bosssetcount
        self.commandersetcount += cape.commandersetcount

# Earring
        self.mempsetcount += earring.mempsetcount
        self.aempsetcount += earring.aempsetcount
        self.necrosetcount += earring.necrosetcount
        self.fafsetcount += earring.fafsetcount
        self.bosssetcount += earring.bosssetcount
        self.commandersetcount += earring.commandersetcount

# Eye
        self.mempsetcount += eye.mempsetcount
        self.aempsetcount += eye.aempsetcount
        self.necrosetcount += eye.necrosetcount
        self.fafsetcount += eye.fafsetcount
        self.bosssetcount += eye.bosssetcount
        self.commandersetcount += eye.commandersetcount

# Face
        self.mempsetcount += face.mempsetcount
        self.aempsetcount += face.aempsetcount
        self.necrosetcount += face.necrosetcount
        self.fafsetcount += face.fafsetcount
        self.bosssetcount += face.bosssetcount
        self.commandersetcount += face.commandersetcount

# Glove
        self.mempsetcount += glove.mempsetcount
        self.aempsetcount += glove.aempsetcount
        self.necrosetcount += glove.necrosetcount
        self.fafsetcount += glove.fafsetcount
        self.bosssetcount += glove.bosssetcount
        self.commandersetcount += glove.commandersetcount

# Hat
        self.mempsetcount += hat.mempsetcount
        self.aempsetcount += hat.aempsetcount
        self.necrosetcount += hat.necrosetcount
        self.fafsetcount += hat.fafsetcount
        self.bosssetcount += hat.bosssetcount
        self.commandersetcount += hat.commandersetcount

# Medal
        self.mempsetcount += medal.mempsetcount
        self.aempsetcount += medal.aempsetcount
        self.necrosetcount += medal.necrosetcount
        self.fafsetcount += medal.fafsetcount
        self.bosssetcount += medal.bosssetcount
        self.commandersetcount += medal.commandersetcount

# Necklace
        self.mempsetcount += necklace.mempsetcount
        self.aempsetcount += necklace.aempsetcount
        self.necrosetcount += necklace.necrosetcount
        self.fafsetcount += necklace.fafsetcount
        self.bosssetcount += necklace.bosssetcount
        self.commandersetcount += necklace.commandersetcount

# Ring
        self.mempsetcount += ring.mempsetcount
        self.aempsetcount += ring.aempsetcount
        self.necrosetcount += ring.necrosetcount
        self.fafsetcount += ring.fafsetcount
        self.bosssetcount += ring.bosssetcount
        self.commandersetcount += ring.commandersetcount

# Swep
        self.mempsetcount += swep.mempsetcount
        self.aempsetcount += swep.aempsetcount
        self.necrosetcount += swep.necrosetcount
        self.fafsetcount += swep.fafsetcount
        self.bosssetcount += swep.bosssetcount
        self.commandersetcount += swep.commandersetcount

# Shoe
        self.mempsetcount += shoe.mempsetcount
        self.aempsetcount += shoe.aempsetcount
        self.necrosetcount += shoe.necrosetcount
        self.fafsetcount += shoe.fafsetcount
        self.bosssetcount += shoe.bosssetcount
        self.commandersetcount += shoe.commandersetcount

# Shoulder
        self.mempsetcount += shoulder.mempsetcount
        self.aempsetcount += shoulder.aempsetcount
        self.necrosetcount += shoulder.necrosetcount
        self.fafsetcount += shoulder.fafsetcount
        self.bosssetcount += shoulder.bosssetcount
        self.commandersetcount += shoulder.commandersetcount

# TBO
        self.mempsetcount += tbo.mempsetcount
        self.aempsetcount += tbo.aempsetcount
        self.necrosetcount += tbo.necrosetcount
        self.fafsetcount += tbo.fafsetcount
        self.bosssetcount += tbo.bosssetcount
        self.commandersetcount += tbo.commandersetcount

# Title
        self.mempsetcount += title.mempsetcount
        self.aempsetcount += title.aempsetcount
        self.necrosetcount += title.necrosetcount
        self.fafsetcount += title.fafsetcount
        self.bosssetcount += title.bosssetcount
        self.commandersetcount += title.commandersetcount

# Weapon
        self.mempsetcount += weapon.mempsetcount
        self.aempsetcount += weapon.aempsetcount
        self.necrosetcount += weapon.necrosetcount
        self.fafsetcount += weapon.fafsetcount
        self.bosssetcount += weapon.bosssetcount
        self.commandersetcount += weapon.commandersetcount

        # Boss Set
        if self.bosssetcount >= 2:
            self.atk += 50
            self.accp += 0.1
            if self.bosssetcount >= 3:
                self.atk += 50
                self.hp += 500
                self.mp += 500
                self.accp += 0.4
                if self.bosssetcount >= 4:
                    self.atk += 50
                    self.pdef += 500
                    self.mdef += 500
                    self.hp += 500
                    self.mp += 500
                    self.accp += 0.5
                    if self.bosssetcount >= 5:
                        self.atk += 50
                        self.pdef += 500
                        self.mdef += 500
                        self.hp += 500
                        self.mp += 500
                        self.cr += 3
                        self.accp += 0.5
                        self.spd += 0.5
                        if self.bosssetcount >= 6:
                            self.atk += 100
                            self.pdef += 500
                            self.mdef += 500
                            self.hp += 1000
                            self.mp += 1000
                            self.bdef += 2
                            self.cr += 1
                            self.cd += 2
                            self.accp += 0.5
                            self.spd += 0.5
                            if self.bosssetcount >= 7:
                                self.atk += 200
                                self.pdef += 1000
                                self.mdef += 1000
                                self.hp += 1000
                                self.mp += 1000
                                self.batk += 5
                                self.bdef += 3
                                self.cr += 1
                                self.cd += 3
                                self.accp += 1
                                self.spd += 0.5
        # Mythic Empress Set
        if self.mempsetcount >= 3:
            self.pdef += 2443
            self.mdef += 2443
            self.hp += 189
            if self.mempsetcount >= 5:
                self.atk += 49
                self.evdp += 5
                self.pdef += 2443
                self.mdef += 2443
                self.hp += 189
                if self.mempsetcount >= 7:
                    self.cr += 2
                    self.accp += 5
                    self.atk += 49
                    self.evdp += 5
                    self.pdef += 2443
                    self.mdef += 2443
                    self.hp += 189
        # Ancient Empress Set
        if self.aempsetcount >= 3:
            self.pdef += 2500
            self.mdef += 2500
            self.hp += 1000
            if self.aempsetcount >= 5:
                self.atk += 100
                self.evdp += 5
                self.pdef += 2500
                self.mdef += 2500
                self.hp += 1000
                if self.aempsetcount >= 7:
                    self.atk += 1000
                    self.cr += 3
                    self.accp += 6
                    self.atk += 100
                    self.evdp += 5
                    self.pdef += 2500
                    self.mdef += 2500
                    self.hp += 1000
        # Fafnir
        if self.fafsetcount >= 2:
            self.batk += 2
            if self.fafsetcount >= 3:
                self.cr += 4
                if self.fafsetcount >= 4:
                    self.atk += 950
        # Necro
        if self.necrosetcount >= 3:
            self.hp += 1000
            self.atkp += 5
            self.dmg += 5
            if self.necrosetcount >= 5:
                self.batk += 10
                if self.necrosetcount >= 7:
                    self.atk += 1500
        """print("\n")
        print(f"boss set: {self.bosssetcount}")
        print(f"memp set: {self.mempsetcount}")
        print(f"aemp set: {self.aempsetcount}")
        print(f"necro set: {self.necrosetcount}")
        print(f"fafnir set: {self.fafsetcount}")
        print(f"commander set: {self.commandersetcount}")
        print(f"atk: {self.atk}")
        print(f"batk: {self.batk}")
        print(f"hp: {self.hp}")"""
