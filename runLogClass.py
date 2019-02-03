import time

class RunLog:

  csvWriter = None

  def __init__(self, csvWriter, databases, queryName, queries, iterations):

    self.csvWriter = csvWriter
    self.databases = databases
    self.queryName = queryName
    self.queries = queries
    self.iterations = iterations
    self.cycleQueries()

  def cycleQueries(self):

    print(self.databases)

    for i in range(1, self.iterations):
      for databaseName, database in self.databases.iteritems():
        self.runQuery(i, databaseName, database, self.queries[databaseName])

  def runQuery(self, iteration, databaseName, database, query):

    start = int(round(time.time() * 1000))
    database.runQuery(query)
    stop = int(round(time.time() * 1000))

    self.logResults(iteration, databaseName, start, stop)

  def logResults(self, iteration, databaseName, start, stop):

    duration = stop - start
    self.csvWriter.writeLine([iteration, databaseName, self.queryName, start, stop, duration])