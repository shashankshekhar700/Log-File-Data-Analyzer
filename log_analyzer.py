def analyze_logs():
    # 1. Simulated log data (No separate file needed!)
    log_data = """INFO: System boot successful
ERROR 404: API endpoint not found
INFO: User 994 logged in
ERROR 500: Database timeout
WARNING: Memory usage at 85%
ERROR 404: API endpoint not found
ERROR 404: API endpoint not found
ERROR 500: Database timeout
INFO: Data backup complete"""

    error_counts = {}
    
    # 2. Read the data and find errors
    for line in log_data.split('\n'):
        if "ERROR" in line:
            error = line.strip()
            # 3. Count occurrences using a dictionary
            error_counts[error] = error_counts.get(error, 0) + 1

    # 4. Sort the dictionary by frequency (highest to lowest)
    sorted_errors = sorted(error_counts.items(), key=lambda item: item[1], reverse=True)

    # 5. Print the final report
    print("--- Server Error Analysis Report ---")
    for error, count in sorted_errors:
        print(f"{count} occurrences -> {error}")

# Run the function
analyze_logs()