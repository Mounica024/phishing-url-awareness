#!/usr/bin/env python3
"""Phishing URL Awareness Checker — checks URL text for common warning signs.

This program does not visit URLs or determine whether a website is truly safe.
"""
import ipaddress
from urllib.parse import urlparse


def check_url(url: str) -> list[str]:
    """Return warning signs found in a URL string."""
    url = url.strip()
    if not url:
        raise ValueError("Please enter a URL.")

    # urlparse needs a scheme to reliably separate the hostname.
    candidate = url if "://" in url else "https://" + url
    parsed = urlparse(candidate)
    hostname = parsed.hostname

    if not hostname:
        raise ValueError("Could not identify a hostname. Check the URL format.")

    warnings = []
    if "@" in url:
        warnings.append("Contains an '@' symbol")
    if len(url) > 100:
        warnings.append(f"URL is long ({len(url)} characters; over 100)")
    try:
        ipaddress.ip_address(hostname)
        warnings.append("Uses an IP address instead of a domain name")
    except ValueError:
        pass
    if len(hostname.split(".")) >= 5:
        warnings.append("Hostname has 5 or more dot-separated segments")
    if "xn--" in hostname.lower():
        warnings.append("Hostname contains the 'xn--' punycode marker")
    if parsed.scheme.lower() == "http":
        warnings.append("Uses HTTP instead of HTTPS")

    return warnings


def main():
    print("=" * 58)
    print("        PHISHING URL AWARENESS CHECKER")
    print("=" * 58)
    print("Checks URL text only; it does not open the website.\n")

    while True:
        try:
            url = input("Enter a URL (or type 'quit' to exit): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting checker.")
            break

        if url.lower() == "quit":
            print("Exiting checker. Stay alert online!")
            break

        try:
            warnings = check_url(url)
        except ValueError as exc:
            print(f"Input error: {exc}\n")
            continue

        print(f"\nURL: {url}")
        if warnings:
            print("Result: WARNING SIGNS FOUND")
            for item in warnings:
                print(f"  - {item}")
        else:
            print("Result: No listed warning signs detected.")
        print("Reminder: This result does NOT prove a URL is safe.\n")


if __name__ == "__main__":
    main()
