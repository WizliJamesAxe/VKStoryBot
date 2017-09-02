import sqlite3 as db;

class DB_CORE:
    def __init__(self):
        self.c = db.connect(database="StoryBotDB");
        self.cu = c.cursor();
        
        try:
            self.cu.execute("""CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY , save_point INTEGER NOT NULL);""");
        except db.DatabaseError:
            print('Ошибка: Таблица users уже существует');

        try:
            self.cu.execute("""CREATE TABLE stories (id INTEGER NOT NULL PRIMARY KEY , answer TEXT );""");
        except db.DatabaseError:
            print('Ошибка: Таблица stories уже существует'); 

        c.commit();   

    def GetUsers(self, idU):
        self.cu.execute("SELECT * FROM users WHERE id=" + str(idU));
        temp_fetch = {};
        temp_fetch['all'] = self.cu.fetchall();
        temp_fetch['len'] = len(temp_fetch['all']);
        return temp_fetch;
        
    def UpdateStories(self):

        c.commit();   
#cu.execute("""CREATE TABLE users (id INTEGER NOT NULL , save_point INTEGER NOT NULL);""");

cu.execute('INSERT INTO users ( id, save_point ) VALUES ( "123", "0" )');

c.commit();

cu.execute("SELECT * FROM users");


