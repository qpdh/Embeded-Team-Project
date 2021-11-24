import pymysql


class BankManagement:
    bank_db = pymysql.connect(host='localhost', user='root', password='root', db='vending_machine', charset='utf8')

    def __init__(self):
        self.curs = self.bank_db.cursor(pymysql.cursors.DictCursor)

    def print_table(self, rows):
        widths = []
        columns = []
        tavnit = '|'
        separator = '+'

        for cd in self.curs.description:
            widths.append(len(cd[0]))
            columns.append(cd[0])

        for w in widths:
            tavnit += " %-" + "%ss |" % (w,)
            separator += '-' * w + '--+'

        print(separator)
        print(tavnit % tuple(columns))
        print(separator)

        for row in rows:
            print(tavnit % tuple(row.values()))
        print(separator)

    def print_all_drink(self):
        sql = """
         select *
         from drinks;
         """
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        self.print_table(rows)

    def insert_drink(self, name, cost, stock):
        sql = """
        insert into `drinks`
        values (NULL,%s,%s,%s)
        """

        self.curs.execute(sql, (name, cost, stock))
        BankManagement.bank_db.commit()

    def purchase_drink(self, name):
        # 현재 선택된 음료의 재고 가져오기
        sql = """
         select name, cost, stock
         from drinks
         where name = %s;
         """
        self.curs.execute(sql, name)
        rows = self.curs.fetchone()

        cost = rows['cost']
        stock = rows['stock']

        print('가져온 비용 : ', cost)
        print('가져온 재고 : ', stock)

        # todo 비용이 부족하거나 재고가 부족하면 예외처리

        sql = """
        update `drinks`
        set stock=%s
        where name = %s
        """

        self.curs.execute(sql, (stock - 1, name))
        BankManagement.bank_db.commit()


bankManagement = BankManagement()
bankManagement.print_all_drink()

# bankManagement.insert_drink('test',20,20)

bankManagement.purchase_drink('Pepsi')
bankManagement.print_all_drink()