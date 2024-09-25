# Admin Panel Finder

A Python script that checks for the existence of admin panels on websites using user-defined paths. The script leverages threading for efficient URL checking and randomizes user agents to mimic real browser requests.

## Features

- **Multi-threaded**: Speeds up the process by using multiple threads to check URLs concurrently.
- **Random User Agents**: Utilizes the `fake_useragent` library to generate random User-Agent strings for each request.
- **Color-coded Output**: Provides clear visual feedback in the terminal with color-coded responses.

## Requirements

- Python 3.x
- `requests`
- `fake_useragent`

## Installation

To install the required packages, run:

```bash
pip install requests fake-useragent
```

## Usage

```bash
python adminfinder.py
```