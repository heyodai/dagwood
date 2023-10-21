# Dagwood

Dagwood is a simple logging tool that lets you setup logging to file and to console in one step.

Why "Dagwood"? Because a.) I was eating a sandwich when I decided to write this package, and b.) the name was available on PyPI.

## Usage

To install Dagwood, run:

```
pip install dagwood
```

### Basic Usage

To quickly set up a logger:

```python
import dagwood
logger = dagwood.assemble()
```

This will create a logger with default settings: log level set to `INFO` and log messages formatted as `'%(asctime)s - %(levelname)s - %(message)s'`. Logs will be written to a folder named `logs`.

### Advanced Usage

You can customize the log folder, log file name, log level, and log format by passing optional parameters to `assemble`.

- `folder_name`: The name of the folder to store log files (default: `'logs'`)
- `file_name`: The name of the log file (default: `None`, which generates a log file with a timestamp)
- `level`: The log level (default: `logging.INFO`)
- `format`: The log format (default: `'%(asctime)s - %(levelname)s - %(message)s'`)

```python
logger = dagwood.assemble(folder_name='my_logs', file_name='app.log', level=logging.DEBUG, format='%(levelname)s - %(message)s')
```

## Contributing

Feel free to open an issue or submit a pull request.

To publish a new version to PyPI:
```bash
pip install twine # if you don't have it already
python setup.py sdist bdist_wheel # build the package
twine upload dist/* # upload to PyPI
```

## Development

### Running Tests

The test suite can be run using Python's built-in `unittest` framework.

Navigate to the `tests` directory and run:

```
python -m unittest test_dagwood.py
```

Or, if you're in the root directory:

```
python -m unittest tests/test_dagwood.py
```
