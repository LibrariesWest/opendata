Items
=====

Our item data includes listings of items held by all 7 library services (millions of items). We are splitting out these exports to be one file per service, to make them more manageable. Plus, because we use GitHub for storage, there is a 100Mb file limit!

#### Summary file

A summary file gives some basic counts of items, aggregated by item type, and library service. In this case we have one summary file for all services.

- [View items summary data](https://github.com/LibrariesWest/opendata/blob/master/catalogue/items_summary.csv)

| Field | Decription | Example |
| ----- | ---------- | ------- |
| Authority | The authority holding the item | Bath and North East Somerset |
| Item type | The item type | Adult Fiction |
| Items | The total number of items | 10 |
| Issues | The total number of issues across those items | 100 |
| Renewals | The total number of renewals across those items | 100 |

#### Detail file

For more details use the full details download. This is split out to give a file per library service.

- [View Bath and North East Somerset Items](https://github.com/LibrariesWest/opendata/blob/master/catalogue/items_banes.csv)
- [View Bristol Items](https://github.com/LibrariesWest/opendata/blob/master/catalogue/items_bristol.csv)
- [View Dorset Items](https://github.com/LibrariesWest/opendata/blob/master/catalogue/items_dorset.csv)
- [View North Somerset Items](https://github.com/LibrariesWest/opendata/blob/master/catalogue/items_northsomerset.csv)
- [View Poole Items](https://github.com/LibrariesWest/opendata/blob/master/catalogue/items_poole.csv)
- [View Somerset Items](https://github.com/LibrariesWest/opendata/blob/master/catalogue/items_somerset.csv)
- [View South Gloucestershire Items](https://github.com/LibrariesWest/opendata/blob/master/catalogue/items_southglos.csv)

| Field | Decription | Example |
| ----- | ---------- | ------- |
| Catalogue flex key | A reference to the catalogue key, to match with a title record | i9780261670501 |
| Item ID | The ID for the item, also the printed barcode found on the item | 1804779308 |
| Authority | The authority holding the item | Bristol |
| Library | The library holding the item | Henleaze |
| Item type | The item type | Adult Fiction |
| Date created | The date the item was created in the system | 2015-03-14 |
| Price | A price for the item (not always reliable) | 3.99 |
| Issues | The total number of issues for the item | 8 |
| Renewals | The total number of renewals for the item | 6 |
