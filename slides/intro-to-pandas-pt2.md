# Lecture Plan: Pandas Data Analysis Basics

**Dataset:** All India Monthly Meteorological Data
(all-india-monthly-rainfall.csv)

## 1. Introduction & Setup (10 Mins)

Pandas is the absolute backbone of data analysis in Python. While you
may already know how to load files and perform basic slicing, this
lecture focuses on the next critical step: **analyzing** and
**manipulating** the data to extract meaningful insights. We move beyond
simply \"opening\" data to actually \"understanding\" it.

We are working with a dataset containing monthly climate values (likely
Average Temperature) for India from 1901 to 2015. Each row represents a
year, and the columns represent the months. This structure allows us to
track climate trends over more than a century. By the end of this hour,
you will be able to clean this data, calculate complex statistics, and
group years by decades to find long-term patterns.

## 2. Inspecting Data Structure (10 Mins)

Before attempting any complex math, we must rigorously inspect the
dataframe. Trusting data blindly is a common source of errors in data
science. We use specific attributes to verify the integrity of our
dataset immediately after loading it.

### Essential Attributes and Methods

-   df.shape: This attribute returns a tuple representing (rows,
    columns).

    -   *Why use it?* It is the quickest way to verify if your data
        loaded completely. If you expect 100 years of data but see only
        5 rows, something went wrong.

-   df.columns: This lists all column headers.

    -   *Why use it?* Spaces or typos in column names (e.g., \" Jan\" vs
        \"Jan\") cause bugs. This helps you catch them early.

-   df.info(): The most comprehensive inspection tool. It provides a
    concise summary including:

    -   The data type of each column (integers, floats, or objects).

    -   The count of non-null values (identifying missing data).

    -   Memory usage (crucial for large datasets).

-   df.describe(): This generates a statistical summary for all numeric
    columns.

    -   *What it gives:* Count, Mean, Std Dev, Min, Max, and Quartiles
        (25%, 50%, 75%). It provides an instant \"snapshot\" of the
        data\'s distribution.

## 3. Statistical Operations (10 Mins)

Pandas provides a wrapper around NumPy functions, allowing us to
calculate statistics vertically (down a column) or horizontally (across
a row). Understanding the axis parameter is key here.

### Column-wise Statistics (Axis 0)

By default, operations like mean() work down the column. This is useful
for summarizing specific months across history.

-   df.mean(): Calculates the average.

    -   *Code:* jan_avg = df\[\'Jan\'\].mean()

    -   *Insight:* Tells us the historical average temperature for
        January.

-   df.std(): Calculates Standard Deviation.

    -   *Code:* volatility = df\[\'Jun\'\].std()

    -   *Insight:* A high standard deviation in June implies the weather
        is unpredictable, whereas a low one implies consistency.

### Row-wise Statistics (Axis 1)

Sometimes we need to aggregate data for a specific **Year** (row) rather
than a Month.

-   df.mean(axis=1): Calculates the average across columns.

    -   *Code:* df\[\'Annual_Avg\'\] = df.mean(axis=1)

    -   *Insight:* This creates a new column showing the average
        temperature for that specific year, which is essential for
        plotting annual trends.

## 4. Data Cleaning & Handling (10 Mins)

Real-world data is rarely perfect. It often contains \"NaN\" (Not a
Number) values or corrupted entries. Pandas provides robust tools to
handle these imperfections without deleting your entire dataset.

### Detecting and Fixing Missing Data

-   df.isna().sum(): This is the standard pattern for detection. It sums
    up the \"True\" values returned by isna(), giving you a count of
    missing items per column.

-   df.dropna(): The \"Nuclear Option\". It removes any row containing
    missing data.

    -   *Code:* df_clean = df.dropna()

    -   *Risk:* In small datasets, you might lose too much valuable
        information.

-   df.fillna(value): The \"Safe Option\". It fills gaps with a
    placeholder or a calculated value.

    -   *Code:* df_filled = df.fillna(df.mean())

    -   *Strategy:* Imputing missing values with the column mean is a
        common statistical technique to maintain the dataset\'s size
        while minimizing bias.

## 5. The Apply Function (10 Mins)

The apply() function is one of the most powerful tools in Pandas. It
allows you to \"broadcast\" a custom function across every single row or
column. It is far faster and more readable than writing a for loop.

### Basic Function Application

You can define a standard Python function and apply it to a column. For
example, converting Celsius to Fahrenheit:

def c_to_f(temp):

return (temp \* 9/5) + 32

\# Apply this function to the January column

df\[\'Jan_Fahrenheit\'\] = df\[\'Jan\'\].apply(c_to_f)

### Advanced Logic with Lambda

For simpler logic, use lambda functions to categorize data on the fly.

\# Create a text label: \'High\' if temp \> 25, else \'Normal\'

df\[\'Heat_Label\'\] = df\[\'May\'\].apply(lambda x: \'High\' if x \> 25
else \'Normal\')

-   *Why use it?* This allows you to create categorical features from
    numerical data, which is essential for classification tasks in
    machine learning.

## 6. Grouping and Aggregation (10 Mins)

The groupby() function implements the \"Split-Apply-Combine\" pattern.
It splits the data into groups based on some criteria, applies a
function to each group independently, and combines the results.

### Creating Categories

Since our dataset is continuous (Years 1901-2015), we first need a
category to group by. Let\'s create a \"Decade\" column.

\# Integer division by 10, then multiply by 10 (e.g., 1904 becomes 1900)

df\[\'Decade\'\] = (df.index // 10) \* 10

### Grouping by Decade

Now we can answer complex questions like: \"How has the average January
temperature changed per decade?\"

\# Group by the new \'Decade\' column and calculate the mean for \'Jan\'

decade_stats = df.groupby(\'Decade\')\[\'Jan\'\].mean()

print(decade_stats)

\# Output:

\# 1900 18.1

\# 1910 18.3

\# \...

You can also apply multiple aggregations at once to see the full
picture:

\# Get the Mean, Min, and Max temperature for January, per decade

summary = df.groupby(\'Decade\')\[\'Jan\'\].agg(\[\'mean\', \'min\',
\'max\'\])
