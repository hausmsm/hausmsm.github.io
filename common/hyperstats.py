import streamlit as st


class hyperstats:
    def __init__(self,type):
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
        fddict = {
            0: 0,
            1: 0.3,
            2: 0.6,
            3: 0.9,
            4: 1.2,
            5: 1.5,
            6: 2.1,
            7: 2.7,
            8: 3.3,
            9: 3.9,
            10: 4.5,
            11: 5.4,
            12: 6.3,
            13: 7.2,
            14: 8.1,
            15: 9,
            16: 10.2,
            17: 11.4,
            18: 12.6,
            19: 13.8,
            20: 15
        }

        maxdmgdict = {
                0: 0,
                1: 30000,
                2: 60000,
                3: 90000,
                4: 120000,
                5: 150000,
                6: 210000,
                7: 270000,
                8: 330000,
                9: 390000,
                10: 450000,
                11: 540000,
                12: 630000,
                13: 720000,
                14: 810000,
                15: 900000,
                16: 1020000,
                17: 1140000,
                18: 1260000,
                19: 1380000,
                20: 1500000
        }
        dmgdict = {
            0: 0,
            1: 0.4,
            2: 0.8,
            3: 1.2,
            4: 1.6,
            5: 2,
            6: 2.8,
            7: 3.6,
            8: 4.4,
            9: 5.2,
            10: 6,
            11: 7.2,
            12: 8.4,
            13: 9.6,
            14: 10.8,
            15: 12,
            16: 13.6,
            17: 15.2,
            18: 16.8,
            19: 18.4,
            20: 20
        }
        crdict = {
            0: 0,
            1: 0.3,
            2: 0.6,
            3: 0.9,
            4: 1.2,
            5: 1.5,
            6: 2.1,
            7: 2.7,
            8: 3.3,
            9: 3.9,
            10: 4.5,
            11: 5.4,
            12: 6.3,
            13: 7.2,
            14: 8.1,
            15: 9,
            16: 10.2,
            17: 11.4,
            18: 12.6,
            19: 13.8,
            20: 15
        }
        cddict = {
            0: 0,
            1: 0.3,
            2: 0.6,
            3: 0.9,
            4: 1.2,
            5: 1.5,
            6: 2.1,
            7: 2.7,
            8: 3.3,
            9: 3.9,
            10: 4.5,
            11: 5.4,
            12: 6.3,
            13: 7.2,
            14: 8.1,
            15: 9,
            16: 10.2,
            17: 11.4,
            18: 12.6,
            19: 13.8,
            20: 15
        }
        batkdict = {
            0: 0,
            1: 0.4,
            2: 0.8,
            3: 1.2,
            4: 1.6,
            5: 2,
            6: 2.8,
            7: 3.6,
            8: 4.4,
            9: 5.2,
            10: 6,
            11: 7.2,
            12: 8.4,
            13: 9.6,
            14: 10.8,
            15: 12,
            16: 13.6,
            17: 15.2,
            18: 16.8,
            19: 18.4,
            20: 20
        }
        expdict = {
            0: 0,
            1: 0.5,
            2: 1,
            3: 1.5,
            4: 2,
            5: 2.5,
            6: 3.5,
            7: 4.5,
            8: 5.5,
            9: 6.5,
            10: 7.5,
            11: 9,
            12: 10.5,
            13: 12,
            14: 13.5,
            15: 15,
            16: 17,
            17: 19,
            18: 21,
            19: 23,
            20: 25
        }
        sfdict = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 10,
            11: 1,
            12: 12,
            13: 13,
            14: 14,
            15: 15,
            16: 16,
            17: 17,
            18: 18,
            19: 19,
            20: 20
        }
        partyexpdict = {
            0: 0,
            1: 0.5,
            2: 1,
            3: 1.5,
            4: 2,
            5: 2.5,
            6: 3.5,
            7: 4.5,
            8: 5.5,
            9: 6.5,
            10: 7.5,
            11: 9,
            12: 10.5,
            13: 12,
            14: 13.5,
            15: 15,
            16: 17,
            17: 19,
            18: 21,
            19: 23,
            20: 25
        }
        kbkresdict = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 7,
            7: 9,
            8: 11,
            9: 13,
            10: 15,
            11: 18,
            12: 21,
            13: 24,
            14: 27,
            15: 30,
            16: 34,
            17: 38,
            18: 42,
            19: 46,
            20: 50
        }
        feverdurationdict = {
            0: 0,
            1: 0.2,
            2: 0.4,
            3: 0.6,
            4: 0.8,
            5: 1,
            6: 1.3,
            7: 1.6,
            8: 1.9,
            9: 2.2,
            10: 2.5,
            11: 2.9,
            12: 3.4,
            13: 3.9,
            14: 4.4,
            15: 4.9,
            16: 5.4,
            17: 5.9,
            18: 6.4,
            19: 6.9,
            20: 7.5
        }
        itemdurationdict = {
            0: 0,
            1: 15,
            2: 30,
            3: 45,
            4: 60,
            5: 75,
            6: 90,
            7: 105,
            8: 120,
            9: 135,
            10: 150,
            11: 165,
            12: 180,
            13: 195,
            14: 210,
            15: 225,
            16: 240,
            17: 255,
            18: 270,
            19: 285,
            20: 300
        }
        adddmgdict = {
            0: [0, 0],
            1: [5, 60],
            2: [5, 65],
            3: [5, 70],
            4: [5, 74],
            5: [5, 79],
            6: [6, 84],
            7: [6, 89],
            8: [6, 94],
            9: [7, 98],
            10: [7, 103],
            11: [8, 108],
            12: [8, 113],
            13: [8, 118],
            14: [9, 122],
            15: [10, 127],
            16: [11, 132],
            17: [12, 137],
            18: [13, 142],
            19: [14, 146],
            20: [15, 150]
        }
        ignoredict = {
            0: 0,
            1: 0.4,
            2: 0.8,
            3: 1.2,
            4: 1.6,
            5: 2,
            6: 2.8,
            7: 3.6,
            8: 4.4,
            9: 5.2,
            10: 6,
            11: 7.2,
            12: 8.4,
            13: 9.6,
            14: 10.8,
            15: 12,
            16: 13.6,
            17: 15.2,
            18: 16.8,
            19: 18.4,
            20: 20
        }

        self.hyperstatlist = []
        self.hyperstatamountlist = []
        with st.beta_expander("Hyper Stats"):
            _, hs1, _, hs2, _ = st.beta_columns([0.02, 0.47, 0.02, 0.47, 0.02])
            # Final DMG%
            fd_choice = hs1.selectbox("Final DMG%", ["No", "Yes"])
            self.fd_choice = fd_choice
            if fd_choice == "Yes":
                fd_level = hs1.slider("Final DMG% Level",min_value=1,max_value=20)
                self.fd += fddict[fd_level]
                self.hyperstatlist.append("Final DMG%")
                self.hyperstatamountlist.append(fddict[fd_level])
            # Max DMG Inc
            maxdmg_choice = hs2.selectbox("Max DMG Inc", ["No", "Yes"])
            self.maxdmg_choice = maxdmg_choice
            if maxdmg_choice == "Yes":
                maxdmg_level = hs2.slider("Max DMG Inc Level", min_value=1, max_value=20)
                self.maxdmg += maxdmgdict[maxdmg_level]
                self.hyperstatlist.append("Max DMG Inc")
                self.hyperstatamountlist.append(maxdmgdict[maxdmg_level])
            # Phy/Mag DMG%
            dmg_choice = hs1.selectbox("Phy/Mag DMG%", ["No", "Yes"])
            self.dmg_choice = dmg_choice
            if dmg_choice == "Yes":
                dmg_level = hs1.slider("Phy/Mag DMG% Level",min_value=1,max_value=20)
                self.dmg += dmgdict[dmg_level]
                self.hyperstatlist.append("Phy/Mag DMG%")
                self.hyperstatamountlist.append(dmgdict[dmg_level])
            # Crit Rate
            cr_choice = hs2.selectbox("Crit Rate%", ["No", "Yes"])
            self.cr_choice = cr_choice
            if cr_choice == "Yes":
                cr_level = hs2.slider("Crit Rate% Level", min_value=1, max_value=20)
                self.cr += crdict[cr_level]
                self.hyperstatlist.append("Crit Rate%")
                self.hyperstatamountlist.append(crdict[cr_level])
            # Crit DMG
            cd_choice = hs1.selectbox("Crit DMG%", ["No", "Yes"])
            self.cd_choice = cd_choice
            if cd_choice == "Yes":
                cd_level = hs1.slider("Crit DMG% Level", min_value=1, max_value=20)
                self.cd += cddict[cd_level]
                self.hyperstatlist.append("Crit DMG%")
                self.hyperstatamountlist.append(cddict[cd_level])
            # Boss ATK
            batk_choice = hs2.selectbox("Boss ATK%", ["No", "Yes"])
            self.batk_choice = batk_choice
            if batk_choice == "Yes":
                batk_level = hs2.slider("Boss ATK% Level", min_value=1, max_value=20)
                self.batk += batkdict[batk_level]
                self.hyperstatlist.append("Boss ATK%")
                self.hyperstatamountlist.append(batkdict[batk_level])
            # EXP%
            exp_choice = hs1.selectbox("EXP%", ["No", "Yes"])
            self.exp_choice = exp_choice
            if exp_choice == "Yes":
                exp_level = hs1.slider("EXP% Level", min_value=1, max_value=20)
                self.exp += expdict[exp_level]
                self.hyperstatlist.append("EXP%")
                self.hyperstatamountlist.append(expdict[exp_level])
            # SF
            sf_choice = hs2.selectbox("SF Increase", ["No", "Yes"])
            self.sf_choice = sf_choice
            if sf_choice == "Yes":
                sf_level = hs2.slider("SF Increase Level", min_value=1, max_value=20)
                self.sf += sfdict[sf_level]
                self.hyperstatlist.append("SF Increase Level")
                self.hyperstatamountlist.append(sfdict[sf_level])
            # Party EXP%
            partyexp_choice = hs1.selectbox("Party EXP%", ["No", "Yes"])
            self.partyexp_choice = partyexp_choice
            if partyexp_choice == "Yes":
                partyexp_level = hs1.slider("Party EXP% Level", min_value=1, max_value=20)
                self.partyexp += partyexpdict[partyexp_level]
                self.hyperstatlist.append("Party EXP%")
                self.hyperstatamountlist.append(partyexpdict[partyexp_level])
            # KBK Res
            kbkres_choice = hs2.selectbox("KBK", ["No", "Yes"])
            self.kbkres_choice = kbkres_choice
            if kbkres_choice == "Yes":
                kbkres_level = hs2.slider("KBK Level", min_value=1, max_value=20)
                self.kbkres += kbkresdict[kbkres_level]
                self.hyperstatlist.append("KBK")
                self.hyperstatamountlist.append(kbkresdict[kbkres_level])
            # Fever Duration
            feverduration_choice = hs1.selectbox("Fever Duration Inc", ["No", "Yes"])
            self.feverduration_choice = feverduration_choice
            if feverduration_choice == "Yes":
                feverduration_level = hs1.slider("Fever Duration Inc Level", min_value=1, max_value=20)
                self.feverduration += feverdurationdict[feverduration_level]
                self.hyperstatlist.append("Fever Duration Inc")
                self.hyperstatamountlist.append(feverdurationdict[feverduration_level])
            # Item Buff Duration
            itemduration_choice = hs2.selectbox("Item Buff Duration", ["No", "Yes"])
            self.itemduration_choice = itemduration_choice
            if itemduration_choice == "Yes":
                itemduration_level = hs2.slider("Item Buff Duration Level", min_value=1, max_value=20)
                self.buffdurationinc += itemdurationdict[itemduration_level]
                self.hyperstatlist.append("Item Buff Duration")
                self.hyperstatamountlist.append(itemdurationdict[itemduration_level])
            # Chance for Add. DMG (%,%)
            adddmg_choice = hs1.selectbox("Chance for Add. DMG", ["No", "Yes"])
            self.adddmg_choice = adddmg_choice
            if adddmg_choice == "Yes":
                adddmg_level = hs1.slider("Chance for Add. DMG Level", min_value=1, max_value=20)
                st.write(adddmgdict[adddmg_level][0])
                self.adddmgchance += adddmgdict[adddmg_level][0]
                self.adddmgskilldmg += adddmgdict[adddmg_level][1]
                self.hyperstatlist.append("Chance for Add. DMG")
                self.hyperstatamountlist.append([adddmgdict[adddmg_level][0],adddmgdict[adddmg_level][1]])
            # ATK Ignore Rate
            ignore_choice = hs2.selectbox("ATK Ignore Rate", ["No", "Yes"])
            self.ignore_choice = ignore_choice
            if ignore_choice == "Yes":
                ignore_level = hs2.slider("ATK Ignore Rate Level", min_value=1, max_value=20)
                self.ignore += ignoredict[ignore_level]
                self.hyperstatlist.append("ATK Ignore Rate")
                self.hyperstatamountlist.append(ignoredict[ignore_level])

    def hyperstatlist(self):
        hyperstatlist = self.hyperstatlist
        return hyperstatlist

    def hyperstatamountlist(self):
        hyperstatamountlist = self.hyperstatamountlist
        return hyperstatamountlist

    def ignore(self):
        ignore = self.ignore
        return ignore

    def adddmgchance(self):
        adddmgchance = self.adddmgchance
        return adddmgchance

    def adddmgskilldmg(self):
        adddmgskilldmg = self.adddmgskilldmg
        return adddmgskilldmg

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