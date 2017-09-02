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
    
 
