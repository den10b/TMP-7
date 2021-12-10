from tkinter import *
from tkinter.ttk import *

AMOUNT = 0


class Zodiac:
    def __init__(self, FN, SN, SI, DT):
        self.first_name = FN
        self.second_name = SN
        self.sign = SI
        self.date = DT


signs = {
    "Aries": 1,
    "Taurus": 2,
    "Gemini": 3,
    "Cancer": 4,
    "Leo": 5,
    "Virgo": 6,
    "Libra": 7,
    "Scorpio": 8,
    "Sagittarius": 9,
    "Capricorn": 10,
    "Aquarius": 11,
    "Pisces": 12
}

ppl = []
for i in range(8):
    sign = signs.keys().__str__().split(',')[i]
    if i == 0:
        sign = sign.split('[')[1]
    if i == 11:
        sign = sign.split(']')[0]
    sign = sign.replace('\'', "")
    men = Zodiac("First" + i.__str__(), "Second" + i.__str__(), sign, [(i + 1) * 3 - 1, i + 1, 1999 - i])
    ppl.append(men)
signnames = []
for i in range(12):
    sign = signs.keys().__str__().split(',')[i]
    if i == 0:
        sign = sign.split('[')[1]
    if i == 11:
        sign = sign.split(']')[0]
    sign = sign.replace('\'', "")
    sign = sign.strip()
    signnames.append(sign)

lables = []


def zodclick(month):
    for el in lables:
        el.grid_remove()
    massiv = []
    f = open('6laba.txt', 'r+', encoding='UTF-8')
    al = f.readlines()
    for stroka in al:
        spl = stroka.split(' ')
        spl[3] = spl[3].split('[')[1].split(',')[0]
        spl[4] = spl[4].split(',')[0]
        spl[5] = spl[5].split(']')[0]
        massiv.append(Zodiac(spl[0], spl[1], spl[2], [int(spl[3]), int(spl[4]), int(spl[5])]))
    check = True
    i = 3
    z = 0
    AMOUNT = i
    lables.clear()
    for men in massiv:
        if men.date[1] == month:
            lables.append(Label(window, text=men.first_name))
            lables[z].grid(column=0, row=i)
            z += 1
            lables.append(Label(window, text=men.second_name))
            lables[z].grid(column=1, row=i)
            z += 1
            lables.append(Label(window, text=men.sign))
            lables[z].grid(column=2, row=i)
            z += 1
            lables.append(Label(window, text=men.date.__str__()))
            lables[z].grid(column=3, row=i)
            z += 1
            i += 1
            AMOUNT += 1
            check = False
    if check:
        print("Таких нет")


def printall():
    for el in lables:
        el.grid_remove()
    massiv = []
    f = open('6laba.txt', 'r+', encoding='UTF-8')
    al = f.readlines()
    for stroka in al:
        spl = stroka.split(' ')
        spl[3] = spl[3].split('[')[1].split(',')[0]
        spl[4] = spl[4].split(',')[0]
        spl[5] = spl[5].split(']')[0]
        massiv.append(Zodiac(spl[0], spl[1], spl[2], [int(spl[3]), int(spl[4]), int(spl[5])]))
    i = 3
    z = 0
    lables.clear()
    for men in massiv:
        lables.append(Label(window, text=men.first_name))
        lables[z].grid(column=0, row=i)
        z += 1
        lables.append(Label(window, text=men.second_name))
        lables[z].grid(column=1, row=i)
        z += 1
        lables.append(Label(window, text=men.sign))
        lables[z].grid(column=2, row=i)
        z += 1
        lables.append(Label(window, text=men.date.__str__()))
        lables[z].grid(column=3, row=i)
        z += 1
        i += 1


def write(FN, SN, SI, DT):
    if FN == "":
        FN = "FirstName"
    if SN == "":
        SN = "SecondName"
    chel = Zodiac(FN, SN, SI, DT)
    massiv = [chel]
    intmass = [signs[chel.sign]]
    f = open('6laba.txt', 'r+', encoding='UTF-8')
    al = f.readlines()
    for stroka in al:
        spl = stroka.split(' ')
        spl[3] = spl[3].split('[')[1].split(',')[0]
        spl[4] = spl[4].split(',')[0]
        spl[5] = spl[5].split(']')[0]
        massiv.append(Zodiac(spl[0], spl[1], spl[2], [int(spl[3]), int(spl[4]), int(spl[5])]))
        intmass.append(signs[spl[2]])
    k = len(massiv)
    for i in range(k - 1):
        for j in range(k - i - 1):
            if intmass[j] > intmass[j + 1]:
                intmass[j], intmass[j + 1] = intmass[j + 1], intmass[j]
                massiv[j], massiv[j + 1] = massiv[j + 1], massiv[j]
    f.close()
    f = open('6laba.txt', 'w', encoding='UTF-8')
    for men in massiv:
        strr = str(
            men.first_name.__str__() + " " + men.second_name.__str__() + " " + men.sign.__str__() + " " + men.date.__str__() + "\n")
        f.write(strr)
    f.close()


f = open('6laba.txt', 'w', encoding='UTF-8')
for men in ppl:
    strr = str(
        men.first_name.__str__() + " " + men.second_name.__str__() + " " + men.sign.__str__().strip() + " " + men.date.__str__() + "\n")
    f.write(strr)
f.close()

window = Tk()
window.title("6 Лабораторная")
tx_im = Label(window, text="Имя")
tx_im.grid(column=0, row=0)
en_im = Entry(window, width=10)
en_im.grid(column=0, row=1)

tx_fm = Label(window, text="Фамилия")
tx_fm.grid(column=1, row=0)
en_fm = Entry(window, width=10)
en_fm.grid(column=1, row=1)

tx_fm = Label(window, text="День")
tx_fm.grid(column=2, row=0)
Dbox = Combobox(window)
Dbox['values'] = list(range(1, 31))
Dbox.current(0)
Dbox.grid(column=2, row=1)

tx_fm = Label(window, text="Месяц")
tx_fm.grid(column=3, row=0)
comboM = Combobox(window)
comboM['values'] = ["Январь", "Февраль", "Март", "Апрель ", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                    "Ноябрь", "Декабрь"]
comboM.current(0)
comboM.grid(column=3, row=1)

tx_fm = Label(window, text="Год")
tx_fm.grid(column=4, row=0)
comboY = Combobox(window)
comboY['values'] = list(range(1900, 2012))
comboY.current(100)
comboY.grid(column=4, row=1)

tx_zd = Label(window, text="Знак Зодиака:")
tx_zd.grid(column=5, row=0)
Zbox = Combobox(window)
Zbox['values'] = signnames
Zbox.current(0)
Zbox.grid(column=5, row=1)

btn = Button(window, text="Занести в файл",
             command=lambda: write(en_fm.get().replace(' ', ""), en_im.get().replace(' ', ""), Zbox.get(),
                                   [int(Dbox.get().replace('\'', "")),
                                    comboM.current() + 1,
                                    int(comboY.get().replace('\'', ""))]))
btn.grid(column=0, row=2)
comboM2 = Combobox(window)
comboM2['values'] = ["Январь", "Февраль", "Март", "Апрель ", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                     "Ноябрь", "Декабрь"]
comboM2.current(0)
comboM2.grid(column=1, row=2)

btn2 = Button(window, text="В этом месяце", command=lambda: zodclick(comboM2.current() + 1))
btn2.grid(column=2, row=2)

btn2 = Button(window, text="Вывести всех", command=lambda: printall())
btn2.grid(column=3, row=2)

window.geometry('850x250')
window.mainloop()
