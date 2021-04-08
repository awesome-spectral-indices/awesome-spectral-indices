import json
import pandas as pd
# Load the list
f = open('spectral-indices-list.json')
indiceslist = json.load(f)
# Convert it to a dataframe
df = pd.DataFrame(indiceslist).sort_values('short_name')
# Save the dataframe as csv
df.to_csv('spectral-indices-list.csv',index = False)
# Convert it to a eemont-style dictionary
indices = dict()
for index in indiceslist:
    indices[index['short_name']] = {
        'long_name': index['long_name'],
        'formula': index['formula'],
        'bands': index['bands'],
        'reference': index['reference'],
        'type': index['type'],
        'date_of_addition': index['date_of_addition'],
    }
# Save the dictionary as a json
with open('spectral-indices-dict.json','w') as fp:
    json.dump(indices, fp, indent = 4, sort_keys = True)