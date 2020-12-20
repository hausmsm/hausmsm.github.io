from flame.flame import flame


class nonemblemcalculations:
    def __init__(self, buffs, flamestats, flame, petstats, starforce, hyperstats, link, mapletree, char):
        # Initialize
        self.normal_emb = 0
        self.unique_acc_emb = 0
        self.legendary_acc_emb = 0
        self.emblem_cd = 0
        self.emblem_batk = 0
        self.emblem_atkp = 0

        # SF Stats
        self.sf = 0

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

        # HP MP Stats
        self.hp = 0
        self.mp = 0
        self.hpinc = 0
        self.mpinc = 0
        self.hprec = 0
        self.mprec = 0
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

        self.normal_emb += buffs.normal_emb
        self.unique_acc_emb += buffs.unique_acc_emb
        self.legendary_acc_emb += buffs.legendary_acc_emb
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

        # HP MP Stats
        self.hp += buffs.hp
        self.mp += buffs.mp
        self.hpinc += buffs.hpinc
        self.mpinc += buffs.mpinc
        self.hprec += buffs.hprec
        self.mprec += buffs.mprec
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

        self.normal_emb += flamestats.normal_emb
        self.unique_acc_emb += flamestats.unique_acc_emb
        self.legendary_acc_emb += flamestats.legendary_acc_emb
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

        # HP MP Stats
        self.hp += flamestats.hp
        self.mp += flamestats.mp
        self.hpinc += flamestats.hpinc
        self.mpinc += flamestats.mpinc
        self.hprec += flamestats.hprec
        self.mprec += flamestats.mprec
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

        self.normal_emb += flame.normal_emb
        self.unique_acc_emb += flame.unique_acc_emb
        self.legendary_acc_emb += flame.legendary_acc_emb
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

        # HP MP Stats
        self.hp += flame.hp
        self.mp += flame.mp
        self.hpinc += flame.hpinc
        self.mpinc += flame.mpinc
        self.hprec += flame.hprec
        self.mprec += flame.mprec
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

        self.normal_emb += petstats.normal_emb
        self.unique_acc_emb += petstats.unique_acc_emb
        self.legendary_acc_emb += petstats.legendary_acc_emb
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

        # HP MP Stats
        self.hp += petstats.hp
        self.mp += petstats.mp
        self.hpinc += petstats.hpinc
        self.mpinc += petstats.mpinc
        self.hprec += petstats.hprec
        self.mprec += petstats.mprec
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

        self.normal_emb += starforce.normal_emb
        self.unique_acc_emb += starforce.unique_acc_emb
        self.legendary_acc_emb += starforce.legendary_acc_emb
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

        # HP MP Stats
        self.hp += starforce.hp
        self.mp += starforce.mp
        self.hpinc += starforce.hpinc
        self.mpinc += starforce.mpinc
        self.hprec += starforce.hprec
        self.mprec += starforce.mprec
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

        self.normal_emb += hyperstats.normal_emb
        self.unique_acc_emb += hyperstats.unique_acc_emb
        self.legendary_acc_emb += hyperstats.legendary_acc_emb
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

        # HP MP Stats
        self.hp += hyperstats.hp
        self.mp += hyperstats.mp
        self.hpinc += hyperstats.hpinc
        self.mpinc += hyperstats.mpinc
        self.hprec += hyperstats.hprec
        self.mprec += hyperstats.mprec
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

        self.normal_emb += link.normal_emb
        self.unique_acc_emb += link.unique_acc_emb
        self.legendary_acc_emb += link.legendary_acc_emb
        self.emblem_cd += link.emblem_cd
        self.emblem_batk += link.emblem_batk
        self.emblem_atkp += link.emblem_atkp

        # SF Stats
        self.sf += link.sf

        # Offensive Stats
        self.atk += link.atk
        self.atkp += link.atkp
        self.dmg += link.dmg
        self.batk += link.batk
        self.platk += link.platk
        self.cr += link.cr
        self.cratk += link.cratk
        self.cd += link.cd
        self.maxdmg += link.maxdmg
        self.fd += link.fd

        # Defensive Stats
        self.pdef += link.pdef
        self.pdefinc += link.pdefinc
        self.pdefdec += link.pdefdec
        self.mdef += link.mdef
        self.mdefinc += link.mdefinc
        self.mdefdec += link.mdefdec
        self.bdef += link.bdef
        self.pldef += link.pldef
        self.critres += link.critres
        self.critdmgres += link.critdmgres

        # Hit Miss Stats
        self.acc += link.acc
        self.accp += link.accp
        self.evd += link.evd
        self.evdp += link.evdp
        self.penrate += link.penrate
        self.block += link.block
        self.abnormalstatres += link.abnormalstatres

        # HP MP Stats
        self.hp += link.hp
        self.mp += link.mp
        self.hpinc += link.hpinc
        self.mpinc += link.mpinc
        self.hprec += link.hprec
        self.mprec += link.mprec
        self.buffdurationinc += link.buffdurationinc

        # Mobility Stats
        self.spd += link.spd
        self.jmp += link.jmp
        self.kbkres += link.kbkres

        # Misc Stats
        self.exp += link.exp
        self.dr += link.dr
        self.meso += link.meso
        self.glincrease += link.glincrease
        self.partyexp += link.partyexp
        self.feverchargeinc += link.feverchargeinc
        self.feverduration += link.feverduration
        self.maxfeverchance += link.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += link.spmulti

        # Set Stats
        self.mempsetcount += link.mempsetcount
        self.aempsetcount += link.aempsetcount
        self.necrosetcount += link.necrosetcount
        self.fafsetcount += link.fafsetcount
        self.bosssetcount += link.bosssetcount
        self.commandersetcount += link.commandersetcount

        # Flame Stats
        self.atklinecount += link.atklinecount
        self.crlinecount += link.crlinecount
        self.cdlinecount += link.cdlinecount

        self.normal_emb += mapletree.normal_emb
        self.unique_acc_emb += mapletree.unique_acc_emb
        self.legendary_acc_emb += mapletree.legendary_acc_emb
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

        # HP MP Stats
        self.hp += mapletree.hp
        self.mp += mapletree.mp
        self.hpinc += mapletree.hpinc
        self.mpinc += mapletree.mpinc
        self.hprec += mapletree.hprec
        self.mprec += mapletree.mprec
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

        self.normal_emb += char.normal_emb
        self.unique_acc_emb += char.unique_acc_emb
        self.legendary_acc_emb += char.legendary_acc_emb
        self.emblem_cd += char.emblem_cd
        self.emblem_batk += char.emblem_batk
        self.emblem_atkp += char.emblem_atkp

        # SF Stats
        self.sf += char.sf

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

        # HP MP Stats
        self.hp += char.hp
        self.mp += char.mp
        self.hpinc += char.hpinc
        self.mpinc += char.mpinc
        self.hprec += char.hprec
        self.mprec += char.mprec
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

        # Set Stats
        self.mempsetcount += char.mempsetcount
        self.aempsetcount += char.aempsetcount
        self.necrosetcount += char.necrosetcount
        self.fafsetcount += char.fafsetcount
        self.bosssetcount += char.bosssetcount
        self.commandersetcount += char.commandersetcount

        # Flame Stats
        self.atklinecount += char.atklinecount
        self.crlinecount += char.crlinecount
        self.cdlinecount += char.cdlinecount

    def normal_emb(self):
        normal_emb = self.normal_emb
        return normal_emb

    def unique_acc_emb(self):
        unique_acc_emb = self.unique_acc_emb
        return unique_acc_emb

    def legendary_acc_emb(self):
        legendary_acc_emb = self.legendary_acc_emb
        return legendary_acc_emb

    def emblem(self):
        emblem = self.emblem
        return emblem

    def emblem_level(self):
        emblem_level = self.emblem_level
        return emblem_level

    def emblem_amount(self):
        emblem_amount = self.emblem_amount
        return emblem_amount

    def type(self):
        type = self.type
        return type

    def sf(self):
        sf = self.sf
        return sf

    def stat(self):
        stat = self.stat
        return stat

    def stat_amount(self):
        stat_amount = self.stat_amount
        return stat_amount

    def level(self):
        level = self.level
        return level

    def atk(self):
        atk = self.atk
        return atk

    def atkp(self):
        atkp = self.atkp
        return atkp

    def dmg(self):
        dmg = self.dmg
        return dmg

    def batk(self):
        batk = self.batk
        return batk

    def platk(self):
        platk = self.platk
        return platk

    def cr(self):
        cr = self.cr
        return cr

    def cratk(self):
        cratk = self.cratk
        return cratk

    def cd(self):
        cd = self.cd
        return cd

    def maxdmg(self):
        maxdmg = self.maxdmg
        return maxdmg

    def fd(self):
        fd = self.fd
        return fd

    def pdef(self):
        pdef = self.pdef
        return pdef

    def pdefinc(self):
        pdefinc = self.pdefinc
        return pdefinc

    def pdefdec(self):
        pdefdec = self.pdefdec
        return pdefdec

    def mdef(self):
        mdef = self.mdef
        return mdef

    def mdefinc(self):
        mdefinc = self.mdefinc
        return mdefinc

    def mdefdec(self):
        mdefdec = self.mdefdec
        return mdefdec

    def bdef(self):
        bdef = self.bdef
        return bdef

    def pldef(self):
        pldef = self.pldef
        return pldef

    def critres(self):
        critres = self.critres
        return critres

    def critdmgres(self):
        critdmgres = self.critdmgres
        return critdmgres

    def acc(self):
        acc = self.acc
        return acc

    def accp(self):
        accp = self.accp
        return accp

    def evd(self):
        evd = self.evd
        return evd

    def evdp(self):
        evdp = self.evdp
        return evdp

    def penrate(self):
        penrate = self.penrate
        return penrate

    def block(self):
        block = self.block
        return block

    def abnormalstatres(self):
        abnormalstatres = self.abnormalstatres
        return abnormalstatres

    def hp(self):
        hp = self.hp
        return hp

    def hpinc(self):
        hpinc = self.hpinc
        return hpinc

    def mp(self):
        mp = self.mp
        return mp

    def mpinc(self):
        mpinc = self.mpinc
        return mpinc

    def hprec(self):
        hprec = self.hprec
        return hprec

    def mprec(self):
        mprec = self.mprec
        return mprec

    def spd(self):
        spd = self.spd
        return spd

    def jmp(self):
        jmp = self.jmp
        return jmp

    def kbkres(self):
        kbkres = self.kbkres
        return kbkres

    def exp(self):
        exp = self.exp
        return exp

    def dr(self):
        dr = self.dr
        return dr

    def meso(self):
        meso = self.meso
        return meso

    def glincrease(self):
        glincrease = self.glincrease
        return glincrease

    def partyexp(self):
        partyexp = self.partyexp
        return partyexp

    def feverchargeinc(self):
        feverchargeinc = self.feverchargeinc
        return feverchargeinc

    def feverduration(self):
        feverduration = self.feverduration
        return feverduration

    def maxfeverchance(self):
        maxfeverchance = self.maxfeverchance
        return maxfeverchance

    def spmulti(self):
        spmulti = self.spmulti
        return spmulti

    def mempsetcount(self):
        mempsetcount = self.mempsetcount
        return mempsetcount

    def aempsetcount(self):
        aempsetcount = self.aempsetcount
        return aempsetcount

    def necrosetcount(self):
        necrosetcount = self.necrosetcount
        return necrosetcount

    def fafsetcount(self):
        fafsetcount = self.fafsetcount
        return fafsetcount

    def bosssetcount(self):
        bosssetcount = self.bosssetcount
        return bosssetcount

    def commandersetcount(self):
        commandersetcount = self.commandersetcount
        return commandersetcount

    def atklinecount(self):
        atklinecount = self.atklinecount
        return atklinecount

    def crlinecount(self):
        crlinecount = self.crlinecount
        return crlinecount

    def cdlinecount(self):
        cdlinecount = self.cdlinecount
        return cdlinecount
