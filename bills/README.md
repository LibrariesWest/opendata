Bills and payments
==================

'Bills and payments' is the terminology we use to describe the normal library charges that can occur through the use of LibrariesWest libraries (e.g. a fine). A bill is a record of money owing between the user and the library.

For example, a user places a reservation (also known as 'hold') on an item, which may incur a small charge, depending on local policies. The bill record is created:

| User ID | Bill number | Bill date | Bill reason | Bill library | Bill amount | Paid? |
| ------- | ----------- | --------- | ----------- | ------------ | ----------- | ----- |
| 12345 | 1 | 13/06/2017 | HOLD | Bath Central | £1 | No |

These bills could be paid straight away. On picking up the item, the customer would be alerted to a charge on their account and could then pay the charge. Or it could be left until a later date.

Paying a bill can be done either by paying the full amount, or it is also possible to pay in multiple smaller amounts. When making a payment, another record is created:

| User ID | Bill number | Payment date | Payment type | Payment library | Amount paid |
| ------- | ----------- | ------------ | ------------ | --------------- | ----------- |
| 12345 | 1 | 13/06/2017 | CASH | Bath Central | £0.50 |

When enough payments have been made to pay off the bill in full, the original bill record is updated to show that the bill is fully paid. Sometimes payment records have a payment type of either FORGIVEN or CANCEL. This means that money hasn't been taken for the bill. Library staff may have decided that either the bill wasn't valid, or it was valid but that the user should not have to pay it. But as far as the system is concerned, the bill has been paid.

- [Bill data](./bills.md)
- [Payments data](./bill-payments.md)

#### Open data extracts

The data provided here is aggregated data to show bill and bill payment counts and amounts, by various categories, such as the library and the payment type. It will include bills and bill payments since 'go live' of our current system (7th June 2016).
