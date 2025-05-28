"""
Marine eDNA Analysis Pipeline - DAG Steps

This package contains modular functions for each step of the marine eDNA
metabolic network analysis workflow. Each module is designed to be:
- Self-contained with clear inputs/outputs
- Marine-optimized with ocean-specific adaptations
- Educational with comprehensive documentation

Modules:
- quality_control: Nanopore QC with contamination detection
- denoising: Error correction for long reads
- taxonomic_profiling: Marine-optimized taxonomic assignment
- humann3_execution: Metabolic pathway quantification
- marine_normalization: Ocean-specific abundance corrections
- timeseries_analysis: Temporal pattern detection
- visualization: Interactive plotting functions
"""

import logging
from pathlib import Path

# Configure module logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Version info
__version__ = "1.0.0"
__author__ = "Marine eDNA Analysis Team"

# Shared utilities
def validate_file_path(path: Path, must_exist: bool = True) -> Path:
    """Validate and return Path object."""
    path = Path(path)
    if must_exist and not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return path

def setup_output_directory(output_path: Path) -> Path:
    """Create output directory if it doesn't exist."""
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path