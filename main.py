from src.indices import spindex
from py_expression_eval import Parser

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