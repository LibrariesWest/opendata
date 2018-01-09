Movement
========

Library items move around a lot. Particularly in a consortium with a shared catalogue. For example, within our registration process, the following type of process will regularly occur.

- A user in Bristol places a reservation on an item. They select to pick that item up at Keynsham library (a Bath and North East Somerset library)
- The item is located at the library it is held at (for example, Dorchester, in Dorset).
- The item is sent to be sorted at the library administration centre in Somerset.
- The item is sent out to Keynsham.
- A notification is sent to the user that the item is available.

When items are sent between libraries they go into 'transit'. A record is created to store the date the item was put into transit, the library the item is being sent from, the library it's being sent to, and a reason why. In this example this reason is 'Hold' as reservations are known as holds.

| Item ID | Library From | Library To | Date transited | Reason |
| ------- | ------------ | ---------- | -------------- | ------ |
| 1234567 | DODOR | BNKY | 2018-09-01 | Hold |

Once the item has been received, the record is removed. The user then goes away and takes the book home, and once finished with it returns it to the library service. They may return it to a library that wasn't the library they picked it up from, in this example perhaps they take it back to Bristol Central. Once the library receive that item back, another transit record is created so that the item is sent back to it's usual library (Dorchester).

| Item ID | Library From | Library To | Date transited | Reason |
| ------- | ------------ | ---------- | -------------- | ------ |
| 1234567 | BSAL | DODOR | 2018-09-16 | Library |

The constant moving around of stock is interesting for analysis. It shows items that within their home library service, and items that move between the different library services in LibrariesWest.

- [Items in transit](./transits.md)

#### Open data

We will export all transit records to show the current snapshot of items moving around LibrariesWest.
