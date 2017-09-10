import sqlite3 as db;

class DB_CORE:
    def __init__(self):
        self.c = db.connect(database="StoryBotDB");
        self.cu = self.c.cursor();
        
        try:
            self.cu.execute("""CREATE TABLE users ( id INTEGER NOT NULL PRIMARY KEY, story INTEGER NOT NULL, this_moment INTEGER NOT NULL, save_point INTEGER NOT NULL );""");
        except db.DatabaseError:
            print('Ошибка: Таблица users уже существует');

        try:
            self.cu.execute("""CREATE TABLE book ( id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT PRIMARY KEY );""");
        except db.DatabaseError:
            print('Ошибка: Таблица stories уже существует'); 

        self.c.commit();   

    def GetUser(self, idU):
        try:
            self.cu.execute('SELECT * FROM users WHERE id = ' + str(idU) + ';');
            return self.cu.fetchall();    
        except db.DatabaseError:
            print("ОШИБКА В ГЕТЮЗЕР")

    def AddUser(self, idU):
        try:
            self.cu.execute('INSERT INTO users VALUES ( ' + str(idU) + ', 0, 0, 0 );');
        except db.DatabaseError:
            print("ОШИБКА В ЭДЮЗЕР")
        self.c.commit();   

    def UpdateUser(self, idU, story, moment, s_point):
        try:
            self.cu.execute('UPDATE users SET story = ' + str(story) + ', this_moment = ' + str(moment) + ', save_point = ' + str(s_point) + ' WHERE id = ' + str(idU) + ';');
        except db.DatabaseError:
            print("ОШИБКА В АПДЕЙТЮЗЕР")
        self.c.commit();   

    def DeleteUser(self, idU):
        try:
            self.cu.execute('DELETE FROM users WHERE id = ' + str(idU) + ';');
        except db.DatabaseError:
            print("ОШИБКА В ДЕЛИТЮЗЕР")
        self.c.commit();   

    def AddQuest(self, title_of_quest):
        try:
            self.cu.execute('INSERT INTO book ( title ) VALUES ( "' + title_of_quest + '" );');
            self.cu.execute('SELECT id FROM book WHERE title = "' + title_of_quest + '";');
            idQ = self.cu.fetchall()[0][0];
            self.cu.execute('CREATE TABLE quest' + str(idQ) + ' ( id INTEGER NOT NULL PRIMARY KEY, message TEXT, next TEXT, choice TEXT );');
        except db.DatabaseError:
            print("ОШИБКА В ЭДСТОРИ")
        self.c.commit();  
        return idQ; 

    def AddPoint(self, idQ, idS, message, nextQ, choice):
        try:
            self.cu.execute('INSERT INTO quest' + str(idQ) + ' VALUES ( ' + str(idS) + ', "' + message + '", "' + str(nextQ) + '", "' + str(choice) + '"" );');
        except db.DatabaseError:
            print("ОШИБКА В ЭДПОИНТ")

    def GetPoint(self, idQ, idS):
        try:
            self.cu.execute('SELECT * FROM quest' + str(idQ) + ' WHERE id=' + str(idS) + ';');
            return self.cu.fetchall();
        except db.DatabaseError:
            print("ОШИБКА В ГЕТПОИНТ")

