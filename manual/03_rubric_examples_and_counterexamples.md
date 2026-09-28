# Module 3: Rubric Examples & Counter-Examples

## 3.1 Pairwise Comparison Example: Technical Problem Solving

### User Prompt
> "Write a Python function to check if a binary tree is symmetric. Include time and space complexity analysis."

---

### Response A
```python
def isSymmetric(root):
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
    
    if not root:
        return True
    return isMirror(root.left, root.right)
```
**Complexity Analysis**:
- **Time Complexity**: $O(N)$ where $N$ is the number of nodes in the tree, since we visit every node once.
- **Space Complexity**: $O(H)$ where $H$ is the tree height, corresponding to the maximum call stack depth.

---

### Response B
"A binary tree is symmetric if it is a mirror image of itself around its center. Here is the code:
`def isSymmetric(root): return root == root[::-1]`
Time complexity is very fast, around O(1)."

---

### Annotator Rating & Rationale
- **Chosen Response**: **Response A**
- **Preference Margin**: **Much Better**
- **Dimension Scores**:
  - Response A: Helpfulness=5, Harmlessness=5, Honesty=5, Reasoning=5, Style=5
  - Response B: Helpfulness=1, Harmlessness=5, Honesty=1, Reasoning=1, Style=2
- **Rationale**: Response A provides a correct recursive algorithm with accurate complexity analysis. Response B provides invalid pseudo-code (`root[::-1]` is invalid for tree structures) and incorrect time complexity ($O(1)$).
