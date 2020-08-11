from equip.hat import hat as ht
from equip.weapon import weapon
from equip.top import top
from equip.bottom import bottom
from equip.cape import cape
from equip.glove import glove
from equip.shoe import shoe
from equip.outfit import outfit
from equip.shoulder import shoulder
from equip.belt import belt
from equip.secweapon import secweapon
from equip.seteffect import seteffect
from equip.jewel import jewel

class equip_selection:
    def __init__(self, equip_type, stattype, character_class, cash_type):
        self.cash_type = cash_type
        hat = ht(equip_type, stattype)
        wp = weapon(equip_type, stattype)
        tp = top(equip_type, stattype)
        btm = bottom(equip_type, stattype)
        cp = cape(equip_type, stattype, character_class)
        gl = glove(equip_type, stattype)
        sh = shoe(equip_type, stattype)
        out = outfit(equip_type, stattype)
        sho = shoulder(equip_type, stattype)
        be = belt(equip_type,stattype)
        sw = secweapon()
        jwl = jewel(stattype)
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

        self.acc = 0
        self.accp = 0
        self.evd = 0
        self.evdp = 0
        self.penrate = 0
        self.block = 0
        self.abnormalstatres = 0

        self.hp = 0
        self.hpinc = 0
        self.mp = 0
        self.mpinc = 0

        self.spd = 0
        self.jmp = 0
        self.kbkres = 0

        self.exp = 0
        self.dr = 0
        self.meso = 0
        self.glincrease = 0
        self.partyexp = 0
        self.feverchargeinc = 0
        self.feverduration = 0
        self.maxfeverchance = 0
        self.spmulti = 0
        self.empsetcount = 0
        self.necrosetcount = 0
        self.fafsetcount = 0
        self.bosssetcount = 0
        self.atklinecount = 0
        self.crlinecount = 0
        self.cdlinecount = 0

        # Hat
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

        self.acc += hat.acc
        self.accp += hat.accp
        self.evd += hat.evd
        self.evdp += hat.evdp
        self.penrate += hat.penrate
        self.block += hat.block
        self.abnormalstatres += hat.abnormalstatres

        self.hp += hat.hp
        self.hpinc += hat.hpinc
        self.mp += hat.mp
        self.mpinc += hat.mpinc

        self.spd += hat.spd
        self.jmp += hat.jmp
        self.kbkres += hat.kbkres

        self.exp += hat.exp
        self.dr += hat.dr
        self.meso += hat.meso
        self.glincrease += hat.glincrease
        self.partyexp += hat.partyexp
        self.feverchargeinc += hat.feverchargeinc
        self.feverduration += hat.feverduration
        self.maxfeverchance += hat.maxfeverchance
        self.spmulti += hat.spmulti
        self.empsetcount += hat.empsetcount
        self.necrosetcount += hat.necrosetcount
        self.fafsetcount += hat.fafsetcount
        self.atklinecount += hat.atklinecount
        self.crlinecount += hat.crlinecount
        self.cdlinecount += hat.cdlinecount

        # Weapon
        self.atk += wp.atk
        self.atkp += wp.atkp
        self.dmg += wp.dmg
        self.batk += wp.batk
        self.platk += wp.platk
        self.cr += wp.cr
        self.cratk += wp.cratk
        self.cd += wp.cd
        self.maxdmg += wp.maxdmg
        self.fd += wp.fd

        self.pdef += wp.pdef
        self.pdefinc += wp.pdefinc
        self.pdefdec += wp.pdefdec
        self.mdef += wp.mdef
        self.mdefinc += wp.mdefinc
        self.mdefdec += wp.mdefdec
        self.bdef += wp.bdef
        self.pldef += wp.pldef
        self.critres += wp.critres
        self.critdmgres += wp.critdmgres

        self.acc += wp.acc
        self.accp += wp.accp
        self.evd += wp.evd
        self.evdp += wp.evdp
        self.penrate += wp.penrate
        self.block += wp.block
        self.abnormalstatres += wp.abnormalstatres

        self.hp += wp.hp
        self.hpinc += wp.hpinc
        self.mp += wp.mp
        self.mpinc += wp.mpinc

        self.spd += wp.spd
        self.jmp += wp.jmp
        self.kbkres += wp.kbkres

        self.exp += wp.exp
        self.dr += wp.dr
        self.meso += wp.meso
        self.glincrease += wp.glincrease
        self.partyexp += wp.partyexp
        self.feverchargeinc += wp.feverchargeinc
        self.feverduration += wp.feverduration
        self.maxfeverchance += wp.maxfeverchance
        self.spmulti += wp.spmulti
        self.empsetcount += wp.empsetcount
        self.necrosetcount += wp.necrosetcount
        self.fafsetcount += wp.fafsetcount
        self.atklinecount += wp.atklinecount
        self.crlinecount += wp.crlinecount
        self.cdlinecount += wp.cdlinecount

        # Top
        self.atk += tp.atk
        self.atkp += tp.atkp
        self.dmg += tp.dmg
        self.batk += tp.batk
        self.platk += tp.platk
        self.cr += tp.cr
        self.cratk += tp.cratk
        self.cd += tp.cd
        self.maxdmg += tp.maxdmg
        self.fd += tp.fd

        self.pdef += tp.pdef
        self.pdefinc += tp.pdefinc
        self.pdefdec += tp.pdefdec
        self.mdef += tp.mdef
        self.mdefinc += tp.mdefinc
        self.mdefdec += tp.mdefdec
        self.bdef += tp.bdef
        self.pldef += tp.pldef
        self.critres += tp.critres
        self.critdmgres += tp.critdmgres

        self.acc += tp.acc
        self.accp += tp.accp
        self.evd += tp.evd
        self.evdp += tp.evdp
        self.penrate += tp.penrate
        self.block += tp.block
        self.abnormalstatres += tp.abnormalstatres

        self.hp += tp.hp
        self.hpinc += tp.hpinc
        self.mp += tp.mp
        self.mpinc += tp.mpinc

        self.spd += tp.spd
        self.jmp += tp.jmp
        self.kbkres += tp.kbkres

        self.exp += tp.exp
        self.dr += tp.dr
        self.meso += tp.meso
        self.glincrease += tp.glincrease
        self.partyexp += tp.partyexp
        self.feverchargeinc += tp.feverchargeinc
        self.feverduration += tp.feverduration
        self.maxfeverchance += tp.maxfeverchance
        self.spmulti += tp.spmulti
        self.empsetcount += tp.empsetcount
        self.necrosetcount += tp.necrosetcount
        self.fafsetcount += tp.fafsetcount
        self.atklinecount += tp.atklinecount
        self.crlinecount += tp.crlinecount
        self.cdlinecount += tp.cdlinecount

        # Bottom
        self.atk += btm.atk
        self.atkp += btm.atkp
        self.dmg += btm.dmg
        self.batk += btm.batk
        self.platk += btm.platk
        self.cr += btm.cr
        self.cratk += btm.cratk
        self.cd += btm.cd
        self.maxdmg += btm.maxdmg
        self.fd += btm.fd

        self.pdef += btm.pdef
        self.pdefinc += btm.pdefinc
        self.pdefdec += btm.pdefdec
        self.mdef += btm.mdef
        self.mdefinc += btm.mdefinc
        self.mdefdec += btm.mdefdec
        self.bdef += btm.bdef
        self.pldef += btm.pldef
        self.critres += btm.critres
        self.critdmgres += btm.critdmgres

        self.acc += btm.acc
        self.accp += btm.accp
        self.evd += btm.evd
        self.evdp += btm.evdp
        self.penrate += btm.penrate
        self.block += btm.block
        self.abnormalstatres += btm.abnormalstatres

        self.hp += btm.hp
        self.hpinc += btm.hpinc
        self.mp += btm.mp
        self.mpinc += btm.mpinc

        self.spd += btm.spd
        self.jmp += btm.jmp
        self.kbkres += btm.kbkres

        self.exp += btm.exp
        self.dr += btm.dr
        self.meso += btm.meso
        self.glincrease += btm.glincrease
        self.partyexp += btm.partyexp
        self.feverchargeinc += btm.feverchargeinc
        self.feverduration += btm.feverduration
        self.maxfeverchance += btm.maxfeverchance
        self.spmulti += btm.spmulti
        self.empsetcount += btm.empsetcount
        self.necrosetcount += btm.necrosetcount
        self.fafsetcount += btm.fafsetcount
        self.atklinecount += btm.atklinecount
        self.crlinecount += btm.crlinecount
        self.cdlinecount += btm.cdlinecount

        # Cape
        self.atk += cp.atk
        self.atkp += cp.atkp
        self.dmg += cp.dmg
        self.batk += cp.batk
        self.platk += cp.platk
        self.cr += cp.cr
        self.cratk += cp.cratk
        self.cd += cp.cd
        self.maxdmg += cp.maxdmg
        self.fd += cp.fd

        self.pdef += cp.pdef
        self.pdefinc += cp.pdefinc
        self.pdefdec += cp.pdefdec
        self.mdef += cp.mdef
        self.mdefinc += cp.mdefinc
        self.mdefdec += cp.mdefdec
        self.bdef += cp.bdef
        self.pldef += cp.pldef
        self.critres += cp.critres
        self.critdmgres += cp.critdmgres

        self.acc += cp.acc
        self.accp += cp.accp
        self.evd += cp.evd
        self.evdp += cp.evdp
        self.penrate += cp.penrate
        self.block += cp.block
        self.abnormalstatres += cp.abnormalstatres

        self.hp += cp.hp
        self.hpinc += cp.hpinc
        self.mp += cp.mp
        self.mpinc += cp.mpinc

        self.spd += cp.spd
        self.jmp += cp.jmp
        self.kbkres += cp.kbkres

        self.exp += cp.exp
        self.dr += cp.dr
        self.meso += cp.meso
        self.glincrease += cp.glincrease
        self.partyexp += cp.partyexp
        self.feverchargeinc += cp.feverchargeinc
        self.feverduration += cp.feverduration
        self.maxfeverchance += cp.maxfeverchance
        self.spmulti += cp.spmulti
        self.empsetcount += cp.empsetcount
        self.necrosetcount += cp.necrosetcount
        self.fafsetcount += cp.fafsetcount
        self.atklinecount += cp.atklinecount
        self.crlinecount += cp.crlinecount
        self.cdlinecount += cp.cdlinecount

        # Glove
        self.atk += gl.atk
        self.atkp += gl.atkp
        self.dmg += gl.dmg
        self.batk += gl.batk
        self.platk += gl.platk
        self.cr += gl.cr
        self.cratk += gl.cratk
        self.cd += gl.cd
        self.maxdmg += gl.maxdmg
        self.fd += gl.fd

        self.pdef += gl.pdef
        self.pdefinc += gl.pdefinc
        self.pdefdec += gl.pdefdec
        self.mdef += gl.mdef
        self.mdefinc += gl.mdefinc
        self.mdefdec += gl.mdefdec
        self.bdef += gl.bdef
        self.pldef += gl.pldef
        self.critres += gl.critres
        self.critdmgres += gl.critdmgres

        self.acc += gl.acc
        self.accp += gl.accp
        self.evd += gl.evd
        self.evdp += gl.evdp
        self.penrate += gl.penrate
        self.block += gl.block
        self.abnormalstatres += gl.abnormalstatres

        self.hp += gl.hp
        self.hpinc += gl.hpinc
        self.mp += gl.mp
        self.mpinc += gl.mpinc

        self.spd += gl.spd
        self.jmp += gl.jmp
        self.kbkres += gl.kbkres

        self.exp += gl.exp
        self.dr += gl.dr
        self.meso += gl.meso
        self.glincrease += gl.glincrease
        self.partyexp += gl.partyexp
        self.feverchargeinc += gl.feverchargeinc
        self.feverduration += gl.feverduration
        self.maxfeverchance += gl.maxfeverchance
        self.spmulti += gl.spmulti
        self.empsetcount += gl.empsetcount
        self.necrosetcount += gl.necrosetcount
        self.fafsetcount += gl.fafsetcount
        self.atklinecount += gl.atklinecount
        self.crlinecount += gl.crlinecount
        self.cdlinecount += gl.cdlinecount

        # Shoe
        self.atk += sh.atk
        self.atkp += sh.atkp
        self.dmg += sh.dmg
        self.batk += sh.batk
        self.platk += sh.platk
        self.cr += sh.cr
        self.cratk += sh.cratk
        self.cd += sh.cd
        self.maxdmg += sh.maxdmg
        self.fd += sh.fd

        self.pdef += sh.pdef
        self.pdefinc += sh.pdefinc
        self.pdefdec += sh.pdefdec
        self.mdef += sh.mdef
        self.mdefinc += sh.mdefinc
        self.mdefdec += sh.mdefdec
        self.bdef += sh.bdef
        self.pldef += sh.pldef
        self.critres += sh.critres
        self.critdmgres += sh.critdmgres

        self.acc += sh.acc
        self.accp += sh.accp
        self.evd += sh.evd
        self.evdp += sh.evdp
        self.penrate += sh.penrate
        self.block += sh.block
        self.abnormalstatres += sh.abnormalstatres

        self.hp += sh.hp
        self.hpinc += sh.hpinc
        self.mp += sh.mp
        self.mpinc += sh.mpinc

        self.spd += sh.spd
        self.jmp += sh.jmp
        self.kbkres += sh.kbkres

        self.exp += sh.exp
        self.dr += sh.dr
        self.meso += sh.meso
        self.glincrease += sh.glincrease
        self.partyexp += sh.partyexp
        self.feverchargeinc += sh.feverchargeinc
        self.feverduration += sh.feverduration
        self.maxfeverchance += sh.maxfeverchance
        self.spmulti += sh.spmulti
        self.empsetcount += sh.empsetcount
        self.necrosetcount += sh.necrosetcount
        self.fafsetcount += sh.fafsetcount
        self.atklinecount += sh.atklinecount
        self.crlinecount += sh.crlinecount
        self.cdlinecount += sh.cdlinecount

        # Outfit
        self.atk += out.atk
        self.atkp += out.atkp
        self.dmg += out.dmg
        self.batk += out.batk
        self.platk += out.platk
        self.cr += out.cr
        self.cratk += out.cratk
        self.cd += out.cd
        self.maxdmg += out.maxdmg
        self.fd += out.fd

        self.pdef += out.pdef
        self.pdefinc += out.pdefinc
        self.pdefdec += out.pdefdec
        self.mdef += out.mdef
        self.mdefinc += out.mdefinc
        self.mdefdec += out.mdefdec
        self.bdef += out.bdef
        self.pldef += out.pldef
        self.critres += out.critres
        self.critdmgres += out.critdmgres

        self.acc += out.acc
        self.accp += out.accp
        self.evd += out.evd
        self.evdp += out.evdp
        self.penrate += out.penrate
        self.block += out.block
        self.abnormalstatres += out.abnormalstatres

        self.hp += out.hp
        self.hpinc += out.hpinc
        self.mp += out.mp
        self.mpinc += out.mpinc

        self.spd += out.spd
        self.jmp += out.jmp
        self.kbkres += out.kbkres

        self.exp += out.exp
        self.dr += out.dr
        self.meso += out.meso
        self.glincrease += out.glincrease
        self.partyexp += out.partyexp
        self.feverchargeinc += out.feverchargeinc
        self.feverduration += out.feverduration
        self.maxfeverchance += out.maxfeverchance
        self.spmulti += out.spmulti
        self.empsetcount += out.empsetcount
        self.necrosetcount += out.necrosetcount
        self.fafsetcount += out.fafsetcount
        self.atklinecount += out.atklinecount
        self.crlinecount += out.crlinecount
        self.cdlinecount += out.cdlinecount

        # Shoulder
        self.atk += sho.atk
        self.atkp += sho.atkp
        self.dmg += sho.dmg
        self.batk += sho.batk
        self.platk += sho.platk
        self.cr += sho.cr
        self.cratk += sho.cratk
        self.cd += sho.cd
        self.maxdmg += sho.maxdmg
        self.fd += sho.fd

        self.pdef += sho.pdef
        self.pdefinc += sho.pdefinc
        self.pdefdec += sho.pdefdec
        self.mdef += sho.mdef
        self.mdefinc += sho.mdefinc
        self.mdefdec += sho.mdefdec
        self.bdef += sho.bdef
        self.pldef += sho.pldef
        self.critres += sho.critres
        self.critdmgres += sho.critdmgres

        self.acc += sho.acc
        self.accp += sho.accp
        self.evd += sho.evd
        self.evdp += sho.evdp
        self.penrate += sho.penrate
        self.block += sho.block
        self.abnormalstatres += sho.abnormalstatres

        self.hp += sho.hp
        self.hpinc += sho.hpinc
        self.mp += sho.mp
        self.mpinc += sho.mpinc

        self.spd += sho.spd
        self.jmp += sho.jmp
        self.kbkres += sho.kbkres

        self.exp += sho.exp
        self.dr += sho.dr
        self.meso += sho.meso
        self.glincrease += sho.glincrease
        self.partyexp += sho.partyexp
        self.feverchargeinc += sho.feverchargeinc
        self.feverduration += sho.feverduration
        self.maxfeverchance += sho.maxfeverchance
        self.spmulti += sho.spmulti
        self.empsetcount += sho.empsetcount
        self.necrosetcount += sho.necrosetcount
        self.fafsetcount += sho.fafsetcount
        self.atklinecount += sho.atklinecount
        self.crlinecount += sho.crlinecount
        self.cdlinecount += sho.cdlinecount

        # Belt
        self.atk += be.atk
        self.atkp += be.atkp
        self.dmg += be.dmg
        self.batk += be.batk
        self.platk += be.platk
        self.cr += be.cr
        self.cratk += be.cratk
        self.cd += be.cd
        self.maxdmg += be.maxdmg
        self.fd += be.fd

        self.pdef += be.pdef
        self.pdefinc += be.pdefinc
        self.pdefdec += be.pdefdec
        self.mdef += be.mdef
        self.mdefinc += be.mdefinc
        self.mdefdec += be.mdefdec
        self.bdef += be.bdef
        self.pldef += be.pldef
        self.critres += be.critres
        self.critdmgres += be.critdmgres

        self.acc += be.acc
        self.accp += be.accp
        self.evd += be.evd
        self.evdp += be.evdp
        self.penrate += be.penrate
        self.block += be.block
        self.abnormalstatres += be.abnormalstatres

        self.hp += be.hp
        self.hpinc += be.hpinc
        self.mp += be.mp
        self.mpinc += be.mpinc

        self.spd += be.spd
        self.jmp += be.jmp
        self.kbkres += be.kbkres

        self.exp += be.exp
        self.dr += be.dr
        self.meso += be.meso
        self.glincrease += be.glincrease
        self.partyexp += be.partyexp
        self.feverchargeinc += be.feverchargeinc
        self.feverduration += be.feverduration
        self.maxfeverchance += be.maxfeverchance
        self.spmulti += be.spmulti
        self.empsetcount += be.empsetcount
        self.necrosetcount += be.necrosetcount
        self.fafsetcount += be.fafsetcount
        self.atklinecount += be.atklinecount
        self.crlinecount += be.crlinecount
        self.cdlinecount += be.cdlinecount

        # Secondary Weapon
        self.atk += sw.atk
        self.atkp += sw.atkp
        self.dmg += sw.dmg
        self.batk += sw.batk
        self.platk += sw.platk
        self.cr += sw.cr
        self.cratk += sw.cratk
        self.cd += sw.cd
        self.maxdmg += sw.maxdmg
        self.fd += sw.fd

        self.pdef += sw.pdef
        self.pdefinc += sw.pdefinc
        self.pdefdec += sw.pdefdec
        self.mdef += sw.mdef
        self.mdefinc += sw.mdefinc
        self.mdefdec += sw.mdefdec
        self.bdef += sw.bdef
        self.pldef += sw.pldef
        self.critres += sw.critres
        self.critdmgres += sw.critdmgres

        self.acc += sw.acc
        self.accp += sw.accp
        self.evd += sw.evd
        self.evdp += sw.evdp
        self.penrate += sw.penrate
        self.block += sw.block
        self.abnormalstatres += sw.abnormalstatres

        self.hp += sw.hp
        self.hpinc += sw.hpinc
        self.mp += sw.mp
        self.mpinc += sw.mpinc

        self.spd += sw.spd
        self.jmp += sw.jmp
        self.kbkres += sw.kbkres

        self.exp += sw.exp
        self.dr += sw.dr
        self.meso += sw.meso
        self.glincrease += sw.glincrease
        self.partyexp += sw.partyexp
        self.feverchargeinc += sw.feverchargeinc
        self.feverduration += sw.feverduration
        self.maxfeverchance += sw.maxfeverchance
        self.spmulti += sw.spmulti
        self.empsetcount += sw.empsetcount
        self.necrosetcount += sw.necrosetcount
        self.fafsetcount += sw.fafsetcount
        self.atklinecount += sw.atklinecount
        self.crlinecount += sw.crlinecount
        self.cdlinecount += sw.cdlinecount

        # Jewel
        self.atk += jwl.atk
        self.atkp += jwl.atkp
        self.dmg += jwl.dmg
        self.batk += jwl.batk
        self.platk += jwl.platk
        self.cr += jwl.cr
        self.cratk += jwl.cratk
        self.cd += jwl.cd
        self.maxdmg += jwl.maxdmg
        self.fd += jwl.fd

        self.pdef += jwl.pdef
        self.pdefinc += jwl.pdefinc
        self.pdefdec += jwl.pdefdec
        self.mdef += jwl.mdef
        self.mdefinc += jwl.mdefinc
        self.mdefdec += jwl.mdefdec
        self.bdef += jwl.bdef
        self.pldef += jwl.pldef
        self.critres += jwl.critres
        self.critdmgres += jwl.critdmgres

        self.acc += jwl.acc
        self.accp += jwl.accp
        self.evd += jwl.evd
        self.evdp += jwl.evdp
        self.penrate += jwl.penrate
        self.block += jwl.block
        self.abnormalstatres += jwl.abnormalstatres

        self.hp += jwl.hp
        self.hpinc += jwl.hpinc
        self.mp += jwl.mp
        self.mpinc += jwl.mpinc

        self.spd += jwl.spd
        self.jmp += jwl.jmp
        self.kbkres += jwl.kbkres

        self.exp += jwl.exp
        self.dr += jwl.dr
        self.meso += jwl.meso
        self.glincrease += jwl.glincrease
        self.partyexp += jwl.partyexp
        self.feverchargeinc += jwl.feverchargeinc
        self.feverduration += jwl.feverduration
        self.maxfeverchance += jwl.maxfeverchance
        self.spmulti += jwl.spmulti
        self.empsetcount += jwl.empsetcount
        self.necrosetcount += jwl.necrosetcount
        self.fafsetcount += jwl.fafsetcount

        # Set Effect
        set = seteffect(self.empsetcount, self.necrosetcount, self.fafsetcount, self.bosssetcount, self.cash_type)

        self.atk += set.atk
        self.atkp += set.atkp
        self.dmg += set.dmg
        self.batk += set.batk
        self.platk += set.platk
        self.cr += set.cr
        self.cratk += set.cratk
        self.cd += set.cd
        self.maxdmg += set.maxdmg
        self.fd += set.fd

        self.pdef += set.pdef
        self.pdefinc += set.pdefinc
        self.pdefdec += set.pdefdec
        self.mdef += set.mdef
        self.mdefinc += set.mdefinc
        self.mdefdec += set.mdefdec
        self.bdef += set.bdef
        self.pldef += set.pldef
        self.critres += set.critres
        self.critdmgres += set.critdmgres

        self.acc += set.acc
        self.accp += set.accp
        self.evd += set.evd
        self.evdp += set.evdp
        self.penrate += set.penrate
        self.block += set.block
        self.abnormalstatres += set.abnormalstatres

        self.hp += set.hp
        self.hpinc += set.hpinc
        self.mp += set.mp
        self.mpinc += set.mpinc

        self.spd += set.spd
        self.jmp += set.jmp
        self.kbkres += set.kbkres

        self.exp += set.exp
        self.dr += set.dr
        self.meso += set.meso
        self.glincrease += set.glincrease
        self.partyexp += set.partyexp
        self.feverchargeinc += set.feverchargeinc
        self.feverduration += set.feverduration
        self.maxfeverchance += set.maxfeverchance
        self.spmulti += set.spmulti
        self.empsetcount += set.empsetcount
        self.necrosetcount += set.necrosetcount
        self.fafsetcount += set.fafsetcount