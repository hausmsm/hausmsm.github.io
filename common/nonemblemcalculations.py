class Nonemblemcalculations:
    def __init__(self, buffs, flamestats, flame, petstats, starforce, hyperstats, links, mapletree, char):
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

# Buffs
        self.normal_emb += buffs.normal_emb
        self.partial_emb += buffs.partial_emb
        self.unique_acc_emb += buffs.unique_acc_emb
        self.legendary_acc_emb += buffs.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += buffs.emblem_cd
        self.emblem_batk += buffs.emblem_batk
        self.emblem_atkp += buffs.emblem_atkp

        # SF Stats
        self.sf += buffs.sf

        # Offensive Stats
        self.atk += buffs.atk
        self.atkp += buffs.atkp
        self.dmg += buffs.dmg
        self.batk += buffs.batk
        self.platk += buffs.platk
        self.cr += buffs.cr
        self.cratk += buffs.cratk
        self.cd += buffs.cd
        self.maxdmg += buffs.maxdmg
        self.fd += buffs.fd

        # Defensive Stats
        self.pdef += buffs.pdef
        self.pdefinc += buffs.pdefinc
        self.pdefdec += buffs.pdefdec
        self.mdef += buffs.mdef
        self.mdefinc += buffs.mdefinc
        self.mdefdec += buffs.mdefdec
        self.bdef += buffs.bdef
        self.pldef += buffs.pldef
        self.critres += buffs.critres
        self.critdmgres += buffs.critdmgres

        # Hit Miss Stats
        self.acc += buffs.acc
        self.accp += buffs.accp
        self.evd += buffs.evd
        self.evdp += buffs.evdp
        self.penrate += buffs.penrate
        self.block += buffs.block
        self.abnormalstatres += buffs.abnormalstatres
        self.ignore += buffs.ignore

        # HP MP Stats
        self.hp += buffs.hp
        self.mp += buffs.mp
        self.hpinc += buffs.hpinc
        self.mpinc += buffs.mpinc
        self.hprec += buffs.hprec
        self.mprec += buffs.mprec
        self.hprecp += buffs.hprecp
        self.mprecp += buffs.mprecp
        self.hppotionrecp += buffs.hppotionrecp
        self.mppotionrecp += buffs.mppotionrecp
        self.buffdurationinc += buffs.buffdurationinc

        # Mobility Stats
        self.spd += buffs.spd
        self.jmp += buffs.jmp
        self.kbkres += buffs.kbkres

        # Misc Stats
        self.exp += buffs.exp
        self.dr += buffs.dr
        self.meso += buffs.meso
        self.glincrease += buffs.glincrease
        self.partyexp += buffs.partyexp
        self.feverchargeinc += buffs.feverchargeinc
        self.feverduration += buffs.feverduration
        self.maxfeverchance += buffs.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += buffs.spmulti

        # Set Stats
        self.mempsetcount += buffs.mempsetcount
        self.aempsetcount += buffs.aempsetcount
        self.necrosetcount += buffs.necrosetcount
        self.fafsetcount += buffs.fafsetcount
        self.bosssetcount += buffs.bosssetcount
        self.commandersetcount += buffs.commandersetcount

        # Flame Stats
        self.atklinecount += buffs.atklinecount
        self.crlinecount += buffs.crlinecount
        self.cdlinecount += buffs.cdlinecount

# Flame Stats
        self.normal_emb += flamestats.normal_emb
        self.partial_emb += flamestats.partial_emb
        self.unique_acc_emb += flamestats.unique_acc_emb
        self.legendary_acc_emb += flamestats.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += flamestats.emblem_cd
        self.emblem_batk += flamestats.emblem_batk
        self.emblem_atkp += flamestats.emblem_atkp

        # SF Stats
        self.sf += flamestats.sf

        # Offensive Stats
        self.atk += flamestats.atk
        self.atkp += flamestats.atkp
        self.dmg += flamestats.dmg
        self.batk += flamestats.batk
        self.platk += flamestats.platk
        self.cr += flamestats.cr
        self.cratk += flamestats.cratk
        self.cd += flamestats.cd
        self.maxdmg += flamestats.maxdmg
        self.fd += flamestats.fd

        # Defensive Stats
        self.pdef += flamestats.pdef
        self.pdefinc += flamestats.pdefinc
        self.pdefdec += flamestats.pdefdec
        self.mdef += flamestats.mdef
        self.mdefinc += flamestats.mdefinc
        self.mdefdec += flamestats.mdefdec
        self.bdef += flamestats.bdef
        self.pldef += flamestats.pldef
        self.critres += flamestats.critres
        self.critdmgres += flamestats.critdmgres

        # Hit Miss Stats
        self.acc += flamestats.acc
        self.accp += flamestats.accp
        self.evd += flamestats.evd
        self.evdp += flamestats.evdp
        self.penrate += flamestats.penrate
        self.block += flamestats.block
        self.abnormalstatres += flamestats.abnormalstatres
        self.ignore += flamestats.ignore

        # HP MP Stats
        self.hp += flamestats.hp
        self.mp += flamestats.mp
        self.hpinc += flamestats.hpinc
        self.mpinc += flamestats.mpinc
        self.hprec += flamestats.hprec
        self.mprec += flamestats.mprec
        self.hprecp += flamestats.hprecp
        self.mprecp += flamestats.mprecp
        self.hppotionrecp += flamestats.hppotionrecp
        self.mppotionrecp += flamestats.mppotionrecp
        self.buffdurationinc += flamestats.buffdurationinc

        # Mobility Stats
        self.spd += flamestats.spd
        self.jmp += flamestats.jmp
        self.kbkres += flamestats.kbkres

        # Misc Stats
        self.exp += flamestats.exp
        self.dr += flamestats.dr
        self.meso += flamestats.meso
        self.glincrease += flamestats.glincrease
        self.partyexp += flamestats.partyexp
        self.feverchargeinc += flamestats.feverchargeinc
        self.feverduration += flamestats.feverduration
        self.maxfeverchance += flamestats.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += flamestats.spmulti

        # Set Stats
        self.mempsetcount += flamestats.mempsetcount
        self.aempsetcount += flamestats.aempsetcount
        self.necrosetcount += flamestats.necrosetcount
        self.fafsetcount += flamestats.fafsetcount
        self.bosssetcount += flamestats.bosssetcount
        self.commandersetcount += flamestats.commandersetcount

        # Flame Stats
        self.atklinecount += flamestats.atklinecount
        self.crlinecount += flamestats.crlinecount
        self.cdlinecount += flamestats.cdlinecount

# Flame
        self.normal_emb += flame.normal_emb
        self.partial_emb += flame.partial_emb
        self.unique_acc_emb += flame.unique_acc_emb
        self.legendary_acc_emb += flame.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += flame.emblem_cd
        self.emblem_batk += flame.emblem_batk
        self.emblem_atkp += flame.emblem_atkp

        # SF Stats
        self.sf += flame.sf

        # Offensive Stats
        self.atk += flame.atk
        self.atkp += flame.atkp
        self.dmg += flame.dmg
        self.batk += flame.batk
        self.platk += flame.platk
        self.cr += flame.cr
        self.cratk += flame.cratk
        self.cd += flame.cd
        self.maxdmg += flame.maxdmg
        self.fd += flame.fd

        # Defensive Stats
        self.pdef += flame.pdef
        self.pdefinc += flame.pdefinc
        self.pdefdec += flame.pdefdec
        self.mdef += flame.mdef
        self.mdefinc += flame.mdefinc
        self.mdefdec += flame.mdefdec
        self.bdef += flame.bdef
        self.pldef += flame.pldef
        self.critres += flame.critres
        self.critdmgres += flame.critdmgres

        # Hit Miss Stats
        self.acc += flame.acc
        self.accp += flame.accp
        self.evd += flame.evd
        self.evdp += flame.evdp
        self.penrate += flame.penrate
        self.block += flame.block
        self.abnormalstatres += flame.abnormalstatres
        self.ignore += flame.ignore

        # HP MP Stats
        self.hp += flame.hp
        self.mp += flame.mp
        self.hpinc += flame.hpinc
        self.mpinc += flame.mpinc
        self.hprec += flame.hprec
        self.mprec += flame.mprec
        self.hprecp += flame.hprecp
        self.mprecp += flame.mprecp
        self.hppotionrecp += flame.hppotionrecp
        self.mppotionrecp += flame.mppotionrecp
        self.buffdurationinc += flame.buffdurationinc

        # Mobility Stats
        self.spd += flame.spd
        self.jmp += flame.jmp
        self.kbkres += flame.kbkres

        # Misc Stats
        self.exp += flame.exp
        self.dr += flame.dr
        self.meso += flame.meso
        self.glincrease += flame.glincrease
        self.partyexp += flame.partyexp
        self.feverchargeinc += flame.feverchargeinc
        self.feverduration += flame.feverduration
        self.maxfeverchance += flame.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += flame.spmulti

        # Set Stats
        self.mempsetcount += flame.mempsetcount
        self.aempsetcount += flame.aempsetcount
        self.necrosetcount += flame.necrosetcount
        self.fafsetcount += flame.fafsetcount
        self.bosssetcount += flame.bosssetcount
        self.commandersetcount += flame.commandersetcount

        # Flame Stats
        self.atklinecount += flame.atklinecount
        self.crlinecount += flame.crlinecount
        self.cdlinecount += flame.cdlinecount

# Pet Stats
        self.normal_emb += petstats.normal_emb
        self.partial_emb += petstats.partial_emb
        self.unique_acc_emb += petstats.unique_acc_emb
        self.legendary_acc_emb += petstats.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += petstats.emblem_cd
        self.emblem_batk += petstats.emblem_batk
        self.emblem_atkp += petstats.emblem_atkp

        # SF Stats
        self.sf += petstats.sf

        # Offensive Stats
        self.atk += petstats.atk
        self.atkp += petstats.atkp
        self.dmg += petstats.dmg
        self.batk += petstats.batk
        self.platk += petstats.platk
        self.cr += petstats.cr
        self.cratk += petstats.cratk
        self.cd += petstats.cd
        self.maxdmg += petstats.maxdmg
        self.fd += petstats.fd

        # Defensive Stats
        self.pdef += petstats.pdef
        self.pdefinc += petstats.pdefinc
        self.pdefdec += petstats.pdefdec
        self.mdef += petstats.mdef
        self.mdefinc += petstats.mdefinc
        self.mdefdec += petstats.mdefdec
        self.bdef += petstats.bdef
        self.pldef += petstats.pldef
        self.critres += petstats.critres
        self.critdmgres += petstats.critdmgres

        # Hit Miss Stats
        self.acc += petstats.acc
        self.accp += petstats.accp
        self.evd += petstats.evd
        self.evdp += petstats.evdp
        self.penrate += petstats.penrate
        self.block += petstats.block
        self.abnormalstatres += petstats.abnormalstatres
        self.ignore += petstats.ignore

        # HP MP Stats
        self.hp += petstats.hp
        self.mp += petstats.mp
        self.hpinc += petstats.hpinc
        self.mpinc += petstats.mpinc
        self.hprec += petstats.hprec
        self.mprec += petstats.mprec
        self.hprecp += petstats.hprecp
        self.mprecp += petstats.mprecp
        self.hppotionrecp += petstats.hppotionrecp
        self.mppotionrecp += petstats.mppotionrecp
        self.buffdurationinc += petstats.buffdurationinc

        # Mobility Stats
        self.spd += petstats.spd
        self.jmp += petstats.jmp
        self.kbkres += petstats.kbkres

        # Misc Stats
        self.exp += petstats.exp
        self.dr += petstats.dr
        self.meso += petstats.meso
        self.glincrease += petstats.glincrease
        self.partyexp += petstats.partyexp
        self.feverchargeinc += petstats.feverchargeinc
        self.feverduration += petstats.feverduration
        self.maxfeverchance += petstats.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += petstats.spmulti

        # Set Stats
        self.mempsetcount += petstats.mempsetcount
        self.aempsetcount += petstats.aempsetcount
        self.necrosetcount += petstats.necrosetcount
        self.fafsetcount += petstats.fafsetcount
        self.bosssetcount += petstats.bosssetcount
        self.commandersetcount += petstats.commandersetcount

        # Flame Stats
        self.atklinecount += petstats.atklinecount
        self.crlinecount += petstats.crlinecount
        self.cdlinecount += petstats.cdlinecount

# Star Force
        self.normal_emb += starforce.normal_emb
        self.partial_emb += starforce.partial_emb
        self.unique_acc_emb += starforce.unique_acc_emb
        self.legendary_acc_emb += starforce.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += starforce.emblem_cd
        self.emblem_batk += starforce.emblem_batk
        self.emblem_atkp += starforce.emblem_atkp

        # SF Stats
        self.sf += starforce.sf

        # Offensive Stats
        self.atk += starforce.atk
        self.atkp += starforce.atkp
        self.dmg += starforce.dmg
        self.batk += starforce.batk
        self.platk += starforce.platk
        self.cr += starforce.cr
        self.cratk += starforce.cratk
        self.cd += starforce.cd
        self.maxdmg += starforce.maxdmg
        self.fd += starforce.fd

        # Defensive Stats
        self.pdef += starforce.pdef
        self.pdefinc += starforce.pdefinc
        self.pdefdec += starforce.pdefdec
        self.mdef += starforce.mdef
        self.mdefinc += starforce.mdefinc
        self.mdefdec += starforce.mdefdec
        self.bdef += starforce.bdef
        self.pldef += starforce.pldef
        self.critres += starforce.critres
        self.critdmgres += starforce.critdmgres

        # Hit Miss Stats
        self.acc += starforce.acc
        self.accp += starforce.accp
        self.evd += starforce.evd
        self.evdp += starforce.evdp
        self.penrate += starforce.penrate
        self.block += starforce.block
        self.abnormalstatres += starforce.abnormalstatres
        self.ignore += starforce.ignore

        # HP MP Stats
        self.hp += starforce.hp
        self.mp += starforce.mp
        self.hpinc += starforce.hpinc
        self.mpinc += starforce.mpinc
        self.hprec += starforce.hprec
        self.mprec += starforce.mprec
        self.hprecp += starforce.hprecp
        self.mprecp += starforce.mprecp
        self.hppotionrecp += starforce.hppotionrecp
        self.mppotionrecp += starforce.mppotionrecp
        self.buffdurationinc += starforce.buffdurationinc

        # Mobility Stats
        self.spd += starforce.spd
        self.jmp += starforce.jmp
        self.kbkres += starforce.kbkres

        # Misc Stats
        self.exp += starforce.exp
        self.dr += starforce.dr
        self.meso += starforce.meso
        self.glincrease += starforce.glincrease
        self.partyexp += starforce.partyexp
        self.feverchargeinc += starforce.feverchargeinc
        self.feverduration += starforce.feverduration
        self.maxfeverchance += starforce.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += starforce.spmulti

        # Set Stats
        self.mempsetcount += starforce.mempsetcount
        self.aempsetcount += starforce.aempsetcount
        self.necrosetcount += starforce.necrosetcount
        self.fafsetcount += starforce.fafsetcount
        self.bosssetcount += starforce.bosssetcount
        self.commandersetcount += starforce.commandersetcount

        # Flame Stats
        self.atklinecount += starforce.atklinecount
        self.crlinecount += starforce.crlinecount
        self.cdlinecount += starforce.cdlinecount

# Hyperstats
        self.normal_emb += hyperstats.normal_emb
        self.partial_emb += hyperstats.partial_emb
        self.unique_acc_emb += hyperstats.unique_acc_emb
        self.legendary_acc_emb += hyperstats.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += hyperstats.emblem_cd
        self.emblem_batk += hyperstats.emblem_batk
        self.emblem_atkp += hyperstats.emblem_atkp

        # SF Stats
        self.sf += hyperstats.sf

        # Offensive Stats
        self.atk += hyperstats.atk
        self.atkp += hyperstats.atkp
        self.dmg += hyperstats.dmg
        self.batk += hyperstats.batk
        self.platk += hyperstats.platk
        self.cr += hyperstats.cr
        self.cratk += hyperstats.cratk
        self.cd += hyperstats.cd
        self.maxdmg += hyperstats.maxdmg
        self.fd += hyperstats.fd

        # Defensive Stats
        self.pdef += hyperstats.pdef
        self.pdefinc += hyperstats.pdefinc
        self.pdefdec += hyperstats.pdefdec
        self.mdef += hyperstats.mdef
        self.mdefinc += hyperstats.mdefinc
        self.mdefdec += hyperstats.mdefdec
        self.bdef += hyperstats.bdef
        self.pldef += hyperstats.pldef
        self.critres += hyperstats.critres
        self.critdmgres += hyperstats.critdmgres

        # Hit Miss Stats
        self.acc += hyperstats.acc
        self.accp += hyperstats.accp
        self.evd += hyperstats.evd
        self.evdp += hyperstats.evdp
        self.penrate += hyperstats.penrate
        self.block += hyperstats.block
        self.abnormalstatres += hyperstats.abnormalstatres
        self.ignore += hyperstats.ignore

        # HP MP Stats
        self.hp += hyperstats.hp
        self.mp += hyperstats.mp
        self.hpinc += hyperstats.hpinc
        self.mpinc += hyperstats.mpinc
        self.hprec += hyperstats.hprec
        self.mprec += hyperstats.mprec
        self.hprecp += hyperstats.hprecp
        self.mprecp += hyperstats.mprecp
        self.hppotionrecp += hyperstats.hppotionrecp
        self.mppotionrecp += hyperstats.mppotionrecp
        self.buffdurationinc += hyperstats.buffdurationinc

        # Mobility Stats
        self.spd += hyperstats.spd
        self.jmp += hyperstats.jmp
        self.kbkres += hyperstats.kbkres

        # Misc Stats
        self.exp += hyperstats.exp
        self.dr += hyperstats.dr
        self.meso += hyperstats.meso
        self.glincrease += hyperstats.glincrease
        self.partyexp += hyperstats.partyexp
        self.feverchargeinc += hyperstats.feverchargeinc
        self.feverduration += hyperstats.feverduration
        self.maxfeverchance += hyperstats.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += hyperstats.spmulti

        # Set Stats
        self.mempsetcount += hyperstats.mempsetcount
        self.aempsetcount += hyperstats.aempsetcount
        self.necrosetcount += hyperstats.necrosetcount
        self.fafsetcount += hyperstats.fafsetcount
        self.bosssetcount += hyperstats.bosssetcount
        self.commandersetcount += hyperstats.commandersetcount

        # Flame Stats
        self.atklinecount += hyperstats.atklinecount
        self.crlinecount += hyperstats.crlinecount
        self.cdlinecount += hyperstats.cdlinecount

# Links
        self.normal_emb += links.normal_emb
        self.partial_emb += links.partial_emb
        self.unique_acc_emb += links.unique_acc_emb
        self.legendary_acc_emb += links.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += links.emblem_cd
        self.emblem_batk += links.emblem_batk
        self.emblem_atkp += links.emblem_atkp

        # SF Stats
        self.sf += links.sf

        # Offensive Stats
        self.atk += links.atk
        self.atkp += links.atkp
        self.dmg += links.dmg
        self.batk += links.batk
        self.platk += links.platk
        self.cr += links.cr
        self.cratk += links.cratk
        self.cd += links.cd
        self.maxdmg += links.maxdmg
        self.fd += links.fd

        # Defensive Stats
        self.pdef += links.pdef
        self.pdefinc += links.pdefinc
        self.pdefdec += links.pdefdec
        self.mdef += links.mdef
        self.mdefinc += links.mdefinc
        self.mdefdec += links.mdefdec
        self.bdef += links.bdef
        self.pldef += links.pldef
        self.critres += links.critres
        self.critdmgres += links.critdmgres

        # Hit Miss Stats
        self.acc += links.acc
        self.accp += links.accp
        self.evd += links.evd
        self.evdp += links.evdp
        self.penrate += links.penrate
        self.block += links.block
        self.abnormalstatres += links.abnormalstatres
        self.ignore += links.ignore

        # HP MP Stats
        self.hp += links.hp
        self.mp += links.mp
        self.hpinc += links.hpinc
        self.mpinc += links.mpinc
        self.hprec += links.hprec
        self.mprec += links.mprec
        self.hprecp += links.hprecp
        self.mprecp += links.mprecp
        self.hppotionrecp += links.hppotionrecp
        self.mppotionrecp += links.mppotionrecp
        self.buffdurationinc += links.buffdurationinc

        # Mobility Stats
        self.spd += links.spd
        self.jmp += links.jmp
        self.kbkres += links.kbkres

        # Misc Stats
        self.exp += links.exp
        self.dr += links.dr
        self.meso += links.meso
        self.glincrease += links.glincrease
        self.partyexp += links.partyexp
        self.feverchargeinc += links.feverchargeinc
        self.feverduration += links.feverduration
        self.maxfeverchance += links.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += links.spmulti

        # Set Stats
        self.mempsetcount += links.mempsetcount
        self.aempsetcount += links.aempsetcount
        self.necrosetcount += links.necrosetcount
        self.fafsetcount += links.fafsetcount
        self.bosssetcount += links.bosssetcount
        self.commandersetcount += links.commandersetcount

        # Flame Stats
        self.atklinecount += links.atklinecount
        self.crlinecount += links.crlinecount
        self.cdlinecount += links.cdlinecount

# Mapletree
        self.normal_emb += mapletree.normal_emb
        self.partial_emb += mapletree.partial_emb
        self.unique_acc_emb += mapletree.unique_acc_emb
        self.legendary_acc_emb += mapletree.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += mapletree.emblem_cd
        self.emblem_batk += mapletree.emblem_batk
        self.emblem_atkp += mapletree.emblem_atkp

        # SF Stats
        self.sf += mapletree.sf

        # Offensive Stats
        self.atk += mapletree.atk
        self.atkp += mapletree.atkp
        self.dmg += mapletree.dmg
        self.batk += mapletree.batk
        self.platk += mapletree.platk
        self.cr += mapletree.cr
        self.cratk += mapletree.cratk
        self.cd += mapletree.cd
        self.maxdmg += mapletree.maxdmg
        self.fd += mapletree.fd

        # Defensive Stats
        self.pdef += mapletree.pdef
        self.pdefinc += mapletree.pdefinc
        self.pdefdec += mapletree.pdefdec
        self.mdef += mapletree.mdef
        self.mdefinc += mapletree.mdefinc
        self.mdefdec += mapletree.mdefdec
        self.bdef += mapletree.bdef
        self.pldef += mapletree.pldef
        self.critres += mapletree.critres
        self.critdmgres += mapletree.critdmgres

        # Hit Miss Stats
        self.acc += mapletree.acc
        self.accp += mapletree.accp
        self.evd += mapletree.evd
        self.evdp += mapletree.evdp
        self.penrate += mapletree.penrate
        self.block += mapletree.block
        self.abnormalstatres += mapletree.abnormalstatres
        self.ignore += mapletree.ignore

        # HP MP Stats
        self.hp += mapletree.hp
        self.mp += mapletree.mp
        self.hpinc += mapletree.hpinc
        self.mpinc += mapletree.mpinc
        self.hprec += mapletree.hprec
        self.mprec += mapletree.mprec
        self.hprecp += mapletree.hprecp
        self.mprecp += mapletree.mprecp
        self.hppotionrecp += mapletree.hppotionrecp
        self.mppotionrecp += mapletree.mppotionrecp
        self.buffdurationinc += mapletree.buffdurationinc

        # Mobility Stats
        self.spd += mapletree.spd
        self.jmp += mapletree.jmp
        self.kbkres += mapletree.kbkres

        # Misc Stats
        self.exp += mapletree.exp
        self.dr += mapletree.dr
        self.meso += mapletree.meso
        self.glincrease += mapletree.glincrease
        self.partyexp += mapletree.partyexp
        self.feverchargeinc += mapletree.feverchargeinc
        self.feverduration += mapletree.feverduration
        self.maxfeverchance += mapletree.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += mapletree.spmulti

        # Set Stats
        self.mempsetcount += mapletree.mempsetcount
        self.aempsetcount += mapletree.aempsetcount
        self.necrosetcount += mapletree.necrosetcount
        self.fafsetcount += mapletree.fafsetcount
        self.bosssetcount += mapletree.bosssetcount
        self.commandersetcount += mapletree.commandersetcount

        # Flame Stats
        self.atklinecount += mapletree.atklinecount
        self.crlinecount += mapletree.crlinecount
        self.cdlinecount += mapletree.cdlinecount

# Character
        # Offensive Stats
        self.atk += char.atk
        self.atkp += char.atkp
        self.dmg += char.dmg
        self.batk += char.batk
        self.platk += char.platk
        self.cr += char.cr
        self.cratk += char.cratk
        self.cd += char.cd
        self.maxdmg += char.maxdmg
        self.fd += char.fd

        # Defensive Stats
        self.pdef += char.pdef
        self.pdefinc += char.pdefinc
        self.pdefdec += char.pdefdec
        self.mdef += char.mdef
        self.mdefinc += char.mdefinc
        self.mdefdec += char.mdefdec
        self.bdef += char.bdef
        self.pldef += char.pldef
        self.critres += char.critres
        self.critdmgres += char.critdmgres

        # Hit Miss Stats
        self.acc += char.acc
        self.accp += char.accp
        self.evd += char.evd
        self.evdp += char.evdp
        self.penrate += char.penrate
        self.block += char.block
        self.abnormalstatres += char.abnormalstatres
        self.ignore += char.ignore

        # HP MP Stats
        self.hp += char.hp
        self.mp += char.mp
        self.hpinc += char.hpinc
        self.mpinc += char.mpinc
        self.hprec += char.hprec
        self.mprec += char.mprec
        self.hprecp += char.hprecp
        self.mprecp += char.mprecp
        self.hppotionrecp += char.hppotionrecp
        self.mppotionrecp += char.mppotionrecp
        self.buffdurationinc += char.buffdurationinc

        # Mobility Stats
        self.spd += char.spd
        self.jmp += char.jmp
        self.kbkres += char.kbkres

        # Misc Stats
        self.exp += char.exp
        self.dr += char.dr
        self.meso += char.meso
        self.glincrease += char.glincrease
        self.partyexp += char.partyexp
        self.feverchargeinc += char.feverchargeinc
        self.feverduration += char.feverduration
        self.maxfeverchance += char.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += char.spmulti
