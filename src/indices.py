from src.SpectralIndex import SpectralIndex
from typing import Dict
from pydantic import BaseModel


class SpectralIndices(BaseModel):
    SpectralIndices: Dict[str, SpectralIndex]


spindex = SpectralIndices(
    SpectralIndices=dict(
        BNDVI=SpectralIndex(
            short_name='BNDVI',
            long_name='Blue Normalized Difference Vegetation Index',
            formula='(N - B)/(N + B)',            
            reference='https://www.indexdatabase.de/db/i-single.php?id=135',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        CIG=SpectralIndex(
            short_name='CIG',
            long_name='Chlorophyll Index Green',
            formula='(N / G) - 1.0',            
            reference='https://www.indexdatabase.de/db/i-single.php?id=391',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        CVI=SpectralIndex(
            short_name='CVI',
            long_name='Chlorophyll Vegetation Index',
            formula='(N * R) / (G ** 2.0)',            
            reference='https://www.indexdatabase.de/db/i-single.php?id=391',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        EVI=SpectralIndex(
            short_name='EVI',
            long_name='Enhanced Vegetation Index',
            formula='g * (N - R) / (N + C1 * R - C2 * B + L)',            
            reference='https://www.indexdatabase.de/db/i-single.php?id=16',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        EVI2=SpectralIndex(
            short_name='EVI2',
            long_name='Two-Band Enhanced Vegetation Index',
            formula='g * (N - R) / (N + 2.4 * R + L)',
            reference='https://doi.org/10.1016/j.rse.2008.06.006',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GARI=SpectralIndex(
            short_name='GARI',
            long_name='Green Atmospherically Resistant Vegetation Index',
            formula='(N - (G - (B - R))) / (N - (G + (B - R)))',
            reference='https://www.indexdatabase.de/db/i-single.php?id=363',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GBNDVI=SpectralIndex(
            short_name='GBNDVI',
            long_name='Green-Blue Normalized Difference Vegetation Index',
            formula='(N - (G + B))/(N + (G + B))',
            reference='https://www.indexdatabase.de/db/i-single.php?id=186',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GEMI=SpectralIndex(
            short_name='GEMI',
            long_name='Global Environment Monitoring Index',
            formula='((2.0*((N ** 2.0)-(R ** 2.0)) + 1.5*N + 0.5*R)/(N + R + 0.5))*(1.0 - 0.25*((2.0 * ((N ** 2.0) - (R ** 2)) + 1.5 * N + 0.5 * R)/(N + R + 0.5)))-((R - 0.125)/(1 - R))',
            reference='https://www.indexdatabase.de/db/i-single.php?id=25',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GLI=SpectralIndex(
            short_name='GLI',
            long_name='Green Leaf Index',
            formula='(2.0 * G - R - B) / (2.0 * G + R + B)',
            reference='https://www.indexdatabase.de/db/i-single.php?id=375',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GNDVI=SpectralIndex(
            short_name='GNDVI',
            long_name='Green Normalized Difference Vegetation Index',
            formula='(N - G)/(N + G)',
            reference='https://www.indexdatabase.de/db/i-single.php?id=401',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GRNDVI=SpectralIndex(
            short_name='GRNDVI',
            long_name='Green-Red Normalized Difference Vegetation Index',
            formula='(N - (G + R))/(N + (G + R))',
            reference='https://www.indexdatabase.de/db/i-single.php?id=185',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GVMI=SpectralIndex(
            short_name='GVMI',
            long_name='Global Vegetation Moisture Index',
            formula='((N + 0.1) - (S2 + 0.02)) / ((N + 0.1) + (S2 + 0.02))',
            reference='https://www.indexdatabase.de/db/i-single.php?id=372',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        MNDVI=SpectralIndex(
            short_name='MNDVI',
            long_name='Modified Normalized Difference Vegetation Index',
            formula='(N - S2)/(N + S2)',
            reference='https://www.indexdatabase.de/db/i-single.php?id=245',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NDVI=SpectralIndex(
            short_name='NDVI',
            long_name='Normalized Difference Vegetation Index',
            formula='(N - R)/(N + R)',
            reference='https://www.indexdatabase.de/db/i-single.php?id=58',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NGRDI=SpectralIndex(
            short_name='NGRDI',
            long_name='Normalized Green Red Difference Index',
            formula='(G - R) / (G + R)',
            reference='https://www.indexdatabase.de/db/i-single.php?id=390',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        RVI=SpectralIndex(
            short_name='RVI',
            long_name='Ratio Vegetation Index',
            formula='N / R',
            reference='https://www.indexdatabase.de/db/i-single.php?id=72',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        SAVI=SpectralIndex(
            short_name='SAVI',
            long_name='Soil-Adjusted Vegetation Index',
            formula='(1.0 + L) * (N - R) / (N + R + L)',
            reference='https://www.indexdatabase.de/db/i-single.php?id=87',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        VARI=SpectralIndex(
            short_name='VARI',
            long_name='Visible Atmospherically Resistant Index',
            formula='(G - R) / (G + R - B)',
            reference='https://www.indexdatabase.de/db/i-single.php?id=356',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        BAI=SpectralIndex(
            short_name='BAI',
            long_name='Burned Area Index',
            formula='1.0 / ((0.1 - R) ** 2.0 + (0.06 - N) ** 2.0)',
            reference='https://digital.csic.es/bitstream/10261/6426/1/Martin_Isabel_Serie_Geografica.pdf',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        BAIS2=SpectralIndex(
            short_name='BAIS2',
            long_name='Burned Area Index for Sentinel 2',
            formula='(1.0 - ((RE2 * RE3 * RE4) / R) ** 0.5) * (((S2 - RE4)/(S2 + RE4) ** 0.5) + 1.0)',
            reference='https://doi.org/10.3390/ecrs-2-05177',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        CSIT=SpectralIndex(
            short_name='CSIT',
            long_name='Char Soil Index Thermal',
            formula='N / (S2 * T1 / 10000.0)',
            reference='https://doi.org/10.1080/01431160600954704',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NBR=SpectralIndex(
            short_name='NBR',
            long_name='Normalized Burn Ratio',
            formula='(N - S2) / (N + S2)',
            reference='https://www.indexdatabase.de/db/i-single.php?id=53',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NBRT=SpectralIndex(
            short_name='NBRT',
            long_name='Normalized Burn Ratio Thermal',
            formula='(N - (S2 * T1 / 10000.0)) / (N + (S2 * T1 / 10000.0))',
            reference='https://doi.org/10.1080/01431160500239008',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NDVIT=SpectralIndex(
            short_name='NDVIT',
            long_name='Normalized Difference Vegetation Index Thermal',
            formula='(N - (R * T1 / 10000.0))/(N + (R * T1 / 10000.0))',
            reference='https://doi.org/10.1080/01431160600954704',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        SAVIT=SpectralIndex(
            short_name='SAVIT',
            long_name='Soil-Adjusted Vegetation Index Thermal',
            formula='(1.0 + L) * (N - (R * T1 / 10000.0)) / (N + (R * T1 / 10000.0) + L)',
            reference='https://doi.org/10.1080/01431160600954704',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        MNDWI=SpectralIndex(
            short_name='MNDWI',
            long_name='Modified Normalized Difference Water Index',
            formula='(G - S1) / (G + S1)',
            reference='https://doi.org/10.1080/01431160600589179',
            type='water',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NDWI=SpectralIndex(
            short_name='NDWI',
            long_name='Normalized Difference Water Index',
            formula='(G - N) / (G + N)',
            reference='https://doi.org/10.1080/01431169608948714',
            type='water',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NDSI=SpectralIndex(
            short_name='NDSI',
            long_name='Normalized Difference Snow Index',
            formula='(G - S1) / (G + S1)',
            reference='https://doi.org/10.1109/IGARSS.1994.399618',
            type='snow',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NDDI=SpectralIndex(
            short_name='NDDI',
            long_name='Normalized Difference Drought Index',
            formula='(((N - R)/(N + R)) - ((G - N)/(G + N)))/(((N - R)/(N + R)) + ((G - N)/(G + N)))',
            reference='https://doi.org/10.1029/2006GL029127',
            type='drought',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        kEVI=SpectralIndex(
            short_name='kEVI',
            long_name='Kernel Enhanced Vegetation Index',
            formula='g * (kNN - kNR) / (kNN + C1 * kNR - C2 * kNB + kNL)',
            reference='https://doi.org/10.1126/sciadv.abc7447',
            type='kernel',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        kNDVI=SpectralIndex(
            short_name='kNDVI',
            long_name='Kernel Normalized Difference Vegetation Index',
            formula='(kNN - kNR)/(kNN + kNR)',
            reference='https://doi.org/10.1126/sciadv.abc7447',
            type='kernel',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        kRVI=SpectralIndex(
            short_name='kRVI',
            long_name='Kernel Ratio Vegetation Index',
            formula='kNN / kNR',
            reference='https://doi.org/10.1126/sciadv.abc7447',
            type='kernel',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        kVARI=SpectralIndex(
            short_name='kVARI',
            long_name='Kernel Visible Atmospherically Resistant Index',
            formula='(kGG - kGR) / (kGG + kGR - kGB)',
            reference='https://doi.org/10.1126/sciadv.abc7447',
            type='kernel',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        SeLI=SpectralIndex(
            short_name='SeLI',
            long_name='Sentinel-2 LAI Green Index',
            formula='(RE4 - RE1) / (RE4 + RE1)',
            reference='https://doi.org/10.3390/s19040904',
            type='vegetation',
            date_of_addition='2021-04-08',
            contributor="https://github.com/davemlz"
        )        
    )
)
