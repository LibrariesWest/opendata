Payments
=============

We export two payment data files. A summary for basic data counts, and a full detail file.

#### Summary file

The summary includes the number of payment records recorded in the Library Management System, separated by Library authority, the bill reason, and financial year of payment. This will cover the previous financial year, and the current.

- [View bill payments summary data](https://github.com/LibrariesWest/opendata/blob/master/bills/payments_summary.csv)

| Field | Description | Example |
| ----- | ----------- | ------- |
| Financial year paid | The financial year the payment was made | 2017/2018 |
| Payment authority | The authority the payment was taken at | Somerset |
| Bill reason | The reason for the original bill | Bill for repacement |
| Payment type | The type of payment | CASH |
| Number of payments | The number of payments in this grouping | 5 |
| System paid | The total amount from the payments | 5 |
| Real amount paid | The real amount taken from the payments. This takes into account that no income is received from CANCEL and FORGIVEN payments. | 5 |

#### Detail file

For more detail use this download, the columns are described below. The data is still aggregated, but provides extra levels of detail.

- [View bill payment data](https://github.com/LibrariesWest/opendata/blob/master/bills/payments.csv)

| Field | Description | Example |
| ----- | ----------- | ------- |
| Month paid | The month the payment was made | 2017-11 |
| Payment authority | The authority the payment was taken at | Somerset |
| Payment library | The library the payment was taken at | Taunton |
| Bill reason | The reason for the bill | HOLD |
| Payment type | The type of payment | CASH |
| Number of payments | The number of payments in this grouping | 5 |
| System paid | The total amount paid | 5 |
| Real amount paid | The real amount taken from the payments. This takes into account that no income is received from CANCEL and FORGIVEN payments. | 5 |
