import vertica_python

class VerticaHelper:

  OVerticaClient = None
  VVerticaDatabase = None
  VVerticaTable = None
  VDataLocation = None

  def __init__(self, OConfigParser):

    self.OConfigParser = OConfigParser

    VUser = self.OConfigParser.get("vertica", "user")
    VPass = self.OConfigParser.get("vertica", "pass")
    VDatabase = self.OConfigParser.get("vertica", "database")
    VPort = self.OConfigParser.get("vertica", "port")
    self.VVerticaTable = self.OConfigParser.get("vertica", "table")
    self.VDataLocation = self.OConfigParser.get("general", "datapath")
    
    DConnInfo = {'host': '127.0.0.1', 'port': VPort, 'user': VUser, 'password': VPass, 'database': VDatabase}
    self.OVerticaClient = vertica_python.connect(**DConnInfo)

    print("initialising vertica")
    # self.deleteBBDD()
    # self.loadCSV()

  def deleteBBDD(self):

    print("removing table content")
    CCursor = self.OVerticaClient.cursor()
    CCursor.execute("DELETE FROM " + self.VVerticaTable + ";")
    self.OVerticaClient.commit()
    CCursor.close()
      
  def loadCSV(self):

    print("loading database content")

    CCursor = self.OVerticaClient.cursor()
    CCursor.execute("COPY " + self.VVerticaTable + " FROM '" + self.VDataLocation + "' DELIMITER '|' ENCLOSED BY '\"' EXCEPTIONS '/tmp/verticaLoadExceptions.txt' SKIP 0 REJECTED DATA '/tmp/verticaLoadRejections.txt' DIRECT NULL AS 'null';")
    self.OVerticaClient.commit()
    CCursor.close()

  def runQuery(self, VQuery):
    CCursor = self.OVerticaClient.cursor()
    CCursor.execute(VQuery)
    CCursor.close()