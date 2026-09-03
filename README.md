# Subdomain Enumerator

A Python-based asynchronous subdomain enumeration tool using
asyncio and aiohttp.

## Features

- Asynchronous subdomain checking
- Wordlist-based enumeration
- Concurrent requests using asyncio
- Faster than sequential checking
- Simple command-line interface

## Requirements

- Python 3.9+
- aiohttp

## Installation

Clone the repository:

    git clone https://github.com/YOUR_USERNAME/Subdomain-Enumerator.git

Enter the directory:

    cd Subdomain-Enumerator

Install dependencies:

    pip install -r requirements.txt

## Usage

    python subdomain_enum.py example.com wordlist.txt

## Example

    python subdomain_enum.py example.com wordlist.txt

Example output:

    [+] https://www.example.com -> 200
    [+] https://mail.example.com -> 200
    [+] https://blog.example.com -> 200

## How It Works

1. Reads subdomain names from a wordlist.
2. Creates asynchronous tasks.
3. Sends concurrent requests using aiohttp.
4. Prints subdomains that respond.

## Disclaimer

This project is intended for educational purposes and
authorized security testing only.

Do not use this tool against domains without permission.
