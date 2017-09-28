import sqlite3 as db;

class DB_CORE:
    def __init__(self):
        self.c = db.connect(database="StoryBotDB");
        self.cu = self.c.cursor();
        
        try:
            self.cu.execute("""CREATE TABLE users ( id INTEGER NOT NULL PRIMARY KEY, story INTEGER NOT NULL, this_moment TEXT NOT NULL, save_point TEXT NOT NULL );""");
        except db.DatabaseError as err:
            print(err);

        try:
           self.cu.execute("""CREATE TABLE book ( id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT);""");
        except db.DatabaseError as err:
            print(err);

        self.c.commit();   

    def GetUser(self, idU):
        try:
            self.cu.execute('SELECT * FROM users WHERE id=:idU;', {'idU':idU});
        except db.DatabaseError as err:
            print(err);
            return "ERROR";
        return self.cu.fetchall();    

    def AddUser(self, idU):
        try:
            self.cu.execute('INSERT INTO users VALUES ( :idU, 1, "0", "0" );', {'idU':idU});
        except db.DatabaseError as err:
            print(err);
            return "ERROR";
        self.c.commit();   
        return self.GetUser(idU);

    def UpdateUser(self, idU, story, moment, s_point):#This can upgrade for optimization
        try:
            self.cu.execute('UPDATE users SET story=:story, this_moment=:moment, save_point=:s_point WHERE id=:idU;', {'idU':idU, 'story':story, 'moment':moment, 's_point':s_point});
        except db.DatabaseError as err:
            print(err);
            return "ERROR";
        self.c.commit();   
        return;

    def DeleteUser(self, idU):
        try:
            self.cu.execute('DELETE FROM users WHERE id=:idU;', {'idU':idU});
        except db.DatabaseError as err:
            print(err);
            return "ERROR";
        self.c.commit();   
        return;

    def AddQuest(self, title_of_quest):
        try:
            self.cu.execute('INSERT INTO book ( title ) VALUES ( :title );', {'title':title_of_quest});
            self.cu.execute('SELECT id FROM book WHERE title=:title;', {'title':title_of_quest});
            idQ = self.cu.fetchall()[0][0];
            self.cu.execute('CREATE TABLE quest' + str(idQ) + ' ( id TEXT NOT NULL PRIMARY KEY, message TEXT, next TEXT, choice TEXT, media TEXT );');
        except db.DatabaseError as err:
            print(err);
            return "ERROR";
        self.c.commit();  
        return idQ; 

    def AddPoint(self, idQ, idS, message, nextQ, choice, media):
        try:
            self.cu.execute('INSERT INTO quest' + str(idQ) + ' VALUES ( :idS, :mes , :nextQ, :choice, :media);', {'idS':idS, 'mes': message, 'nextQ':nextQ, 'choice':choice, 'media':media});
        except db.DatabaseError as err:
            print(err);
            return "ERROR";
        self.c.commit();  
        return;

    def GetPoint(self, idQ, idS):
        try:
            self.cu.execute('SELECT * FROM quest' + str(idQ) + ' WHERE id=:idS;', {'idS':idS});
        except db.DatabaseError as err:
            print(err);
            return "ERROR";
        return self.cu.fetchall();

    def Exec(self, s):
        try:
            self.cu.execute(s);
        except db.DatabaseError as err:
            print(err);
            return "ERROR";
        return self.cu.fetchall();

    def PrintTable(self):
        try:
            self.cu.execute('select * from sqlite_master where type = "table";');
        except db.DatabaseError as err:
            print(err);
            return "ERROR";
        return self.cu.fetchall();

    def PrintBook(self):
        try:
            self.cu.execute('select * from book;');
        except db.DatabaseError as err:
            print(err);
            return "ERROR";
        return self.cu.fetchall();

    def PrintQuest(self, idQ):
        try:
            self.cu.execute('select * from quest'+str(idQ)+';');
        except db.DatabaseError as err:
            print(err);
            return "ERROR";
        return self.cu.fetchall();

    def DropAllTables(self):
        try:
            self.cu.execute('DROP TABLE users;');
        except db.DatabaseError as err:
            print(err);
        
        try:
            self.cu.execute('SELECT * FROM book;');
        except db.DatabaseError as err:
            print(err);

        Quests = self.cu.fetchall();

        for i in Quests:
            try:
                self.cu.execute('DROP TABLE quest' + str(i[0]) + ';');
            except db.DatabaseError as err:
                print(err);
                continue;

        try:
            self.cu.execute('DROP TABLE book;');
        except db.DatabaseError as err:
            print(err);

        self.c.commit();  
        self.c.close();
        exit();