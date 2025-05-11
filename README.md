# sollu
Your Terminal Dictionary powered by AI

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://github.com/ash-01xor/Sollu/blob/main/LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/sollu.svg)](https://pypi.org/project/sollu/)

## Overview

**sollu** is a simple yet powerful command-line utility designed to provide instant definitions and example sentences for words using the capabilities of the Google Gemini model. Built for anyone who wants to stay in the flow without distractions, tabs.

## Features

- **Fast Lookups:** Get definitions and examples quickly.
- **Multiple Words:** Define several words in a single command.

## Prerequisites

Before you can use Sollu, you need:

1.  **Python 3.9+:** Make sure you have a compatible Python version installed.
2.  **Google Gemini API Key:** Obtain a free API key from the [Google AI Studio](https://makersuite.google.com/app/apikey)

## Installation 

It's highly recommended to install `sollu` within a virtual environment. 

```bash
pip install sollu
```

## Configuration

Sollu requires your Google Gemini API key to function. Configuration commands are grouped under `sollu config`

Your API key will be stored in a file named .env inside the directory `~/.config/sollu`.

### Set API key
Use the config set subcommand to save your API key:
```bash
sollu config set --key YOUR_API_KEY
```
### Delete API key
To remove just the saved API key:
```bash  
sollu config delete
```
### Reset configuration
To delete the entire `~/.config/sollu/` directory and all its contents:
```bash  
sollu config reset
```

## Usage

Once installed and configured, you can use the define command to look up words:
```bash
sollu define <word1> <word2> ...
```
### Examples
Defining a single word
```bash
sollu define work-ethic
```
![Single word](https://raw.githubusercontent.com/ash-01xor/sollu/refs/heads/main/images/output_word.png)

Defining multiple words:
```bash
sollu define stoic healthy
```
![Multiple words](https://raw.githubusercontent.com/ash-01xor/sollu/refs/heads/main/images/output_multiple_words.png)

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details
