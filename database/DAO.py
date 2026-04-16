from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getAllAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT DISTINCT YEAR(Date) AS anno 
                   FROM go_daily_sales 
                   ORDER BY anno"""

        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(row)
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select  distinct g.product_brand as brand
                from go_products g
                order by brand """

        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(row)
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllRetailer():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct g.Retailer_name as name
                    from go_retailers g
                    order by name """

        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(row)
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllRicavi(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT s.*, p.Product_brand, r.Retailer_name,
            (s.Unit_sale_price * s.Quantity) AS ricavo
            FROM go_daily_sales s
            JOIN go_products p ON s.Product_number = p.Product_number
            JOIN go_retailers r ON s.Retailer_code = r.Retailer_code
            WHERE YEAR(s.Date) = COALESCE(%s, YEAR(s.Date))
            AND p.Product_brand = COALESCE(%s, p.Product_brand)
            AND r.Retailer_name = COALESCE(%s, r.Retailer_name)
            ORDER BY ricavo DESC
            LIMIT 5"""

        cursor.execute(query, (anno, brand, retailer))
        res = []
        for row in cursor:
            res.append(row)
        cursor.close()
        cnx.close()
        return res