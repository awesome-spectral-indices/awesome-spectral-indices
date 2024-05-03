constants = {
    "L": {
        "short_name": "L",
        "description": "Canopy background adjustment",
        "default": 1.0,
    },
    "g": {"short_name": "g", "description": "Gain factor", "default": 2.5},
    "C1": {
        "short_name": "C1",
        "description": "Coefficient 1 for the aerosol resistance term",
        "default": 6.0,
    },
    "C2": {
        "short_name": "C2",
        "description": "Coefficient 2 for the aerosol resistance term",
        "default": 7.5,
    },
    "cexp": {
        "short_name": "cexp",
        "description": "Exponent used for OCVI",
        "default": 1.16,
    },
    "nexp": {
        "short_name": "nexp",
        "description": "Exponent used for GDVI",
        "default": 2.0,
    },
    "alpha": {
        "short_name": "alpha",
        "description": "Weighting coefficient used for WDRVI",
        "default": 0.1,
    },
    "beta": {
        "short_name": "beta",
        "description": "Calibration parameter used for NDSInw",
        "default": 0.05,
    },
    "gamma": {
        "short_name": "gamma",
        "description": "Weighting coefficient used for ARVI",
        "default": 1.0,
    },
    "omega": {
        "short_name": "omega",
        "description": "Weighting coefficient used for MBWI",
        "default": 2.0,
    },
    "k": {
        "short_name": "k",
        "description": "Slope parameter by soil used for NIRvH2",
        "default": 0.0,
    },
    "PAR": {
        "short_name": "PAR",
        "description": "Photosynthetically Active Radiation",
        "default": None,
    },
    "lambdaG": {
        "short_name": "lambdaG",
        "description": "Green central wavelength (nm)",
        "default": None,
    },
    "lambdaR": {
        "short_name": "lambdaR",
        "description": "Red central wavelength (nm)",
        "default": None,
    },
    "lambdaN": {
        "short_name": "lambdaN",
        "description": "NIR central wavelength (nm)",
        "default": None,
    },
    "lambdaS1": {
        "short_name": "lambdaS1",
        "description": "SWIR1 central wavelength (nm)",
        "default": None,
    },
    "sla": {
        "short_name": "sla",
        "description": "Soil line slope",
        "default": 1.0,
    },
    "slb": {
        "short_name": "slb",
        "description": "Soil line intercept",
        "default": 0.0,
    },
    "sigma": {
        "short_name": "sigma",
        "description": "Length-scale parameter in the RBF kernel",
        "default": 0.5,
    },
    "p": {
        "short_name": "p",
        "description": "Kernel degree in the polynomial kernel",
        "default": 2.0,
    },
    "c": {
        "short_name": "c",
        "description": "Trade-off parameter in the polynomial kernel",
        "default": 1.0,
    },
    "fdelta": {
        "short_name": "fdelta",
        "description": "Adjustment factor used for SEVI",
        "default": 0.581,
    },
    "epsilon": {
        "short_name": "epsilon",
        "description": "Adjustment constant used for EBI",
        "default": 1,
    },
}
