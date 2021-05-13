from src.indices import spindex
from py_expression_eval import Parser
import pandas as pd
import json

parser = Parser()

# Adding band attribute
for key in spindex.SpectralIndices:
    SpectralIndex = spindex.SpectralIndices[key]
    formula = parser.parse(SpectralIndex.formula)
    SpectralIndex.bands = formula.variables()
    spindex.SpectralIndices[key] = SpectralIndex

# Save results
with open('output/spectral-indices-dict.json', 'w') as fp:
    fp.write(spindex.json(indent=4, sort_keys=True))
    
# Convert to pandas and save CSV
file = open('output/spectral-indices-dict.json')
indices = json.load(file)
df = pd.DataFrame(list(indices['SpectralIndices'].values()))
df = df[["short_name","long_name","type","formula","bands","reference","contributor","date_of_addition"]]
df.to_csv('output/spectral-indices-table.csv',index = False)

# Save tables for Docs
for t in ["vegetation","burn","water","snow","drought","kernel"]:
    name = "docs/_static/indices_" + t + ".csv"
    df[df["type"] == t][["short_name","long_name","reference"]].to_csv(name,index = False)