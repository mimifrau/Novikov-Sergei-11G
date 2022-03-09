import unittest
import sqlite3


class TestBD(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.database = sqlite3.connect('test1.db')

        self.cur = self.database.cursor()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS "klient" (
        "id_user"	INTEGER NOT NULL UNIQUE,
        "login"	TEXT NOT NULL UNIQUE,
        "password"	TEXT NOT NULL,
        "e_mail"	TEXT UNIQUE,
        "nickname"	TEXT,
        "birthday"	TEXT,   
        "date_of_reg"	TEXT,
        PRIMARY KEY("id_user" AUTOINCREMENT)
);''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS "tovar" (
	    "id_tovar"	INTEGER NOT NULL UNIQUE,
	    "kol_vo"	TEXT NOT NULL,
	    "description"	TEXT NOT NULL,
	    "price"	REAL,
	    PRIMARY KEY("id_tovar" AUTOINCREMENT)
);''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS "zakaz" (
	    "id_products"	INTEGER NOT NULL,
	    "id_user"	INTEGER NOT NULL,
	    "price"	REAL NOT NULL,
	    "adress"	TEXT NOT NULL,
	    "id_zakaz"	INTEGER NOT NULL UNIQUE,
	    PRIMARY KEY("id_zakaz" AUTOINCREMENT)
);''')




        self.cur.execute("INSERT INTO 'klient' VALUES (1,'spike','6lol9','spike@gmail.com','sergei','2002-02-02','2021-02-02');")
        self.cur.execute("INSERT INTO 'klient' VALUES (2,'pupa','lolkek','keklol@ya.ru','arnold','2000-30-11','2021-11-02');")
        self.cur.execute("INSERT INTO 'klient' VALUES (3,'lololoshka','lolololo1111','lololoshka@mail.ru','ivan','2004-04-12','2021-11-12');")

        self.cur.execute("INSERT INTO 'tovar' VALUES (1,'shely','Шелли имеет среднюю скорость передвижения и среднее количество здоровья. Выстреливает дробью пуль, и соответственно количество нанесённого урона и разброс становится меньше, что делает её превосходной для ближнего боя. Её Супер такой же, как и обычная атака, только более мощный, способный отталкивать противников и разрушать препятствия. Шелли очень проста в освоении, что поможет начинающим игрокам.',1000.0);")
        self.cur.execute("INSERT INTO 'tovar' VALUES (2,'spike','Спайк имеет ​​очень низкий показатель здоровья, нормальную скорость передвижения и высокий урон вблизи, из-за чего он и полезен для борьбы со сгруппированными бойцами. Он уникален тем, что урон, который он наносит на близком расстоянии, также зависит от «хитбокса» противника (чем «хитбокс» выше, тем больше шипов может коснуться его).',22000.0);")


        self.cur.execute("INSERT INTO 'zakaz' VALUES (1,1,1000.0,'Окская 1к1',1);")
        self.cur.execute("INSERT INTO 'zakaz' VALUES (2,2,23000.0,'Нагорная 9',2);")
        self.cur.execute("INSERT INTO 'zakaz' VALUES (3,3,22000.0,'Минская 5',3);")


    @classmethod
    def tearDownClass(self):
        self.cur.execute("DROP TABLE klient")
        self.cur.execute("DROP TABLE tovar")
        self.cur.execute("DROP TABLE zakaz")
        self.database.commit()

    def test_1(self):
        print('Первый тест:')
        self.cur.execute("SELECT DISTINCT(SUBSTR(birthday, 1, 4)) FROM klient;")
        print(*self.cur.fetchall())

    def test_2(self):
        print('Второй тест:')
        self.cur.execute("SELECT AVG(CAST((julianday('now') - julianday(birthday)) AS INTEGER) / 365) FROM klient WHERE (CAST((julianday('now') - julianday(date_of_reg)) AS INTEGER) <= 61);")
        for el in self.cur.fetchall():
            print(*el)

    def test_3(self):
        print('Третий тест:')
        self.cur.execute('SELECT COUNT(*) AS "total_items" FROM tovar;')
        for el in self.cur.fetchall():
            print(*el)

if __name__ == "__main__":
    unittest.main()
