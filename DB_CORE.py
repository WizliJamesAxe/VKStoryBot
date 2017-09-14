import sqlite3 as db;

class DB_CORE:
    def __init__(self):
        self.c = db.connect(database="StoryBotDB");
        self.cu = self.c.cursor();
        
        try:
            self.cu.execute("""CREATE TABLE users ( id INTEGER NOT NULL PRIMARY KEY, story INTEGER NOT NULL, this_moment TEXT NOT NULL, save_point INTEGER NOT NULL );""");
        except db.Error:
            print('Ошибка: Таблица users уже существует');

        try:
            self.cu.execute("""CREATE TABLE book ( id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT);""");
        except db.Error:
            print('Ошибка: Таблица book уже существует'); 

        self.c.commit();   

    def GetUser(self, idU):
        try:
            self.cu.execute('SELECT * FROM users WHERE id = ' + str(idU) + ';');
            return self.cu.fetchall();    
        except db.Error:
            print("ОШИБКА В ГЕТЮЗЕР")

    def AddUser(self, idU):
        try:
            self.cu.execute('INSERT INTO users VALUES ( ' + str(idU) + ', 1, "BEGIN", 0 );');
        except db.Error:
            print("ОШИБКА В ЭДЮЗЕР")
        self.c.commit();   
        self.cu.execute('SELECT * FROM users WHERE id="' + str(idU) + '";');
        return self.cu.fetchall();


    def UpdateUser(self, idU, story, moment, s_point):
        try:
            self.cu.execute('UPDATE users SET story = ' + str(story) + ', this_moment = "' + str(moment) + '", save_point = ' + str(s_point) + ' WHERE id = ' + str(idU) + ';');
            print('UPDATE users SET story = ' + str(story) + ', this_moment = "' + str(moment) + '", save_point = ' + str(s_point) + ' WHERE id = ' + str(idU) + ';');
        except db.Error:
            print("ОШИБКА В АПДЕЙТЮЗЕР")
        self.c.commit();   

    def DeleteUser(self, idU):
        try:
            self.cu.execute('DELETE FROM users WHERE id =' + str(idU) + ';');
        except db.Error:
            print("ОШИБКА В ДЕЛИТЮЗЕР")
        self.c.commit();   

    def AddQuest(self, title_of_quest):
        try:
            self.cu.execute('INSERT INTO book ( title ) VALUES ( "' + title_of_quest + '" );');
            self.cu.execute('SELECT id FROM book WHERE title = "' + title_of_quest + '";');
            idQ = self.cu.fetchall()[0][0];
            self.cu.execute('CREATE TABLE quest' + str(idQ) + ' ( id TEXT NOT NULL PRIMARY KEY, message TEXT, next TEXT, choice TEXT );');
        except db.Error:
            print("ОШИБКА В ЭДКВЕСТ")
        self.c.commit();  
        return idQ; 

    def AddPoint(self, idQ, idS, message, nextQ, choice):
        try:
            self.cu.execute('INSERT INTO quest' + str(idQ) + ' VALUES ( "' + str(idS) + '", :mes , "' + str(nextQ) + '", "' + str(choice) + '" );', {'mes': message});
            #self.cu.execute('INSERT INTO quest', );
            #print('INSERT INTO quest' + str(idQ) + ' VALUES ( "' + str(idS) + '", "' + message + '", "' + str(nextQ) + '", "' + str(choice) + '" );')
        except db.Error:
            print("ОШИБКА В ЭДПОИНТ")
            return;        
        self.c.commit();  

    def GetPoint(self, idQ, idS):
        try:
            self.cu.execute('SELECT * FROM quest' + str(idQ) + ' WHERE id="' + str(idS) + '";');
            return self.cu.fetchall();
        except db.Error:
            print("ОШИБКА В ГЕТПОИНТ")

    def Exec(self, s):
        try:
            self.cu.execute(s);
            return self.cu.fetchall();
        except db.DatabaseError:
            print("ОШИБКА")

    def PrintTable(self):
        try:
            self.cu.execute('select * from sqlite_master where type = "table"');
            return self.cu.fetchall();
        except db.Error:
            print("ОШИБКА В ПРИНТТЭЙБЛ")
