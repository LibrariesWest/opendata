Movement
========

Library items move around a lot. Particularly when there is a shared catalogue in a consortium like LibrariesWest. For example, within our reservation process, the following could easily occur.

- A Bristol registered member places a reservation on an item. They select to pick that item up at Keynsham library, a Bath and North East Somerset library located near Bristol.
- The item is found at the library it is held at (for example Dorchester, in Dorset).
- The item is sent to be sorted at the library administration centre in Bridgwater, Somerset.
- The item is sent out to Keynsham.
- When the item has arrived and has been scanned, a notification is sent to the user that the item is available.

When items are sent between libraries they go into 'transit'. We store the date the item was put into transit, the library the item is being sent from, the library it's being sent to, and a reason. In this example this reason is 'Hold', as reservations are known as holds in our system.

| Item ID | Library From | Library To | Date transited | Reason |
| ------- | ------------ | ---------- | -------------- | ------ |
| 1234567 | Dorchester | Keynsham | 2018-09-01 | Hold |

Once the item has been received, the record is removed. The user then goes away and takes the book home (perhaps), and once finished with it returns it to the library service. They may return it to a library that wasn't the library they picked it up from. In our example, perhaps they take it back to Bristol Central library. Once Bristol Central receive that item, another transit record is created so that the item can be sent back to it's usual library (Dorchester).

| Item ID | Library From | Library To | Date transited | Reason |
| ------- | ------------ | ---------- | -------------- | ------ |
| 1234567 | Bristol Central | Dorchester | 2018-09-16 | Library |

The constant moving around of stock is interesting for analysis. It could possibly be used to refine the copies held within each library, if particular stock is regularly moving from one library to another. Or show characteristics of missing stock types in different authorities, if certain types of items are often moving from one authority to another.

- [Items in transit](./transits.md)

#### Open data

We will export all transit records to show the current snapshot of items moving around LibrariesWest.
