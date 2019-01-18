import requests

"""r = requests.get('http://www.pogodaiklimat.ru/weather.php', params={'id':'29635', 'bday':'1', 'fday':'3', 'amonth':'12', 'ayear':'2018', 'bot':'2'})
r.encoding = 'utf-8'
t = r.text
t = t[t.find('</tr'):t.find('</table')] # выпиливаем нужное из таблицы html файла
t = t.strip('</tr>').strip('\n').split('</tr>')
del t[-1]
"""
listOfParam = ['Час по местному времени', 'День.Месяц', 'Направление ветра', 'V ветра, м/с', 't воздуха, `C', 'Влажность. %',
                'Давление воздуха на высоте места измерения над уровнем моря, мм рт. ст.', 'min t воздуха, `C', 'max t воздуха, `C',
                'Количество осадков за последние 12ч, мм', 'Высота снежного покрова, см', 'Состояние снега, величина покрытия местности в баллах']
tableInString = ['<tr height="30" bgColor=#ffffff>\n<td class=black><b>00</b></td>\n<td class=black><b>1.12</b></td>\n<td class="wind_w">З</td>\n<td class="ff_3">3</td>\n<td class="vis_2">20 км</td>\n<td class="w_"> <i>{ливн. осадки}</i></td>\n<td class="vis_8">8/8 600 м<br>[Cb cap]</td>\n<td class="temp_30"><nobr>-21.0</nobr></td>\n<td class="temp_29"><nobr>-24.7</nobr></td>\n<td class="temp_38">72</td>\n<td class="temp_27"><nobr>-29</nobr></td>\n<td class="temp_27"><nobr>-29</nobr></td>\n<td class="black" bgcolor=""></td>\n<td class="temp_37">1026.4</td>\n<td class="black">1009.8</td>\n<td class="temp_30"><nobr>-21.0</nobr></td>\n<td class="temp_"><nobr></nobr></td>\n<td title="за 12 ч." class="temp_39">1</td>\n<td class="temp_"></td>\n<td title="сухой снег 10 баллов" class="snow_9">36</td>\n', '\n<tr height="30" bgColor=#daf1f7>\n<td class=black><b>03</b></td>\n<td class=black><b>1.12</b></td>\n<td class="wind_sw">ЮЗ</td>\n<td class="ff_2">2</td>\n<td class="vis_3">10 км</td>\n<td class="w_sn">слаб. снег</td>\n<td class="vis_10">10 баллов</td>\n<td class="temp_30"><nobr>-22.1</nobr></td>\n<td class="temp_28"><nobr>-25.8</nobr></td>\n<td class="temp_38">72</td>\n<td class="temp_28"><nobr>-28</nobr></td>\n<td class="temp_28"><nobr>-28</nobr></td>\n<td class="black" bgcolor=""></td>\n<td class="temp_36">1031.9</td>\n<tdclass="black">1014.7</td>\n<td class="temp_30"><nobr>-22.1</nobr></td>\n<td class="temp_"><nobr></nobr></td>\n<td title="" class="temp_"></td>\n<td class="temp_"></td>\n<td title="" class="snow_"></td>\n', '\n<tr height="30" bgColor=#ffffff>\n<td class=black><b>06</b></td>\n<td class=black><b>1.12</b></td>\n<td class="wind_sw">ЮЗ</td>\n<td class="ff_3">3</td>\n<td class="vis_2">20 км</td>\n<td class="w_"> <i>{снег}</i></td>\n<td class="vis_10">10/0<br>[As trans]</td>\n<td class="temp_30"><nobr>-21.7</nobr></td>\n<td class="temp_28"><nobr>-25.9</nobr></td>\n<td class="temp_38">69</td>\n<td class="temp_27"><nobr>-30</nobr></td>\n<td class="temp_27"><nobr>-29</nobr></td>\n<td class="black" bgcolor=""></td>\n<td class="temp_35">1033.1</td>\n<td class="black">1016.3</td>\n<td class="temp_"><nobr></nobr></td>\n<td class="temp_"><nobr></nobr></td>\n<td title="" class="temp_"></td>\n<td class="temp_"></td>\n<td title="" class="snow_"></td>\n', '\n<tr height="30" bgColor=#daf1f7>\n<td class=black><b>09</b></td>\n<td class=black><b>1.12</b></td>\n<td class="wind_sw">ЮЗ</td>\n<td class="ff_2">2</td>\n<td class="vis_3">10 км</td>\n<td class="w_sn">слаб. снег</td>\n<td class="vis_10">10/0<br>[As op]</td>\n<td class="temp_30"><nobr>-20.4</nobr></td>\n<td class="temp_29"><nobr>-23.9</nobr></td>\n<td class="temp_38">73</td>\n<td class="temp_28"><nobr>-26</nobr></td>\n<td class="temp_28"><nobr>-26</nobr></td>\n<td class="black" bgcolor=""></td>\n<td class="temp_35">1034.2</td>\n<td class="black">1017.5</td>\n<td class="temp_"><nobr></nobr></td>\n<td class="temp_"><nobr></nobr></td>\n<td title="" class="temp_"></td>\n<td class="temp_"></td>\n<td title="" class="snow_"></td>\n', '\n<tr height="30" bgColor=#ffffff>\n<td class=black><b>12</b></td>\n<td class=black><b>1.12</b></td>\n<td class="wind_s">Ю</td>\n<td class="ff_6">6</td>\n<td class="vis_3">10 км</td>\n<td class="w_sn">слаб. снег</td>\n<td class="vis_10">10/0<br>[As op]</td>\n<td class="temp_30"><nobr>-19.9</nobr></td>\n<td class="temp_29"><nobr>-22.7</nobr></td>\n<td class="temp_37">78</td>\n<td class="temp_27"><nobr>-31</nobr></td>\n<td class="temp_27"><nobr>-31</nobr></td>\n<td class="black" bgcolor="#9600FE">опасность<br> обморожения</td>\n<td class="temp_35">1035.7</td>\n<td class="black">1019.0</td>\n<td class="temp_"><nobr></nobr></td>\n<td class="temp_30"><nobr>-19.9</nobr></td>\n<td title="за 12 ч." class="temp_39">0.5</td>\n<td class="temp_"></td>\n<td title="" class="snow_"></td>\n', '\n<tr height="30" bgColor=#daf1f7>\n<td class=black><b>15</b></td>\n<td class=black><b>1.12</b></td>\n<td class="wind_s">Ю</td>\n<td class="ff_3">3</td>\n<td class="vis_2">20 км</td>\n<td class="w_sn">слаб. снег</td>\n<td class="vis_10">10/0<br>[As op]</td>\n<td class="temp_31"><nobr>-18.9</nobr></td>\n<td class="temp_30"><nobr>-21.5</nobr></td>\n<td class="temp_37">80</td>\n<td class="temp_28"><nobr>-26</nobr></td>\n<td class="temp_28"><nobr>-26</nobr></td>\n<td class="black" bgcolor=""></td>\n<td class="temp_35">1036.0</td>\n<td class="black">1019.3</td>\n<td class="temp_"><nobr></nobr></td>\n<td class="temp_"><nobr></nobr></td>\n<td title="" class="temp_"></td>\n<td class="temp_"></td>\n<td title="" class="snow_"></td>\n', '\n<tr height="30" bgColor=#ffffff>\n<td class=black><b>18</b></td>\n<td class=black><b>1.12</b></td>\n<td class="wind_se">ЮВ</td>\n<td class="ff_1">1</td>\n<td class="vis_2">20 км</td>\n<td class="w_sn">слаб. снег</td>\n<td class="vis_10">10/0<br>[As op]</td>\n<td class="temp_31"><nobr>-19.5</nobr></td>\n<td class="temp_30"><nobr>-21.8</nobr></td>\n<td class="temp_37">82</td>\n<td class="temp_30"><nobr>-22</nobr></td>\n<td class="temp_30"><nobr>-22</nobr></td>\n<td class="black" bgcolor=""></td>\n<td class="temp_35">1036.3</td>\n<td class="black">1019.6</td>\n<td class="temp_"><nobr></nobr></td>\n<td class="temp_"><nobr></nobr></td>\n<td title="" class="temp_"></td>\n<td class="temp_"></td>\n<td title="" class="snow_"></td>\n', '\n<tr height="30" bgColor=#daf1f7>\n<td class=black><b>21</b></td>\n<td class=black><b>1.12</b></td>\n<td class="wind_s">Ю</td>\n<td class="ff_1">1</td>\n<td class="vis_2">20 км</td>\n<td class="w_sn">слаб. снег</td>\n<td class="vis_10">10/0<br>[As op]</td>\n<td class="temp_30"><nobr>-21.2</nobr></td>\n<td class="temp_29"><nobr>-23.4</nobr></td>\n<td class="temp_37">82</td>\n<td class="temp_29"><nobr>-24</nobr></td>\n<td class="temp_29"><nobr>-24</nobr></td>\n<td class="black" bgcolor=""></td>\n<td class="temp_35">1036.9</td>\n<td class="black">1020.1</td>\n<td class="temp_"><nobr></nobr></td>\n<td class="temp_"><nobr></nobr></td>\n<td title="" class="temp_"></td>\n<td class="temp_"></td>\n<td title="" class="snow_"></td>\n', '\n<tr height="30" bgColor=#ffffff>\n<td class=black><b>00</b></td>\n<td class=black><b>2.12</b></td>\n<td class="wind_">штиль</td>\n<td class="ff_0">0</td>\n<td class="vis_2">20 км</td>\n<td class="w_sn">слаб. снег</td>\n<td class="vis_10">10/0<br>[As op Cs]</td>\n<td class="temp_30"><nobr>-21.9</nobr></td>\n<td class="temp_29"><nobr>-24.4</nobr></td>\n<td class="temp_37">80</td>\n<td class="temp_30"><nobr>-22</nobr></td>\n<td class="temp_30"><nobr>-22</nobr></td>\n<td class="black" bgcolor=""></td>\n<tdclass="temp_34">1038.8</td>\n<td class="black">1021.9</td>\n<td class="temp_30"><nobr>-21.9</nobr></td>\n<td class="temp_"><nobr></nobr></td>\n<td title="за 12 ч." class="temp_39">0.3</td>\n<td class="temp_"></td>\n<td title="сухой снег 10 баллов" class="snow_9">36</td>\n', '\n<tr height="30" bgColor=#daf1f7>\n<td class=black><b>03</b></td>\n<td class=black><b>2.12</b></td>\n<td class="wind_">штиль</td>\n<td class="ff_0">0</td>\n<td class="vis_2">20 км</td>\n<td class="w_"></td>\n<td class="vis_10">10 баллов</td>\n<td class="temp_29"><nobr>-23.2</nobr></td>\n<td class="temp_28"><nobr>-25.7</nobr></td>\n<td class="temp_37">80</td>\n<td class="temp_29"><nobr>-23</nobr></td>\n<td class="temp_29"><nobr>-23</nobr></td>\n<td class="black" bgcolor=""></td>\n<td class="temp_33">1042.8</td>\n<td class="black">1025.3</td>\n<td class="temp_29"><nobr>-23.6</nobr></td>\n<td class="temp_"><nobr></nobr></td>\n<td title="" class="temp_"></td>\n<td class="temp_"></td>\n<td title="" class="snow_"></td>\n', '\n<tr height="30" bgColor=#ffffff>\n<td class=black><b>06</b></td>\n<td class=black><b>2.12</b></td>\n<td class="wind_s">Ю</td>\n<td class="ff_1">1</td>\n<td class="vis_2">20 км</td>\n<td class="w_"> <i>{снег}</i></td>\n<td class="vis_10">10/0<br>[Ac trans Cs]</td>\n<td class="temp_30"><nobr>-21.6</nobr></td>\n<td class="temp_29"><nobr>-24.8</nobr></td>\n<td class="temp_38">75</td>\n<td class="temp_29"><nobr>-25</nobr></td>\n<td class="temp_29"><nobr>-24</nobr></td>\n<td class="black" bgcolor=""></td>\n<td class="temp_34">1041.8</td>\n<td class="black">1024.9</td>\n<td class="temp_"><nobr></nobr></td>\n<td class="temp_"><nobr></nobr></td>\n<td title="" class="temp_"></td>\n<td class="temp_"></td>\n<td title="" class="snow_"></td>\n', '\n<tr height="30" bgColor=#daf1f7>\n<td class=black><b>09</b></td>\n<td class=black><b>2.12</b></td>\n<td class="wind_s">Ю</td>\n<td class="ff_2">2</td>\n<td class="vis_3">10 км</td>\n<tdclass="w_sn">слаб. снег</td>\n<td class="vis_10">10/0<br>[As op]</td>\n<td class="temp_30"><nobr>-20.9</nobr></td>\n<td class="temp_29"><nobr>-23.5</nobr></td>\n<td class="temp_37">80</td>\n<td class="temp_28"><nobr>-27</nobr></td>\n<td class="temp_28"><nobr>-27</nobr></td>\n<td class="black" bgcolor=""></td>\n<td class="temp_34">1042.1</td>\n<td class="black">1025.2</td>\n<td class="temp_"><nobr></nobr></td>\n<td class="temp_"><nobr></nobr></td>\n<td title="" class="temp_"></td>\n<td class="temp_"></td>\n<td title="" class="snow_"></td>\n', '\n<tr height="30" bgColor=#ffffff>\n<td class=black><b>12</b></td>\n<td class=black><b>2.12</b></td>\n<td class="wind_sw">ЮЗ</td>\n<td class="ff_1">1</td>\n<td class="vis_2">20 км</td>\n<td class="w_"> <i>{снег}</i></td>\n<td class="vis_10">10/0<br>[Cs]</td>\n<td class="temp_30"><nobr>-21.4</nobr></td>\n<td class="temp_29"><nobr>-23.7</nobr></td>\n<td class="temp_37">82</td>\n<td class="temp_29"><nobr>-25</nobr></td>\n<td class="temp_29"><nobr>-25</nobr></td>\n<td class="black" bgcolor=""></td>\n<td class="temp_33">1042.6</td>\n<td class="black">1025.7</td>\n<td class="temp_"><nobr></nobr></td>\n<td class="temp_30"><nobr>-20.5</nobr></td>\n<td title="за 12 ч." class="temp_39">0.2</td>\n<td class="temp_"></td>\n<td title="" class="snow_"></td>\n']
tableInString = [i.split('<td') for i in tableInString] # еще нарезка строк

# выбираем строки с нужной информацией, удаляем мешающие извлечению данных тэги
tableInString = [[i[1].replace('<b>', ''), i[2].replace('<b>', ''), i[3], i[4],
                  i[8].replace('<nobr>', ''), i[10], i[15], i[16].replace('<nobr>', ''),
                  i[17].replace('<nobr>', ''), i[18], i[20]] for i in tableInString]
# выборка данных и заполнение списка
listOfData = []
n = 0
for i in tableInString:
    listOfData.append([])
    for j in i:
        data = j[j.find('>') + 1:j.find('<')]
        listOfData[n].append(data)
        if i.index(j) == 10:                        # получение данных по виду снежного покрова
            data = j[j.find('"') + 1:j.find('" ')]
            listOfData[n].append(data)
    n += 1
    

print(tableInString)
print(listOfData)