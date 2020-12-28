class Flamestats:
    # Equipment + Set
    # Soul + Soul Set
    # Jewel + Jewel Set
    # Style + Style Set
    # Potential Options
    # Pet Set
    def __init__(self, badge, belt, cape, cash, earring, eye, face, glove, hat, jewel, medal, necklace, pet, ring, swep,
                 seteffect, shoe, shoulder, soul, tbo, title, weapon):
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
        # Type of Emblem
        self.normal_emb += badge.normal_emb
        self.partial_emb += badge.partial_emb
        self.unique_acc_emb += badge.unique_acc_emb
        self.legendary_acc_emb += badge.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += badge.emblem_cd
        self.emblem_batk += badge.emblem_batk
        self.emblem_atkp += badge.emblem_atkp

        # SF Stats
        self.sf += badge.sf

        # Offensive Stats
        self.atk += badge.atk
        self.atkp += badge.atkp
        self.dmg += badge.dmg
        self.batk += badge.batk
        self.platk += badge.platk
        self.cr += badge.cr
        self.cratk += badge.cratk
        self.cd += badge.cd
        self.maxdmg += badge.maxdmg
        self.fd += badge.fd

        # Defensive Stats
        self.pdef += badge.pdef
        self.pdefinc += badge.pdefinc
        self.pdefdec += badge.pdefdec
        self.mdef += badge.mdef
        self.mdefinc += badge.mdefinc
        self.mdefdec += badge.mdefdec
        self.bdef += badge.bdef
        self.pldef += badge.pldef
        self.critres += badge.critres
        self.critdmgres += badge.critdmgres

        # Hit Miss Stats
        self.acc += badge.acc
        self.accp += badge.accp
        self.evd += badge.evd
        self.evdp += badge.evdp
        self.penrate += badge.penrate
        self.block += badge.block
        self.abnormalstatres += badge.abnormalstatres
        self.ignore += badge.ignore

        # HP MP Stats
        self.hp += badge.hp
        self.mp += badge.mp
        self.hpinc += badge.hpinc
        self.mpinc += badge.mpinc
        self.hprec += badge.hprec
        self.mprec += badge.mprec
        self.hprecp += badge.hprecp
        self.mprecp += badge.mprecp
        self.hppotionrecp += badge.hppotionrecp
        self.mppotionrecp += badge.mppotionrecp
        self.buffdurationinc += badge.buffdurationinc

        # Mobility Stats
        self.spd += badge.spd
        self.jmp += badge.jmp
        self.kbkres += badge.kbkres

        # Misc Stats
        self.exp += badge.exp
        self.dr += badge.dr
        self.meso += badge.meso
        self.glincrease += badge.glincrease
        self.partyexp += badge.partyexp
        self.feverchargeinc += badge.feverchargeinc
        self.feverduration += badge.feverduration
        self.maxfeverchance += badge.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += badge.spmulti

        # Set Stats
        self.mempsetcount += badge.mempsetcount
        self.aempsetcount += badge.aempsetcount
        self.necrosetcount += badge.necrosetcount
        self.fafsetcount += badge.fafsetcount
        self.bosssetcount += badge.bosssetcount
        self.commandersetcount += badge.commandersetcount

        # Flame Stats
        self.atklinecount += badge.atklinecount
        self.crlinecount += badge.crlinecount
        self.cdlinecount += badge.cdlinecount

        # Belt
        self.normal_emb += belt.normal_emb
        self.partial_emb += belt.partial_emb
        self.unique_acc_emb += belt.unique_acc_emb
        self.legendary_acc_emb += belt.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += belt.emblem_cd
        self.emblem_batk += belt.emblem_batk
        self.emblem_atkp += belt.emblem_atkp

        # SF Stats
        self.sf += belt.sf

        # Offensive Stats
        self.atk += belt.atk
        self.atkp += belt.atkp
        self.dmg += belt.dmg
        self.batk += belt.batk
        self.platk += belt.platk
        self.cr += belt.cr
        self.cratk += belt.cratk
        self.cd += belt.cd
        self.maxdmg += belt.maxdmg
        self.fd += belt.fd

        # Defensive Stats
        self.pdef += belt.pdef
        self.pdefinc += belt.pdefinc
        self.pdefdec += belt.pdefdec
        self.mdef += belt.mdef
        self.mdefinc += belt.mdefinc
        self.mdefdec += belt.mdefdec
        self.bdef += belt.bdef
        self.pldef += belt.pldef
        self.critres += belt.critres
        self.critdmgres += belt.critdmgres

        # Hit Miss Stats
        self.acc += belt.acc
        self.accp += belt.accp
        self.evd += belt.evd
        self.evdp += belt.evdp
        self.penrate += belt.penrate
        self.block += belt.block
        self.abnormalstatres += belt.abnormalstatres
        self.ignore += belt.ignore

        # HP MP Stats
        self.hp += belt.hp
        self.mp += belt.mp
        self.hpinc += belt.hpinc
        self.mpinc += belt.mpinc
        self.hprec += belt.hprec
        self.mprec += belt.mprec
        self.hprecp += belt.hprecp
        self.mprecp += belt.mprecp
        self.hppotionrecp += belt.hppotionrecp
        self.mppotionrecp += belt.mppotionrecp
        self.buffdurationinc += belt.buffdurationinc

        # Mobility Stats
        self.spd += belt.spd
        self.jmp += belt.jmp
        self.kbkres += belt.kbkres

        # Misc Stats
        self.exp += belt.exp
        self.dr += belt.dr
        self.meso += belt.meso
        self.glincrease += belt.glincrease
        self.partyexp += belt.partyexp
        self.feverchargeinc += belt.feverchargeinc
        self.feverduration += belt.feverduration
        self.maxfeverchance += belt.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += belt.spmulti

        # Set Stats
        self.mempsetcount += belt.mempsetcount
        self.aempsetcount += belt.aempsetcount
        self.necrosetcount += belt.necrosetcount
        self.fafsetcount += belt.fafsetcount
        self.bosssetcount += belt.bosssetcount
        self.commandersetcount += belt.commandersetcount

        # Flame Stats
        self.atklinecount += belt.atklinecount
        self.crlinecount += belt.crlinecount
        self.cdlinecount += belt.cdlinecount

        # Cape
        self.normal_emb += cape.normal_emb
        self.partial_emb += cape.partial_emb
        self.unique_acc_emb += cape.unique_acc_emb
        self.legendary_acc_emb += cape.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += cape.emblem_cd
        self.emblem_batk += cape.emblem_batk
        self.emblem_atkp += cape.emblem_atkp

        # SF Stats
        self.sf += cape.sf

        # Offensive Stats
        self.atk += cape.atk
        self.atkp += cape.atkp
        self.dmg += cape.dmg
        self.batk += cape.batk
        self.platk += cape.platk
        self.cr += cape.cr
        self.cratk += cape.cratk
        self.cd += cape.cd
        self.maxdmg += cape.maxdmg
        self.fd += cape.fd

        # Defensive Stats
        self.pdef += cape.pdef
        self.pdefinc += cape.pdefinc
        self.pdefdec += cape.pdefdec
        self.mdef += cape.mdef
        self.mdefinc += cape.mdefinc
        self.mdefdec += cape.mdefdec
        self.bdef += cape.bdef
        self.pldef += cape.pldef
        self.critres += cape.critres
        self.critdmgres += cape.critdmgres

        # Hit Miss Stats
        self.acc += cape.acc
        self.accp += cape.accp
        self.evd += cape.evd
        self.evdp += cape.evdp
        self.penrate += cape.penrate
        self.block += cape.block
        self.abnormalstatres += cape.abnormalstatres
        self.ignore += cape.ignore

        # HP MP Stats
        self.hp += cape.hp
        self.mp += cape.mp
        self.hpinc += cape.hpinc
        self.mpinc += cape.mpinc
        self.hprec += cape.hprec
        self.mprec += cape.mprec
        self.hprecp += cape.hprecp
        self.mprecp += cape.mprecp
        self.hppotionrecp += cape.hppotionrecp
        self.mppotionrecp += cape.mppotionrecp
        self.buffdurationinc += cape.buffdurationinc

        # Mobility Stats
        self.spd += cape.spd
        self.jmp += cape.jmp
        self.kbkres += cape.kbkres

        # Misc Stats
        self.exp += cape.exp
        self.dr += cape.dr
        self.meso += cape.meso
        self.glincrease += cape.glincrease
        self.partyexp += cape.partyexp
        self.feverchargeinc += cape.feverchargeinc
        self.feverduration += cape.feverduration
        self.maxfeverchance += cape.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += cape.spmulti

        # Set Stats
        self.mempsetcount += cape.mempsetcount
        self.aempsetcount += cape.aempsetcount
        self.necrosetcount += cape.necrosetcount
        self.fafsetcount += cape.fafsetcount
        self.bosssetcount += cape.bosssetcount
        self.commandersetcount += cape.commandersetcount

        # Flame Stats
        self.atklinecount += cape.atklinecount
        self.crlinecount += cape.crlinecount
        self.cdlinecount += cape.cdlinecount

        # Cash
        self.normal_emb += cash.normal_emb
        self.partial_emb += cash.partial_emb
        self.unique_acc_emb += cash.unique_acc_emb
        self.legendary_acc_emb += cash.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += cash.emblem_cd
        self.emblem_batk += cash.emblem_batk
        self.emblem_atkp += cash.emblem_atkp

        # SF Stats
        self.sf += cash.sf

        # Offensive Stats
        self.atk += cash.atk
        self.atkp += cash.atkp
        self.dmg += cash.dmg
        self.batk += cash.batk
        self.platk += cash.platk
        self.cr += cash.cr
        self.cratk += cash.cratk
        self.cd += cash.cd
        self.maxdmg += cash.maxdmg
        self.fd += cash.fd

        # Defensive Stats
        self.pdef += cash.pdef
        self.pdefinc += cash.pdefinc
        self.pdefdec += cash.pdefdec
        self.mdef += cash.mdef
        self.mdefinc += cash.mdefinc
        self.mdefdec += cash.mdefdec
        self.bdef += cash.bdef
        self.pldef += cash.pldef
        self.critres += cash.critres
        self.critdmgres += cash.critdmgres

        # Hit Miss Stats
        self.acc += cash.acc
        self.accp += cash.accp
        self.evd += cash.evd
        self.evdp += cash.evdp
        self.penrate += cash.penrate
        self.block += cash.block
        self.abnormalstatres += cash.abnormalstatres
        self.ignore += cash.ignore

        # HP MP Stats
        self.hp += cash.hp
        self.mp += cash.mp
        self.hpinc += cash.hpinc
        self.mpinc += cash.mpinc
        self.hprec += cash.hprec
        self.mprec += cash.mprec
        self.hprecp += cash.hprecp
        self.mprecp += cash.mprecp
        self.hppotionrecp += cash.hppotionrecp
        self.mppotionrecp += cash.mppotionrecp
        self.buffdurationinc += cash.buffdurationinc

        # Mobility Stats
        self.spd += cash.spd
        self.jmp += cash.jmp
        self.kbkres += cash.kbkres

        # Misc Stats
        self.exp += cash.exp
        self.dr += cash.dr
        self.meso += cash.meso
        self.glincrease += cash.glincrease
        self.partyexp += cash.partyexp
        self.feverchargeinc += cash.feverchargeinc
        self.feverduration += cash.feverduration
        self.maxfeverchance += cash.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += cash.spmulti

        # Set Stats
        self.mempsetcount += cash.mempsetcount
        self.aempsetcount += cash.aempsetcount
        self.necrosetcount += cash.necrosetcount
        self.fafsetcount += cash.fafsetcount
        self.bosssetcount += cash.bosssetcount
        self.commandersetcount += cash.commandersetcount

        # Flame Stats
        self.atklinecount += cash.atklinecount
        self.crlinecount += cash.crlinecount
        self.cdlinecount += cash.cdlinecount

        # Earring
        self.normal_emb += earring.normal_emb
        self.partial_emb += earring.partial_emb
        self.unique_acc_emb += earring.unique_acc_emb
        self.legendary_acc_emb += earring.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += earring.emblem_cd
        self.emblem_batk += earring.emblem_batk
        self.emblem_atkp += earring.emblem_atkp

        # SF Stats
        self.sf += earring.sf

        # Offensive Stats
        self.atk += earring.atk
        self.atkp += earring.atkp
        self.dmg += earring.dmg
        self.batk += earring.batk
        self.platk += earring.platk
        self.cr += earring.cr
        self.cratk += earring.cratk
        self.cd += earring.cd
        self.maxdmg += earring.maxdmg
        self.fd += earring.fd

        # Defensive Stats
        self.pdef += earring.pdef
        self.pdefinc += earring.pdefinc
        self.pdefdec += earring.pdefdec
        self.mdef += earring.mdef
        self.mdefinc += earring.mdefinc
        self.mdefdec += earring.mdefdec
        self.bdef += earring.bdef
        self.pldef += earring.pldef
        self.critres += earring.critres
        self.critdmgres += earring.critdmgres

        # Hit Miss Stats
        self.acc += earring.acc
        self.accp += earring.accp
        self.evd += earring.evd
        self.evdp += earring.evdp
        self.penrate += earring.penrate
        self.block += earring.block
        self.abnormalstatres += earring.abnormalstatres
        self.ignore += earring.ignore

        # HP MP Stats
        self.hp += earring.hp
        self.mp += earring.mp
        self.hpinc += earring.hpinc
        self.mpinc += earring.mpinc
        self.hprec += earring.hprec
        self.mprec += earring.mprec
        self.hprecp += earring.hprecp
        self.mprecp += earring.mprecp
        self.hppotionrecp += earring.hppotionrecp
        self.mppotionrecp += earring.mppotionrecp
        self.buffdurationinc += earring.buffdurationinc

        # Mobility Stats
        self.spd += earring.spd
        self.jmp += earring.jmp
        self.kbkres += earring.kbkres

        # Misc Stats
        self.exp += earring.exp
        self.dr += earring.dr
        self.meso += earring.meso
        self.glincrease += earring.glincrease
        self.partyexp += earring.partyexp
        self.feverchargeinc += earring.feverchargeinc
        self.feverduration += earring.feverduration
        self.maxfeverchance += earring.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += earring.spmulti

        # Set Stats
        self.mempsetcount += earring.mempsetcount
        self.aempsetcount += earring.aempsetcount
        self.necrosetcount += earring.necrosetcount
        self.fafsetcount += earring.fafsetcount
        self.bosssetcount += earring.bosssetcount
        self.commandersetcount += earring.commandersetcount

        # Flame Stats
        self.atklinecount += earring.atklinecount
        self.crlinecount += earring.crlinecount
        self.cdlinecount += earring.cdlinecount

        # Eye
        self.normal_emb += eye.normal_emb
        self.partial_emb += eye.partial_emb
        self.unique_acc_emb += eye.unique_acc_emb
        self.legendary_acc_emb += eye.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += eye.emblem_cd
        self.emblem_batk += eye.emblem_batk
        self.emblem_atkp += eye.emblem_atkp

        # SF Stats
        self.sf += eye.sf

        # Offensive Stats
        self.atk += eye.atk
        self.atkp += eye.atkp
        self.dmg += eye.dmg
        self.batk += eye.batk
        self.platk += eye.platk
        self.cr += eye.cr
        self.cratk += eye.cratk
        self.cd += eye.cd
        self.maxdmg += eye.maxdmg
        self.fd += eye.fd

        # Defensive Stats
        self.pdef += eye.pdef
        self.pdefinc += eye.pdefinc
        self.pdefdec += eye.pdefdec
        self.mdef += eye.mdef
        self.mdefinc += eye.mdefinc
        self.mdefdec += eye.mdefdec
        self.bdef += eye.bdef
        self.pldef += eye.pldef
        self.critres += eye.critres
        self.critdmgres += eye.critdmgres

        # Hit Miss Stats
        self.acc += eye.acc
        self.accp += eye.accp
        self.evd += eye.evd
        self.evdp += eye.evdp
        self.penrate += eye.penrate
        self.block += eye.block
        self.abnormalstatres += eye.abnormalstatres
        self.ignore += eye.ignore

        # HP MP Stats
        self.hp += eye.hp
        self.mp += eye.mp
        self.hpinc += eye.hpinc
        self.mpinc += eye.mpinc
        self.hprec += eye.hprec
        self.mprec += eye.mprec
        self.hprecp += eye.hprecp
        self.mprecp += eye.mprecp
        self.hppotionrecp += eye.hppotionrecp
        self.mppotionrecp += eye.mppotionrecp
        self.buffdurationinc += eye.buffdurationinc

        # Mobility Stats
        self.spd += eye.spd
        self.jmp += eye.jmp
        self.kbkres += eye.kbkres

        # Misc Stats
        self.exp += eye.exp
        self.dr += eye.dr
        self.meso += eye.meso
        self.glincrease += eye.glincrease
        self.partyexp += eye.partyexp
        self.feverchargeinc += eye.feverchargeinc
        self.feverduration += eye.feverduration
        self.maxfeverchance += eye.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += eye.spmulti

        # Set Stats
        self.mempsetcount += eye.mempsetcount
        self.aempsetcount += eye.aempsetcount
        self.necrosetcount += eye.necrosetcount
        self.fafsetcount += eye.fafsetcount
        self.bosssetcount += eye.bosssetcount
        self.commandersetcount += eye.commandersetcount

        # Flame Stats
        self.atklinecount += eye.atklinecount
        self.crlinecount += eye.crlinecount
        self.cdlinecount += eye.cdlinecount

        # Face
        self.normal_emb += face.normal_emb
        self.partial_emb += face.partial_emb
        self.unique_acc_emb += face.unique_acc_emb
        self.legendary_acc_emb += face.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += face.emblem_cd
        self.emblem_batk += face.emblem_batk
        self.emblem_atkp += face.emblem_atkp

        # SF Stats
        self.sf += face.sf

        # Offensive Stats
        self.atk += face.atk
        self.atkp += face.atkp
        self.dmg += face.dmg
        self.batk += face.batk
        self.platk += face.platk
        self.cr += face.cr
        self.cratk += face.cratk
        self.cd += face.cd
        self.maxdmg += face.maxdmg
        self.fd += face.fd

        # Defensive Stats
        self.pdef += face.pdef
        self.pdefinc += face.pdefinc
        self.pdefdec += face.pdefdec
        self.mdef += face.mdef
        self.mdefinc += face.mdefinc
        self.mdefdec += face.mdefdec
        self.bdef += face.bdef
        self.pldef += face.pldef
        self.critres += face.critres
        self.critdmgres += face.critdmgres

        # Hit Miss Stats
        self.acc += face.acc
        self.accp += face.accp
        self.evd += face.evd
        self.evdp += face.evdp
        self.penrate += face.penrate
        self.block += face.block
        self.abnormalstatres += face.abnormalstatres
        self.ignore += face.ignore

        # HP MP Stats
        self.hp += face.hp
        self.mp += face.mp
        self.hpinc += face.hpinc
        self.mpinc += face.mpinc
        self.hprec += face.hprec
        self.mprec += face.mprec
        self.hprecp += face.hprecp
        self.mprecp += face.mprecp
        self.hppotionrecp += face.hppotionrecp
        self.mppotionrecp += face.mppotionrecp
        self.buffdurationinc += face.buffdurationinc

        # Mobility Stats
        self.spd += face.spd
        self.jmp += face.jmp
        self.kbkres += face.kbkres

        # Misc Stats
        self.exp += face.exp
        self.dr += face.dr
        self.meso += face.meso
        self.glincrease += face.glincrease
        self.partyexp += face.partyexp
        self.feverchargeinc += face.feverchargeinc
        self.feverduration += face.feverduration
        self.maxfeverchance += face.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += face.spmulti

        # Set Stats
        self.mempsetcount += face.mempsetcount
        self.aempsetcount += face.aempsetcount
        self.necrosetcount += face.necrosetcount
        self.fafsetcount += face.fafsetcount
        self.bosssetcount += face.bosssetcount
        self.commandersetcount += face.commandersetcount

        # Flame Stats
        self.atklinecount += face.atklinecount
        self.crlinecount += face.crlinecount
        self.cdlinecount += face.cdlinecount

        # Glove
        self.normal_emb += glove.normal_emb
        self.partial_emb += glove.partial_emb
        self.unique_acc_emb += glove.unique_acc_emb
        self.legendary_acc_emb += glove.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += glove.emblem_cd
        self.emblem_batk += glove.emblem_batk
        self.emblem_atkp += glove.emblem_atkp

        # SF Stats
        self.sf += glove.sf

        # Offensive Stats
        self.atk += glove.atk
        self.atkp += glove.atkp
        self.dmg += glove.dmg
        self.batk += glove.batk
        self.platk += glove.platk
        self.cr += glove.cr
        self.cratk += glove.cratk
        self.cd += glove.cd
        self.maxdmg += glove.maxdmg
        self.fd += glove.fd

        # Defensive Stats
        self.pdef += glove.pdef
        self.pdefinc += glove.pdefinc
        self.pdefdec += glove.pdefdec
        self.mdef += glove.mdef
        self.mdefinc += glove.mdefinc
        self.mdefdec += glove.mdefdec
        self.bdef += glove.bdef
        self.pldef += glove.pldef
        self.critres += glove.critres
        self.critdmgres += glove.critdmgres

        # Hit Miss Stats
        self.acc += glove.acc
        self.accp += glove.accp
        self.evd += glove.evd
        self.evdp += glove.evdp
        self.penrate += glove.penrate
        self.block += glove.block
        self.abnormalstatres += glove.abnormalstatres
        self.ignore += glove.ignore

        # HP MP Stats
        self.hp += glove.hp
        self.mp += glove.mp
        self.hpinc += glove.hpinc
        self.mpinc += glove.mpinc
        self.hprec += glove.hprec
        self.mprec += glove.mprec
        self.hprecp += glove.hprecp
        self.mprecp += glove.mprecp
        self.hppotionrecp += glove.hppotionrecp
        self.mppotionrecp += glove.mppotionrecp
        self.buffdurationinc += glove.buffdurationinc

        # Mobility Stats
        self.spd += glove.spd
        self.jmp += glove.jmp
        self.kbkres += glove.kbkres

        # Misc Stats
        self.exp += glove.exp
        self.dr += glove.dr
        self.meso += glove.meso
        self.glincrease += glove.glincrease
        self.partyexp += glove.partyexp
        self.feverchargeinc += glove.feverchargeinc
        self.feverduration += glove.feverduration
        self.maxfeverchance += glove.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += glove.spmulti

        # Set Stats
        self.mempsetcount += glove.mempsetcount
        self.aempsetcount += glove.aempsetcount
        self.necrosetcount += glove.necrosetcount
        self.fafsetcount += glove.fafsetcount
        self.bosssetcount += glove.bosssetcount
        self.commandersetcount += glove.commandersetcount

        # Flame Stats
        self.atklinecount += glove.atklinecount
        self.crlinecount += glove.crlinecount
        self.cdlinecount += glove.cdlinecount

        # Hat
        self.normal_emb += hat.normal_emb
        self.partial_emb += hat.partial_emb
        self.unique_acc_emb += hat.unique_acc_emb
        self.legendary_acc_emb += hat.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += hat.emblem_cd
        self.emblem_batk += hat.emblem_batk
        self.emblem_atkp += hat.emblem_atkp

        # SF Stats
        self.sf += hat.sf

        # Offensive Stats
        self.atk += hat.atk
        self.atkp += hat.atkp
        self.dmg += hat.dmg
        self.batk += hat.batk
        self.platk += hat.platk
        self.cr += hat.cr
        self.cratk += hat.cratk
        self.cd += hat.cd
        self.maxdmg += hat.maxdmg
        self.fd += hat.fd

        # Defensive Stats
        self.pdef += hat.pdef
        self.pdefinc += hat.pdefinc
        self.pdefdec += hat.pdefdec
        self.mdef += hat.mdef
        self.mdefinc += hat.mdefinc
        self.mdefdec += hat.mdefdec
        self.bdef += hat.bdef
        self.pldef += hat.pldef
        self.critres += hat.critres
        self.critdmgres += hat.critdmgres

        # Hit Miss Stats
        self.acc += hat.acc
        self.accp += hat.accp
        self.evd += hat.evd
        self.evdp += hat.evdp
        self.penrate += hat.penrate
        self.block += hat.block
        self.abnormalstatres += hat.abnormalstatres
        self.ignore += hat.ignore

        # HP MP Stats
        self.hp += hat.hp
        self.mp += hat.mp
        self.hpinc += hat.hpinc
        self.mpinc += hat.mpinc
        self.hprec += hat.hprec
        self.mprec += hat.mprec
        self.hprecp += hat.hprecp
        self.mprecp += hat.mprecp
        self.hppotionrecp += hat.hppotionrecp
        self.mppotionrecp += hat.mppotionrecp
        self.buffdurationinc += hat.buffdurationinc

        # Mobility Stats
        self.spd += hat.spd
        self.jmp += hat.jmp
        self.kbkres += hat.kbkres

        # Misc Stats
        self.exp += hat.exp
        self.dr += hat.dr
        self.meso += hat.meso
        self.glincrease += hat.glincrease
        self.partyexp += hat.partyexp
        self.feverchargeinc += hat.feverchargeinc
        self.feverduration += hat.feverduration
        self.maxfeverchance += hat.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += hat.spmulti

        # Set Stats
        self.mempsetcount += hat.mempsetcount
        self.aempsetcount += hat.aempsetcount
        self.necrosetcount += hat.necrosetcount
        self.fafsetcount += hat.fafsetcount
        self.bosssetcount += hat.bosssetcount
        self.commandersetcount += hat.commandersetcount

        # Flame Stats
        self.atklinecount += hat.atklinecount
        self.crlinecount += hat.crlinecount
        self.cdlinecount += hat.cdlinecount

        # Jewel
        self.normal_emb += jewel.normal_emb
        self.partial_emb += jewel.partial_emb
        self.unique_acc_emb += jewel.unique_acc_emb
        self.legendary_acc_emb += jewel.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += jewel.emblem_cd
        self.emblem_batk += jewel.emblem_batk
        self.emblem_atkp += jewel.emblem_atkp

        # SF Stats
        self.sf += jewel.sf

        # Offensive Stats
        self.atk += jewel.atk
        self.atkp += jewel.atkp
        self.dmg += jewel.dmg
        self.batk += jewel.batk
        self.platk += jewel.platk
        self.cr += jewel.cr
        self.cratk += jewel.cratk
        self.cd += jewel.cd
        self.maxdmg += jewel.maxdmg
        self.fd += jewel.fd

        # Defensive Stats
        self.pdef += jewel.pdef
        self.pdefinc += jewel.pdefinc
        self.pdefdec += jewel.pdefdec
        self.mdef += jewel.mdef
        self.mdefinc += jewel.mdefinc
        self.mdefdec += jewel.mdefdec
        self.bdef += jewel.bdef
        self.pldef += jewel.pldef
        self.critres += jewel.critres
        self.critdmgres += jewel.critdmgres

        # Hit Miss Stats
        self.acc += jewel.acc
        self.accp += jewel.accp
        self.evd += jewel.evd
        self.evdp += jewel.evdp
        self.penrate += jewel.penrate
        self.block += jewel.block
        self.abnormalstatres += jewel.abnormalstatres
        self.ignore += jewel.ignore

        # HP MP Stats
        self.hp += jewel.hp
        self.mp += jewel.mp
        self.hpinc += jewel.hpinc
        self.mpinc += jewel.mpinc
        self.hprec += jewel.hprec
        self.mprec += jewel.mprec
        self.hprecp += jewel.hprecp
        self.mprecp += jewel.mprecp
        self.hppotionrecp += jewel.hppotionrecp
        self.mppotionrecp += jewel.mppotionrecp
        self.buffdurationinc += jewel.buffdurationinc

        # Mobility Stats
        self.spd += jewel.spd
        self.jmp += jewel.jmp
        self.kbkres += jewel.kbkres

        # Misc Stats
        self.exp += jewel.exp
        self.dr += jewel.dr
        self.meso += jewel.meso
        self.glincrease += jewel.glincrease
        self.partyexp += jewel.partyexp
        self.feverchargeinc += jewel.feverchargeinc
        self.feverduration += jewel.feverduration
        self.maxfeverchance += jewel.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += jewel.spmulti

        # Set Stats
        self.mempsetcount += jewel.mempsetcount
        self.aempsetcount += jewel.aempsetcount
        self.necrosetcount += jewel.necrosetcount
        self.fafsetcount += jewel.fafsetcount
        self.bosssetcount += jewel.bosssetcount
        self.commandersetcount += jewel.commandersetcount

        # Flame Stats
        self.atklinecount += jewel.atklinecount
        self.crlinecount += jewel.crlinecount
        self.cdlinecount += jewel.cdlinecount

        # Medal
        self.normal_emb += medal.normal_emb
        self.partial_emb += medal.partial_emb
        self.unique_acc_emb += medal.unique_acc_emb
        self.legendary_acc_emb += medal.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += medal.emblem_cd
        self.emblem_batk += medal.emblem_batk
        self.emblem_atkp += medal.emblem_atkp

        # SF Stats
        self.sf += medal.sf

        # Offensive Stats
        self.atk += medal.atk
        self.atkp += medal.atkp
        self.dmg += medal.dmg
        self.batk += medal.batk
        self.platk += medal.platk
        self.cr += medal.cr
        self.cratk += medal.cratk
        self.cd += medal.cd
        self.maxdmg += medal.maxdmg
        self.fd += medal.fd

        # Defensive Stats
        self.pdef += medal.pdef
        self.pdefinc += medal.pdefinc
        self.pdefdec += medal.pdefdec
        self.mdef += medal.mdef
        self.mdefinc += medal.mdefinc
        self.mdefdec += medal.mdefdec
        self.bdef += medal.bdef
        self.pldef += medal.pldef
        self.critres += medal.critres
        self.critdmgres += medal.critdmgres

        # Hit Miss Stats
        self.acc += medal.acc
        self.accp += medal.accp
        self.evd += medal.evd
        self.evdp += medal.evdp
        self.penrate += medal.penrate
        self.block += medal.block
        self.abnormalstatres += medal.abnormalstatres
        self.ignore += medal.ignore

        # HP MP Stats
        self.hp += medal.hp
        self.mp += medal.mp
        self.hpinc += medal.hpinc
        self.mpinc += medal.mpinc
        self.hprec += medal.hprec
        self.mprec += medal.mprec
        self.hprecp += medal.hprecp
        self.mprecp += medal.mprecp
        self.hppotionrecp += medal.hppotionrecp
        self.mppotionrecp += medal.mppotionrecp
        self.buffdurationinc += medal.buffdurationinc

        # Mobility Stats
        self.spd += medal.spd
        self.jmp += medal.jmp
        self.kbkres += medal.kbkres

        # Misc Stats
        self.exp += medal.exp
        self.dr += medal.dr
        self.meso += medal.meso
        self.glincrease += medal.glincrease
        self.partyexp += medal.partyexp
        self.feverchargeinc += medal.feverchargeinc
        self.feverduration += medal.feverduration
        self.maxfeverchance += medal.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += medal.spmulti

        # Set Stats
        self.mempsetcount += medal.mempsetcount
        self.aempsetcount += medal.aempsetcount
        self.necrosetcount += medal.necrosetcount
        self.fafsetcount += medal.fafsetcount
        self.bosssetcount += medal.bosssetcount
        self.commandersetcount += medal.commandersetcount

        # Flame Stats
        self.atklinecount += medal.atklinecount
        self.crlinecount += medal.crlinecount
        self.cdlinecount += medal.cdlinecount

        # Necklace
        self.normal_emb += necklace.normal_emb
        self.partial_emb += necklace.partial_emb
        self.unique_acc_emb += necklace.unique_acc_emb
        self.legendary_acc_emb += necklace.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += necklace.emblem_cd
        self.emblem_batk += necklace.emblem_batk
        self.emblem_atkp += necklace.emblem_atkp

        # SF Stats
        self.sf += necklace.sf

        # Offensive Stats
        self.atk += necklace.atk
        self.atkp += necklace.atkp
        self.dmg += necklace.dmg
        self.batk += necklace.batk
        self.platk += necklace.platk
        self.cr += necklace.cr
        self.cratk += necklace.cratk
        self.cd += necklace.cd
        self.maxdmg += necklace.maxdmg
        self.fd += necklace.fd

        # Defensive Stats
        self.pdef += necklace.pdef
        self.pdefinc += necklace.pdefinc
        self.pdefdec += necklace.pdefdec
        self.mdef += necklace.mdef
        self.mdefinc += necklace.mdefinc
        self.mdefdec += necklace.mdefdec
        self.bdef += necklace.bdef
        self.pldef += necklace.pldef
        self.critres += necklace.critres
        self.critdmgres += necklace.critdmgres

        # Hit Miss Stats
        self.acc += necklace.acc
        self.accp += necklace.accp
        self.evd += necklace.evd
        self.evdp += necklace.evdp
        self.penrate += necklace.penrate
        self.block += necklace.block
        self.abnormalstatres += necklace.abnormalstatres
        self.ignore += necklace.ignore

        # HP MP Stats
        self.hp += necklace.hp
        self.mp += necklace.mp
        self.hpinc += necklace.hpinc
        self.mpinc += necklace.mpinc
        self.hprec += necklace.hprec
        self.mprec += necklace.mprec
        self.hprecp += necklace.hprecp
        self.mprecp += necklace.mprecp
        self.hppotionrecp += necklace.hppotionrecp
        self.mppotionrecp += necklace.mppotionrecp
        self.buffdurationinc += necklace.buffdurationinc

        # Mobility Stats
        self.spd += necklace.spd
        self.jmp += necklace.jmp
        self.kbkres += necklace.kbkres

        # Misc Stats
        self.exp += necklace.exp
        self.dr += necklace.dr
        self.meso += necklace.meso
        self.glincrease += necklace.glincrease
        self.partyexp += necklace.partyexp
        self.feverchargeinc += necklace.feverchargeinc
        self.feverduration += necklace.feverduration
        self.maxfeverchance += necklace.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += necklace.spmulti

        # Set Stats
        self.mempsetcount += necklace.mempsetcount
        self.aempsetcount += necklace.aempsetcount
        self.necrosetcount += necklace.necrosetcount
        self.fafsetcount += necklace.fafsetcount
        self.bosssetcount += necklace.bosssetcount
        self.commandersetcount += necklace.commandersetcount

        # Flame Stats
        self.atklinecount += necklace.atklinecount
        self.crlinecount += necklace.crlinecount
        self.cdlinecount += necklace.cdlinecount

        # Pet
        self.normal_emb += pet.normal_emb
        self.partial_emb += pet.partial_emb
        self.unique_acc_emb += pet.unique_acc_emb
        self.legendary_acc_emb += pet.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += pet.emblem_cd
        self.emblem_batk += pet.emblem_batk
        self.emblem_atkp += pet.emblem_atkp

        # SF Stats
        self.sf += pet.sf

        # Offensive Stats
        self.atk += pet.atk
        self.atkp += pet.atkp
        self.dmg += pet.dmg
        self.batk += pet.batk
        self.platk += pet.platk
        self.cr += pet.cr
        self.cratk += pet.cratk
        self.cd += pet.cd
        self.maxdmg += pet.maxdmg
        self.fd += pet.fd

        # Defensive Stats
        self.pdef += pet.pdef
        self.pdefinc += pet.pdefinc
        self.pdefdec += pet.pdefdec
        self.mdef += pet.mdef
        self.mdefinc += pet.mdefinc
        self.mdefdec += pet.mdefdec
        self.bdef += pet.bdef
        self.pldef += pet.pldef
        self.critres += pet.critres
        self.critdmgres += pet.critdmgres

        # Hit Miss Stats
        self.acc += pet.acc
        self.accp += pet.accp
        self.evd += pet.evd
        self.evdp += pet.evdp
        self.penrate += pet.penrate
        self.block += pet.block
        self.abnormalstatres += pet.abnormalstatres
        self.ignore += pet.ignore

        # HP MP Stats
        self.hp += pet.hp
        self.mp += pet.mp
        self.hpinc += pet.hpinc
        self.mpinc += pet.mpinc
        self.hprec += pet.hprec
        self.mprec += pet.mprec
        self.hprecp += pet.hprecp
        self.mprecp += pet.mprecp
        self.hppotionrecp += pet.hppotionrecp
        self.mppotionrecp += pet.mppotionrecp
        self.buffdurationinc += pet.buffdurationinc

        # Mobility Stats
        self.spd += pet.spd
        self.jmp += pet.jmp
        self.kbkres += pet.kbkres

        # Misc Stats
        self.exp += pet.exp
        self.dr += pet.dr
        self.meso += pet.meso
        self.glincrease += pet.glincrease
        self.partyexp += pet.partyexp
        self.feverchargeinc += pet.feverchargeinc
        self.feverduration += pet.feverduration
        self.maxfeverchance += pet.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += pet.spmulti

        # Set Stats
        self.mempsetcount += pet.mempsetcount
        self.aempsetcount += pet.aempsetcount
        self.necrosetcount += pet.necrosetcount
        self.fafsetcount += pet.fafsetcount
        self.bosssetcount += pet.bosssetcount
        self.commandersetcount += pet.commandersetcount

        # Flame Stats
        self.atklinecount += pet.atklinecount
        self.crlinecount += pet.crlinecount
        self.cdlinecount += pet.cdlinecount

        # Ring
        self.normal_emb += ring.normal_emb
        self.partial_emb += ring.partial_emb
        self.unique_acc_emb += ring.unique_acc_emb
        self.legendary_acc_emb += ring.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += ring.emblem_cd
        self.emblem_batk += ring.emblem_batk
        self.emblem_atkp += ring.emblem_atkp

        # SF Stats
        self.sf += ring.sf

        # Offensive Stats
        self.atk += ring.atk
        self.atkp += ring.atkp
        self.dmg += ring.dmg
        self.batk += ring.batk
        self.platk += ring.platk
        self.cr += ring.cr
        self.cratk += ring.cratk
        self.cd += ring.cd
        self.maxdmg += ring.maxdmg
        self.fd += ring.fd

        # Defensive Stats
        self.pdef += ring.pdef
        self.pdefinc += ring.pdefinc
        self.pdefdec += ring.pdefdec
        self.mdef += ring.mdef
        self.mdefinc += ring.mdefinc
        self.mdefdec += ring.mdefdec
        self.bdef += ring.bdef
        self.pldef += ring.pldef
        self.critres += ring.critres
        self.critdmgres += ring.critdmgres

        # Hit Miss Stats
        self.acc += ring.acc
        self.accp += ring.accp
        self.evd += ring.evd
        self.evdp += ring.evdp
        self.penrate += ring.penrate
        self.block += ring.block
        self.abnormalstatres += ring.abnormalstatres
        self.ignore += ring.ignore

        # HP MP Stats
        self.hp += ring.hp
        self.mp += ring.mp
        self.hpinc += ring.hpinc
        self.mpinc += ring.mpinc
        self.hprec += ring.hprec
        self.mprec += ring.mprec
        self.hprecp += ring.hprecp
        self.mprecp += ring.mprecp
        self.hppotionrecp += ring.hppotionrecp
        self.mppotionrecp += ring.mppotionrecp
        self.buffdurationinc += ring.buffdurationinc

        # Mobility Stats
        self.spd += ring.spd
        self.jmp += ring.jmp
        self.kbkres += ring.kbkres

        # Misc Stats
        self.exp += ring.exp
        self.dr += ring.dr
        self.meso += ring.meso
        self.glincrease += ring.glincrease
        self.partyexp += ring.partyexp
        self.feverchargeinc += ring.feverchargeinc
        self.feverduration += ring.feverduration
        self.maxfeverchance += ring.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += ring.spmulti

        # Set Stats
        self.mempsetcount += ring.mempsetcount
        self.aempsetcount += ring.aempsetcount
        self.necrosetcount += ring.necrosetcount
        self.fafsetcount += ring.fafsetcount
        self.bosssetcount += ring.bosssetcount
        self.commandersetcount += ring.commandersetcount

        # Flame Stats
        self.atklinecount += ring.atklinecount
        self.crlinecount += ring.crlinecount
        self.cdlinecount += ring.cdlinecount

        # Swep
        self.normal_emb += swep.normal_emb
        self.partial_emb += swep.partial_emb
        self.unique_acc_emb += swep.unique_acc_emb
        self.legendary_acc_emb += swep.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += swep.emblem_cd
        self.emblem_batk += swep.emblem_batk
        self.emblem_atkp += swep.emblem_atkp

        # SF Stats
        self.sf += swep.sf

        # Offensive Stats
        self.atk += swep.atk
        self.atkp += swep.atkp
        self.dmg += swep.dmg
        self.batk += swep.batk
        self.platk += swep.platk
        self.cr += swep.cr
        self.cratk += swep.cratk
        self.cd += swep.cd
        self.maxdmg += swep.maxdmg
        self.fd += swep.fd

        # Defensive Stats
        self.pdef += swep.pdef
        self.pdefinc += swep.pdefinc
        self.pdefdec += swep.pdefdec
        self.mdef += swep.mdef
        self.mdefinc += swep.mdefinc
        self.mdefdec += swep.mdefdec
        self.bdef += swep.bdef
        self.pldef += swep.pldef
        self.critres += swep.critres
        self.critdmgres += swep.critdmgres

        # Hit Miss Stats
        self.acc += swep.acc
        self.accp += swep.accp
        self.evd += swep.evd
        self.evdp += swep.evdp
        self.penrate += swep.penrate
        self.block += swep.block
        self.abnormalstatres += swep.abnormalstatres
        self.ignore += swep.ignore

        # HP MP Stats
        self.hp += swep.hp
        self.mp += swep.mp
        self.hpinc += swep.hpinc
        self.mpinc += swep.mpinc
        self.hprec += swep.hprec
        self.mprec += swep.mprec
        self.hprecp += swep.hprecp
        self.mprecp += swep.mprecp
        self.hppotionrecp += swep.hppotionrecp
        self.mppotionrecp += swep.mppotionrecp
        self.buffdurationinc += swep.buffdurationinc

        # Mobility Stats
        self.spd += swep.spd
        self.jmp += swep.jmp
        self.kbkres += swep.kbkres

        # Misc Stats
        self.exp += swep.exp
        self.dr += swep.dr
        self.meso += swep.meso
        self.glincrease += swep.glincrease
        self.partyexp += swep.partyexp
        self.feverchargeinc += swep.feverchargeinc
        self.feverduration += swep.feverduration
        self.maxfeverchance += swep.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += swep.spmulti

        # Set Stats
        self.mempsetcount += swep.mempsetcount
        self.aempsetcount += swep.aempsetcount
        self.necrosetcount += swep.necrosetcount
        self.fafsetcount += swep.fafsetcount
        self.bosssetcount += swep.bosssetcount
        self.commandersetcount += swep.commandersetcount

        # Flame Stats
        self.atklinecount += swep.atklinecount
        self.crlinecount += swep.crlinecount
        self.cdlinecount += swep.cdlinecount

        # Set Effect
        self.normal_emb += seteffect.normal_emb
        self.partial_emb += seteffect.partial_emb
        self.unique_acc_emb += seteffect.unique_acc_emb
        self.legendary_acc_emb += seteffect.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += seteffect.emblem_cd
        self.emblem_batk += seteffect.emblem_batk
        self.emblem_atkp += seteffect.emblem_atkp

        # SF Stats
        self.sf += seteffect.sf

        # Offensive Stats
        self.atk += seteffect.atk
        self.atkp += seteffect.atkp
        self.dmg += seteffect.dmg
        self.batk += seteffect.batk
        self.platk += seteffect.platk
        self.cr += seteffect.cr
        self.cratk += seteffect.cratk
        self.cd += seteffect.cd
        self.maxdmg += seteffect.maxdmg
        self.fd += seteffect.fd

        # Defensive Stats
        self.pdef += seteffect.pdef
        self.pdefinc += seteffect.pdefinc
        self.pdefdec += seteffect.pdefdec
        self.mdef += seteffect.mdef
        self.mdefinc += seteffect.mdefinc
        self.mdefdec += seteffect.mdefdec
        self.bdef += seteffect.bdef
        self.pldef += seteffect.pldef
        self.critres += seteffect.critres
        self.critdmgres += seteffect.critdmgres

        # Hit Miss Stats
        self.acc += seteffect.acc
        self.accp += seteffect.accp
        self.evd += seteffect.evd
        self.evdp += seteffect.evdp
        self.penrate += seteffect.penrate
        self.block += seteffect.block
        self.abnormalstatres += seteffect.abnormalstatres
        self.ignore += seteffect.ignore

        # HP MP Stats
        self.hp += seteffect.hp
        self.mp += seteffect.mp
        self.hpinc += seteffect.hpinc
        self.mpinc += seteffect.mpinc
        self.hprec += seteffect.hprec
        self.mprec += seteffect.mprec
        self.hprecp += seteffect.hprecp
        self.mprecp += seteffect.mprecp
        self.hppotionrecp += seteffect.hppotionrecp
        self.mppotionrecp += seteffect.mppotionrecp
        self.buffdurationinc += seteffect.buffdurationinc

        # Mobility Stats
        self.spd += seteffect.spd
        self.jmp += seteffect.jmp
        self.kbkres += seteffect.kbkres

        # Misc Stats
        self.exp += seteffect.exp
        self.dr += seteffect.dr
        self.meso += seteffect.meso
        self.glincrease += seteffect.glincrease
        self.partyexp += seteffect.partyexp
        self.feverchargeinc += seteffect.feverchargeinc
        self.feverduration += seteffect.feverduration
        self.maxfeverchance += seteffect.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += seteffect.spmulti

        # Set Stats
        self.mempsetcount += seteffect.mempsetcount
        self.aempsetcount += seteffect.aempsetcount
        self.necrosetcount += seteffect.necrosetcount
        self.fafsetcount += seteffect.fafsetcount
        self.bosssetcount += seteffect.bosssetcount
        self.commandersetcount += seteffect.commandersetcount

        # Flame Stats
        self.atklinecount += seteffect.atklinecount
        self.crlinecount += seteffect.crlinecount
        self.cdlinecount += seteffect.cdlinecount

        # Shoe
        self.normal_emb += shoe.normal_emb
        self.partial_emb += shoe.partial_emb
        self.unique_acc_emb += shoe.unique_acc_emb
        self.legendary_acc_emb += shoe.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += shoe.emblem_cd
        self.emblem_batk += shoe.emblem_batk
        self.emblem_atkp += shoe.emblem_atkp

        # SF Stats
        self.sf += shoe.sf

        # Offensive Stats
        self.atk += shoe.atk
        self.atkp += shoe.atkp
        self.dmg += shoe.dmg
        self.batk += shoe.batk
        self.platk += shoe.platk
        self.cr += shoe.cr
        self.cratk += shoe.cratk
        self.cd += shoe.cd
        self.maxdmg += shoe.maxdmg
        self.fd += shoe.fd

        # Defensive Stats
        self.pdef += shoe.pdef
        self.pdefinc += shoe.pdefinc
        self.pdefdec += shoe.pdefdec
        self.mdef += shoe.mdef
        self.mdefinc += shoe.mdefinc
        self.mdefdec += shoe.mdefdec
        self.bdef += shoe.bdef
        self.pldef += shoe.pldef
        self.critres += shoe.critres
        self.critdmgres += shoe.critdmgres

        # Hit Miss Stats
        self.acc += shoe.acc
        self.accp += shoe.accp
        self.evd += shoe.evd
        self.evdp += shoe.evdp
        self.penrate += shoe.penrate
        self.block += shoe.block
        self.abnormalstatres += shoe.abnormalstatres
        self.ignore += shoe.ignore

        # HP MP Stats
        self.hp += shoe.hp
        self.mp += shoe.mp
        self.hpinc += shoe.hpinc
        self.mpinc += shoe.mpinc
        self.hprec += shoe.hprec
        self.mprec += shoe.mprec
        self.hprecp += shoe.hprecp
        self.mprecp += shoe.mprecp
        self.hppotionrecp += shoe.hppotionrecp
        self.mppotionrecp += shoe.mppotionrecp
        self.buffdurationinc += shoe.buffdurationinc

        # Mobility Stats
        self.spd += shoe.spd
        self.jmp += shoe.jmp
        self.kbkres += shoe.kbkres

        # Misc Stats
        self.exp += shoe.exp
        self.dr += shoe.dr
        self.meso += shoe.meso
        self.glincrease += shoe.glincrease
        self.partyexp += shoe.partyexp
        self.feverchargeinc += shoe.feverchargeinc
        self.feverduration += shoe.feverduration
        self.maxfeverchance += shoe.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += shoe.spmulti

        # Set Stats
        self.mempsetcount += shoe.mempsetcount
        self.aempsetcount += shoe.aempsetcount
        self.necrosetcount += shoe.necrosetcount
        self.fafsetcount += shoe.fafsetcount
        self.bosssetcount += shoe.bosssetcount
        self.commandersetcount += shoe.commandersetcount

        # Flame Stats
        self.atklinecount += shoe.atklinecount
        self.crlinecount += shoe.crlinecount
        self.cdlinecount += shoe.cdlinecount

        # Shoulder
        self.normal_emb += shoulder.normal_emb
        self.partial_emb += shoulder.partial_emb
        self.unique_acc_emb += shoulder.unique_acc_emb
        self.legendary_acc_emb += shoulder.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += shoulder.emblem_cd
        self.emblem_batk += shoulder.emblem_batk
        self.emblem_atkp += shoulder.emblem_atkp

        # SF Stats
        self.sf += shoulder.sf

        # Offensive Stats
        self.atk += shoulder.atk
        self.atkp += shoulder.atkp
        self.dmg += shoulder.dmg
        self.batk += shoulder.batk
        self.platk += shoulder.platk
        self.cr += shoulder.cr
        self.cratk += shoulder.cratk
        self.cd += shoulder.cd
        self.maxdmg += shoulder.maxdmg
        self.fd += shoulder.fd

        # Defensive Stats
        self.pdef += shoulder.pdef
        self.pdefinc += shoulder.pdefinc
        self.pdefdec += shoulder.pdefdec
        self.mdef += shoulder.mdef
        self.mdefinc += shoulder.mdefinc
        self.mdefdec += shoulder.mdefdec
        self.bdef += shoulder.bdef
        self.pldef += shoulder.pldef
        self.critres += shoulder.critres
        self.critdmgres += shoulder.critdmgres

        # Hit Miss Stats
        self.acc += shoulder.acc
        self.accp += shoulder.accp
        self.evd += shoulder.evd
        self.evdp += shoulder.evdp
        self.penrate += shoulder.penrate
        self.block += shoulder.block
        self.abnormalstatres += shoulder.abnormalstatres
        self.ignore += shoulder.ignore

        # HP MP Stats
        self.hp += shoulder.hp
        self.mp += shoulder.mp
        self.hpinc += shoulder.hpinc
        self.mpinc += shoulder.mpinc
        self.hprec += shoulder.hprec
        self.mprec += shoulder.mprec
        self.hprecp += shoulder.hprecp
        self.mprecp += shoulder.mprecp
        self.hppotionrecp += shoulder.hppotionrecp
        self.mppotionrecp += shoulder.mppotionrecp
        self.buffdurationinc += shoulder.buffdurationinc

        # Mobility Stats
        self.spd += shoulder.spd
        self.jmp += shoulder.jmp
        self.kbkres += shoulder.kbkres

        # Misc Stats
        self.exp += shoulder.exp
        self.dr += shoulder.dr
        self.meso += shoulder.meso
        self.glincrease += shoulder.glincrease
        self.partyexp += shoulder.partyexp
        self.feverchargeinc += shoulder.feverchargeinc
        self.feverduration += shoulder.feverduration
        self.maxfeverchance += shoulder.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += shoulder.spmulti

        # Set Stats
        self.mempsetcount += shoulder.mempsetcount
        self.aempsetcount += shoulder.aempsetcount
        self.necrosetcount += shoulder.necrosetcount
        self.fafsetcount += shoulder.fafsetcount
        self.bosssetcount += shoulder.bosssetcount
        self.commandersetcount += shoulder.commandersetcount

        # Flame Stats
        self.atklinecount += shoulder.atklinecount
        self.crlinecount += shoulder.crlinecount
        self.cdlinecount += shoulder.cdlinecount

        # Soul
        self.normal_emb += soul.normal_emb
        self.partial_emb += soul.partial_emb
        self.unique_acc_emb += soul.unique_acc_emb
        self.legendary_acc_emb += soul.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += soul.emblem_cd
        self.emblem_batk += soul.emblem_batk
        self.emblem_atkp += soul.emblem_atkp

        # SF Stats
        self.sf += soul.sf

        # Offensive Stats
        self.atk += soul.atk
        self.atkp += soul.atkp
        self.dmg += soul.dmg
        self.batk += soul.batk
        self.platk += soul.platk
        self.cr += soul.cr
        self.cratk += soul.cratk
        self.cd += soul.cd
        self.maxdmg += soul.maxdmg
        self.fd += soul.fd

        # Defensive Stats
        self.pdef += soul.pdef
        self.pdefinc += soul.pdefinc
        self.pdefdec += soul.pdefdec
        self.mdef += soul.mdef
        self.mdefinc += soul.mdefinc
        self.mdefdec += soul.mdefdec
        self.bdef += soul.bdef
        self.pldef += soul.pldef
        self.critres += soul.critres
        self.critdmgres += soul.critdmgres

        # Hit Miss Stats
        self.acc += soul.acc
        self.accp += soul.accp
        self.evd += soul.evd
        self.evdp += soul.evdp
        self.penrate += soul.penrate
        self.block += soul.block
        self.abnormalstatres += soul.abnormalstatres
        self.ignore += soul.ignore

        # HP MP Stats
        self.hp += soul.hp
        self.mp += soul.mp
        self.hpinc += soul.hpinc
        self.mpinc += soul.mpinc
        self.hprec += soul.hprec
        self.mprec += soul.mprec
        self.hprecp += soul.hprecp
        self.mprecp += soul.mprecp
        self.hppotionrecp += soul.hppotionrecp
        self.mppotionrecp += soul.mppotionrecp
        self.buffdurationinc += soul.buffdurationinc

        # Mobility Stats
        self.spd += soul.spd
        self.jmp += soul.jmp
        self.kbkres += soul.kbkres

        # Misc Stats
        self.exp += soul.exp
        self.dr += soul.dr
        self.meso += soul.meso
        self.glincrease += soul.glincrease
        self.partyexp += soul.partyexp
        self.feverchargeinc += soul.feverchargeinc
        self.feverduration += soul.feverduration
        self.maxfeverchance += soul.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += soul.spmulti

        # Set Stats
        self.mempsetcount += soul.mempsetcount
        self.aempsetcount += soul.aempsetcount
        self.necrosetcount += soul.necrosetcount
        self.fafsetcount += soul.fafsetcount
        self.bosssetcount += soul.bosssetcount
        self.commandersetcount += soul.commandersetcount

        # Flame Stats
        self.atklinecount += soul.atklinecount
        self.crlinecount += soul.crlinecount
        self.cdlinecount += soul.cdlinecount

        # TBO
        self.normal_emb += tbo.normal_emb
        self.partial_emb += tbo.partial_emb
        self.unique_acc_emb += tbo.unique_acc_emb
        self.legendary_acc_emb += tbo.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += tbo.emblem_cd
        self.emblem_batk += tbo.emblem_batk
        self.emblem_atkp += tbo.emblem_atkp

        # SF Stats
        self.sf += tbo.sf

        # Offensive Stats
        self.atk += tbo.atk
        self.atkp += tbo.atkp
        self.dmg += tbo.dmg
        self.batk += tbo.batk
        self.platk += tbo.platk
        self.cr += tbo.cr
        self.cratk += tbo.cratk
        self.cd += tbo.cd
        self.maxdmg += tbo.maxdmg
        self.fd += tbo.fd

        # Defensive Stats
        self.pdef += tbo.pdef
        self.pdefinc += tbo.pdefinc
        self.pdefdec += tbo.pdefdec
        self.mdef += tbo.mdef
        self.mdefinc += tbo.mdefinc
        self.mdefdec += tbo.mdefdec
        self.bdef += tbo.bdef
        self.pldef += tbo.pldef
        self.critres += tbo.critres
        self.critdmgres += tbo.critdmgres

        # Hit Miss Stats
        self.acc += tbo.acc
        self.accp += tbo.accp
        self.evd += tbo.evd
        self.evdp += tbo.evdp
        self.penrate += tbo.penrate
        self.block += tbo.block
        self.abnormalstatres += tbo.abnormalstatres
        self.ignore += tbo.ignore

        # HP MP Stats
        self.hp += tbo.hp
        self.mp += tbo.mp
        self.hpinc += tbo.hpinc
        self.mpinc += tbo.mpinc
        self.hprec += tbo.hprec
        self.mprec += tbo.mprec
        self.hprecp += tbo.hprecp
        self.mprecp += tbo.mprecp
        self.hppotionrecp += tbo.hppotionrecp
        self.mppotionrecp += tbo.mppotionrecp
        self.buffdurationinc += tbo.buffdurationinc

        # Mobility Stats
        self.spd += tbo.spd
        self.jmp += tbo.jmp
        self.kbkres += tbo.kbkres

        # Misc Stats
        self.exp += tbo.exp
        self.dr += tbo.dr
        self.meso += tbo.meso
        self.glincrease += tbo.glincrease
        self.partyexp += tbo.partyexp
        self.feverchargeinc += tbo.feverchargeinc
        self.feverduration += tbo.feverduration
        self.maxfeverchance += tbo.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += tbo.spmulti

        # Set Stats
        self.mempsetcount += tbo.mempsetcount
        self.aempsetcount += tbo.aempsetcount
        self.necrosetcount += tbo.necrosetcount
        self.fafsetcount += tbo.fafsetcount
        self.bosssetcount += tbo.bosssetcount
        self.commandersetcount += tbo.commandersetcount

        # Flame Stats
        self.atklinecount += tbo.atklinecount
        self.crlinecount += tbo.crlinecount
        self.cdlinecount += tbo.cdlinecount

        # Title
        self.normal_emb += title.normal_emb
        self.partial_emb += title.partial_emb
        self.unique_acc_emb += title.unique_acc_emb
        self.legendary_acc_emb += title.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += title.emblem_cd
        self.emblem_batk += title.emblem_batk
        self.emblem_atkp += title.emblem_atkp

        # SF Stats
        self.sf += title.sf

        # Offensive Stats
        self.atk += title.atk
        self.atkp += title.atkp
        self.dmg += title.dmg
        self.batk += title.batk
        self.platk += title.platk
        self.cr += title.cr
        self.cratk += title.cratk
        self.cd += title.cd
        self.maxdmg += title.maxdmg
        self.fd += title.fd

        # Defensive Stats
        self.pdef += title.pdef
        self.pdefinc += title.pdefinc
        self.pdefdec += title.pdefdec
        self.mdef += title.mdef
        self.mdefinc += title.mdefinc
        self.mdefdec += title.mdefdec
        self.bdef += title.bdef
        self.pldef += title.pldef
        self.critres += title.critres
        self.critdmgres += title.critdmgres

        # Hit Miss Stats
        self.acc += title.acc
        self.accp += title.accp
        self.evd += title.evd
        self.evdp += title.evdp
        self.penrate += title.penrate
        self.block += title.block
        self.abnormalstatres += title.abnormalstatres
        self.ignore += title.ignore

        # HP MP Stats
        self.hp += title.hp
        self.mp += title.mp
        self.hpinc += title.hpinc
        self.mpinc += title.mpinc
        self.hprec += title.hprec
        self.mprec += title.mprec
        self.hprecp += title.hprecp
        self.mprecp += title.mprecp
        self.hppotionrecp += title.hppotionrecp
        self.mppotionrecp += title.mppotionrecp
        self.buffdurationinc += title.buffdurationinc

        # Mobility Stats
        self.spd += title.spd
        self.jmp += title.jmp
        self.kbkres += title.kbkres

        # Misc Stats
        self.exp += title.exp
        self.dr += title.dr
        self.meso += title.meso
        self.glincrease += title.glincrease
        self.partyexp += title.partyexp
        self.feverchargeinc += title.feverchargeinc
        self.feverduration += title.feverduration
        self.maxfeverchance += title.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += title.spmulti

        # Set Stats
        self.mempsetcount += title.mempsetcount
        self.aempsetcount += title.aempsetcount
        self.necrosetcount += title.necrosetcount
        self.fafsetcount += title.fafsetcount
        self.bosssetcount += title.bosssetcount
        self.commandersetcount += title.commandersetcount

        # Flame Stats
        self.atklinecount += title.atklinecount
        self.crlinecount += title.crlinecount
        self.cdlinecount += title.cdlinecount

        # Weapon
        self.normal_emb += weapon.normal_emb
        self.partial_emb += weapon.partial_emb
        self.unique_acc_emb += weapon.unique_acc_emb
        self.legendary_acc_emb += weapon.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += weapon.emblem_cd
        self.emblem_batk += weapon.emblem_batk
        self.emblem_atkp += weapon.emblem_atkp

        # SF Stats
        self.sf += weapon.sf

        # Offensive Stats
        self.atk += weapon.atk
        self.atkp += weapon.atkp
        self.dmg += weapon.dmg
        self.batk += weapon.batk
        self.platk += weapon.platk
        self.cr += weapon.cr
        self.cratk += weapon.cratk
        self.cd += weapon.cd
        self.maxdmg += weapon.maxdmg
        self.fd += weapon.fd

        # Defensive Stats
        self.pdef += weapon.pdef
        self.pdefinc += weapon.pdefinc
        self.pdefdec += weapon.pdefdec
        self.mdef += weapon.mdef
        self.mdefinc += weapon.mdefinc
        self.mdefdec += weapon.mdefdec
        self.bdef += weapon.bdef
        self.pldef += weapon.pldef
        self.critres += weapon.critres
        self.critdmgres += weapon.critdmgres

        # Hit Miss Stats
        self.acc += weapon.acc
        self.accp += weapon.accp
        self.evd += weapon.evd
        self.evdp += weapon.evdp
        self.penrate += weapon.penrate
        self.block += weapon.block
        self.abnormalstatres += weapon.abnormalstatres
        self.ignore += weapon.ignore

        # HP MP Stats
        self.hp += weapon.hp
        self.mp += weapon.mp
        self.hpinc += weapon.hpinc
        self.mpinc += weapon.mpinc
        self.hprec += weapon.hprec
        self.mprec += weapon.mprec
        self.hprecp += weapon.hprecp
        self.mprecp += weapon.mprecp
        self.hppotionrecp += weapon.hppotionrecp
        self.mppotionrecp += weapon.mppotionrecp
        self.buffdurationinc += weapon.buffdurationinc

        # Mobility Stats
        self.spd += weapon.spd
        self.jmp += weapon.jmp
        self.kbkres += weapon.kbkres

        # Misc Stats
        self.exp += weapon.exp
        self.dr += weapon.dr
        self.meso += weapon.meso
        self.glincrease += weapon.glincrease
        self.partyexp += weapon.partyexp
        self.feverchargeinc += weapon.feverchargeinc
        self.feverduration += weapon.feverduration
        self.maxfeverchance += weapon.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += weapon.spmulti

        # Set Stats
        self.mempsetcount += weapon.mempsetcount
        self.aempsetcount += weapon.aempsetcount
        self.necrosetcount += weapon.necrosetcount
        self.fafsetcount += weapon.fafsetcount
        self.bosssetcount += weapon.bosssetcount
        self.commandersetcount += weapon.commandersetcount

        # Flame Stats
        self.atklinecount += weapon.atklinecount
        self.crlinecount += weapon.crlinecount
        self.cdlinecount += weapon.cdlinecount

