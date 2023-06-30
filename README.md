# AirborneSWTestAssignment

Airborne SW project on Reports Generation
This project takes .JSON file as an input. It processes and generates different .csv reports

•	Input file is JSON file with the different key values of reports, polygon, ply shape, ply result, pick result and ply shape.
•	Different CSV Reports are generated through main program based on success and failure, ply shape, ply result, pick result and ply shape inputs from the json file.
•	Five different csv reports are generated using loader & csv_reports programs.

1.	Input file is .json file
2.	Main program allows the entry to process and formulate the reports.
3.	Base program builds structure of the json file with the classes and constructs the structure at ground level with default values.
4.	Loader program reads input file and processes the values from the lists, dictionaries. And then it dumps related values to respective fields of respective reports.
5.	Csv_reports program generates 6 csv validated different reports as given below.

CSVReportFormatter (Detailed Data Output (CSV))
CSVAttentionPliesFormatter (Plies Requiring Attention Overview (CSV))
CSVUnprocessedPliesFormatter (Overview of DXF files with warnings (CSV))
CSVBoundingBoxFormatter (Detailed Data Output w Bounding Box (CSV))
CSVSinglePhiFormatter (Simple Data Output w Bounding Box (CSV))
CSVTimeEstFormatter (Time Estimate (CSV))



