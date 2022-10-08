# Inheritance and DFS

## Inheritance

Paste and run the following code:

```python
class Parent:
    def twice(self):
        self.message()
        self.message()
        
    def message(self):
        print("parent says hi")
        
class Child:
    def message(self):
        print("child says hi")
        
c = Child()
```

Modify `Child` so that it inherits from `Parent`.

What do you think will be printed if you call `c.twice()`?  Discuss
with your group, then run it to find out.

When `self.some_method(...)` is called, and there are multiple methods
named `some_method` in your program, the type of `self` is what
matters for determining which one runs.  It doesn't matter where the
`self.some_method(...)` is (could be any method).

## GraphSearcher

Copy and paste the following starter code (which you'll build on in the project):

```python
class GraphSearcher:
    def __init__(self):
        self.visited = set()
        self.order = []

    def visit_and_get_children(self, node):
        """ Record the node value in self.order, and return its children
        param: node
        return: children of the given node
        """
        raise Exception("must be overridden in sub classes -- don't change me here!")

    def dfs_search(self, node):
        # 1. clear out visited set and order list
        # 2. start recursive search by calling dfs_visit

    def dfs_visit(self, node):
        # 1. if this node has already been visited, just `return` (no value necessary)
        # 2. mark node as visited by adding it to the set
        # 3. call self.visit_and_get_children(node) to get the children
        # 4. in a loop, call dfs_visit on each of the children
```

The graphs we search on come in many shapes and formats
(e.g. matrices, files or web), but it would be nice if we could use
the same depth-first search (DFS) code when we want to search
different kinds of graphs.  Therefore, we would like to implement a
base class `GraphSearcher` and implement the DFS algorithm in it.

For our purposes, we aren't using DFS to find a specific path.  We
just want to see what nodes are reachable from a given starting
`node`, so these methods don't need to return any value.  Your job is
to replace the comments in `dfs_search` and `dfs_visit` with code
(some comments may require a couple lines of code).

The `dfs_visit` method will call `visit_and_get_children` to record
the node value and determine the children of a given node. Subclasses
of `GraphSearcher` can override `visit_and_get_children` to lookup the
children of a node in different kinds of graphs (e.g. matrices, files
or web).


Try your code:

```python
g = GraphSearcher()
g.dfs_search("A")
```

You should get an exception.  The purpose of `GraphSearcher` is not to
directly create objects, it is to let other clases inherit
`dfs_search` (we'll do the inheritance soon).

## Matrix Format

Paste and run the following:

```python
import pandas as pd

df = pd.DataFrame([
    [0,1,0,1],
    [0,0,1,0],
    [0,0,0,1],
    [0,0,1,0],
], index=["A", "B", "C", "D"], columns=["A", "B", "C", "D"])
df
```

A grid of ones and zeros like this is a common way to represent
directed graphs.  A `1` in the "C" column of the "B" row means that
there is an edge from node B to node C.

Try drawing a directed graph on a piece of paper based on the above
grid.

`df.loc["????"]` looks up a row in a DataFrame.  Use it to lookup the
children of node B.

Complete the following to print all the children of "B" (should be "C" and "D"):

```python
for node, has_edge in df.loc["B"].items():
    if ????:
        print(????)
```

Let's create a class that inherits from `GraphSearcher` and works with
graphs represented as matrices:

```python
class MatrixSearcher(????):
    def __init__(self, df):
        super().????() # call constructor method of parent class
        self.df = df

    def visit_and_get_children(self, node):
        # TODO: Record the node value in self.order
        children = []
        # TODO: use `self.df` to determine what children the node has and append them
        return children
```

Complete the `????` and `TODO` parts.  Test it, checking what nodes
are reachable from each starting point:

```python
m = MatrixSearcher(df)
m.dfs_search(????)
m.order
```

From "A", for example, `m.order` should be `['A','B', 'C', 'D']`.  Look
back at the picture you drew of the graph and make sure you're getting
what you expect when starting from other nodes.

## scrape.py

If you've been doing this work in a notebook, you should now move your
code to a new module called `scrape.py` in your `s22/p3` directory.
