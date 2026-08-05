from enum import Enum, unique


@unique
class Bands(Enum):
    """
    Bands supported by SpectralIndex DataClass
    """

    AEROSOL = "A"
    BLUE = "B"
    GREEN1 = "G1"
    GREEN = "G"
    YELLOW = "Y"
    RED = "R"
    NIR = "N"
    NIR2 = "N2"
    WATERVAPOUR = "WV"
    RED1 = "RE1"
    RED2 = "RE2"
    RED3 = "RE3"
    SWIR1 = "S1"
    SWIR2 = "S2"
    TIR = "T"
    TIR1 = "T1"
    TIR2 = "T2"
    HV = "HV"
    HH = "HH"
    VV = "VV"
    VH = "VH"
@unique
class Constants(Enum):
    """Constants supported by spectral-index formulas."""

    GAIN_FACTOR = "g"
    CANOPY_BACKGROUND_ADJUSTMENT = "L"
    AEROSOL_COEFFICIENT1 = "C1"
    AEROSOL_COEFFICIENT2 = "C2"
    GAMMA = "gamma"
    ALPHA = "alpha"
    BETA = "beta"
    SOIL_LINE_SLOPE = "sla"
    SOIL_LINE_INTERCEPT = "slb"
    OMEGA = "omega"
    F_DELTA = "fdelta"
    EPSILON = "epsilon"
    SLOPE_PARAMETER_SOIL = "k"
    N_FACTOR = "n"
    LAMBDA = "lmb"
    ETA = "eta"
    NEG_ABSCISSA = "X"
    EMPIRICAL_PARAMETER_A = "a"
    EMPIRICAL_PARAMETER_B = "b"
    CENTRAL_WAVELENGTH_NIR = "lambdaN"
    CENTRAL_WAVELENGTH_NIR2 = "lambdaN2"
    CENTRAL_WAVELENGTH_RED = "lambdaR"
    CENTRAL_WAVELENGTH_GREEN = "lambdaG"
    CENTRAL_WAVELENGTH_SWIR1 = "lambdaS1"
    CENTRAL_WAVELENGTH_SWIR2 = "lambdaS2"
    KERNEL_LENGTH_SCALE = "sigma"
    KERNEL_DEGREE = "p"
    KERNEL_TRADE_OFF = "c"


@unique
class External(Enum):
    """External variables supported by spectral-index formulas."""

    PAR = "PAR"


class IndexType(Enum):
    """
    IndexType supported by SpectralIndex DataClass
    """

    VEGETATION = "vegetation"
    WATER = "water"
    BURN = "burn"
    SNOW = "snow"
    SOIL = "soil"
    URBAN = "urban"
    KERNEL = "kernel"
    CLOUDS = "clouds"
    RADAR = "radar"
