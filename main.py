import time;
import json;
from VK_CORE import VK_CORE;

vk = VK_CORE("f53d1cee34e8c4ad7db77784832cf20b4ab1c81f52718e411a12044cf4f75c23b47678e4cb30ca564d41a");

#НАЧАЛО ТАЙМЕРА
def go():
    
#ОСМОТР НОВЫХ СООБЩЕНИЙ    
    echo = vk.Check_dialogs();
    print (echo);
    return echo;
#ИЩЕМ ИД В БД, ЕСЛИ НЕТ ТО СОЗДАЕМ С 0
#ЕСЛИ ЕСТЬ ТО СМОТРИМ ЧЕКПОИНТ И ОТВЕТ
#СВЕРЯЕМ ОТВЕТ В БД И ВЫДАЕМ ОТВЕТ СВЯЗАННЫЙ JSON
#МЕНЯЕМ ЧЕКПОИНТ ЧЕЛОВЕКА ПО ИД В БД
#СЛЕДУЮЩИЙ ЧЕЛОВЕК

    
#КОНЕЦ ТАЙМЕРА
    #time.sleep(5);
    #go();

echo = go();


#stroka = {"yes":[1,"hi"],"no":[2,"bue"]};
#diction = json.dumps(stroka);
#stroka = json.loads(diction);

#print(json.dumps(stroka, sort_keys=True, indent=4));
