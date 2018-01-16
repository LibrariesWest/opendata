Rain
====

Historic precipitation data is available through the Met Office Hadley Centre observations datasets: HadUKP.

HadUKP is a series of datasets of UK regional precipitation, which incorporates the long-running England & Wales Precipitation (EWP) series beginning in 1766, the longest instrumental series of this kind in the world.

The data is available on a regional basis so we have taken a copy of the South West daily totals data. These provide a daily precipitation value since 1931. This data is provided as a text file with a row for each month, values separated by spaces. A python script in this repository converts the data into a friendlier CSV file.

- [Download HadSWEP CSV](./HadSWEP.csv)

| Field | Description | Example |
| ----- | ----------- | ------- |
| Date | The date measured | 2016-06-19 |
| Precipitation | Daily Southwest England & Wales precipitation (mm) | 21.50 |

#### Licence

Data is made available under the Open Government Licence, with a requirement to attribute the original source, which is the [Met Office Hadley Centre](https://www.metoffice.gov.uk/hadobs/hadukp/).
