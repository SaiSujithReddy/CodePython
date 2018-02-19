
#link - https://stackoverflow.com/questions/245878/how-do-i-choose-between-a-hash-table-and-a-trie-prefix-tree
#link - https://www.quora.com/What-is-the-difference-between-HashTable-Trie-and-Tree-bst-and-when-to-use-which-data-structure
#link - https://stackoverflow.com/questions/14708134/what-is-the-difference-between-trie-and-radix-trie-data-structures
The basics:

Predictable O(k) lookup time where k is the size of the key
Lookup can take less than k time if it's not there
Supports ordered traversal
No need for a hash function
Deletion is straightforward
New operations:

You can quickly look up prefixes of keys, enumerate all entries with a given prefix, etc.
Advantages of linked structure:

If there are many common prefixes, the space they require is shared.
Immutable tries can share structure. Instead of updating a trie in place, you can build a new one that's different only along one branch, elsewhere pointing into the old trie. This can be useful for concurrency, multiple simultaneous versions of a table, etc.
An immutable trie is compressible. That is, it can share structure on the suffixes as well, by hash-consing.
Advantages of hashtables:

Everyone knows hashtables, right? Your system will already have a nice well-optimized implementation, faster than tries for most purposes.
Your keys need not have any special structure.
More space-efficient than the obvious linked trie structure (see comments below)



Everyone knows hash table and its uses but it is not exactly constant look up time , it depends on how big the hash table is , the computational complexity of the hash function.

Creating huge hash tables for efficient lookup is not an elegant solution in most of the industrial scenarios where even small latency/scalability matters (e.g.: high frequency trading). You have to care about the data structures to be optimized for space it takes up in memory too to reduce cache miss.

A very good example where trie better suits the requirements is messaging middleware . You have a million subscribers and publishers of messages to various categories (in JMS terms - Topics or exchanges) , in such cases if you want to filter out messages based on topics (which are actually strings) , you definitely do not want create hash table for the million subscriptions with million topics .
A better approach is store the topics in trie , so when filtering is done based on topic match , its complexity is independent of number of topics/subscriptions/publishers (only depends on the length of string).
I like it because you can be creative with this data structure to optimize space requirements and hence have lower cache miss.

It
all
depends
on
what
problem
you
're trying to solve. If all you need to do is insertions and lookups, go with a hash table. If you need to solve more complex problems such as prefix-related queries, then a trie might be the better solution.



Hash Table:
Internet routers is a good example of why hash tables are required.
A router table (especially in those routers in the backbone networks of internet operators) may contain hundreds of thousands or millions of entries. When a packet has to be routed to a specific IP address, the router has to determine the best route by querying the router table in an efficient manner.
HashTables are used as an efficient lookup structure having as key the IP address and as value the path that should be follow for that address.

Trie:
A Trie could be a good data structure for building a memory-efficient dictionary with fast lookups and auto-completion.
Think of it as a hashtable, providing fast lookup of key-value pairs (or just lookup of keys), but unlike a hashtable it allows you to iterate over the keys in sorted order.

BST:
Check out the following link on StackOverflow: Concrete examples of using binary search trees.