# asyncprbot

Have agents work on PRs for you while you're AFK.

## Setup

### Step 1: Activate your virtual environment

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Step 2: Install dependencies

```bash
pip install -r dev-requirements.txt
```

This installs the core dependencies plus dev tools (pytest, ruff).

### Step 3: Configure API access

Create a `.env` file with your Anthropic API key:

```bash
ANTHROPIC_API_KEY=your_api_key_here
```

## Running `asyncprbot`

```bash
python -m asyncprbot
```

Note: This must be run from the project root directory (where you can see the `asyncprbot/` folder). The `-m` flag runs it as a module, which ensures proper import resolution.

## Development Workflows

### Linting and Formatting

```bash
ruff check .   # Check for linting issues
ruff format .  # Auto-format code
```

### Testing
```bash
pytest              # Run all tests
pytest tests/unit/  # Run only unit tests
pytest -v           # Verbose output
```

### Why These Commands Work (note to self)
* `python -m asyncprbot` - Runs the package correctly (has `__main__.py`)
* `ruff` - Configured in `pyproject.toml` for Python 3.12+ standards  
* `pytest` - Finds tests in `tests/` directory automatically