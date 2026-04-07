#!/bin/bash


while read LINE
do
	grep "$LINE" life-expectancy.csv >>  ./data-per-country/"$LINE".csv 

 done < list-of-countries.txt
