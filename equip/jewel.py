import streamlit as st


class Jewel:
    def __init__(self, char_type):
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

        with st.beta_expander("Jewels"):
            _, jewel1, _, jewel2, _, jewel3, _ = st.beta_columns([0.02, 0.305, 0.02, 0.305, 0.02, 0.305, 0.02])
            rank = jewel1.selectbox("Choose Jewel Rank", ["S", "SS", "SSS"])
            self.rank = rank
            colour = jewel2.selectbox("Choose Jewel Colour", ["Red", "Blue", "Green", "Yellow", "Purple"])
            if colour == "Red":
                stat = jewel1.selectbox("Choose Jewel Type", ["Phy ATK (Red)", "Mag ATK (Red)", "JMP (RED)", "Crit DMG Res (Red)"])
            elif colour == "Blue":
                stat = jewel1.selectbox("Choose Jewel Type", ["Phy DMG (Blue)", "ACC (Blue)", "SPD (Blue)", "Mag DEF (Blue)"])
            elif colour == "Green":
                stat = jewel1.selectbox("Choose Jewel Type", ["Mag DMG (Green)", "Crit DMG (Green)", "EVD (Green)", "Phy DEF (Green)"])
            elif colour == "Yellow":
                stat = jewel1.selectbox("Choose Jewel Type", ["EXP (Yellow)", "PEN Rate (Yellow)", "KBK Res (Yellow)", "Drop Rate (Yellow)"])
            elif colour == "Purple":
                stat = jewel1.selectbox("Choose Jewel Type", ["Crit Rate (Purple)", "Boss ATK (Purple)", "Boss DEF (Purple)", "Block (Purple)"])
            self.stat = stat
            if colour == "Red":
                if rank == "S":
                    self.atk += 200
                    self.jmp += 5
                    self.critres += 2
                elif rank == "SS":
                    self.atk += 300
                    self.jmp += 10
                    self.critres += 4
                elif rank == "SSS":
                    self.atk += 400
                    self.jmp += 15
                    self.critres += 5
            elif colour == "Blue":
                if rank == "S":
                    self.mdef += 250
                    self.spd += 2
                    if char_type == "PHYSICAL":
                        self.dmg += 3
                elif rank == "SS":
                    self.mdef += 500
                    self.accp += 3
                    self.spd += 4
                    if char_type == "PHYSICAL":
                        self.dmg += 5
                elif rank == "SSS":
                    self.mdef += 750
                    self.accp += 4
                    self.spd += 5
                    if char_type == "PHYSICAL":
                        self.dmg += 8
            elif colour == "Green":
                if rank == "S":
                    self.pdef += 250
                    self.spd += 2
                    if char_type == "MAGICAL":
                        self.dmg += 3
                elif rank == "SS":
                    self.pdef += 500
                    self.accp += 3
                    self.spd += 4
                    if char_type == "MAGICAL":
                        self.dmg += 5
                elif rank == "SSS":
                    self.pdef += 750
                    self.accp += 4
                    self.spd += 5
                    if char_type == "MAGICAL":
                        self.dmg += 8
            elif colour == "Yellow":
                if rank == "S":
                    self.kbkres += 100
                    self.exp += 1.5
                    self.dr += 2
                elif rank == "SS":
                    self.kbkres += 200
                    self.exp += 3
                    self.dr += 3
                elif rank == "SSS":
                    self.kbkres += 300
                    self.exp += 4.5
                    self.dr += 5
            elif colour == "Purple":
                if rank == "S":
                    self.batk += 2
                    self.bdef += 2
                    self.cd += 2
                elif rank == "SS":
                    self.batk += 3
                    self.bdef += 3
                    self.cr += 2
                    self.cd += 3
                elif rank == "SSS":
                    self.batk += 5
                    self.bdef += 5
                    self.cr += 2
                    self.cd += 4

            if stat == "Phy ATK (Red)":
                if char_type == "PHYSICAL":
                    if rank == "S":
                        self.atk += 43*5
                    elif rank == "SS":
                        # Base
                        self.atk += 60*5
                    elif rank == "SSS":
                        self.atk += 80*5
            elif stat == "Mag ATK (Red)":
                if char_type == "MAGICAL":
                    if rank == "S":
                        self.atk += 43*5
                    elif rank == "SS":
                        # Base
                        self.atk += 60*5
                    elif rank == "SSS":
                        self.atk += 80*5
            elif stat == "JMP (Red)":
                if rank == "S":
                    self.jmp += 1.5*5
                elif rank == "SS":
                    self.jmp += 2*5
                elif rank == "SSS":
                    self.jmp += 2.5*5
            elif stat == "Crit DMG Res (Red)":
                if rank == "S":
                    self.critdmgres += 0.6*5
                elif rank == "SS":
                    self.critdmgres += 0.8*5
                elif rank == "SSS":
                    self.critdmgres += 1*5
            elif stat == "Phy DMG (Blue)":
                if char_type == "PHYSICAL":
                    if rank == "S":
                        self.dmg += 0.5*5
                    elif rank == "SS":
                        self.dmg += 0.7*5
                    elif rank == "SSS":
                        self.dmg += 1*5
            elif stat == "ACC (Blue)":
                if rank == "S":
                    self.accp += 1.2*5
                elif rank == "SS":
                    self.accp += 1.6*5
                elif rank == "SSS":
                    self.accp += 2.1*5
            elif stat == "SPD (Blue)":
                if rank == "S":
                    self.spd += 1.5*5
                elif rank == "SS":
                    self.spd += 2*5
                elif rank == "SSS":
                    self.spd += 2.5*5
            elif stat == "Mag DEF (Blue)":
                if rank == "S":
                    self.mdef += 103*5
                elif rank == "SS":
                    self.mdef += 143*5
                elif rank == "SSS":
                    self.mdef += 200*5
            elif stat == "Mag DMG (Green)":
                if char_type == "MAGICAL":
                    if rank == "S":
                        self.dmg += 0.5*5
                    elif rank == "SS":
                        self.dmg += 0.7*5
                    elif rank == "SSS":
                        self.dmg += 1*5
            elif stat == "Crit DMG (Green)":
                if rank == "S":
                    self.cd += 0.5*5
                elif rank == "SS":
                    self.cd += 0.8*5
                elif rank == "SSS":
                    self.cd += 1*5
            elif stat == "EVD (Green)":
                if rank == "S":
                    self.evdp += 1.2*5
                elif rank == "SS":
                    self.evdp += 1.6*5
                elif rank == "SSS":
                    self.evdp += 2.1*5
            elif stat == "Phy DEF (Green)":
                if rank == "S":
                    self.pdef += 103*5
                elif rank == "SS":
                    self.pdef += 143*5
                elif rank == "SSS":
                    self.pdef += 200*5
            elif stat == "KBK Res (Yellow)":
                if rank == "S":
                    self.kbkres += 4*5
                elif rank == "SS":
                    self.kbkres += 6*5
                elif rank == "SSS":
                    self.kbkres += 8*5
            elif stat == "EXP (Yellow)":
                if rank == "S":
                    self.exp += 1.8*5
                elif rank == "SS":
                    self.exp += 2.4*5
                elif rank == "SSS":
                    self.exp += 3.1*5
            elif stat == "Drop Rate (Yellow)":
                if rank == "S":
                    self.dr += 1*5
                elif rank == "SS":
                    self.dr += 1.3*5
                elif rank == "SSS":
                    self.dr += 1.6*5
            elif stat == "PEN Rate (Yellow)":
                if rank == "S":
                    self.penrate += 1.4*5
                elif rank == "SS":
                    self.penrate += 2*5
                elif rank == "SSS":
                    self.penrate += 3.8*5
            elif stat == "Crit Rate (Purple)":
                if rank == "S":
                    self.cr += 0.5*5
                elif rank == "SS":
                    self.cr += 0.6*5
                elif rank == "SSS":
                    self.cr += 0.7*5
            elif stat == "Boss ATK (Purple)":
                if rank == "S":
                    self.batk += 0.7*5
                elif rank == "SS":
                    self.batk += 1*5
                elif rank == "SSS":
                    self.batk += 1.3*5
            elif stat == "Boss DEF (Purple)":
                if rank == "S":
                    self.bdef += 0.6*5
                elif rank == "SS":
                    self.bdef += 0.8*5
                elif rank == "SSS":
                    self.bdef += 1*5
            elif stat == "Block (Purple)":
                if rank == "S":
                    self.block += 1.2*5
                elif rank == "SS":
                    self.block += 1.6*5
                elif rank == "SSS":
                    self.block += 2.1*5
