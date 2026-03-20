Old Commit Hash: 02c1f77779d92e2961e0f8e2951aa06d4a1e86e8 

New Commit Hash: 5f0b158775e47be4c2b4530c2bc76ca2d2eb0875

Observation:
After updating the commit message, the hash value of the commit was no longer the same.

Reason:
In Git, every commit has a unique hash that is calculated using the commit’s content, message, author details, and timestamp. When the commit message was changed using the amend command, Git did not edit the existing commit. Instead, it generated a completely new commit with a different hash.

Conclusion:
This clearly shows that Git commits are immutable. Once a commit is created, it cannot be modified directly, and any change leads to the creation of a new commit with a new hash.