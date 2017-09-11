import time;
import json;
from VK_CORE import VK_CORE;
from DB_CORE import DB_CORE;
import STORY

def ReadFile():
	A = STORY.ParseFile("test.txt");
	idQ = db.AddQuest("test");
	for obj in A:
		db.AddPoint(idQ, obj['id'], obj['message'], obj['next'], obj['choice']);

vk = VK_CORE("f53d1cee34e8c4ad7db77784832cf20b4ab1c81f52718e411a12044cf4f75c23b47678e4cb30ca564d41a");
db = DB_CORE();

#НАЧАЛО ТАЙМЕРА
#ОСМОТР НОВЫХ СООБЩЕНИЙ
def go():    
    # echo = vk.Check_dialogs();
    # try:
    #     echo['response']['unread_dialogs']
    # except KeyError:
    #     return;

    # messages = echo['response']['items'];
    messages = vk.GetUnread();
    messages = messages['response']['items'];
    
    for i in messages:
        try:
            i['unread'];
        except KeyError:
            continue;
            
        #Считываем ID и сообщение
        user_id = i['message']['user_id'];
        message = i['message']['body'];
	
        #ИЩЕМ ИД В БД, ЕСЛИ НЕТ ТО СОЗДАЕМ С 0
        find_user = db.GetUser(user_id);
        if(len(find_user)==0):
            db.AddUser(user_id);
			
        #ЕСЛИ ЕСТЬ ТО СМОТРИМ ЧЕКПОИНТ И ОТВЕТ
        elif (len(find_user)==1):
           print(db.GetPoint(find_user[0][1],find_user[0][2]));
        #ERROR
        else:
            print("Ты конченный, это пиздец, в БД вот столько этих записей: " + str(len(find_user)));
#СВЕРЯЕМ ОТВЕТ В БД И ВЫДАЕМ ОТВЕТ СВЯЗАННЫЙ JSON
#МЕНЯЕМ ЧЕКПОИНТ ЧЕЛОВЕКА ПО ИД В БД
#СЛЕДУЮЩИЙ ЧЕЛОВЕК

# while (True):
#     go();
	
#     #КОНЕЦ ТАЙМЕРА	
#     time.sleep(5);








#stroka = {"yes":[1,"hi"],"no":[2,"bue"]};
#diction = json.dumps(stroka);
#stroka = json.loads(diction);

#print(json.dumps(stroka, sort_keys=True, indent=4));

# {
#     "response": {
#         "count": 1,
#         "items": [
#             {
#                 "in_read": 0,
#                 "message": {
#                     "body": "\u0414\u0430",
#                     "date": 1504364769,
#                     "id": 1,
#                     "out": 0,
#                     "read_state": 0,
#                     "title": "",
#                     "user_id": 42318366
#                 },
#                 "out_read": 1,
#                 "unread": 1
#             }
#         ],
#         "unread_dialogs": 1
#     }
# }
