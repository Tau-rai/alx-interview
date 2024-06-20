# Log Parsing

This repository contains code for log parsing in Python. The purpose of this project is to extract useful information from log files and perform analysis on the data.

The Python script reads log entries from standard input (`stdin`), processes them to extract key metrics, and prints statistical summaries. The script handles specific log formats, processes data efficiently, and provides real-time updates every 10 lines or upon receiving a keyboard interrupt (Ctrl+C).

## Key Concepts Covered

**File I/O**: Reads input line by line from `stdin`.

**Signal Handling**: Handles keyboard interruption (Ctrl+C) to print statistics before exiting.

**Data Processing**: Uses regular expressions to parse and validate the format of each log line.

**Dictionaries**: Uses dictionaries to count occurrences of status codes and accumulate file sizes.

**Exception Handling**: Manages exceptions during file reading and data processing.