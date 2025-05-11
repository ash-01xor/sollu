# sollu
Your Terminal Dictionary powered by AI

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://github.com/ash-01xor/Sollu/blob/main/LICENSE)

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
### Example
Define single word
```bash
sollu define life
```
Define multiple words:
```bash
sollu define ubiquitous stoic
```

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details
