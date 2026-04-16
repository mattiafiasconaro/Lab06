from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAllAnni(self):
        return DAO.getAllAnni()

    def getAllBrand(self):
        return DAO.getAllBrand()

    def getAllRetailer(self):
        return DAO.getAllRetailer()
    def getAllRicavi(self,anno,brand,retailer):
        return DAO.getAllRicavi(anno,brand,retailer)
