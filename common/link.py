import streamlit as st


class link:
    def __init__(self, character_class, type):
        # Initialize
        # Initialize
        self.stat_amount = 0
        self.emblem_amount = 0
        self.normal_emb = 0
        self.emblem_cd = 0
        self.emblem_batk = 0
        self.emblem_atkp = 0
        self.unique_acc_emb = 0
        self.legendary_acc_emb = 0

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

        joblink = {
            # Warrior
            "Dark Knight": "Phy DEF (Dark Knight)",
            "Hero": "Boss DEF (Hero)",
            "Paladin": "PEN Rate (Paladin)",
            "Dawn Warrior": "Mag DEF (Dawn Warrior)",
            "Aran": "Fever Recharge (Aran)",
            "Demon Slayer": "Boss ATK (Demon Slayer)",
            "Demon Avenger": "Phy DMG (Demon Avenger)",
            # Mage
            "Bishop": "Party EXP (Bishop)",
            "Ice Lightning Mage": "MP% (Ice Lightning Mage)",
            "Fire Poison Mage": "Mag ATK (Fire Poison Mage)",
            "Blaze Wizard": "Fever Duration (Blaze Wizard)",
            "Evan": "Boss ATK (Evan)",
            "Luminous": "Mag DMG (Luminous)",
            "Battle Mage": "Abnormal Status RES (Battle Mage, Wild Hunter & Mechanic)",
            # Archer
            "Bow Master": "Gold Leaf (Bow Master)",
            "Marksman": "ACC (Marksman)",
            "Wind Archer": "HP/MP Rec (Wind Archer)",
            "Mercedes": "EXP (Mercedes)",
            "Wild Hunter": "Abnormal Status RES (Battle Mage, Wild Hunter & Mechanic)",
            # Thief
            "Night Lord": "Meso (Night Lord)",
            "Shadower": "Crit Rate (Shadower)",
            "Night Walker": "Drop (Night Walker)",
            "Phantom": "Crit DMG (Phantom)",
            # Pirate
            "Corsair": "KBK RES (Corsair)",
            "Buccaneer": "Phy ATK (Buccaneer)",
            "Thunder Breaker": "HP% (Thunder Breaker)",
            "Shade": "Survival Chance (Shade)",
            "Mechanic": "Abnormal Status RES (Battle Mage, Wild Hunter & Mechanic)"
        }
        linkskills = ["Phy DEF (Dark Knight)", "Boss DEF (Hero)", "PEN Rate (Paladin)", "Mag DEF (Dawn Warrior)",
                      "Fever Recharge (Aran)", "Boss ATK (Demon Slayer)", "Phy DMG (Demon Avenger)",
                      "Party EXP (Bishop)", "MP% (Ice Lightning Mage)", "Mag ATK (Fire Poison Mage)",
                      "Fever Duration (Blaze Wizard)", "Boss ATK (Evan)", "Mag DMG (Luminous)",
                      "Abnormal Status RES (Battle Mage, Wild Hunter & Mechanic)", "Gold Leaf (Bow Master)",
                      "ACC (Marksman)", "HP/MP Rec (Wind Archer)", "EXP (Mercedes)", "Meso (Night Lord)",
                      "Crit Rate (Shadower)", "Drop (Night Walker)", "Crit DMG (Phantom)", "KBK RES (Corsair)",
                      "Phy ATK (Buccaneer)", "HP% (Thunder Breaker)", "Survival Chance (Shade)"]

        linkskills.remove(joblink[character_class])
        with st.beta_expander("Link Skills"):
            st.write("Note: Character Innate Link Skill Already Included")
            link_list = st.multiselect("Choose 12 Link Skills", linkskills)
            self.links = link_list
            _, link1, _, link2, _ = st.beta_columns([0.02, 0.47, 0.02, 0.47, 0.02])
            if len(link_list) == 12:
                link1.write(link_list[0])
                link1.write(link_list[1])
                link1.write(link_list[2])
                link1.write(link_list[3])
                link1.write(link_list[4])
                link1.write(link_list[5])
                link2.write(link_list[6])
                link2.write(link_list[7])
                link2.write(link_list[8])
                link2.write(link_list[9])
                link2.write(link_list[10])
                link2.write(link_list[11])
                if "Phy DEF (Dark Knight)" in link_list:
                    self.pdefinc += 4
                if "Boss DEF (Hero)" in link_list:
                    self.bdef += 4
                if "PEN Rate (Paladin)" in link_list:
                    self.penrate += 4
                if "Mag DEF (Dawn Warrior)" in link_list:
                    self.mdefinc += 4
                if "Fever Recharge (Aran)" in link_list:
                    self.feverchargeinc += 4
                if "Boss ATK (Demon Slayer)" in link_list:
                    self.batk += 4
                if "Phy DMG (Demon Avenger)" in link_list:
                    if type == "PHYSICAL":
                        self.dmg += 4
                if "Party EXP (Bishop)" in link_list:
                    self.partyexp += 4
                if "MP% (Ice Lightning Mage)" in link_list:
                    self.mpinc += 4
                if "Mag ATK (Fire Poison Mage)" in link_list:
                    if type == "MAGICAL":
                        self.atkp += 4
                if "Fever Duration (Blaze Wizard)" in link_list:
                    self.feverduration += 5
                if "Boss ATK (Evan)" in link_list:
                    self.batk += 5
                if "Mag DMG (Luminous)" in link_list:
                    if type == "MAGICAL":
                        self.dmg += 4
                if "Abnormal Status RES (Battle Mage, Wild Hunter & Mechanic)" in link_list:
                    self.abnormalstatres += 6
                if "Gold Leaf (Bow Master)" in link_list:
                    self.glincrease += 4
                if "ACC (Marksman)" in link_list:
                    self.accp += 4
                if "HP/MP Rec (Wind Archer)" in link_list:
                    self.hprec += 100
                    self.mprec += 100
                if "EXP (Mercedes)" in link_list:
                    self.exp += 4
                if "Meso (Night Lord)" in link_list:
                    self.meso += 4
                if "Crit Rate (Shadower)" in link_list:
                    self.cr += 4
                if "Drop (Night Walker)" in link_list:
                    self.dr += 4
                if "Crit DMG (Phantom)" in link_list:
                    self.cd += 4
                if "KBK RES (Corsair)" in link_list:
                    self.kbkres += 10
                if "Phy ATK (Buccaneer)" in link_list:
                    if type == "PHYSICAL":
                        self.atkp += 4
                if "HP% (Thunder Breaker)" in link_list:
                    self.hpinc += 4
                if "Survival Chance (Shade)" in link_list:
                    pass
            elif len(link_list) > 12:
                st.write(f"Above Link Skill Limit. Currently {len(link_list)}/12.")
            else:
                st.write(f"Only {len(link_list)}/12")

    def links(self):
        links = self.links
        return links

    def normal_emb(self):
        normal_emb = self.normal_emb
        return normal_emb

    def unique_acc_emb(self):
        unique_acc_emb = self.unique_acc_emb
        return unique_acc_emb

    def legendary_acc_emb(self):
        legendary_acc_emb = self.legendary_acc_emb
        return legendary_acc_emb

    def emblem_cd(self):
        emblem_cd = self.emblem_cd
        return emblem_cd

    def emblem_batk(self):
        emblem_batk = self.emblem_batk
        return emblem_batk

    def emblem_atkp(self):
        emblem_atkp = self.emblem_atkp
        return emblem_atkp

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