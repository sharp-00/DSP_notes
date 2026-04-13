#!/bin/bash


while read LINE
do
	grep "$LINE" life-expectancy.csv >>  ./data-per-country/"$LINE".csv 

 done < list-of-countries.txt
 #!/bin/bash

# Configuration: Set your file names here
INPUT_FILE="data.csv"
OUTPUT_FILE="counts.csv"

# Check if the input file exists before starting
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: $INPUT_FILE not found."
    exit 1
fi

# The logic:
# 1. Skip header
# 2. Extract first column
# 3. Sort and count
# 4. Use sed to reformat "count Name" to "Name,count"
# 5. Save to output file
tail -n +2 "$INPUT_FILE" | cut -d',' -f1 | sort | uniq -c | sed -E 's/^[[:space:]]*([0-9]+)[[:space:]]+(.*)/\2,\1/' > "$OUTPUT_FILE"

echo "Success! The counts have been saved to $OUTPUT_FILE."












./get_counts.sh | sort -t',' -k2,2rn > entries_per_country.csv
