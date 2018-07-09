Active members by area
======================

#### Summary

Summary data provides basic active member counts per library.

- [Download membership summary data](https://github.com/LibrariesWest/opendata/blob/master/membership/members_summary.csv)

| Field | Description | Example |
| ----- | ----------- | ------- |
| Registered authority | The library authority the users are registered with | Bath and North East Somerset |
| Users | The number of users, to the nearest 10 | 100 |

#### Detail

Further detail breaks down the membership counts into statistical areas that represent where members are based. These are listed by county, district, and super output areas. For more info on these see our [geography data](./../geography/README.md)

Because this data is reported at fairly detailed geographic detail, we suppress reporting of values less than 5, by using a * in place of a number. This should be taken into account when using the data, and trying to sum the values of members in each area. For more accurate total numbers you would be better off using the summary data which is correct to the nearest 10 people.

| Field | Description | Example |
| ----- | ----------- | ------- |
| Registered authority | The library authority the users are registered with | Bath and North East Somerset |
| Registered library | The library the users are registered with | Bath Central |
| District name | The local authority district | Sedgemoor District |
| District code | The 9 character code for the local authority district  | E07000188 |
| County name | The county name | Somerset County |
| County code | The 9 character code for the county | E10000027 |
| Ward name | The descriptive name for the local government Ward | Huntspill and Pawlett Ward |
| Ward code | The 9 character code for the local government Ward | E05008908 |
| MSOA name | The descriptive name for the middle layer super output area | Sedgemoor 006 |
| MSOA code | The 9 character code for the middle layer super output area | E02006066 |
| LSOA name | The descriptive name for the lower layer super output area | Sedgemoor 006A |
| LSOA code | The 9 character code for the lower layer super output area | E01029135 |
| Users | The number of registered members in this grouping | 60 |

(Note: the above examples do not represent 'real' rows of data)
