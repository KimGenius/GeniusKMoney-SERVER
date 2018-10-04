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
        self.cur.execute("SELECT * FROM money_histories ORDER BY date_created ASC")
        result = self.cur.fetchall()

        return result
