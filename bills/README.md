Billing open data
==================

This describes the open data for bills and bill payments. In the Library Management System, bill data is made up of Bills and Bill payments.

Files
-----



Definitions
-----------

File: bills.csv




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

Bills
-----

Bill data holds the data on bills that have been incurred by patrons.

For example, User A places a reservation (known as a 'hold') on an item, which incurs a bill of £1. In the system, that creates a bill record that will look a bit like the following:

| User ID | Bill number | Bill reason | Bill library | Bill amount |
| ------- | ----------- | ----------- | ------------ | ----------- |
| 12345 | 1 | HOLD | Bath Central | 1 |


Bill payments
-------------

Bill payment data holds the data on payments that have been made by patrons to pay bills.

