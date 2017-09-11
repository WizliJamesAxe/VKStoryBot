import requests;

class VK_CORE:
    URL = "https://api.vk.com/method/";
    token = '';
    def __init__(self, t0ken):
        print("I'am Ready");
        self.token = t0ken;
        
    def __Execute__(self, item, method, params):
        req = requests.get(self.URL + item + '.' + method + '?' + params + '&v=5.52&access_token=' + self.token);
        return req.json();

    def Check_dialogs(self):
        return self.__Execute__("messages","getDialogs","count=20");

    def GetUnread(self):
        try:
            self.Check_dialogs()['response']['unread_dialogs']
        except KeyError:
            print("Все прочитаны");
            return {};
        return self.Check_dialogs();

    def SendMessage(self, user_id, message):
        self.__Execute__("messages", "send", "user_id="+str(user_id)+"&message="+message);

    
 
