# my403 Bypasser

A Python tool to bypass 403/401 HTTP status code using various techniques such as header manipulation, protocol adjustments, port changes, and more.

## Features 
- **Header Bypass**: Manipulates HTTP header to bypass restrictions.
- **Protocol Bypass**: Exploits protocol discrepanices.
- **Port Bypass**: Tests various ports for access.
- **HTTP Method Bypass**: Tries different HTTP methods like `POST`, `TRACE`, etc.
- **URL Encode Bypass**: Encodes the URL to bypass filters.
- **SQL Injection Bypass**: Leverages SQL payloads to bypass WAFs like ModSecurity. 

## Usage

```bash
python3 my403.py --url <target_url> [options]
```

## Modes

- Scan with specific payloads: 

    `--header` Supprt HEADER Based bypasses/payloads
    ```bash
    python3 my403.py --url <target_url> --header
    ```

    `--protocol` Support PROTOCOL based bypasses/payloads
    ```bash
    python3 my403.py --url <target_url> --protocol
    ```

    `--port` Support PORT based bypasses/payloads
    ```bash
    python3 my403.py --url <target_url> --port
    ```

    `--HTTPmethod` Support HTTP Method based bypasses/payload
    ```bash
    python3 my403.py --url <target_url> --HTTPmethod
    ```

    `--encode` Support URL Encoding based bypasses/payloads
    ```bash
    python3 my403.py --url <target_url> --encode
    ```

    `--SQLi` Support SQLi based bypasses/payload
    ```bash
    python3 my403.py --url <target_url> --SQLi
    ```

    `--exploit` Run all bypass techniques 
    ```bash
    python3 my403.py --url <target_url> --exploit
    ```


## Output Indicators
Green: 2xx status codes (Success).

Yellow: 3xx status codes (Redirection).

Red: 4xx/5xx status codes (Client/Server errors).

Blue: 4xx status codes


## Prerequisites 

python 3.x

`request` module

Install via
```bash
pip3 install requests
```


### Disclaimer

- This tool is intended for educational purposes and authorized penetration testing only. Unauthorized usage is prohibited and may result in legal consequences.
