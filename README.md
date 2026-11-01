# Phishing URL Awareness Checker

## Overview
A beginner-friendly Python command-line tool that checks the text of a URL for six common warning signs. It is an awareness tool, not a definitive phishing detector.

## Features
- Checks for an `@` symbol.
- Flags URLs longer than 100 characters.
- Detects an IP address used as the hostname.
- Flags hostnames with five or more dot-separated segments.
- Detects the `xn--` punycode marker in a hostname.
- Flags URLs using HTTP rather than HTTPS.
- Supports checking multiple URLs in one run; type `quit` to exit.
- Handles blank or malformed input with a helpful message.

## Requirements
- Python 3.10 or newer
- Python standard library only; no third-party packages required

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python phishing_checker.py
   ```

4. Paste a URL when prompted. Type `quit` to exit.

## Example
Input:
`http://192.0.2.10/account`

Expected warning signs include:
- Uses an IP address instead of a domain name
- Uses HTTP instead of HTTPS

## Tests
See [`tests/test_samples.md`](tests/test_samples.md) for five sample test cases. You can run the automated tests with:

```bash
python -m unittest discover -s tests -v
```

## Screenshots
The `screenshots` folder contains a sample program run and test results captured from this project.

## Improvements included
1. A loop allows users to check multiple URLs without restarting the program.
2. Blank or malformed input is handled with a clear error message.

## Limitations
- The program checks URL text only and never visits a website.
- These six signs are clues, not proof of phishing.
- A URL with no listed warning signs may still be malicious.
- HTTPS only encrypts the connection; it does not guarantee that a site is trustworthy.

## Ethical use
Use this tool for learning and awareness. Do not enter passwords or other private information. Do not visit suspicious links just to test them.

## Author
## Student Details

Name: Appalabhakthula Lakshmi Naga Mounica
Batch: 1
