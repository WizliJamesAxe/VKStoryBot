import time;
import json;
import random as rand;

from VK_CORE import VK_CORE;
from DB_CORE import DB_CORE;
import STORY

def ReadFile(name = "test.txt"):
	A = STORY.ParseFile(name);
	idQ = db.AddQuest("test");
	for obj in A:
		db.AddPoint(idQ, obj['id'], obj['message'], obj['next'], obj['choice']);

vk = VK_CORE("f53d1cee34e8c4ad7db77784832cf20b4ab1c81f52718e411a12044cf4f75c23b47678e4cb30ca564d41a");
db = DB_CORE();

def CheckAnswer(id, message):
	try:
		answer = int(message);
	except ValueError:
		vk.SendMessage(id, 'Пишите пожалуйста цифрами, уважаемый долбаеб.');
		return False;
	if ((answer<1)or(answer>9)):
		vk.SendMessage(id, 'Выбери вариант ответа правильно, Даун.');
		return False;
	return True;

def CreateMessage(u_ID, thisQuest, cStory, message=''):
    #THIS FUNCTION RETURN [message, idS_last]
    result={};

    if message!='':
        find_Story = db.GetPoint(thisQuest,cStory); 
        try:
            cStory = find_Story[0][2].split(' ')[int(message)-1];
        except IndexError:
            vk.SendMessage(user_id, 'Еблан, нормально вариант выбери, ну.');
            return;


    find_Story = db.GetPoint(thisQuest,cStory);
    if(find_Story==[]):
        print('Не считал' +' '+ str(thisQuest) +' '+ str(cStory))
        return;

    message_to_user = find_Story[0][1];
    vk.SendMessage(u_ID, message_to_user);

    while(find_Story[0][3]=='[]'):
        s_Next = rand.randint(0, len(find_Story[0][2].split(' '))-1);
        find_Story = db.GetPoint(thisQuest, find_Story[0][2].split(' ')[s_Next]);
        message_to_user = find_Story[0][1];
        vk.SendMessage(u_ID, message_to_user);

    message_to_user = '\n Выберите ответ:\n'
    for i, j in enumerate(json.loads(find_Story[0][3].replace("'",'"'))):
        message_to_user += str(i+1) + '. ' + j + '\n';

    vk.SendMessage(u_ID, message_to_user);





    db.UpdateUser(u_ID, thisQuest, find_Story[0][0], 0);

    # result['mes'] = message_to_user;
    # result['lastID'] = find_Story[0][0];
    return result;
        

def StartTalk(user):
    s_Mes = CreateMessage(user[0][0], user[0][1], user[0][2]);
    #vk.SendMessage(user[0][0], s_Mes['mes']);
    #db.UpdateUser(user[0][0], user[0][1], s_Mes['lastID'], user[0][3]);


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
    if(messages=={}):
        return;
    messages = messages['response']['items'];
    
    for i in messages:
        try:
            i['unread'];
        except KeyError:
			#СЛЕДУЮЩИЙ ЧЕЛОВЕК
            continue;
            
        #Считываем ID и сообщение
        user_id = i['message']['user_id'];
        message = i['message']['body'];
	
        #ИЩЕМ ИД В БД, ЕСЛИ НЕТ ТО СОЗДАЕМ С 0
        find_user = db.GetUser(user_id);
        if(len(find_user)==0):
            find_user = db.AddUser(user_id);
            StartTalk(find_user);
            #db.DeleteUser(user_id);
			
        #ЕСЛИ ЕСТЬ ТО СМОТРИМ ЧЕКПОИНТ И ОТВЕТ
        elif (len(find_user)==1):            
            if (CheckAnswer(user_id, message)==True):
                # try:
                #     next_Story = find_Story[0][2].split(' ')[int(message)-1];
                # except IndexError:
                #     vk.SendMessage(user_id, 'Еблан, нормально вариант выбери, ну.');
                #     continue;
                #find_Story = db.GetPoint(find_user[0][1], find_user[0][2]);
                s_Mes = CreateMessage(find_user[0][0], find_user[0][1], find_user[0][2], message);#next_Story);
                #vk.SendMessage(user_id, s_Mes['mes']);
                #db.UpdateUser(user_id, find_user[0][1], s_Mes['lastID'], 1);
            else:
                continue;

        #ERROR
        else:
            print("Ты конченный, это пиздец, в БД вот столько этих записей: " + str(len(find_user)));
#СВЕРЯЕМ ОТВЕТ В БД И ВЫДАЕМ ОТВЕТ СВЯЗАННЫЙ JSON
#МЕНЯЕМ ЧЕКПОИНТ ЧЕЛОВЕКА ПО ИД В БД

def LoopRun():
    while (True):
        go();
        time.sleep(5);


    #go();
	
    #КОНЕЦ ТАЙМЕРА	
    #vk.SendMessage(46072729, "Привет")
    #time.sleep(1);
    #vk.SendMessage(46072729, "ТЫ ПИДОР")
    #time.sleep(1);
    #vk.SendMessage(46072729, "ПОКА")
    #time.sleep(1);






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




# def CreateMessage(thisQuest, cStory):
#     #THIS FUNCTION RETURN [message, idS_last]
#     result={};
#     message_to_user = '';

#     find_Story = db.GetPoint(thisQuest,cStory);
#     if(find_Story==[]):
#         print('Не считал')
#         return;

#     message_to_user += find_Story[0][1];

#     while(find_Story[0][3]=='[]'):
#         s_Next = rand.randint(0, len(find_Story[0][2].split(' '))-1);
#         find_Story = db.GetPoint(thisQuest, find_Story[0][2].split(' ')[s_Next]);
#         message_to_user += find_Story[0][1];

#     message_to_user += '\n Выберите ответ:\n'
#     for i, j in enumerate(json.loads(find_Story[0][3].replace("'",'"'))):
#         message_to_user += str(i+1) + '. ' + j + '\n';

#     result['mes'] = message_to_user;
#     result['lastID'] = find_Story[0][0];
#     return result;