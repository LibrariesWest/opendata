Bills and payments
==================

*Bills and payments* is how we describe library charges that occur through the use of LibrariesWest libraries (e.g. an overdue fine). A bill is a record of money owing between the user and the library. A payment is a payment made to pay off that bill.

For example, a user places a reservation (also known as 'hold') on an item, which may incur a charge. A bill record is created.

| User ID | Bill number | Bill date | Bill reason | Bill library | Bill amount | Paid? |
| ------- | ----------- | --------- | ----------- | ------------ | ----------- | ----- |
| 12345 | 1 | 13/06/2017 | HOLD | Bath Central | £1 | No |

This bill could be paid straight away. On collecting the item, the user would be alerted to a charge on their account and could pay it then. Or it could be left until a later date.

Paying a bill can be done by paying the full amount, or by paying in smaller amounts. When making a payment, another record is created.

| User ID | Bill number | Payment date | Payment type | Payment library | Amount paid |
| ------- | ----------- | ------------ | ------------ | --------------- | ----------- |
| 12345 | 1 | 13/06/2017 | CASH | Bath Central | £0.50 |

When enough payments have been made, the original bill record is updated to show that it's been fully paid. Sometimes payments have a payment type of either FORGIVEN or CANCEL. This means that 'real' money hasn't been taken for the bill. Library staff may have decided that either the bill wasn't valid, or it was valid but that the user should not have to pay it. But as far as the system is concerned, the bill has been paid.

- [Bill data](./bills.md)
- [Payments data](./bill-payments.md)

#### Open data extracts

The data provided here is aggregated data to show bill and bill payment counts and amounts, by various categories, such as the library and the payment type. It will include bills and bill payments for the past two years, from the time the reports are run. Our data for payments includes FORGIVEN and CANCEL payments, but we also include a column to represent the amount in 'real' money, which will be £0 for those payments.
