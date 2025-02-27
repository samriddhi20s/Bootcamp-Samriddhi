# Poetry Setup Notes

## Understanding the Task
The objective was to install and configure Poetry, a dependency management and packaging tool for Python, on a Linux system, and successfully build and publish packages to TestPyPI.

## Approach
1. Installed and configured Poetry.
2. Created a Python project and managed dependencies.
3. Built and published a module using TestPyPI.
4. Configured `pyproject.toml` for automatic TestPyPI publishing.
5. Developed a CLI tool with Typer.
6. Ensured `pip install` works with an entry-point command.
7. Learned how to work with `requirements.txt` in Poetry.

## Problems Faced

### Command Not Found
After running the initial installation command, the terminal returned:

> Command 'poetry' not found, but can be installed with: sudo apt install python3-poetry

**Solution:** Installed it using the suggested command.

### Invalid Configuration Error
Encountered the following error after setting up Poetry:

> The Poetry configuration is invalid: - data.source[0] must not contain {'default'} properties

**Solution:** Identified and corrected the misconfiguration by changing `default` to `primary`.

### Build Command Error
**Command:**
```sh
poetry build
```
**Error:**
> The Poetry configuration is invalid: - data.source[0].priority must be one of ['primary', 'supplemental', 'explicit']

**Solution:** Modified `priority` to `primary` in the configuration.

### Publishing Error
**Command:**
```sh
poetry publish -r testpypi --username __token__ --password <testpypi_token>
```
**Error:**
> HTTP Error 405: Method Not Allowed

**Solution:** Attempted an alternative approach:
```sh
poetry config pypi-token.testpypi <your_testpypi_token>
```

## What I Learned
- Alternative ways to install Poetry when the primary method fails.
- How to troubleshoot common installation and configuration errors.
- The importance of verifying installations after setup.
- Proper configuration steps for publishing packages to TestPyPI.

## ChatGPT Assistance
ChatGPT helped by:
- Suggesting alternative installation methods when the first attempt failed.
- Providing insights on resolving the Poetry configuration issue.
- Assisting in troubleshooting build and publishing errors.
- Explaining how to set up authentication for TestPyPI publishing.

### Links:
- [ChatGPT Share Link 1](https://chatgpt.com/share/67bafadc-745c-8004-8e82-0b615d40ec54)
- [ChatGPT Share Link 2](https://chatgpt.com/share/67bafb15-748c-8004-9a53-956ed3a45fc5)
- [ChatGPT Share Link 3](https://chatgpt.com/share/67bafa38-b690-8004-87cf-df9cda14d140)
