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

    @staticmethod
    def getAllVendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT 
                SUM(Quantity * Unit_sale_price) AS volume,
                COUNT(*) AS num_vendite,
                COUNT(DISTINCT gds.Retailer_code) AS num_retailer,
                COUNT(DISTINCT gds.Product_number) AS num_prodotti
            FROM go_daily_sales gds, go_products gp, go_retailers gr
            WHERE YEAR(gds.Date) = COALESCE(%s, YEAR(gds.Date))
            AND gp.Product_brand = COALESCE(%s, gp.Product_brand)
            AND gr.Retailer_name = COALESCE(%s, gr.Retailer_name)
            AND gr.Retailer_code = gds.Retailer_code
            AND gp.Product_number=gds.Product_number"""

        cursor.execute(query, (anno, brand, retailer))
        res = []
        for row in cursor:
            res.append(row)
        cursor.close()
        cnx.close()
        return res