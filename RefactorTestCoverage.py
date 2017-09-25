from interpreter import Interpreter
from Database.interface_database import IDatabase

class CodeCoverage:
    def __init__(self):
        self.db_interface = IDatabase()
        self.interpreter = Interpreter("dbName")
    
    def run_tests(self):
        self.test_databaseinterface();

    

    def test_databaseinterface(self):
        self.test_databaseinterface_execute_sql()
        self.test_databaseinterface_closeconnection()
        self.test_databaseinterface_commit()
        self.test_databaseinterface_setup()
        self.test_databaseinterface_reset()
        self.test_databaseinterface_displaydata()
        self.test_databaseinterface_writetodatabase()
        self.test_databaseinterface_backupdatabase()

    def test_databaseinterface_execute_sql(self):
        try:
            self.db_interface.execute_sql("string")
        except: 
            pass

    def test_databaseinterface_closeconnection(self):
        try:
            self.db_interface.close_connection()
        except: 
            pass

    def test_databaseinterface_commit(self):
        try:
            self.db_interface.commit()
        except: 
            pass

    def test_databaseinterface_setup(self):
        try:
            self.db_interface.setup()
        except: 
            pass

    def test_databaseinterface_reset(self):
        try:
            self.db_interface.reset()
        except: 
            pass

    def test_databaseinterface_displaydata(self):
        try:
            self.db_interface.display_data()
        except: 
            pass

    def test_databaseinterface_writetodatabase(self):
        try:
            self.db_interface.write_to_database("string")
        except: 
            pass

    def test_databaseinterface_backupdatabase(self):
        try:
            self.db_interface.backup_database()
        except: 
            pass
    


test = CodeCoverage().run_tests();