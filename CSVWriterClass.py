import csv

class CSVWriter(object):

  def __init__(self, VFileName, AHeader = None):

    print("creating and opening file for writing: " + VFileName)
    self.VFileName = VFileName

    with open(self.VFileName, 'w+') as FFile:
      Writer = csv.writer(FFile, delimiter=";", lineterminator='\n')
      Writer.writerow(AHeader)
      FFile.flush()

  def writeLine(self, ARow):

    with open(self.VFileName, 'a') as FFile:
      Writer = csv.writer(FFile, delimiter=";", lineterminator='\n')
      Writer.writerow(ARow)
      FFile.flush()