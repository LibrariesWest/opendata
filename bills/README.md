Bills and payments
==================

In the Library Management System, our bill data is made up of Bills and Bill Payments.

A bill is a record of money owing between the user and the library.

For example, a user places a reservation (also known as 'hold') on an item, which may incur a bill of £1 (depending on local policies). That would create a bill record:

| User ID | Bill number | Bill date | Bill reason | Bill library | Bill amount | Paid? |
| ------- | ----------- | --------- | ----------- | ------------ | ----------- | ----- |
| 12345 | 1 | 13/06/2017 | HOLD | Bath Central | £1 | No |

Bill records could be paid straight away. For example, if a user returned an item and it was overdue then that would generate a bill of type OVERDUE at the point the item is returned. This could then be paid before they leave, or left until a later date.

Paying a bill can be done either by paying the full amount, or it is possible to pay in smaller amounts, multiple times. When making a payment, a 'bill payment' record is created:

| User ID | Bill number | Payment date | Payment type | Payment library | Amount paid |
| ------- | ----------- | ------------ | ------------ | --------------- | ----------- |
| 12345 | 1 | 13/06/2017 | CASH | Bath Central | £0.50 |

This payment record is linked to the bill record by User ID and Bill number. When the payment has been made in full, the original bill record is updated to show that the bill is fully paid. Sometimes payment records are created with a type of either FORGIVEN or CANCEL. This means that money hasn't been taken for the bill, staff will have decided that either the bill wasn't valid, or it was valid but that the user should not have to pay it. As far as the system is concerned, the bill has been paid.

- [Bill data](./bills.md)
- [Bill payments data](./bill-payments.md)

#### Open data extracts

The data we provide here is aggregated data to show bill and bill payment amounts by month, by various categories, such as the library and the payment type. It will include bills and bill payments since 'go live' of our current system (7th June 2016).
