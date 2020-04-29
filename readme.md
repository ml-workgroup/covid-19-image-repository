COVID-19 Image Repository
=========================

Feature Set
-----------

| id |          label          |   unit | comment / reference interval (precision)   |
| -- | ----------------------- | -----: | ------------------------------------------ |
| 1  | patient_id              |        | randomly generated patient id              |
| 2  | sex                     |   m/w  |                                            |
| 3  | age                     | years  | currently redacted (see below)             |
| 4  | size                    |    cm  | currently redacted (see below)             |
| 5  | weight                  |    kg  | currently redacted (see below)             |
| 6  | admission offset        |  days  | days since admission (begin of symptoms)   |
| 7  | icu admission offset    |  days  |                                            |
| 8  | survival                |  days  | days until death or null                   |
| 9  | image_id                |        | randomly generated image id                |
| 10 | modality                |        | currently all images are chest radiographs |
| 11 | projection              |        | ap, pa ...                                 |
| 12 | lactate dehydrogenase   |   U/l  | < 248 (5)                                  |
| 13 | c-reactive protein      |  mg/l  | <= 5 (1)                                   |
| 14 | d-dimer                 |  mg/l  | 0 - 0.5 (0.1)                              |
| 15 | coagulation factor XIII |     %  | 70 - 140 (5)                               |
| 16 | neutrophils             | Tsd/µl | 1.5 - 7.7 (0.1)                            |
| 17 | lymphocytes             | Tsd/µl | 1.1 - 4.0 (0.1)                            |
| 18 | corona test type        |        |                                            |

Age, size and weight are currently redacted. We will publish this data when there are enough patients, that meaningfull intervals can be chosen according to the concept of k-anonymity and l-diversity. 

All lab values (12 - 17) are given in intervals to protect patient identity. A value below the detection limit is denoted by -2, above the detection limit by -1. 
