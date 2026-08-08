import re
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


class Hyperspectral:
    """Range-based hyperspectral reflectance standards used in formulas."""

    PREFIX = "R"
    MIN_WAVELENGTH = 300
    MAX_WAVELENGTH = 2500
    _PATTERN = re.compile(r"R([1-9][0-9]*)")

    @classmethod
    def wavelength(cls, value):
        """Return the wavelength encoded by a valid standard, otherwise None."""
        if not isinstance(value, str):
            return None
        match = cls._PATTERN.fullmatch(value)
        if match is None:
            return None
        wavelength = int(match.group(1))
        if cls.MIN_WAVELENGTH <= wavelength <= cls.MAX_WAVELENGTH:
            return wavelength
        return None

    @classmethod
    def is_band(cls, value):
        """Return whether a variable is a canonical hyperspectral band name."""
        return cls.wavelength(value) is not None


@unique
class Polarizations(Enum):
    """Radar polarizations supported by spectral-index formulas."""

    HH = "HH"
    HV = "HV"
    VH = "VH"
    VV = "VV"


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


@unique
class ApplicationDomain(Enum):
    """Application domains supported by the v1 catalogue."""

    VEGETATION = "vegetation"
    WATER = "water"
    BURN = "burn"
    SNOW = "snow"
    SOIL = "soil"
    URBAN = "urban"
    GEOLOGY = "geology"
    CLOUDS = "clouds"


@unique
class SensingModality(Enum):
    """Sensing modalities generated from formula input standards."""

    MULTISPECTRAL = "multispectral"
    HYPERSPECTRAL = "hyperspectral"
    THERMAL = "thermal"
    RADAR = "radar"


@unique
class IndexFamily(Enum):
    """Optional scientific families assigned to spectral indices."""

    KERNEL = "kernel"
    TASSELED_CAP = "tasseled_cap"
    RADAR = "radar"
