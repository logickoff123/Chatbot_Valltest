import random
import math


# Определяем функцию shablon_1
def power(size=100):
    shablon_1 = {}
    shablon_1['i'] = random.randint(1, 101)
    shablon_1['u'] = random.randint(1, 101)
    shablon_1['text'] = 'Вычислите мощность тока, зная, что I = {i} и U = {u}'.format(i=shablon_1["i"],u=shablon_1["u"])
    shablon_1['ans'] = shablon_1['i'] * shablon_1['u']

    return shablon_1


def work(size=100):
    shablon_2 = {}
    shablon_2['p'] = random.randint(1, 101)
    shablon_2['t'] = random.randint(1, 101)
    shablon_2['text'] = 'Определите работу электродвигателя если известно, что его мощность равна {p} и время {t}(мин). Ответ предоставте в кДж(округлите до целых)'.format(p=shablon_2["p"],t=shablon_2["t"])
    shablon_2['ans'] = round((shablon_2['p'] * shablon_2['t'] * 60) / 1000)

    return shablon_2


def current_strength(size=100):
    shablon_3 = {}
    shablon_3['q'] = random.randint(10001, 10101)
    shablon_3['t'] = random.randint(1, 101)
    shablon_3['text'] = 'Определите силу тока, если в цепи протекает заряд {q} А·ч за время {t} секунд. Округлите до двух знаков после запятой'.format(q=shablon_3["q"],t=shablon_3["t"])
    shablon_3['ans'] = round(shablon_3['q'] / (shablon_3['t'] * 3600), 2)

    return shablon_3


def resistance(size=100):
    shablon_4 = {}
    shablon_4['u'] = random.randint(1, 101)
    shablon_4['i'] = random.randint(1, 101)
    shablon_4['text'] = 'Найдите электрическое сопротивление проводника, если при напряжении {u} В на нем протекает ток {i} А. Округлите до двух знаков после запятой'.format(i=shablon_4["i"],u=shablon_4["u"])
    shablon_4['ans'] = round(shablon_4['u'] / shablon_4['i'], 2)

    return shablon_4


def voltage(size=100):
    shablon_5 = {}
    shablon_5['r'] = random.randint(1, 101)
    shablon_5['i'] = random.randint(1, 101)
    shablon_5['text'] = 'Определите напряжение на проводнике, если его сопротивление {r} Ом, а сила тока {i} А'.format(i=shablon_5["i"],r=shablon_5["r"])
    shablon_5['ans'] = shablon_5['r'] * shablon_5['i']

    return shablon_5


def charges_amount(size=100):
    shablon_6 = {}
    shablon_6['t'] = random.randint(1, 101)
    shablon_6['i'] = random.randint(1, 101)
    shablon_6['text'] = 'Сколько зарядов проходит через проводник за {t} секунд, если ток равен {i} А? Ответ разделите на 10 в 17 степени.'.format(i=shablon_6["i"],t=shablon_6["t"])
    shablon_6['ans'] = round(shablon_6['i'] * shablon_6['t'] / (1.6 * pow(10, -19)) / pow(10, 17))

    return shablon_6


def resistance_2(size=100):
    shablon_7 = {}
    shablon_7['l'] = random.randint(10001, 10101)
    shablon_7['s'] = random.randint(1, 101)
    shablon_7['text'] = 'Найдите сопротивление проволоки, если известно, что ее длина равна {l} м, а площадь поперечного сечения составляет {s} мм^2? Округлите до 2 знаков после запятой'.format(s=shablon_7["s"],l=shablon_7["l"])
    shablon_7['ans'] = round((4 * pow(10, -3) * shablon_7['l']) / shablon_7['s'], 2)

    return shablon_7

def current_strength_2(size=100):
    shablon_8 = {}
    shablon_8['r'] = random.randint(1, 101)
    shablon_8['u'] = random.randint(1, 101)
    shablon_8['text'] = 'Определите величину силы тока, протекающего через проводник сопротивлением {r} Ом, если приложенное к нему напряжение составляет {u} В. Округлите до двух знаков после запятой'.format(r=shablon_8["r"],u=shablon_8["u"])
    shablon_8['ans'] = round(shablon_8['u'] / shablon_8['r'], 2)

    return shablon_8

def inductance(size=100):
    shablon_9 = {}
    shablon_9['f'] = random.randint(1, 101)
    shablon_9['c'] = random.randint(1, 101)
    shablon_9['text'] = 'Определите индуктивность катушки, если частота тока {f} Гц, емкость конденсатора {c} Ф и ёмкость катушки примерно равна емкости конденсатора.Умножте на 1000 и округлите до двух знаков после запятой'.format(f=shablon_9["f"],c=shablon_9["c"])
    shablon_9['ans'] = round(1 / (2 * math.pi * shablon_9['f'] * shablon_9['c']) * 1000, 2)

    return shablon_9

def resistance_3(size=100):
    shablon_10 = {}
    shablon_10['r1'] = random.randint(1, 101)
    shablon_10['r2'] = random.randint(1, 101)
    shablon_10['text'] = 'Вычислите сопротивление цепи, в которой последовательно соединены резисторы {r1} Ом и {r2} Ом'.format(r1=shablon_10["r1"],r2=shablon_10["r2"])
    shablon_10['ans'] = shablon_10['r1'] + shablon_10['r2']
    
    return shablon_10
