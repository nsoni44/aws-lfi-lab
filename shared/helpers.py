# file: shared/helpers.py
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEM = ROOT / 'shared' / 'memory.json'
CFG = ROOT / 'shared' / 'config.json'

class State:
    @staticmethod
    def load_mem():
        if not MEM.exists():
            MEM.write_text('{}')
        return json.loads(MEM.read_text())

    @staticmethod
    def save_mem(data):
        MEM.write_text(json.dumps(data, indent=2))

    @staticmethod
    def load_cfg():
        if not CFG.exists():
            raise SystemExit("shared/config.json is missing. Add your base_url there.")
        cfg = json.loads(CFG.read_text())
        if 'base_url' not in cfg or not cfg['base_url'].startswith('http'):
            raise SystemExit("Set a valid 'base_url' (full https Lambda URL) in shared/config.json")
        # defaults
        cfg.setdefault('region', 'us-east-1')
        cfg.setdefault('profile', 'lfi')
        return cfg