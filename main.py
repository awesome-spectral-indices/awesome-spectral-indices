from src.indices import spindex
from src.utils import Bands
from py_expression_eval import Parser
import pandas as pd
import json

bandVars = [
    'A',
    'B',
    'G',
    'R',
    'N',
    'N2',
    'RE1',
    'RE2',
    'RE3',
    'S1',
    'S2',
    'T1',
    'T2',
    'HV',
    'HH',
    'VV',
    'VH',
    'kNN',
    'kNR',
    'kNB',
    'kNL',
    'kGG',
    'kGR',
    'kGB',
    'kBB',
    'kBR',
    'kBL',
    'kRR',
    'kRB',
    'kRL',
    'kLL'
]

bandsPlatform = {
    "Sentinel-1": [
        'HV',
        'HH',
        'VV',
        'VH'
    ],
    "Sentinel-2": [
        'A',
        'B',
        'G',
        'R',
        'N',
        'N2',
        'RE1',
        'RE2',
        'RE3',
        'S1',
        'S2',
        'kNN',
        'kNR',
        'kNB',
        'kNL',
        'kGG',
        'kGR',
        'kGB',
        'kBB',
        'kBR',
        'kBL',
        'kRR',
        'kRB',
        'kRL',
        'kLL'
    ],
    "Landsat-89": [
        'A',
        'B',
        'G',
        'R',
        'N',
        'S1',
        'S2',
        'T1',
        'T2',
        'kNN',
        'kNR',
        'kNB',
        'kNL',
        'kGG',
        'kGR',
        'kGB',
        'kBB',
        'kBR',
        'kBL',
        'kRR',
        'kRB',
        'kRL',
        'kLL'
    ],
    "Landsat-457": [
        'B',
        'G',
        'R',
        'N',
        'S1',
        'S2',
        'T1',
        'kNN',
        'kNR',
        'kNB',
        'kNL',
        'kGG',
        'kGR',
        'kGB',
        'kBB',
        'kBR',
        'kBL',
        'kRR',
        'kRB',
        'kRL',
        'kLL'
    ],
    "MODIS": [
        'B',
        'G',
        'R',
        'N',
        'S1',
        'S2',
        'kNN',
        'kNR',
        'kNB',
        'kNL',
        'kGG',
        'kGR',
        'kGB',
        'kBB',
        'kBR',
        'kBL',
        'kRR',
        'kRB',
        'kRL',
        'kLL'
    ],
    "Planet-Fusion": [
        'B',
        'G',
        'R',
        'N',
        'kNN',
        'kNR',
        'kNB',
        'kNL',
        'kGG',
        'kGR',
        'kGB',
        'kBB',
        'kBR',
        'kBL',
        'kRR',
        'kRB',
        'kRL',
        'kLL'
    ],
} 

bandsToCheck = list(Bands._value2member_map_.keys())
[bandsToCheck.remove(i) for i in bandVars]

def checkPlatforms(bandsSpindex):
    availablePlatforms = []
    for platform, bandList in bandsPlatform.items():
        if all([x in bandsToCheck + bandList for x in bandsSpindex]):
            availablePlatforms.append(platform)
    return availablePlatforms

parser = Parser()

# Adding band attribute
for key in spindex.SpectralIndices:
    SpectralIndex = spindex.SpectralIndices[key]
    formula = parser.parse(SpectralIndex.formula)
    SpectralIndex.bands = formula.variables()
    SpectralIndex.platforms = checkPlatforms(SpectralIndex.bands)
    spindex.SpectralIndices[key] = SpectralIndex

# ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square)
# ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square)
# ![Landsat-89](https://img.shields.io/badge/-Landsat%208,%209-blue?style=flat-square)
# ![Landsat-457](https://img.shields.io/badge/-Landsat%204,%205,%207-blueviolet?style=flat-square)
# ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)

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