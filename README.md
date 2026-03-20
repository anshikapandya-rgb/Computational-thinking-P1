Computational Thinking - P1
Task 1: Identity Investigation

Objective:
To understand how different data types behave in memory when modified.

 Procedure:
A Python file `identity_anshika.py` was created. For each data type (integer, string, list, tuple), the memory ID was printed before and after performing a change using the `id()` function.

 Results:
- Integer → ID changed  
- String → ID changed  
- Tuple → ID changed  
- List → ID remained the same  

Inference:
Integers, strings, and tuples are immutable because they create new objects when modified. Lists are mutable since they are updated in the same memory location.

Task 2: Nature of Commit History

 Procedure:
A Git repository was initialized and a file was added. Multiple commits were made with messages such as "Version 1" and "Version 2".

 Question:
Does "Version 2" still exist in the folder?

Answer:
Yes, Version 2 exists along with Version 1 in the commit history.

 Explanation:
Git follows an immutable model, meaning commits cannot be altered once created. Instead of modifying an existing commit, Git creates a new one for every change. This ensures that all previous versions remain intact.

Key Points:
- Full history is always preserved  
- Changes can be tracked easily  
- Older versions can be restored anytime  
- Data loss is prevented  

 Inference:
Git maintains all versions permanently, proving that commits are immutable.

Task 3: Shallow Copy Behavior

Procedure:
A nested list was created and copied using `list()`. An element inside the copied list was modified, and both lists were printed.
 Results:
The original list was also modified.

 Explanation:
The copy created was a shallow copy, where only the outer list is duplicated, but inner lists share the same references. Therefore, changes in one affect the other.

 Inference:
To avoid shared references, a deep copy should be used.
 Task 4: Commit Immutability

Procedure:
A file was committed and its hash was recorded using `git log`. The commit message was then modified using `git commit --amend`, and the new hash was noted.

 Results:
The commit hash changed after modifying the message.

Explanation:
The commit hash is generated using the commit’s content and metadata. Any change, even in the message, results in a completely new commit with a new hash.

Inference:
This confirms that Git commits are immutable and cannot be changed once created.