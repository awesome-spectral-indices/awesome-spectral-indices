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
    x = x.replace("^nexp","^{n}")
    x = x.replace("^cexp","^{c}")
    x = x.replace("gamma","\\gamma ")
    x = x.replace("alpha","\\alpha ")
    x = x.replace("beta","\\beta ")
    x = x.replace("omega","\\omega ")
    x = x.replace("lambdaN","\\lambda_{N} ")
    x = x.replace("lambdaR","\\lambda_{R} ")
    x = x.replace("lambdaG","\\lambda_{G} ")
    x = x.replace("*","\\times ")
    x = f":math:`{x}`"
    return x
df["Equation"] = df["formula"].apply(toMath)
df["Long Name"] = df["long_name"] + " [`ref <" + df["reference"] + ">`_]"
df["Index"] = df["short_name"]
for t in ["vegetation","burn","water","snow","urban","kernel","radar"]:
    name = "docs/_static/indices_" + t + ".csv"
    df[df["type"] == t][["Index","Long Name","Equation"]].to_csv(name,index = False)