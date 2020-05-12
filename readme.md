COVID-19 Image Repository
=========================
The aim of this project is to make an anonymized data set of COVID-19 positive patients with a focus on radiological imaging publicly available. This data set includes master-, image- and laboratory-data.

The repository contains image data from the [Institute for Diagnostic and Interventional Radiology][radiology mhh], Hannover Medical School, Hannover, Germany.


Download
--------
The Dicom files have been converted to Nifti. We are currently working on making the Nifti files publicly available. Unfortunately, the files are too large to host them on Github. For the moment, please send us an EMail (see Contact Information), we will figure out a way to get the images to you.

We included downscaled versions of the Nifti images in the png folder.


Feature Set
-----------

| id |          label          |   unit | comment / reference interval (precision)   |
| -- | ----------------------- | -----: | ------------------------------------------ |
| 1  | patient_id              |        | randomly generated patient id              |
| 2  | image_id                |        | randomly generated image id (filename)     |
| 3  | sex                     |   m/w  |                                            |
| 4  | age                     | years  | currently redacted (see below)             |
| 5  | size                    |    cm  | currently redacted (see below)             |
| 6  | weight                  |    kg  | currently redacted (see below)             |
| 7  | admission offset        |  days  | days since admission (begin of symptoms)   |
| 8  | icu admission offset    |  days  |                                            |
| 9  | death_offset            |  days  | days until death or null                   |
| 10 | modality                |        | currently all images are chest radiographs |
| 11 | projection              |        | ap, pa ...                                 |
| 12 | lactate dehydrogenase   |   U/l  | < 248 (5)                                  |
| 13 | c-reactive protein      |  mg/l  | <= 5 (1)                                   |
| 14 | d-dimer                 |  mg/l  | 0 - 0.5 (0.1)                              |
| 15 | coagulation factor XIII |     %  | 70 - 140 (5)                               |
| 16 | neutrophils             | Tsd/µl | 1.5 - 7.7 (0.1)                            |
| 17 | lymphocytes             | Tsd/µl | 1.1 - 4.0 (0.1)                            |
| 18 | pO2                     |   mmHg | (5)                                        |
| 19 | pCO2                    |   mmHg | (5)                                        |
| 20 | corona test type        |        |                                            |

Age, size, and weight are currently redacted. We will publish this data when there are enough patients, that meaningfull intervals can be chosen according to the concept of k-anonymity and l-diversity. 

All lab values (12 - 19) are given in intervals to protect patient identity. A value below the detection limit is denoted by `-inf`, above the detection limit by `inf`.


Observations (FAQ)
------------------
  - admission offset > icu admission offset  
    Some of the cases suggest that the admission to the clinic was after admission to the ICU. This is an artifact due to using the specific (COVID) case data for determining the admission date (and therefore offset). The patient may have already been at the ICU before being diagnosed with COVID.


License and Attribution
-----------------------
Master-, image- and laboratory-data of this repository are licensed under the Creative Commons Attribution 3.0 Unported ([CC BY 3.0]).

If you use this data, you must attribute the authors in any publication (DOI: [10.6084/m9.figshare.12275009][DOI]). You may include the specific [release] or [commit hash][commits] for reproducibility.


Contact Information
-------------------
Please use the ticketing system where applicable. Otherwise, please use the following EMail address: winther.hinrich@mh-hannover.de



[radiology mhh]: https://www.mhh.de/institute-zentren-forschungseinrichtungen/institut-fuer-diagnostische-und-interventionelle-radiologie
[CC BY 3.0]: https://creativecommons.org/licenses/by/3.0/
[DOI]:       https://doi.org/10.6084/m9.figshare.12275009
[release]:   https://github.com/ml-workgroup/covid-19-image-repository/releases
[commits]:   https://github.com/ml-workgroup/covid-19-image-repository/commits/
