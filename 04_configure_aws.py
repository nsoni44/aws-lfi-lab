# file: 04_configure_aws.py
import subprocess
from shared.helpers import State

def aws_config_set(profile, key, value):
    cmd = ["aws", "configure", "set", key, value, "--profile", profile]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"Failed: {' '.join(cmd)}\n{r.stderr}")

def main():
    cfg = State.load_cfg()
    mem = State.load_mem()

    req = ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'AWS_SESSION_TOKEN']
    missing = [k for k in req if not mem.get(k)]
    if missing:
        raise SystemExit(f"Missing creds in memory.json: {missing}. Run 03_extract_creds.py")

    profile = cfg['profile']
    aws_config_set(profile, 'aws_access_key_id', mem['AWS_ACCESS_KEY_ID'])
    aws_config_set(profile, 'aws_secret_access_key', mem['AWS_SECRET_ACCESS_KEY'])
    aws_config_set(profile, 'aws_session_token', mem['AWS_SESSION_TOKEN'])
    aws_config_set(profile, 'region', cfg['region'])

    print(f"[+] AWS CLI profile '{profile}' configured for region {cfg['region']}")

if __name__ == '__main__':
    main()