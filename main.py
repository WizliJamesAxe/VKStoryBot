import random as rand;
import json;
import time;

from VK_CORE import VK_CORE;
from DB_CORE import DB_CORE;
from TOKENS import TOKEN;
from STORY import STORY;

workS = STORY();
def ReadFile(nameQuest, nameFile = "Scenary/test.txt"):
	A = workS.ParseFile(nameFile);
	idQ = db.AddQuest(nameQuest);
	for obj in A:
		db.AddPoint(idQ, obj['id'], obj['message'], obj['next'], obj['choice'], obj['media']);

token = TOKEN();        
vkU = VK_CORE(token.GetUToken());
vk = VK_CORE(token.GetGToken());
db = DB_CORE();

def CreateMessage(user, message):  #Само общение
    find_Story = db.GetPoint(user[1], user[2])[0]; 
    if (find_Story=="ERROR"):
        return find_Story;

    if (message!=''):
        try:
            find_Story[2].split(' ')[int(message)-1];
        except:
            vk.SendMessage(user[0], 'Правильно выберите вариант ответа.');
            return;
        find_Story = db.GetPoint(user[1], find_Story[2].split(' ')[int(message)-1])[0]; 
        if(find_Story=="ERROR"):
            return find_Story;
    #На данном этапе у нас имеется точка, с которой нужно писать

    status = vk.SendMessage(user[0], find_Story[1], find_Story[4]);
    if(status=="ERROR"):
        return "ERROR";

    while(find_Story[3]=='[]'):
        try:
            s_Next = rand.randint(0, len(find_Story[2].split(' '))-1);
        except:
            print("Ошибка в Рандоме.");
            return "ERROR";

        find_Story = db.GetPoint(user[1], find_Story[2].split(' ')[s_Next])[0];
        if(find_Story=="ERROR"):
            return find_Story;

        status = vk.SendMessage(user[0], find_Story[1], find_Story[4]);
        if(status=="ERROR"):
            return "ERROR";

    ChoiceMessage = '\n Выберите ответ:\n'
    for i, j in enumerate(json.loads(find_Story[3].replace("'",'"'))):
        ChoiceMessage += str(i+1) + '. ' + j + '\n';

    status = vk.SendMessage(user[0], ChoiceMessage);
    if(status=="ERROR"):
        return "ERROR";

    if(db.UpdateUser(user[0], user[1], find_Story[0], 0)=="ERROR"):      #FIX CHECK POINT
        return "ERROR";
    return;


def Talking(uID, mes):   #Нахождение юзера в бд, и общение
    find_user = db.GetUser(uID);
    if (find_user=="ERROR"):
        return find_user;

    if(len(find_user)==0):
        find_user = db.AddUser(uID); 
        if (find_user=="ERROR"):
            return find_user;        

        mes='';

    elif(len(find_user)!=1):
        print("Ошибка: В БД " + str(len(find_user)) + " записей пользователя ");#UNREAL
        print(find_user);
        return "ERROR";

    return CreateMessage(find_user[0], mes);

def go():    #Определение Человека с которым ведется разговор, и общение
    messages = vk.GetUnread();
    if(messages=="ERROR"):
        print("Ошибка в методе vk.GetUnread()");
        return "ERROR";
    if(messages=="None"):
        return;
    
    for i in messages:
        try:
            i['unread'];
        except KeyError:
            continue;
            
        user_id = i['message']['user_id'];
        message = i['message']['body'];
        if(Talking(user_id, message)=="ERROR"):
            return "ERROR";


def LoopRun():   #Бесконечная работа скрипта
    while (True):
        if(go()=="ERROR"):
            break;
        #time.sleep(3);


def ForRoma(rec_ID = 39236203, fin_Fave = 'wall-76525381_48922'):
    A = vkU.AllFave();
    if(A=="ERROR"):
        return A;

    vk.SendMessage(rec_ID,'Привет, по просьбе моего сексуального хозяина - Вячеслава Сысоева, я скину тебе все записи, которые он оценил за сегодня:')

    i=0;
    
    while(('wall'+str(A['items'][i]['from_id'])+'_'+str(A['items'][i]['id']))!=fin_Fave):
        vk.SendMessage(rec_ID, '', ('wall'+str(A['items'][i]['from_id'])+'_'+str(A['items'][i]['id'])));
        i+=1;

    


#stroka = {"yes":[1,"hi"],"no":[2,"bue"]};
#diction = json.dumps(stroka);
#stroka = json.loads(diction);

#print(json.dumps(stroka, sort_keys=True, indent=4));
