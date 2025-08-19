# AWS LFI Lab

A hands-on lab for exploring Local File Inclusion (LFI) vulnerabilities and their exploitation in AWS environments. This project provides a series of scripts and resources to simulate, detect, and exploit LFI scenarios, as well as to extract sensitive information and interact with AWS services.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Scripts Description](#scripts-description)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This lab is designed for security researchers, penetration testers, and developers to understand the risks associated with LFI vulnerabilities in cloud environments, particularly AWS. The scripts automate the process of checking for LFI, extracting credentials, configuring AWS CLI, and retrieving secrets.

---

## Project Structure

```
aws-lfi-lab/
├── 01_lfi_check.py         # Check for LFI vulnerabilities
├── 02_dump_environ.py      # Dump environment variables
├── 03_extract_creds.py     # Extract AWS credentials
├── 04_configure_aws.py     # Configure AWS CLI with extracted creds
├── 05_get_secrets.py       # Retrieve secrets from AWS
├── chain.sh                # Script to chain all steps
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── shared/
    ├── config.json         # Configuration file
    ├── helpers.py          # Shared helper functions
    ├── memory.json         # Persistent memory for scripts
    └── __pycache__/        # Python cache files
```

---

## Prerequisites

- Python 3.12+
- AWS CLI (if interacting with AWS)
- pip (Python package manager)
- Access to an AWS account (for testing AWS interactions)

---

## Installation



2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

---

## Usage

You can run each script individually or use the `chain.sh` script to execute the full workflow.

**Example:**
```powershell
python 01_lfi_check.py
python 02_dump_environ.py
python 03_extract_creds.py
python 04_configure_aws.py
python 05_get_secrets.py
```

Or run the chain script (on Unix-like systems):
```bash
bash chain.sh
```

---

## Scripts Description

- **01_lfi_check.py**: Scans for LFI vulnerabilities in the target application.
- **02_dump_environ.py**: Dumps environment variables, potentially exposing sensitive data.
- **03_extract_creds.py**: Extracts AWS credentials from environment or files.
- **04_configure_aws.py**: Configures AWS CLI using the extracted credentials.
- **05_get_secrets.py**: Retrieves secrets from AWS services (e.g., Secrets Manager, SSM).
- **shared/helpers.py**: Contains utility functions used by the scripts.
- **shared/config.json**: Stores configuration parameters.
- **shared/memory.json**: Used for persisting data between script runs.

---

## Configuration

Edit `shared/config.json` to set up target URLs, AWS region, or other parameters as needed.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---