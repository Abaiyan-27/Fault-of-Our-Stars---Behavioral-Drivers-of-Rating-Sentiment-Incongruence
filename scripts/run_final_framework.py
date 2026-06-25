#!/usr/bin/env python3
"""Run the final tourism review analysis framework from a source checkout."""

from __future__ import annotations

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from tourism_review_analysis.pipeline import main


if __name__ == "__main__":
    main()
