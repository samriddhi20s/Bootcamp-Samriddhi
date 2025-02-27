# Streams Notes

## Tasks Covered
- Drills
- Workflow Apps
- Record Processing
- Step 1: Basic Record Processing
- Step 1.5: Extending Functionality
- Step 2: Customizing the Application
- Step 2.5: Learning Iterators
- Step 2.75: Stream Functions
- Step 3: Using Iterators for Pipelines
- Step 3.5: Adapter Functions

## Approach
For each step, I followed the given guidelines, implemented the functionality, and tested the scripts to ensure correctness.

## Issues Faced & Solutions

### 1. Error: poetry.lock not found. Run poetry lock to create it.
**Solution:** Run the following command to generate the lock file:
```sh
poetry lock
```
If the error persists, ensure that your `pyproject.toml` is correctly set up and try:
```sh
poetry install
```

### 2. Because samriddhi-wf-dynamic depends on samriddhi-wf-basic (^0.2.0) which doesn't match any versions, version solving failed.
**Solution:** Ensure that `samriddhi-wf-basic` version 0.2.0 is correctly published. If not, republish it using:
```sh
poetry publish --build
```
Then, try updating dependencies in `samriddhi-wf-dynamic`:
```sh
poetry update
```

### 3. ERROR: Could not find a version that satisfies the requirement samriddhi-wf-basic==0.2.0 (from versions: none)
**Solution:** Check if the package was successfully uploaded to Test PyPI:
```sh
poetry publish --repository testpypi
```
Verify package availability at [Test PyPI](https://test.pypi.org/). If needed, update and republish the package.

### 4. ERROR: 400 Bad Request from Test PyPI
**Solution:** This is usually due to authentication issues. Ensure correct credentials by running:
```sh
poetry config pypi-token.testpypi YOUR_TOKEN
```
Then, retry publishing with:
```sh
poetry publish --build --repository testpypi
```

### 5. Error: dynamic: command not found
**Solution:**
- Step 1: Ensure the package is installed correctly.
- Step 2: Verify that the dynamic command exists.
- Step 3: Check pyproject.toml for correct configurations.
- Step 4: Check Python path issues.

### 6. Error: toml-lint: command not found
**Solution:** Install toml-lint using:
```sh
pip install toml-lint
```
and validate.

### 7. Error: Could not find a version that satisfies the requirement toml-lint
**Solution:** Manually check and validate `pyproject.toml` and attempt to reinstall.

## Learnings
- How to use iterators and streams efficiently.
- How to process large files without loading them into memory.
- How to create pipelines for stream processing.
- How to package and publish Python modules using Poetry.
- How to debug dependency and packaging issues.

## ChatGPT Assistance
ChatGPT helped in debugging errors, suggesting improvements for iterator-based pipelines, and clarifying concepts related to Poetry package management.
