  def loadAndCleanData(file):
        data = pd.read_csv(file)
        data.fillna(0)
        return data

  def mergeData(dataset1, dataset2, column):
      data = []
      data = data.insert(dataset2(column))
      data[column] = 0
      data[column] = dataset1
      return dataset1
