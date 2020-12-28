from scipy.optimize import minimize
import streamlit as st
import pandas as pd


class Emblemcalculations:
    def __init__(self, nec, character):
        self.nb_poutput = 0
        self.b_poutput = 0
        self.nb_soutput = 0
        self.b_soutput = 0

        char = character.char

        self.cd_normalemb = 20
        self.batk_normalemb = 10
        self.atkp_normalemb = 10

        self.cd_partialemb = 10
        self.batk_partialemb = 5
        self.atkp_partialemb = 5

        self.cd_uniqueemb = 1
        self.batk_uniqueemb = 1
        self.atkp_uniqueemb = 1

        self.cd_legendaryemb = 5
        self.batk_legendaryemb = 5
        self.atkp_legendaryemb = 5

        self.ncdnormalemb = 0
        self.natkpnormalemb = 0
        self.nbatknormalemb = 0

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

        self.normal_emb += nec.normal_emb
        self.partial_emb += nec.partial_emb
        self.unique_acc_emb += nec.unique_acc_emb
        self.legendary_acc_emb += nec.legendary_acc_emb

        # Emblem Stats
        self.emblem_cd += nec.emblem_cd
        self.emblem_batk += nec.emblem_batk
        self.emblem_atkp += nec.emblem_atkp

        # SF Stats
        self.sf += nec.sf

        # Offensive Stats
        self.atk += nec.atk
        self.atkp += nec.atkp
        self.dmg += nec.dmg
        self.batk += nec.batk
        self.platk += nec.platk
        self.cr += nec.cr
        self.cratk += nec.cratk
        self.cd += nec.cd
        self.maxdmg += nec.maxdmg
        self.fd += nec.fd

        # Defensive Stats
        self.pdef += nec.pdef
        self.pdefinc += nec.pdefinc
        self.pdefdec += nec.pdefdec
        self.mdef += nec.mdef
        self.mdefinc += nec.mdefinc
        self.mdefdec += nec.mdefdec
        self.bdef += nec.bdef
        self.pldef += nec.pldef
        self.critres += nec.critres
        self.critdmgres += nec.critdmgres

        # Hit Miss Stats
        self.acc += nec.acc
        self.accp += nec.accp
        self.evd += nec.evd
        self.evdp += nec.evdp
        self.penrate += nec.penrate
        self.block += nec.block
        self.abnormalstatres += nec.abnormalstatres
        self.ignore += nec.ignore

        # HP MP Stats
        self.hp += nec.hp
        self.mp += nec.mp
        self.hpinc += nec.hpinc
        self.mpinc += nec.mpinc
        self.hprec += nec.hprec
        self.mprec += nec.mprec
        self.hprecp += nec.hprecp
        self.mprecp += nec.mprecp
        self.hppotionrecp += nec.hppotionrecp
        self.mppotionrecp += nec.mppotionrecp
        self.buffdurationinc += nec.buffdurationinc

        # Mobility Stats
        self.spd += nec.spd
        self.jmp += nec.jmp
        self.kbkres += nec.kbkres

        # Misc Stats
        self.exp += nec.exp
        self.dr += nec.dr
        self.meso += nec.meso
        self.glincrease += nec.glincrease
        self.partyexp += nec.partyexp
        self.feverchargeinc += nec.feverchargeinc
        self.feverduration += nec.feverduration
        self.maxfeverchance += nec.maxfeverchance

        # Shadow Partner Stats
        self.spmulti += nec.spmulti

        # Set Stats
        self.mempsetcount += nec.mempsetcount
        self.aempsetcount += nec.aempsetcount
        self.necrosetcount += nec.necrosetcount
        self.fafsetcount += nec.fafsetcount
        self.bosssetcount += nec.bosssetcount
        self.commandersetcount += nec.commandersetcount

        # Flame Stats
        self.atklinecount += nec.atklinecount
        self.crlinecount += nec.crlinecount
        self.cdlinecount += nec.cdlinecount

        self.pname = char.pname
        self.pskilldmg = char.pskilldmg
        self.phitcount = char.phitcount
        self.pchance = char.pchance
        self.patkp = char.patkp
        self.pdmg = char.pdmg
        self.pbatk = char.pbatk
        self.pplatk = char.pplatk
        self.pcr = char.pcr
        self.pcratk = char.pcratk
        self.pcd = char.pcd
        self.pmaxdmg = char.pmaxdmg
        self.pfd = char.pfd

        self.sname = char.sname
        self.sskilldmg = char.sskilldmg
        self.shitcount = char.shitcount
        self.schance = char.schance
        self.satkp = char.satkp
        self.sdmg = char.sdmg
        self.sbatk = char.sbatk
        self.splatk = char.splatk
        self.scr = char.scr
        self.scratk = char.scratk
        self.scd = char.scd
        self.smaxdmg = char.smaxdmg
        self.sfd = char.sfd

        self.tname = char.tname
        self.tskilldmg = char.tskilldmg
        self.thitcount = char.thitcount
        self.tchance = char.tchance
        self.tatkp = char.tatkp
        self.tdmg = char.tdmg
        self.tbatk = char.tbatk
        self.tplatk = char.tplatk
        self.tcr = char.tcr
        self.tcratk = char.tcratk
        self.tcd = char.tcd
        self.tmaxdmg = char.tmaxdmg
        self.tfd = char.tfd

        with st.beta_expander("Emblem Calculations"):
            _, cres1, _ = st.beta_columns([0.02, 0.96, 0.02])
            cres = cres1.number_input("Input Boss Crit Res Here, (For No Crit Res Put 0")
            maxdmginc = cres1.number_input("Input Extra Max Dmg Here")
            self.maxdmg += maxdmginc
            if self.cr >= 100: # If cr above 100, revert back to 100 and minus crit res
                self.croverflow = 100 - cres
            elif self.cr - cres <= 0: # If after subtraction is below 0, revert back to 0
                self.croverflow = 0
            else:
                self.croverflow = self.cr - cres
            def pobjective(x):
                cd = x[0] * self.cd_normalemb + x[3]*self.cd_uniqueemb + x[6]*self.cd_legendaryemb + x[9]*self.cd_partialemb
                atkp = x[1] * self.atkp_normalemb + x[4]*self.atkp_uniqueemb + x[7]*self.atkp_legendaryemb + x[10]*self.atkp_partialemb
                batk = x[2] * self.batk_normalemb + x[5]*self.batk_uniqueemb + x[8]*self.batk_legendaryemb + x[11]*self.batk_partialemb
                #cdatt = (self.atk * (1 + (self.dmg + self.pdmg)/100) * (1 + (self.fd + self.pfd)/100) * (1 + ((self.atkp + atkp + self.patkp) / 100) + ((self.pskilldmg / 100) * ((self.batk + batk + self.pbatk) / 100))) * (1 + ((self.cd + cd + self.pcd) / 100) + 0.2))
                #ncdatt = (self.atk * (1 + (self.dmg + self.pdmg)/100) * (1 + (self.fd + self.pfd)/100) * (1 + ((self.atkp + atkp + self.patkp) / 100) + ((self.pskilldmg / 100) * ((self.batk + batk + self.pbatk) / 100))))
                obj = -((min((self.atk * (1 + (self.dmg + self.pdmg)/100) * (1 + (self.fd + self.pfd)/100) * (1 + ((self.atkp + atkp + self.patkp) / 100) + ((self.pskilldmg / 100) * ((self.batk + batk + self.pbatk) / 100))) * (1 + ((self.cd + cd + self.pcd) / 100) + 0.2))
                , self.maxdmg) * (self.croverflow/100)) + (min((self.atk * (1 + (self.dmg + self.pdmg)/100) * (1 + (self.fd + self.pfd)/100) * (1 + ((self.atkp + atkp + self.patkp) / 100) + ((self.pskilldmg / 100) * ((self.batk + batk + self.pbatk) / 100))))
                , self.maxdmg) * (1 - (self.croverflow/100))))
                return obj

            def constraint1(x):
                sum = self.normal_emb
                sum = sum - x[0] - x[1] - x[2]
                return sum

            def constraint2(x):
                sum = self.unique_acc_emb
                sum = sum - x[3] - x[4] - x[5]
                return sum

            def constraint3(x):
                sum = self.legendary_acc_emb
                sum = sum - x[6] - x[7] - x[8]
                return sum

            def constraint4(x):
                sum = self.partial_emb
                sum = sum - x[9] - x[10] - x[11]
                return sum

            cd_normalamount = self.normal_emb * 20
            cd_uniqueamount = self.unique_acc_emb * 1
            cd_legendaryamount = self.legendary_acc_emb * 5
            cd_partialamount = self.partial_emb * 10
            atkp_normalamount = self.normal_emb * 10
            atkp_uniqueamount = self.unique_acc_emb * 1
            atkp_legendaryamount = self.legendary_acc_emb * 5
            atkp_partialamount = self.partial_emb * 5
            batk_normalamount = self.normal_emb * 10
            batk_uniqueamount = self.unique_acc_emb * 1
            batk_legendaryamount = self.legendary_acc_emb * 5
            batk_partialamount = self.partial_emb * 5

            x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            cd_normalbound = (0, cd_normalamount)
            atkp_normalbound = (0, atkp_normalamount)
            batk_normalbound = (0, batk_normalamount)
            cd_uniquebound = (0, cd_uniqueamount)
            atkp_uniquebound = (0, atkp_uniqueamount)
            batk_uniquebound = (0, batk_uniqueamount)
            cd_legendarybound = (0, cd_legendaryamount)
            atkp_legendarybound = (0, atkp_legendaryamount)
            batk_legendarybound = (0, batk_legendaryamount)
            cd_partialbound = (0, cd_partialamount)
            atkp_partialbound = (0, atkp_partialamount)
            batk_partialbound = (0, batk_partialamount)
            bnds = (cd_normalbound, atkp_normalbound, batk_normalbound, cd_uniquebound, atkp_uniquebound, batk_uniquebound,
                    cd_legendarybound, atkp_legendarybound, batk_legendarybound, cd_partialbound, atkp_partialbound, batk_partialbound)
            cons = [{'type': 'eq', 'fun': constraint1}, {'type': 'eq', 'fun': constraint2},
                    {'type': 'eq', 'fun': constraint3}, {'type': 'eq', 'fun': constraint4}]
            sol = minimize(pobjective, x0, method='SLSQP', bounds=bnds, constraints=cons)

            ncdnormalemb = int(round(sol.x[0]))
            natkpnormalemb = int(round(sol.x[1]))
            nbatknormalemb = int(round(sol.x[2]))
            ncduniqueemb = int(round(sol.x[3]))
            natkpuniqueemb = int(round(sol.x[4]))
            nbatkuniqueemb = int(round(sol.x[5]))
            ncdlegendaryemb = int(round(sol.x[6]))
            natkplegendaryemb = int(round(sol.x[7]))
            nbatklegendaryemb = int(round(sol.x[8]))
            ncdpartialemb = int(round(sol.x[9]))
            natkppartialemb = int(round(sol.x[10]))
            nbatkpartialemb = int(round(sol.x[11]))

            self.ncdnormalemb = ncdnormalemb
            self.natkpnormalemb = natkpnormalemb
            self.nbatknormalemb = nbatknormalemb

            self.ncduniqueemb = ncduniqueemb
            self.natkpuniqueemb = natkpuniqueemb
            self.nbatkuniqueemb = nbatkuniqueemb

            self.ncdlegendaryemb = ncdlegendaryemb
            self.natkplegendaryemb = natkplegendaryemb
            self.nbatklegendaryemb = nbatklegendaryemb

            self.ncdpartialemb = ncdpartialemb
            self.natkppartialemb = natkppartialemb
            self.nbatkpartialemb = nbatkpartialemb

            self.embatkp = (self.atkp_normalemb * self.natkpnormalemb) + (self.atkp_uniqueemb * self.natkpuniqueemb) + \
                           (self.atkp_legendaryemb * self.natkplegendaryemb) + (self.atkp_partialemb * self.natkppartialemb)
            self.embbatk = (self.batk_normalemb * self.nbatknormalemb) + (self.batk_uniqueemb * self.nbatkuniqueemb) + \
                           (self.batk_legendaryemb * self.nbatklegendaryemb) + (self.batk_partialemb * self.nbatkpartialemb)
            self.embcd = (self.cd_normalemb * self.ncdnormalemb) + (self.cd_uniqueemb * self.ncduniqueemb) + \
                         (self.cd_legendaryemb * self.ncdlegendaryemb) + (self.cd_partialemb * self.ncdpartialemb)

            def nb_nc_output(atk, dmg, hdmg, atkp, hatkp, embatkp, skilldmg, fd, hfd):
                output = int(round(atk * (1 + ((dmg + hdmg) / 100)) * (1 + ((atkp + hatkp + embatkp) / 100)) * (1 + ((fd + hfd) / 100)) \
                         * (skilldmg / 100), 0))
                return output

            def nb_c_output(atk, dmg, hdmg, atkp, hatkp, embatkp, cd, embcd, hcd, skilldmg, fd, hfd):
                output = int(round(atk * (1 + ((dmg + hdmg) / 100)) * (1 + ((atkp + hatkp + embatkp) / 100)) * (1 + ((fd + hfd) / 100)) \
                         * (1 + ((cd + embcd + hcd) / 100) + 0.2) * (skilldmg / 100), 0))
                return output

            def b_nc_output(atk, dmg, hdmg, atkp, hatkp, embatkp, batk, hbatk, embbatk, skilldmg, fd, hfd):
                output = int(round(atk * (1 + ((dmg + hdmg) / 100)) * (1 + ((atkp + hatkp + embatkp) / 100) + ((skilldmg / 100) * ((batk + hbatk + embbatk)/100))) * (1 + ((fd + hfd) / 100)) \
                          * (skilldmg / 100), 0))
                return output

            def b_c_output(atk, dmg, hdmg, atkp, hatkp, embatkp, batk, hbatk, embbatk, cd, embcd, hcd, skilldmg, fd, hfd):
                output = int(round(atk * (1 + ((dmg + hdmg) / 100)) * (1 + ((atkp + hatkp + embatkp) / 100) + ((skilldmg / 100) * ((batk + hbatk + embbatk)/100))) * (1 + ((fd + hfd) / 100)) \
                          * (1 + ((cd + embcd + hcd) / 100) + 0.2) * (skilldmg / 100), 0))
                return output

        # Primary Skill
            # Non Boss Non Crit
            self.nb_nc_poutput = nb_nc_output(self.atk, self.dmg, self.pdmg, self.atkp, self.patkp, self.embatkp, self.pskilldmg, self.fd, self.pfd)

            # Non Boss Crit
            self.nb_c_poutput = nb_c_output(self.atk, self.dmg, self.pdmg, self.atkp, self.patkp, self.embatkp, self.cd, self.embcd, self.pcd, self.pskilldmg, self.fd, self.pfd)

            # Non Boss Average
            self.nb_poutput = int(
                round((((self.nb_c_poutput * self.croverflow) + ((100.0 - self.croverflow) * self.nb_nc_poutput)) / 100),
                      0))

            # Boss Non Crit
            self.b_nc_poutput = b_nc_output(self.atk, self.dmg, self.pdmg, self.atkp, self.patkp, self.embatkp, self.batk, self.pbatk, self.embbatk, self.pskilldmg, self.fd, self.pfd)

            # Boss Crit
            self.b_c_poutput = b_c_output(self.atk, self.dmg, self.pdmg, self.atkp, self.patkp, self.embatkp, self.batk, self.pbatk, self.embbatk, self.cd, self.embcd, self.pcd, self.pskilldmg, self.fd, self.pfd)

            # Boss Average
            self.b_poutput = int(
                round((((self.b_c_poutput * self.croverflow) + ((100.0 - self.croverflow) * self.b_nc_poutput)) / 100), 0))

            primaryoutput = [self.pname, self.nb_nc_poutput, self.nb_c_poutput, self.nb_poutput, self.b_nc_poutput, self.b_c_poutput, self.b_poutput]

        # Secondary Skill
            # Non Boss Non Crit
            self.nb_nc_soutput = nb_nc_output(self.atk, self.dmg, self.sdmg, self.atkp, self.satkp, self.embatkp, self.sskilldmg, self.fd, self.sfd)

            # Non Boss Crit
            self.nb_c_soutput = nb_c_output(self.atk, self.dmg, self.sdmg, self.atkp, self.satkp, self.embatkp, self.cd, self.embcd, self.scd, self.sskilldmg, self.fd, self.sfd)

            # Non Boss Average
            self.nb_soutput = int(round(((self.nb_c_soutput * self.croverflow) + ((100.0 - self.croverflow) * self.nb_nc_soutput)) / 100))

            # Boss Non Crit
            self.b_nc_soutput = b_nc_output(self.atk, self.dmg, self.sdmg, self.atkp, self.satkp, self.embatkp, self.batk, self.sbatk, self.embbatk, self.sskilldmg, self.fd, self.sfd)

            # Boss Crit
            self.b_c_soutput = b_c_output(self.atk, self.dmg, self.sdmg, self.atkp, self.satkp, self.embatkp, self.batk, self.sbatk, self.embbatk, self.cd, self.embcd, self.scd, self.sskilldmg, self.fd, self.sfd)

            # Boss Average
            self.b_soutput = int(round((((self.b_c_soutput * self.croverflow) + ((100.0 - self.croverflow) * self.b_nc_soutput)) / 100), 0))

            secondaryoutput = [self.sname, self.nb_nc_soutput, self.nb_c_soutput, self.nb_soutput, self.b_nc_soutput, self.b_c_soutput,
                             self.b_soutput]

        # Tertiary Skill
            # Non Boss Non Crit
            self.nb_nc_toutput = nb_nc_output(self.atk, self.dmg, self.tdmg, self.atkp, self.tatkp, self.embatkp,
                                              self.tskilldmg, self.fd, self.tfd)

            # Non Boss Crit
            self.nb_c_toutput = nb_c_output(self.atk, self.dmg, self.tdmg, self.atkp, self.tatkp, self.embatkp, self.cd,
                                            self.embcd, self.tcd, self.tskilldmg, self.fd, self.tfd)

            # Non Boss Average
            self.nb_toutput = int(round(((self.nb_c_toutput * self.croverflow) + ((100.0 - self.croverflow) * self.nb_nc_toutput)) / 100))

            # Boss Non Crit
            self.b_nc_toutput = b_nc_output(self.atk, self.dmg, self.tdmg, self.atkp, self.tatkp, self.embatkp, self.batk,
                                            self.tbatk, self.embbatk, self.tskilldmg, self.fd, self.tfd)

            # Boss Crit
            self.b_c_toutput = b_c_output(self.atk, self.dmg, self.tdmg, self.atkp, self.tatkp, self.embatkp, self.batk,
                                          self.tbatk, self.embbatk, self.cd, self.embcd, self.tcd, self.tskilldmg, self.fd,
                                          self.tfd)

            # Boss Average
            self.b_toutput = int(round((((self.b_c_toutput * self.croverflow) + ((100.0 - self.croverflow) * self.b_nc_toutput)) / 100), 0))

            tertiaryoutput = [self.tname, self.nb_nc_toutput, self.nb_c_toutput, self.nb_toutput, self.b_nc_toutput, self.b_c_toutput,
                             self.b_toutput]

            self.atkp += self.embatkp
            self.batk += self.embbatk
            self.cd += self.embcd

            outputdf = pd.DataFrame(columns = ["Skill Name", "Non-Boss Non-Crit", "Non-Boss Crit", "Non-Boss Average", "Boss Non-Crit", "Boss Crit", "Boss Average"])
            outputdf.loc[len(outputdf)] = primaryoutput
            outputdf.loc[len(outputdf)] = secondaryoutput
            outputdf.loc[len(outputdf)] = tertiaryoutput

            cres1.table(outputdf)

