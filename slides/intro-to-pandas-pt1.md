# Lecture Plan: Introduction to Pandas

Based on:
https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

## Learning Objectives

By the end of this session, you will be able to:

1.  Construct and manipulate Pandas Series and DataFrames.
2.  Select, filter, and modify specific subsets of data.
3.  Handle missing data and perform essential data cleaning.
4.  Execute statistical operations and aggregations.
5.  Combine datasets and manage basic input/output operations.

## Lecture Outline

### 1. Introduction and Object Creation (10 Minutes)

*Goal: Understand the core data structures that power Pandas.*

-   **1.1 Setup and Import**

    -   Standard convention: import pandas as pd and import numpy as np.

-   **1.2 The Series Object**

    -   Definition: One-dimensional labeled array.
    -   Creation: Creating a Series from a Python list.
    -   Handling Types: Default indices and data types.

-   **1.3 The DataFrame Object**

    -   Definition: Two-dimensional labeled data structure (table).
    -   Creation Method 1: Passing a NumPy array with a datetime index
        > and labeled columns.
    -   Creation Method 2: Passing a dictionary of objects (keys become
        > column labels, values become data columns).
    -   Attribute Inspection: Checking dtypes of different columns.

### 2. Viewing and Inspecting Data (10 Minutes)

*Goal: Learn how to perform initial Exploratory Data Analysis (EDA).*

-   **2.1 Visualizing the Top and Bottom**

    -   Using head() and tail() to see data samples.

-   **2.2 Accessing Structural Metadata**

    -   Retrieving the index (df.index).
    -   Retrieving column names (df.columns).

-   **2.3 Underlying Data Representation**

    -   Converting to NumPy arrays using to_numpy().
    -   *Note on Performance:* Discuss when this operation is expensive
        > (mixed types) vs. cheap (homogeneous float data).

-   **2.4 Statistical Summary**

    -   Using describe() for quick count, mean, std, min, and quartile
        > analysis.

-   **2.5 Sorting**

    -   Sorting by axis (sort_index).
    -   Sorting by values (sort_values).

### 3. Selection and Indexing (20 Minutes)

*Goal: Master the extraction of specific data subsets, a critical skill
for feature engineering.*

-   **3.1 Standard Python Selection**

    -   Selecting a single column (df\[\'A\'\]).
    -   Row slicing (df\[0:3\]).
    -   *Production Warning:* Discuss why standard expressions are for
        > interactive use, while optimized methods (.at, .iat, .loc) are
        > recommended for production code.

-   **3.2 Selection by Label (.loc)**

    -   Selecting a cross-section by label.
    -   Multi-axis selection (getting specific rows and columns by
        > name).
    -   Label slicing (endpoints are included).

-   **3.3 Selection by Position (.iloc)**

    -   Selecting via integers (e.g., df.iloc\[3\]).
    -   Integer slicing (similar to NumPy/Python lists).
    -   Explicit lists of integer positions.

-   **3.4 Boolean Indexing (Filtering)**

    -   Filtering rows based on column values (e.g., df\[df\[\'A\'\] \>
        > 0\]).
    -   Filtering entire DataFrames (values that don\'t match become
        > NaN).
    -   Using isin() for filtering categorical/list membership.

### 4. Data Cleaning: Handling Missing Data (15 Minutes)

*Goal: Address the real-world problem of imperfect data.*

-   **4.1 Representation**

    -   Understanding np.nan and its role.

-   **4.2 Detection**

    -   Using isna() (or isnull()) to create boolean masks of missing
        > data.

-   **4.3 Deletion**

    -   Using dropna() to remove rows with any missing values.

-   **4.4 Imputation**

    -   Using fillna() to replace missing values (e.g., with a mean or
        > scalar).

### 5. Operations and Aggregation (15 Minutes)

*Goal: Apply functions to data for analysis and transformation.*

-   **5.1 Statistical Operations**

    -   Calculating the mean (df.mean()). Note: Operations exclude
        > missing data by default.
    -   Broadcasting: Operating between objects of different dimensions
        > (shifting, subtracting).

-   **5.2 Applying Functions**

    -   Using apply() to run custom functions (e.g., np.cumsum or lambda
        > functions) over data.

-   **5.3 String Manipulation**

    -   Vectorized string operations (str.lower(), str.len()) on Series.

-   **5.4 Histogramming**

    -   Using value_counts() to understand distribution of values.

### 6. Merging, Grouping, and Reshaping (15 Minutes)

*Goal: Combine disparate data sources and summarize them.*

-   **6.1 Concatenation**

    -   Using pd.concat() to stack DataFrames together.

-   **6.2 Database-style Joins**

    -   Using pd.merge() for SQL-style joins (inner, outer, left,
        > right).

-   **6.3 Grouping (groupby)**

    -   The \'Split-Apply-Combine\' methodology (Split data into groups
        > -\> Apply function -\> Combine results).
    -   Grouping by one or multiple columns and applying sums or means.

-   **6.4 Reshaping**

    -   Understanding stack() (compressing columns into index) and
        > pivot_table().

### 7. Time Series and I/O (5 Minutes)

*Goal: Brief overview of temporal data and persistence.*

-   **7.1 Time Series**

    -   Resampling data (e.g., converting second-level data to 5-minute
        > means).
    -   Time zone handling.

-   **7.2 Input / Output**

    -   Reading and writing CSV files (read_csv, to_csv).
    -   Reading and writing Excel files (read_excel, to_excel).
