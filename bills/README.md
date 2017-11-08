Billing
=======

This describes the open data for bills and bill payments. In the Library Management System, bill data is made up of Bills and Bill payments.

Description
-----------

A bill is a record of money owing between the user and the library.

For example, a user places a reservation on an item, which incurs a bill of £1. That would create a bill record a bit like the following:

| User ID | Bill number | Bill date | Bill reason | Bill library | Bill amount | Paid? |
| ------- | ----------- | --------- | ----------- | ------------ | ----------- | ----- |
| 12345 | 1 | 13/06/2017 | HOLD | Bath Central | £1 | No |

Bill records could be paid instantly. If a user returns an item and it turns out to be overdue then that would generate a bill of type OVERDUE. This could then be paid before they leave, or left until a later date.

Paying a bill can be done by paying the full amount, or it is possible to pay in smaller amounts multiple times.  When paying a bill, a 'bill payment' record is created, such as the following:

| User ID | Bill number | Payment date | Payment type | Bill library | Amount paid |
| ------- | ----------- | ------------ | ------------ | ------------ | ----------- |
| 12345 | 1 | 13/06/2017 | CASH | Bath Central | £0.50 |

When the payment has been made in full, the original bill record is updated to show that the bill is fully paid. Sometimes bills are 'paid' with a reason of either FORGIVEN or CANCELLED. This means that moeny hasn't been taken for the bill, it's been deemed that either the bill wasn't valid, or it was valid but that the user does not have to pay it.


Definitions
-----------

File: bills.csv

| Field | Description | Example |
| ----- | ----------- | ------- |


File: billpayments.csv

| Field | Description | Example |
| ----- | ----------- | ------- |
| Month paid |  |  |
| Payment authority |  |  |
| Payment library |  |  |
| Bill reason |  |  |
| Payment type |  |  |
| Number of bills |  |  |
| Total paid |  |  |
