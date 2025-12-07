# logPy
Simple set of Python scripts to automatically create, record and delete message logs from python scripts.

## Installation

### From GitHub (requirements.txt)
Add this line to your `requirements.txt`:
```
git+https://github.com/PatrickEasy/logPy.git
```

Or install directly:
```bash
pip install git+https://github.com/PatrickEasy/logPy.git
```

### Local Development Installation
```bash
git clone https://github.com/PatrickEasy/logPy.git
cd logPy
pip install -e .
```

## Usage

### Quick Start - Run the Example

```bash
python3 example.py
```

This will demonstrate all the features of logpy and create a timestamped JSON log file.

### Print timestamped messages with logging
```python
from logpy import printtime

# Simple message
printtime("This is a log message")

# Log lists and dictionaries
printtime(["Item 1", "Item 2", {"key": "value"}])
printtime({"status": "success", "data": ["a", "b", "c"]})
```

### Delete log files
```python
from logpy import delete_log_files

# Delete log files in current directory
delete_log_files()

# Delete log files in specific folder
delete_log_files("path/to/folder")

# Delete log files in multiple folders
delete_log_files(["folder1", "folder2"])
```

### Find files by extension
```python
from logpy import find_files_with_extension

# Find all .py files in a directory
python_files = find_files_with_extension("./src", ".py")
for file in python_files:
    print(file)
```

## Features

- **printtime**: Print timestamped messages and automatically save them to JSON log files
- **delete_log_files**: Clean up log files matching the pattern `log_*.json`
- **find_files_with_extension**: Recursively search for files with specific extensions

## License

MIT
