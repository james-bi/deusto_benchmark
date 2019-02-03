import time

from configparser import ConfigParser

from monetHelperClass import MonetHelper
from MySQLHelperClass import MySQLHelper
from verticaHelperClass import VerticaHelper

from runLogClass import RunLog
from CSVWriterClass import CSVWriter
from queriesClass import Queries

VConfFileLocation = "genConf.ini"
print("parsing config file found at: " + VConfFileLocation)

OConfigParser = ConfigParser()
OConfigParser.read(VConfFileLocation)

VOutputFile = time.strftime("output/db_benchmark_%Y%m%d_%H%M%S.csv")
CSVWriter = CSVWriter(VOutputFile, ["iteration", "database", "query", "start", "stop", "duration"])

monethelper = MonetHelper(OConfigParser)
mysqlhelper = MySQLHelper(OConfigParser)
verticahelper = VerticaHelper(OConfigParser)

databases = {"monet": monethelper, "MySQL": mysqlhelper, "vertica": verticahelper}
queryName = "simpleAggregate"
queries = Queries()

RunLog(CSVWriter, databases, queryName, queries.getQueries(queryName), 100)