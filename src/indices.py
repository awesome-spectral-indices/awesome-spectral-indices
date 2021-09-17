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
            reference='https://doi.org/10.1078/0176-1617-00887',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        CVI=SpectralIndex(
            short_name='CVI',
            long_name='Chlorophyll Vegetation Index',
            formula='(N * R) / (G ** 2.0)',            
            reference='https://www.cabdirect.org/cabdirect/abstract/20073176046',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        EVI=SpectralIndex(
            short_name='EVI',
            long_name='Enhanced Vegetation Index',
            formula='g * (N - R) / (N + C1 * R - C2 * B + L)',            
            reference='https://doi.org/10.1016/S0034-4257(96)00112-5',
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
            reference='http://dx.doi.org/10.1007/bf00031911',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GLI=SpectralIndex(
            short_name='GLI',
            long_name='Green Leaf Index',
            formula='(2.0 * G - R - B) / (2.0 * G + R + B)',
            reference='http://dx.doi.org/10.1080/10106040108542184',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GNDVI=SpectralIndex(
            short_name='GNDVI',
            long_name='Green Normalized Difference Vegetation Index',
            formula='(N - G)/(N + G)',
            reference='https://doi.org/10.1016/S0034-4257(96)00072-7',
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
            reference='https://doi.org/10.1016/S0034-4257(02)00037-8',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        MNDVI=SpectralIndex(
            short_name='MNDVI',
            long_name='Modified Normalized Difference Vegetation Index',
            formula='(N - S2)/(N + S2)',
            reference='https://doi.org/10.1080/014311697216810',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NDVI=SpectralIndex(
            short_name='NDVI',
            long_name='Normalized Difference Vegetation Index',
            formula='(N - R)/(N + R)',
            reference='https://doi.org/10.1016/0034-4257(79)90013-0',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NGRDI=SpectralIndex(
            short_name='NGRDI',
            long_name='Normalized Green Red Difference Index',
            formula='(G - R) / (G + R)',
            reference='https://doi.org/10.1016/0034-4257(79)90013-0',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        RVI=SpectralIndex(
            short_name='RVI',
            long_name='Ratio Vegetation Index',
            formula='N / R',
            reference='https://doi.org/10.2134/agronj1968.00021962006000060016x',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        SAVI=SpectralIndex(
            short_name='SAVI',
            long_name='Soil-Adjusted Vegetation Index',
            formula='(1.0 + L) * (N - R) / (N + R + L)',
            reference='https://doi.org/10.1016/0034-4257(88)90106-X',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        VARI=SpectralIndex(
            short_name='VARI',
            long_name='Visible Atmospherically Resistant Index',
            formula='(G - R) / (G + R - B)',
            reference='https://doi.org/10.1016/S0034-4257(01)00289-9',
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
            date_of_addition='2021-05-10',
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
            date_of_addition='2021-05-10',
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
        ),
        OSAVI=SpectralIndex(
            short_name='OSAVI',
            long_name='Optimized Soil-Adjusted Vegetation Index',
            formula='(N - R) / (N + R + 0.16)',
            reference='https://doi.org/10.1016/0034-4257(95)00186-7',
            type='vegetation',
            date_of_addition='2021-05-11',
            contributor="https://github.com/davemlz"
        ),
        ARVI=SpectralIndex(
            short_name='ARVI',
            long_name='Atmospherically Resistant Vegetation Index',
            formula='(N - (R - (R - B))) / (N + (R - (R - B)))',
            reference='https://doi.org/10.1109/36.134076',
            type='vegetation',
            date_of_addition='2021-05-11',
            contributor="https://github.com/davemlz"
        ),
        SARVI=SpectralIndex(
            short_name='SARVI',
            long_name='Soil Adjusted and Atmospherically Resistant Vegetation Index',
            formula='(1 + L)*(N - (R - (R - B))) / (N + (R - (R - B)) + L)',
            reference='https://doi.org/10.1109/36.134076',
            type='vegetation',
            date_of_addition='2021-05-11',
            contributor="https://github.com/davemlz"
        ),
        NLI=SpectralIndex(
            short_name='NLI',
            long_name='Non-Linear Vegetation Index',
            formula='((N ** 2) - R)/((N ** 2) + R)',
            reference='https://doi.org/10.1080/02757259409532252',
            type='vegetation',
            date_of_addition='2021-05-11',
            contributor="https://github.com/davemlz"
        ),
        MNLI=SpectralIndex(
            short_name='MNLI',
            long_name='Modified Non-Linear Vegetation Index',
            formula='(1 + L)*((N ** 2) - R)/((N ** 2) + R + L)',
            reference='https://doi.org/10.1109/TGRS.2003.812910',
            type='vegetation',
            date_of_addition='2021-05-11',
            contributor="https://github.com/davemlz"
        ),
        NMDI=SpectralIndex(
            short_name='NMDI',
            long_name='Normalized Multi‐band Drought Index',
            formula='(N - (S1 - S2))/(N + (S1 - S2))',
            reference='https://doi.org/10.1029/2007GL031021',
            type='drought',
            date_of_addition='2021-05-11',
            contributor="https://github.com/davemlz"
        ),
        MSAVI=SpectralIndex(
            short_name='MSAVI',
            long_name='Modified Soil-Adjusted Vegetation Index',
            formula='0.5 * (2.0 * N + 1 - (((2 * N + 1) ** 2) - 8 * (N - R)) ** 0.5)',
            reference='https://doi.org/10.1016/0034-4257(94)90134-1',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        MCARI=SpectralIndex(
            short_name='MCARI',
            long_name='Modified Chlorophyll Absorption in Reflectance Index',
            formula='((RE1 - R) - 0.2 * (RE1 - G)) * (RE1 / R)',
            reference='http://dx.doi.org/10.1016/S0034-4257(00)00113-9',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        OCVI=SpectralIndex(
            short_name='OCVI',
            long_name='Optimized Chlorophyll Vegetation Index',
            formula='(N / G) * (R / G) ** cexp',            
            reference='http://dx.doi.org/10.1007/s11119-008-9075-z',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        NDREI=SpectralIndex(
            short_name='NDREI',
            long_name='Normalized Difference Red Edge Index',
            formula='(N - RE1) / (N + RE1)',            
            reference='https://doi.org/10.1016/1011-1344(93)06963-4',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        CIRE=SpectralIndex(
            short_name='CIRE',
            long_name='Chlorophyll Index Red Edge',
            formula='(N / RE1) - 1',            
            reference='https://doi.org/10.1078/0176-1617-00887',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        MTCI=SpectralIndex(
            short_name='MTCI',
            long_name='MERIS Terrestrial Chlorophyll Index',
            formula='(RE2 - RE1) / (RE1 - R)',            
            reference='https://doi.org/10.1080/0143116042000274015',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        TCARI=SpectralIndex(
            short_name='TCARI',
            long_name='Transformed Chlorophyll Absorption in Reflectance Index',
            formula='3 * ((RE1 - R) - 0.2 * (RE1 - G) * (RE1 / R))',
            reference='https://doi.org/10.1016/S0034-4257(02)00018-4',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        GDVI=SpectralIndex(
            short_name='GDVI',
            long_name='Generalized Difference Vegetation Index',
            formula='((N ** nexp) - (R ** nexp)) / ((N ** nexp) + (R ** nexp))',
            reference='https://doi.org/10.3390/rs6021211',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        WDRVI=SpectralIndex(
            short_name='WDRVI',
            long_name='Wide Dynamic Range Vegetation Index',
            formula='(alpha * N - R) / (alpha * N + R)',
            reference='https://doi.org/10.1078/0176-1617-01176',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        MCARI1=SpectralIndex(
            short_name='MCARI1',
            long_name='Modified Chlorophyll Absorption in Reflectance Index 1',
            formula='1.2 * (2.5 * (N - R) - 1.3 * (N - G))',
            reference='https://doi.org/10.1016/j.rse.2003.12.013',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        MTVI1=SpectralIndex(
            short_name='MTVI1',
            long_name='Modified Triangular Vegetation Index 1',
            formula='1.2 * (1.2 * (N - G) - 2.5 * (R - G))',
            reference='https://doi.org/10.1016/j.rse.2003.12.013',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        MCARI2=SpectralIndex(
            short_name='MCARI2',
            long_name='Modified Chlorophyll Absorption in Reflectance Index 2',
            formula='(1.5 * (2.5 * (N - R) - 1.3 * (N - G))) / ((((2.0 * N + 1) ** 2) - (6.0 * N - 5 * (R ** 0.5)) - 0.5) ** 0.5)',
            reference='https://doi.org/10.1016/j.rse.2003.12.013',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        MTVI2=SpectralIndex(
            short_name='MTVI2',
            long_name='Modified Triangular Vegetation Index 2',
            formula='(1.5 * (1.2 * (N - G) - 2.5 * (R - G))) / ((((2.0 * N + 1) ** 2) - (6.0 * N - 5 * (R ** 0.5)) - 0.5) ** 0.5)',
            reference='https://doi.org/10.1016/j.rse.2003.12.013',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        TVI=SpectralIndex(
            short_name='TVI',
            long_name='Triangular Vegetation Index',
            formula='0.5 * (120 * (N - G) - 200 * (R - G))',
            reference='http://dx.doi.org/10.1016/S0034-4257(00)00197-8',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        MSR=SpectralIndex(
            short_name='MSR',
            long_name='Modified Simple Ratio',
            formula='(N / R - 1) / ((N / R + 1) ** 0.5)',
            reference='https://doi.org/10.1080/07038992.1996.10855178',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        RDVI=SpectralIndex(
            short_name='RDVI',
            long_name='Renormalized Difference Vegetation Index',
            formula='(N - R) / ((N + R) ** 0.5)',
            reference='https://doi.org/10.1016/0034-4257(94)00114-3',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        NDBI=SpectralIndex(
            short_name='NDBI',
            long_name='Normalized Difference Built-Up Index',
            formula='(S1 - N) / (S1 + N)',
            reference='http://dx.doi.org/10.1080/01431160304987',
            type='urban',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        MGRVI=SpectralIndex(
            short_name='MGRVI',
            long_name='Modified Green Red Vegetation Index',
            formula='(G ** 2.0 - R ** 2.0) / (G ** 2.0 + R ** 2.0)',
            reference='https://doi.org/10.1016/j.jag.2015.02.012',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        ExG=SpectralIndex(
            short_name='ExG',
            long_name='Excess Green Index',
            formula='2 * G - R - B',
            reference='https://doi.org/10.13031/2013.27838',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        DVI=SpectralIndex(
            short_name='DVI',
            long_name='Difference Vegetation Index',
            formula='N - R',
            reference='https://doi.org/10.2307/1936256',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        WDVI=SpectralIndex(
            short_name='WDVI',
            long_name='Weighted Difference Vegetation Index',
            formula='N - sla * R',
            reference='https://doi.org/10.1016/0034-4257(89)90076-X',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        TSAVI=SpectralIndex(
            short_name='TSAVI',
            long_name='Transformed Soil-Adjusted Vegetation Index',
            formula='sla * (N - sla * R - slb) / (sla * N + R - sla * slb)',
            reference='https://doi.org/10.1109/IGARSS.1989.576128',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        ATSAVI=SpectralIndex(
            short_name='ATSAVI',
            long_name='Adjusted Transformed Soil-Adjusted Vegetation Index',
            formula='sla * (N - sla * R - slb) / (sla * N + R - sla * slb + 0.08 * (1 + sla ** 2.0))',
            reference='https://doi.org/10.1016/0034-4257(91)90009-U',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        SAVI2=SpectralIndex(
            short_name='SAVI2',
            long_name='Soil-Adjusted Vegetation Index 2',
            formula='N / (R + (slb / sla))',
            reference='https://doi.org/10.1080/01431169008955053',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        TCI=SpectralIndex(
            short_name='TCI',
            long_name='Triangular Chlorophyll Index',
            formula='1.2 * (RE1 - G) - 1.5 * (R - G) * (RE1 / R) ** 0.5',
            reference='http://dx.doi.org/10.1109/TGRS.2007.904836',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        TGI=SpectralIndex(
            short_name='TGI',
            long_name='Triangular Greenness Index',
            formula='- 0.5 * (190 * (R - G) - 120 * (R - B))',
            reference='http://dx.doi.org/10.1016/j.jag.2012.07.020',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        IRECI=SpectralIndex(
            short_name='IRECI',
            long_name='Inverted Red-Edge Chlorophyll Index',
            formula='(RE3 - R) / (RE1 / RE2)',
            reference='https://doi.org/10.1016/j.isprsjprs.2013.04.007',
            type='vegetation',
            date_of_addition='2021-09-17',
            contributor="https://github.com/davemlz"
        ),
        S2REP=SpectralIndex(
            short_name='S2REP',
            long_name='Sentinel-2 Red-Edge Position',
            formula='705.0 + 35.0 * ((((RE3 + R) / 2.0) - RE1) / (RE2 - RE1))',
            reference='https://doi.org/10.1016/j.isprsjprs.2013.04.007',
            type='vegetation',
            date_of_addition='2021-09-17',
            contributor="https://github.com/davemlz"
        ),
        EBBI=SpectralIndex(
            short_name='EBBI',
            long_name='Enhanced Built-Up and Bareness Index',
            formula='(S1 - N) / (10.0 * ((S1 + T1) ** 0.5))',
            reference='https://doi.org/10.3390/rs4102957',
            type='urban',
            date_of_addition='2021-09-17',
            contributor="https://github.com/davemlz"
        ),
        NDBaI=SpectralIndex(
            short_name='NDBaI',
            long_name='Normalized Difference Bareness Index',
            formula='(S1 - T1) / (S1 + T1)',
            reference='https://doi.org/10.1109/IGARSS.2005.1526319',
            type='urban',
            date_of_addition='2021-09-17',
            contributor="https://github.com/davemlz"
        ),
        SIPI=SpectralIndex(
            short_name='SIPI',
            long_name='Structure Insensitive Pigment Index',
            formula='(N - A) / (N - R)',
            reference='https://eurekamag.com/research/009/395/009395053.php',
            type='vegetation',
            date_of_addition='2021-09-17',
            contributor="https://github.com/davemlz"
        ),
        NHFD=SpectralIndex(
            short_name='NHFD',
            long_name='Non-Homogeneous Feature Difference',
            formula='(RE1 - A) / (RE1 + A)',
            reference='https://www.semanticscholar.org/paper/Using-WorldView-2-Vis-NIR-MSI-Imagery-to-Support-Wolf/5e5063ccc4ee76b56b721c866e871d47a77f9fb4',
            type='urban',
            date_of_addition='2021-09-17',
            contributor="https://github.com/davemlz"
        ),
    )
)
