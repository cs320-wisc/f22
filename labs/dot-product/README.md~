# Lab 11: Matrices

## Part 1: Dot Product

In lecture, we've talked about what the dot product means to multiply
a vector by a vector.  Here, we'll review that, and also learn what it
means to multiply a matrix by a vector, or a matrix by a matrix.

### 1. Vector dot Vector

Complete the following function so that it compute the dot product of
two vectors:

```python
def v_dot_v(v1, v2):
    assert len(v1) == len(v2)
    total = 0
    for i in range(len(v1)):
        total += ????
    return total

a = np.array([100,10,1])
b = np.array([3,2,0])
v_dot_v(a, b) # should be 320
```

Although the vectors are one dimensional, we'll assume `v1` is
horizontal and `v2` is vertical.

<details>
    <summary>ANSWER</summary>
    <code>v1[i] * v2[i]</code>
</details>

### 2. Matrix dot Vector

We can multiply a matrix by a vector by doing vector-by-vector
multiplications, taking one row at a time from the matrix for the
first vector.  This will give us a vector containing output value per
row in the matrix.

Complete the following function so that it computes the dot product of
a matrix and a 1-dimensional vector (assumed to be vertical):

```python
def m_dot_v(m, v):
    output = []
    for row in m:
        assert len(row) == len(v)
        output.append(????)
    return np.array(output)

A = np.array([
    [1,0,3],
    [0,2,3],
])
x = np.array([1,10,100])
m_dot_v(A, x) # should be [301, 320]
```

<details>
    <summary>ANSWER</summary>
    <code>v_dot_v(row, v)</code>
</details>

### 3. Matrix dot Matrix

We can multiply a matrix by a matrix by doing matrix-by-vector
multiplications, taking one column at a time from the second matrix
for the vector.  Each of these multiplications gives an output vector
-- arranging these output vectors as columns in an output matrix gives
the result of the matrix multiplication.

Complete the following function so that it compute the dot product of
a two matrices:

```python
def m_dot_m(m1, m2):
    output_cols = []
    for col in m2.T:
        output_cols.append(????)
    return np.array(output_cols).T

A = np.array([
    [1,0],
    [1,2],
    [1,3],
    [0,5],
    [100,200],
])
B = np.array([
    [1,0,10],
    [0,1,1],
])
m_dot_m(A, B)
```

The result should be this:

```
array([[   1,    0,   10],
       [   1,    2,   12],
       [   1,    3,   13],
       [   0,    5,    5],
       [ 100,  200, 1200]])
```

<details>
    <summary>ANSWER</summary>
    <code>m_dot_v(m1, col)</code>
</details>

## Part 2: Geographic Raster Data

In class, we learned geopandas, which is a *vector-based* GIS tool --
that means geo data is represented by vectors of coordinates, which
form polygons and other shapes.

*Raster* data is the other common kind of geo data you'll encounter.
 With raster data, you break land into a matrix, with numbers in each
 cell telling you something about the land at a given position.

In this part, we'll learn a bit about the `rasterio` module.  It will
help us create numpy arrays corresponding to how land is used in a
given WI county (this will be useful for predicting things like a
county's population).

First, install some packages:

```
pip3 install rasterio Pillow
```

P6 includes an `f21/p6/land.zip` dataset.  Let's open it (this assumes
your notebook is in `f21/lab11` -- you may need to modify the path to
`land.zip` if you're in a different directory):

```python
import rasterio
land = rasterio.open("zip://../p6/land.zip!wi.tif")
```

This is the dataset for all of WI.  Let's say we want to only see Dane
County (which contains Madison).  We can get this from TIGERweb, a
service run by the US Census Bureau.

1. go to https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/
2. click "TIGERweb/tigerWMS_Census2020"
3. click "Counties (82)"
4. at the bottom, click "Query"
5. in the "Where" box, type `NAME='Dane County'` exactly
6. under "Format", choose "GeoJSON"
7. click "Query (GET)"
8. copy the URL

Paste the URL into the following code snippet:

```python
import geopandas as gpd
url = "????"
dane = gpd.read_file(url)
dane.plot()
```

You should see a rough outline of Dane County.

We can use that outline as a *mask* on the raster data to get a numpy
array of land use.  A mask identifies specific cells in a matrix that
matter to us (note that we need to convert our geopandas data to the
same CRS as the rasterio data):

```python
from rasterio.mask import mask
matrix, _ = mask(land, dane.to_crs(land.crs)["geometry"], crop=True)
matrix = matrix[0]
```

Let's visualize the county:

```
import matplotlib.pyplot as plt
plt.imshow(matrix)
```

It should look like this:

<img src="dane.png" width=400>

Browse the legend here: https://www.mrlc.gov/data/legends/national-land-cover-database-2019-nlcd2019-legend

We see water is encoded as 11.  We can highlight all the water regions in Dane County like this:

```python
plt.imshow(matrix == 11)
```

Try filtering the matrix in different ways to see where the following land covers are dominant:

* Deciduous Forest
* Cultivated Crops
* Developed, Low Intensity

## Part 3: Counting Cells

Run the following:

```python
import numpy as np
a = np.array([
    [0,0,5,8],
    [1,2,4,8],
    [2,4,6,9],
])
```

How many even numbers are in this matrix?  What percentage of the
numbers are even?  We'll walk you through the solution.  Please run
each step (which builds on the previous) to see what's happening.

First step, mod by 2, to get a 0 in every odd cell:

```python
a % 2
```

Now, let's do an elementwise comparison to get a True in every place where there is an even number:

```python
a % 2 == 0
```

It will be easier to count matches if we represent True as 1 and False as 0:

```python
(a % 2 == 0).astype(int)
```

How many is that?

```python
(a % 2 == 0).astype(int).sum()
```

And what percent of the total is that?

```python
(a % 2 == 0).astype(int).mean() * 100
```

This may be useful for counting what percentage of an area matches a
given land type in P6.
