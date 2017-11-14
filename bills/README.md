Billing
=======

This describes the open data for bills. In the Library Management System, bill data is made up of Bills and Bill Payments.

Description
-----------

A bill is a record of money owing between the user and the library.

For example, a user places a reservation on an item, which incurs a bill of £1. That would create a bill record:

| User ID | Bill number | Bill date | Bill reason | Bill library | Bill amount | Paid? |
| ------- | ----------- | --------- | ----------- | ------------ | ----------- | ----- |
| 12345 | 1 | 13/06/2017 | HOLD | Bath Central | £1 | No |

Bill records could be paid instantly. If a user returns an item and it turns out to be overdue then that would generate a bill of type OVERDUE. This could then be paid before they leave, or left until a later date.

Paying a bill can be done by paying the full amount, or it is possible to pay in smaller amounts, multiple times.  When paying a bill, a 'bill payment' record is created:

| User ID | Bill number | Payment date | Payment type | Payment library | Amount paid |
| ------- | ----------- | ------------ | ------------ | ------------ | ----------- |
| 12345 | 1 | 13/06/2017 | CASH | Bath Central | £0.50 |

When the payment has been made in full, the original bill record is updated to show that the bill is fully paid. Sometimes bills are 'paid' with a reason of either FORGIVEN or CANCEL. This means that moeny hasn't been taken for the bill, it's been deemed either the bill wasn't valid, or it was valid but that the user does not have to pay it (perhaps in exceptional circumstances).

Open data
---------

The data we provide here is aggregated data to show bill and bill payment amounts by month, by various categories, such as the library and the payment type. It will include all bills and bill payments currently stored in the system.

Definitions
-----------

File: bills.csv

| Field | Description | Example |
| ----- | ----------- | ------- |
| Month billed | The month the bill record was created | 2017-11 |
| Bill authority | The authority the bill record was created for | Somerset |
| Bill library | The library the bill was created for | Taunton |
| Item type | The type of item that the bill record is for | ADU_FIC |
| Bill reason | The reason for the bill | HOLD |
| Number of bills | The number of bills included in this grouping | 5 |
| Total billed | The total amount billed in pounds | 5 |

File: billpayments.csv

| Field | Description | Example |
| ----- | ----------- | ------- |
| Month paid | The month the payment was made | 2017-11 |
| Payment authority | The authority the payment was taken at | Somerset |
| Payment library | The library the payment was taken at | Taunton |
| Bill reason | The reason for the bill | HOLD |
| Payment type | The type of payment | CASH |
| Number of payments | The number of payments in this grouping | 5 |
| Total paid | The total amount paid | 5 |

Update frequency
----------------

This data will be updated every night.