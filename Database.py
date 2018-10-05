import pymysql


class GeniusKMoney:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "root"
        db = "geniusk_money"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def list_customers(self):
        self.cur.execute("SELECT * FROM customers")
        result = self.cur.fetchall()

        return result

    def list_money_histories(self):
        self.cur.execute("SELECT h.idx, c.name, h.type, h.money, h.memo, h.date_created FROM money_histories as h INNER JOIN customers c on h.udx = c.idx ORDER BY h.date_created DESC;")
        result = self.cur.fetchall()

        return result
