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
def toMath(x):
    x = x.replace(" ","")
    x = x.replace("**","^")
    x = x.replace("^2.0","^{2.0}")
    x = x.replace("^0.5","^{0.5}")
    x = x.replace("^nexp","^{nexp}")
    x = x.replace("^cexp","^{cexp}")
    x = x.replace("*","\\times ")
    x = f":math:`{x}`"
    return x
df["equation"] = df["formula"].apply(toMath)
for t in ["vegetation","burn","water","snow","drought","urban","kernel"]:
    name = "docs/_static/indices_" + t + ".csv"
    df[df["type"] == t][["short_name","long_name","reference","equation"]].to_csv(name,index = False)