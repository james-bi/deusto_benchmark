class Queries:

  def getQueries(self, queryName):

    if(queryName == "simpleAggregate"):
  	  return self.simpleAggregate()
    if(queryName == "something else"):
  	  print("program me!")

  def simpleAggregate(self):

    simpleAggregate = {"monet" : "SELECT COUNT(*), SUM(production), AVG(production) FROM \"metalData\".\"factTable\";",
      "MySQL" : "SELECT COUNT(*), SUM(production), AVG(production) FROM factTable;",
      "vertica": "SELECT COUNT(*), SUM(production), AVG(production) FROM factTable;",
    }

    return simpleAggregate