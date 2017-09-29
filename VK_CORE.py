import requests;
import time;

class VK_CORE:
    URL = "https://api.vk.com/method/";
    count_Req = 0;
    token = '';
    def __init__(self, t0ken):
        self.token = t0ken;
        print("Token is SET!");
        
    def __Execute__(self, item, method, params):
        ver_and_tok = {'v': '5.52', 'access_token': self.token};
        params.update(ver_and_tok);#Добавили версию и токен

        req = requests.post(self.URL + item + '.' + method, data=params)#Делаем запрос

        self.count_Req = self.count_Req + 1;
        print(str(self.count_Req)+" запрос к VK API.");#Считаем номер запросов

        if(self.count_Req%5==0):
            time.sleep(1);

        try:
            return req.json();
        except:
            print("Ошибка VK.Execute.req.json");
            print(req.text);
            return "ERROR";

    def Check_dialogs(self):
        return self.__Execute__("messages","getDialogs",{"count": "20"});

    def GetUnread(self):
        tDialogs = self.Check_dialogs();
        if(tDialogs=="ERROR"):
            return tDialogs;

        try:
            tDialogs['response']['unread_dialogs']
        except KeyError:
            return "None";
        return tDialogs['response']['items'];

    def SendMessage(self, user_id, message='error', attachment=''):
        resp = self.__Execute__("messages", "send", {"user_id":str(user_id), "message":message, "attachment":attachment});
        if(resp=='ERROR'):
            return 'ERROR';

        try:
            resp['response'];
        except:
            try:
                resp['error'];
            except:
                print(resp);
                return 'ERROR';
            print(resp);
            return 'ERROR';
        return 'OK';

    def AllFave(self):
        resp = self.__Execute__("fave", "getPosts",{'count':20})
        if(resp=='ERROR'):
            return 'ERROR';

        try:
            resp['response'];
        except:
            try:
                resp['error'];
            except:
                print(resp);
                return 'ERROR';
            print(resp);
            return 'ERROR';
        return resp['response'];
