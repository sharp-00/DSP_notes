# NumPy: The Absolute Basics for Beginners
<!-- https://numpy.org/doc/stable/user/absolute_beginners.html --> 

## Why use NumPy?
- Python lists are general-purpose but can be inefficient for large numeric
  computations.
- NumPy arrays are homogeneous (all elements same type), enabling:
  - faster operations;
  - lower memory use;
  - high-level mathematical syntax.
- This makes NumPy ideal for processing large quantities of numeric data.
  :contentReference[oaicite:3]{index=3}

## What is an “array”?
- An *array* in NumPy is a data structure for storing and retrieving values.
- It can be 1D, 2D, 3D, or higher dimensional (`ndarray`).
- **Key properties of NumPy arrays:**
  - All elements must be the same type.
  - Size is fixed once created.
  - Shape must be rectangular (e.g., all rows same length).
- These constraints allow NumPy to optimize memory and performance.
  :contentReference[oaicite:4]{index=4}

## Array fundamentals
- You create an array from a Python sequence using `np.array([...])`.
- Access elements with zero-based indexing, as with Python lists.
- Arrays are **mutable** — you can change values after creation.
- Slicing an array returns a *view* (not a copy), meaning changes in the view
  affect the original.
- You can create multi-dimensional arrays from nested lists.
  :contentReference[oaicite:5]{index=5}

## Array attributes
- Every array has useful attributes that describe its structure:
  - `ndim` – number of dimensions (axes).
  - `shape` – tuple describing number of elements along each axis.
  - `size` – total number of elements (`product(shape)`).
  - `dtype` – data type of elements (e.g., `int64`, `float64`).
- These make it easy to introspect arrays programmatically.
  :contentReference[oaicite:6]{index=6}

## How to create a basic array
- Besides `np.array()`, NumPy offers routines to construct arrays:
  - `np.zeros(n)` — array of *n* zeros.
  - `np.ones(n)` — array of *n* ones.
  - `np.empty(n)` — array of *n* uninitialized values (fast but arbitrary
    content).
  - `np.arange(start, stop, step)` — range of values similar to Python’s
    `range()`.
  - `np.linspace(start, stop, num)` — *num* values evenly spaced between start
    and stop.
- You can also specify the `dtype` explicitly (e.g., integer vs float).
  :contentReference[oaicite:7]{index=7}

## Adding, removing, and sorting elements
- You can sort arrays using `np.sort()`:
  - Produces a sorted copy; original array unchanged.
  - Variants include indirect sorts (`argsort`, `lexsort`) and partial sorts
    (`partition`).
- You can concatenate arrays using `np.concatenate((a, b), axis=…)`.
- To remove elements, use indexing to select only the elements you want to keep.
  :contentReference[oaicite:8]{index=8}

## How do you know the shape and size of an array?
- Use `ndarray.ndim` to find the number of dimensions.
- Use `ndarray.size` to get total number of elements.
- Use `ndarray.shape` to see the length of each dimension.
- These help you understand and manipulate array geometry programmatically.
  :contentReference[oaicite:9]{index=9}

## Can you reshape an array?
- `arr.reshape(new_shape)` returns a view of the array with the same data but
  reorganized.
- The total number of elements must match between original and new shapes.
- Optional parameters let you control memory ordering (`C`, `F`, `A`).
  :contentReference[oaicite:10]{index=10}

## How to convert a 1D array into a 2D array
- Use `np.newaxis` or `np.expand_dims()` to **add a new axis**.
- This turns a 1D vector into a row or column vector.
- E.g., `a[np.newaxis, :]` becomes shape `(1, n)`; `a[:, np.newaxis]` becomes
  shape `(n, 1)`. :contentReference[oaicite:11]{index=11}

## Indexing and slicing
- You can index and slice NumPy arrays the same way as Python lists.
- Supports negative indices, slices, and combinations.
- You can apply conditions to filter data (boolean indexing).
- `np.nonzero()` returns indices where a condition holds.
- Boolean combinations (`&`, `|`) allow compound filters.
  :contentReference[oaicite:12]{index=12}

## How to create an array from existing data
- You can slice existing arrays to make new ones.
- Stacking functions:
  - `np.vstack` — vertical stacking.
  - `np.hstack` — horizontal stacking.
  - `np.hsplit` — split array into subarrays.
- **Views vs copies:**
  - Slicing and many operations return **views** (shared memory).
  - Use `.copy()` to force an independent copy.
    :contentReference[oaicite:13]{index=13}

## Basic array operations
- Arithmetic operators work element-wise:
  - `+`, `-`, `*`, `/` on arrays perform vectorised math.
- Use `.sum()` to compute the sum of all elements.
- For multi-D arrays, specify `axis` to sum along rows or columns.
- These operations scale to higher dimensions.
  :contentReference[oaicite:14]{index=14}

## Broadcasting
- Broadcasting allows operations between arrays of different shapes:
  - E.g., multiply a 1D array by a scalar or by a compatible shaped array.
- Arrays must be compatible by dimension rules for broadcasting to work.
- If shapes are incompatible, a `ValueError` is raised.
  :contentReference[oaicite:15]{index=15}

## More useful array operations
- Aggregation functions beyond sum:
  - `.max()` – maximum element.
  - `.min()` – minimum.
  - `.mean()` – average.
  - `.prod()` – product of elements.
  - `.std()` – standard deviation.
- You can aggregate across axes to summarise rows or columns separately.
  :contentReference[oaicite:16]{index=16}

## Creating matrices
- Construct a 2D array from a list of lists.
- You can index and slice matrices (e.g., `data[row, col]`, submatrix slices).
- Aggregate matrices like vectors (`.sum()`, `.max()`, etc.).
- Arithmetic operations follow the same broadcasting rules.
  :contentReference[oaicite:17]{index=17}

## Generating random numbers
- Use NumPy’s `Generator` API (e.g., `rng = np.random.default_rng()`).
- `rng.integers()` generates random integers within a specified range.
- You can produce arrays of random values with given shape.
  :contentReference[oaicite:18]{index=18}

## How to get unique items and counts
- `np.unique(array)` returns sorted unique values from the array.
- You can optionally return indices and counts associated with each unique
  value.
- Works for multi-D arrays with the `axis` argument.
  :contentReference[oaicite:19]{index=19}

## Transposing and reshaping a matrix
- Use `.T` or `.transpose()` to switch axes of a matrix.
- Use `reshape()` to reorganise the shape without changing data.
- Transposing makes rows into columns and vice-versa.
  :contentReference[oaicite:20]{index=20}

## How to reverse an array
- `np.flip()` reverses array contents along specified axes.
- Without an axis argument, all axes are flipped.
- You can reverse rows or columns independently.
  :contentReference[oaicite:21]{index=21}

## Reshaping and flattening multidimensional arrays
- `x.flatten()` returns a **copy** 1D array.
- `x.ravel()` returns a **view** 1D array.
- Changes in a `ravel()` result affect the original; changes in `flatten()` do
  not. :contentReference[oaicite:22]{index=22}

## How to access the docstring for more information
- Every object in Python has a *docstring* summarising its purpose.
- Use `help(obj)` to access documentation programmatically.
- In IPython/Jupyter, `obj?` shows the docstring and `obj??` shows source when
  available. :contentReference[oaicite:23]{index=23}

