"""
Example script demonstrating how to use logpy utilities
"""

from logpy import printtime, delete_log_files, find_files_with_extension

def main():
    print("=" * 60)
    print("logpy Example Demonstration")
    print("=" * 60)
    print()
    
    # Example 1: Simple timestamped logging
    print("Example 1: Simple messages")
    print("-" * 60)
    printtime("Starting the application...")
    printtime("Processing data...")
    printtime("Application completed successfully!")
    print()
    
    # Example 2: Logging lists
    print("Example 2: Logging lists")
    print("-" * 60)
    tasks = ["Initialize database", "Load configuration", "Start server"]
    printtime(tasks)
    print()
    
    # Example 3: Logging dictionaries
    print("Example 3: Logging dictionaries")
    print("-" * 60)
    config = {
        "app_name": "MyApp",
        "version": "1.0.0",
        "settings": {
            "debug": True,
            "port": 8080
        },
        "features": ["logging", "authentication", "api"]
    }
    printtime(config)
    print()
    
    # Example 4: Logging with custom indentation
    print("Example 4: Mixed data structures")
    print("-" * 60)
    result = {
        "status": "success",
        "data": {
            "users": ["Alice", "Bob", "Charlie"],
            "count": 3
        },
        "timestamp": "2025-12-07"
    }
    printtime(result)
    print()
    
    # Example 5: Find files with specific extension
    print("Example 5: Finding Python files in current directory")
    print("-" * 60)
    py_files = find_files_with_extension(".", ".py")
    printtime(f"Found {len(py_files)} Python files:")
    for file in py_files:
        print(f"  - {file}")
    print()
    
    # Example 6: Information about log files
    print("Example 6: Log file management")
    print("-" * 60)
    log_files = find_files_with_extension(".", ".json")
    log_files = [f for f in log_files if "log_" in f]
    printtime(f"Current log files: {len(log_files)}")
    print()
    
    # Note: Uncomment the line below to delete all log files
    # print("Cleaning up log files...")
    # delete_log_files()
    
    print("=" * 60)
    print("Demo complete! Check the generated log_*.json file.")
    print("=" * 60)

if __name__ == "__main__":
    main()

# example.py - Example script demonstrating how to use logpy utilities