import pymysql


class DrinkDBManagement:
    bank_db = pymysql.connect(host='embeded.clez5ac4cxmt.us-east-2.rds.amazonaws.com', user='root', password='rlaehdgus', db='VendingMachine', charset='utf8')

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

    def purchase_drink(self, i):

        sql = """
        update drinks
        set stock = stock - 1
        where id=%s;
        """

        self.curs.execute(sql, i)
        DrinkDBManagement.bank_db.commit()

        return self.print_drink(i)

    def fill_drink(self, i):

        sql = """
        update drinks
        set stock = 9
        where id=%s;
        """

        self.curs.execute(sql, i)
        DrinkDBManagement.bank_db.commit()

        return self.print_drink(i)

    def print_all_drink(self):
        sql = """
         select name,cost
         from drinks;
         """
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        self.print_table(rows)

        return rows

    def print_drink(self, id):
        sql = """
         select *
         from drinks
         where id = %s;
         """
        self.curs.execute(sql, id)
        rows = self.curs.fetchall()

        return rows[0]

    def insert_drink(self, name, cost, stock):
        sql = """
        insert into `drinks`
        values (NULL,%s,%s,%s)
        """

        self.curs.execute(sql, (name, cost, stock))
        DrinkDBManagement.bank_db.commit()

    # def purchase_drink(self, name):
    #     # ?????? ????????? ????????? ?????? ????????????
    #     sql = """
    #      select name, cost, stock
    #      from drinks
    #      where name = %s;
    #      """
    #     self.curs.execute(sql, name)
    #     rows = self.curs.fetchone()
    #
    #     cost = rows['cost']
    #     stock = rows['stock']
    #
    #     print('????????? ?????? : ', cost)
    #     print('????????? ?????? : ', stock)
    #
    #     # todo ????????? ??????????????? ????????? ???????????? ????????????
    #
    #     sql = """
    #     update `drinks`
    #     set stock=%s
    #     where name = %s
    #     """
    #
    #     self.curs.execute(sql, (stock - 1, name))
    #     DrinkDBManagement.bank_db.commit()

#
# bankManagement = DrinkDBManagement()
# bankManagement.print_all_drink()
#
# # bankManagement.insert_drink('test',20,20)
#
# bankManagement.purchase_drink('Pepsi')
# bankManagement.print_all_drink()
