import pymonetdb

class MonetHelper:

  OMonetClient = None
  VMonetDatabase = None
  VMonetTable = None
  VDataLocation = None

  def __init__(self, OConfigParser):

    self.OConfigParser = OConfigParser

    VUser = self.OConfigParser.get("monet", "user")
    VPass = self.OConfigParser.get("monet", "pass")
    VDatabase = self.OConfigParser.get("monet", "database")
    VPort = self.OConfigParser.get("monet", "port")
    self.VMonetDatabase = self.OConfigParser.get("monet", "database")
    self.VMonetTable = self.OConfigParser.get("monet", "table")
    self.VDataLocation = self.OConfigParser.get("general", "datapath")

    print("initialising monet")
    self.OMonetClient = pymonetdb.connect(username = VUser, password = VPass, hostname = "localhost", database = VDatabase, autocommit = True)
    # self.deleteBBDD()
    # self.loadCSV()

  def deleteBBDD(self):
    
    print("removing table content")
    CCursor = self.OMonetClient.cursor()
    CCursor.execute("DELETE FROM \"metalData\".\"factTable\";")
    CCursor.close()

  def loadCSV(self):

    print("loading database content")
    CCursor = self.OMonetClient.cursor()
    VCommand = "COPY  INTO  \"" + self.VMonetDatabase + "\".\"" + self.VMonetTable + "\" FROM '" + self.VDataLocation + "' USING DELIMITERS '|','\\n','\"'"
    CCursor.execute(VCommand)
    CCursor.close()

  def runQuery(self, VQuery):
    CCursor = self.OMonetClient.cursor()
    CCursor.execute(VQuery)
    CCursor.close()