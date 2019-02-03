import csv
import mysql.connector

class MySQLHelper:

  OMysqlClient = None
  VMysqlTable = None
  VDataLocation = None

  def __init__(self, OConfigParser):

    self.OConfigParser = OConfigParser

    VUser = self.OConfigParser.get("mysql", "user")
    VPass = self.OConfigParser.get("mysql", "pass")
    VDatabase = self.OConfigParser.get("mysql", "database")
    VPort = self.OConfigParser.get("mysql", "port")
    self.VMySQLTable = self.OConfigParser.get("mysql", "table")
    self.VDataLocation = self.OConfigParser.get("general", "datapath")

    print("initialising mysql")
    self.OMySQLClient = mysql.connector.connect(user=VUser, password=VPass, host='127.0.0.1', database=VDatabase)
    # self.deleteBBDD()
    # self.loadCSV()

  def deleteBBDD(self):

    print("removing table content")
    CCursor = self.OMySQLClient.cursor()
    CCursor.execute("TRUNCATE " + self.VMySQLTable + ";")
    CCursor.close()


  def loadCSV(self):

    print("loading database content")
    CCursor = self.OMySQLClient.cursor()
    VCommand = "LOAD DATA LOCAL INFILE '" + self.VDataLocation + "' INTO TABLE " + self.VMySQLTable + " FIELDS TERMINATED BY '|' ENCLOSED BY '\"' ESCAPED BY '\\\\'"
    CCursor.execute(VCommand)
    self.OMySQLClient.commit()
    CCursor.close()

  def runQuery(self, VQuery):
    CCursor = self.OMySQLClient.cursor(buffered = True)
    CCursor.execute(VQuery)
    CCursor.close()