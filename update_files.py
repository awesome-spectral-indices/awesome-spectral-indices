import json
import pandas as pd
from indices import indices
from py_expression_eval import Parser
# Convert to list of dictionaries
parser = Parser()
listOfIndices = []
for index in indices:
    formula = parser.parse(index.formula)
    indexDict = index.dict()
    indexDict['reference'] = str(index.reference)
    indexDict['contributor'] = str(index.contributor)
    indexDict['date_of_addition'] = str(index.date_of_addition)
    indexDict['bands'] = formula.variables()
    indexDict['formula'] = formula.toString()
    listOfIndices.append(indexDict)
# Convert to Pandas DataFrame
df = pd.DataFrame(listOfIndices).sort_values('short_name')
# Convert to dictionary
dictOfIndices = dict()
for index in listOfIndices:
    dictOfIndices[index['short_name']] = {
        'long_name': index['long_name'],
        'formula': index['formula'],
        'bands': index['bands'],
        'reference': index['reference'],
        'type': index['type'],
        'date_of_addition': index['date_of_addition'],
        'contributor': index['contributor']
    }
# Save DatFrame, Dictionary and List
df.to_csv('spectral-indices-list.csv',index = False)
with open('spectral-indices-dict.json','w') as fp:
    json.dump(dictOfIndices, fp, indent = 4, sort_keys = True)
with open('spectral-indices-list.json','w') as fp:
    json.dump(listOfIndices, fp, indent = 4, sort_keys = True)