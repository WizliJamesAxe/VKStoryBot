import sqlite3 as db;

c = db.connect(database="users");
cu = c.cursor();
try:
    cu.execute("""CREATE TABLE users (id INTEGER NOT NULL , save_point INTEGER NOT NULL);""");
except db.DatabaseError:
    print('Ошибка: База данных уже существует');
    
cu.execute('INSERT INTO users ( id, save_point ) VALUES ( "123", "0" )');

cu.execute('DELETE FROM users WHERE id = 123');


c.commit();
cu.execute("SELECT * FROM users");

for idu, story in cu.fetchall():
    print(str(idu) + " на " + str(story) + " моменте.");
