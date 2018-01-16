Usage
=====

Considering the multiple ways in which people use libraries, we don't hold that much data. We don't have people browsing around, visiting, reading newspapers, working on laptops, working on public access PCs, asking questions, going to events. There will be data for many of these things, but much of it will be held by the individual library services.

LibrariesWest manage the Library Management System, so that concerns data about usage of the catalogue. People reserving items, taking out items, and renewing them.

When placing a reservation, the reservation is normally placed against the Title rather then the Item. See our [catalogue data](./../catalogue/README.md) for difference between titles and items. For example, there may be 10 copies of 'Voyage of the Dawn Treader' around LibrariesWest. If none are available and a user wants to reserve one, the system will need to decide which one of those copies to assign to the reservation. This will be influenced by things such as which library the user wants to pick up the item from, which copies are available, whether the item can be sourced and transferred within a single library service, and other factors. This can also change if a copy becomes available while the reservation is active - that copy would normally then be assigned to the next user in the queue.

When a reservation is placed a reservation record is created, also known as 'hold'.

| Date Placed | Date expires | Date available | User | Item | Library | Pickup library | Position | Reservation Method |
| ----------- | ------------ | -------------- | ---- | ---- | ------- | -------------- | -------- | ------------------ |
| 15/01/2018 | 15/01/2019 | | 12345 | 12345 | Bath Central  | Keynsham | 8 | Branch |

That's a simplified view of a reservation record, but gives some of the key principles. If a number of people are waiting for a particular title, the system needs to keep track of the queue (the 'position'), and we can also see the method used to make the reservation. It could be online through the library catalogue, or by coming in to a branch.

When the item is available the user is notified and it can then be issued to the user. 

When issuing an item, we track the data for that issue.

| Item | User | Date issued | Date due | Renewals |
| ---- | ---- | ----------- | -------- | -------- |
| 123456 | 123456 | 12/12/2018 | 17/01/2018 | 2 |

This issue record keeps track of when items are due back. If an item is renewed then the number of renewals will change, and the item is due will update.

- [Issues](./issues.md)
- [Reservations](./reservations.md)

#### Open data

We will export aggregated issue and reservation data to show how many are occuring per month and library, with some associated item data such as item type. The data is from 'go live' of our current system: June 2016.
