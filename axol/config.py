# -*- coding: utf-8 -*-
token = '409875476:AAGHNcCsWsB4RhreN7qRKQZK8S_I90A99'
root = ['random_answer', 'Deepwarrior']

seconds_in_day = 60 #86000

hi_stickers = ['CAADAgADWwQAAm4y2AABD38IAooC_j4C', 'CAADAgADhAEAAjZ2IA7YnALZRRvJMwI']
hi_citrus = ['/DELITAPELSIN', 'ГРЕЙПФРУКТ!', 'ОПРИВЕТ', 'ЦИТРУС!', 'Я ЗНАЮ ЭТУ ДЕВЧОНКУ!', 'ЧТО НОВЕНЬКОГО', 'СПОЙ ПЕСЕНКУ!', 'НУ МАААААМ!']

help_list = ['см. /donate', 'А ЧТО ТУТ НЕПОНЯТНОГО?', 'АЙ НИД СОМБАДИ', '8-800-555-35-35', ';)', 'ХОДЯТ СЛУХИ, ЧТО ВЗЯТКА СОЗДАТЕЛЯМ ПОМОГАЕТ В ПРОХОЖДЕНИИ ЗАДАНИЯ', "ХОЧЕШЬ МНЕ ПОМОЧЬ? У МЕНЯ КАК РАЗ ЕСТЬ ДЛЯ ТЕБЯ ЗАДАНИЕ!",
             "ТЫ НЕ ПОЛУЧИШЬ ЗАДАНИЕ ЧАЩЕ ЧЕМ РАЗ В СУТКИ", "ЕСЛИ ЧОТ НЕ НРАВИТСЯ - ТАК И ПИШИ"]
donate_list = ['С ТЕБЯ ПИВО', 'С ТЕБЯ ЛИМЕРИК', 'С ТЕБЯ ФОТОЧКА', "С ТЕБЯ ГОЛОС", 'С ТЕБЯ ОБНИМАШКИ^^', 'ПРИШЛИ СВОЙ ВАРИАНТ ЗАДАНИЯ', 'Поздравляю! Вы подключили услугу VIP-VIP-VIP. Теперь все задания для Вас платные.', '/donate',
               "ОТПРАВЬ ЗАРЯДЫ: ДИПУ - 30% ЗА БОТА, ЦИТРУСУ - 30% ЗА ЗАДАНИЯ И #зелёныйаксолотль (тм), ЛИИРЕ И СУПЕРУ ПО 10% ЗА СТИКЕРЫ, ШЬЮЗЕН - 20% ЗА СЕРВЕР", "НЕ ЗАБУДЬ ПОКОРМИТЬ СОЗДАТЕЛЕЙ НА БЛИЖАЙШЕЙ РАКОНОСХОДКЕ",
               "ТЕПЕРЬ ТЫ ПОПЛАТИШЬСЯ!", "ОТ РАСПЛАТЫ НЕ УЙДЁШЬ!", "РАБОТАЮ ЗА СПАСИБУ. А ПАПА С МАМОЙ - НЕТ", "Я ТЕБЯ ЗАПОМНИЛ!"]
#format: sticker + task
tasks = [['CAADAgADSgADP_vRD6EHNhBBV7W_Ag', 'ТЫ ДИП. ИСПОЛЬЗУЙ ДИПЯНКУ БЛИЖАЙШИЕ 300 СООБЩЕНИЙ.'],
         ['CAADAgADSAADP_vRDxb1PT65ZcS8Ag', 'ТЫ ЦИТРУС. СПОЙ ПЕСЕНКУ.'], 
         ['CAADAgADQgADP_vRDyRMg2vP6pd8Ag', 'ТЫ АРЕАТАНГЕНТ. ОТПРАВЛЯЙ КАЖДУЮ КАРТИНКУ И СТИКЕР ДИСТОРШН БОТУ БЛИЖАЙШИЕ 70 СООБЩЕНИЙ И ПОКАЗЫВАЙ НАМ.'],
         ['CAADAgADWAADP_vRD8CYBmhcMhZxAg', 'ТЫ ЧЕТЫРЕ))) ЦЕЛЫЙ ЧАС ПИШИ СО СКОБОЧКАМИ)))'],
         ['CAADAgADWgADP_vRD_VQ9Woa3bIOAg', 'ТЫ ЗЛОЙ АДМИН. ПОПРОСИ АДМИНА КОГО-НИБУДЬ ЗАБАНИТЬ ИЛИ СДЕЛАЙ ЭТО САМ, ЕСЛИ У ТЕБЯ ЕСТЬ БАНХАММЕР.'],
         ['CAADAgADVAADP_vRD-VGSEORarUwAg', 'ТЫ НОРМАЛЬ. ПРОБЕЙСЯ В ТОП-3 ПО ФЛУДУ.'], 
         ['CAADAgADXwADP_vRD-j0lU68FiFsAg', 'ТЫ ГОДВИЛЛЬ. ЭКОНОМЬ ВИРТУАЛЬНОЕ ПРОСТРАНСТВО, ПИШИ БЗ ГЛСНХ.'],
         ['CAADAgADdQADP_vRDwPTSwahmq5oAg', 'ТЫ ИИОО. НЕ СДЕРЖИВАЙ СВОЮ НЕНАВИСТЬ К СОГЛАСНЫМ, ПИШИ ИХ НЕ БОЛЕЕ ДВУХ ШТУК В СЛОВЕ.'], 
         ['CAADAgADWQADP_vRDxArNUvEnLZiAg', 'ТЫ БАГ. СЛОМАЙ ПУШКА ИЛИ ЛЮБОЙ ДРУГОЙ БОТ.'],
         ['CAADAgADagADP_vRDy9WxzZxe_NUAg', 'ТЫ ЭЛЕКСОРИЕН. ПЕРЕИМЕНУЙСЯ НА ВЕСЬ ДЕНЬ И ПОМЕНЯЙ ПОЛ.'], 
         ['CAADAgADbAADP_vRD6Xn7qb5y-9YAg', 'ТЫ АНАЛЕПТИК. ПОСТАВЬ КОМУ-НИБУДЬ АНАЛИЗ ПО АВАТАРКЕ.'],
         ['CAADAgADSwADP_vRD5Fg55OC3EGYAg', 'ТЫ ПУШИСТЫЙ ТРИББЛ. ставь точки. и не забывай писать всё с маленькой буквы.'], 
         ['CAADAgADRgADP_vRD5ypDI2RyuAxAg', 'ТЫ СИЛЬФУР. НАПИШИ ЧТО-НИБУДЬ НА ЯПОНСКОМ^^'],
         ['CAADAgADQAADP_vRD85Bwdr_xrWpAg', 'ТЫ СУПЕР ТРУПЕР. ИСПОЛЬЗУЙ КАКИЕ-НИБУДЬ НЕОБЫЧНЫЕ СИМВОЛЫ.'], 
         ['CAADAgADUQADP_vRD60coEpglSQTAg', 'ТЫ ЭЛЛИОТТ. ОТВЕДИ КОГО-НИБУДЬ НА ВЫХОД, ЛОГ В СТУДИЮ.'],
         ['CAADAgADVQADP_vRD3lc6Dt9R8B_Ag', 'ТЫ ЛЕОНАРДО. СПИЛИ КОГО-НИБУДЬ, ЛОГ В СТУДИЮ.'], 
         ['CAADAgADTwADP_vRD3-aLVhdSKPhAg', 'ТЫ ШЕНМАН. ОТПРАВЬ АУДИОСООБЩЕНИЕ ДЛИНОЙ В МИНУТУ ИЛИ БОЛЕЕ.']]  