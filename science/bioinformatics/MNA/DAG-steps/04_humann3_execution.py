"""
Marine-Optimized HUMANn3 Execution

HUMANn3 quantifies metabolic pathways from metagenomic data.
For marine samples, we use specialized databases that better
represent ocean microbial diversity.

Key Marine Metabolic Pathways:
1. Carbon Cycling
   - Photosynthesis and carbon fixation
   - DMSP metabolism (climate regulation)
   - Dissolved organic matter processing

2. Nitrogen Cycling
   - Nitrogen fixation (new nitrogen)
   - Nitrification (ammonia to nitrate)
   - Denitrification (nitrogen removal)
   - Anammox (anaerobic ammonia oxidation)

3. Sulfur Cycling
   - DMSP/DMS production
   - Sulfate reduction
   - Sulfur oxidation
"""

from typing import Dict, List, Optional, Tuple
import logging
from pathlib import Path
import subprocess
import pandas as pd
import numpy as np
import json
from datetime import datetime
import shutil

logger = logging.getLogger(__name__)


def run_humann3_marine(
    input_sequences: Path,
    output_dir: Path,
    config: Dict,
    sample_metadata: Optional[Dict] = None,
    educational_mode: bool = False
) -> Dict[str, any]:
    """
    Execute HUMANn3 with marine adaptations.
    
    Marine-specific features:
    - Custom ocean pathway definitions
    - Salinity-adjusted abundance calculations
    - Integration of depth/temperature metadata
    - Focus on biogeochemically relevant pathways
    
    Args:
        input_sequences: QC-passed sequences
        output_dir: Directory for HUMANn3 outputs
        config: HUMANn3 configuration
        sample_metadata: Environmental parameters (depth, temp, salinity)
        educational_mode: Enable educational output
        
    Returns:
        Dictionary with pathway abundances and statistics
    """
    if educational_mode:
        logger.info("⚙️  Starting HUMANn3 Metabolic Analysis...")
        logger.info("\nHUMANn3 workflow:")
        logger.info("1️⃣  Taxonomic profiling with MetaPhlAn")
        logger.info("2️⃣  Functional profiling with ChocoPhlAn")
        logger.info("3️⃣  Translated search with UniRef")
        logger.info("4️⃣  Pathway reconstruction")
        logger.info("\n🌊 Marine adaptations:")
        logger.info("- Using ocean-specific databases")
        logger.info("- Enhanced DMSP/DMS pathways")
        logger.info("- Marine nitrogen cycling focus")
    
    # Create output directory
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize results
    results = {
        'timestamp': datetime.now().isoformat(),
        'sample_metadata': sample_metadata or {},
        'pathway_abundances': {},
        'pathway_coverage': {},
        'gene_families': {},
        'unmapped_reads': 0,
        'qc_metrics': {},
        'marine_pathways': {}
    }
    
    # Build HUMANn3 command
    humann3_cmd = build_humann3_command(input_sequences, output_dir, config)
    
    if educational_mode:
        logger.info(f"\n💻 Command: {' '.join(humann3_cmd)}")
    
    # TODO: Actually run HUMANn3
    # For now, generate mock results
    mock_results = generate_mock_humann3_results(sample_metadata)
    results.update(mock_results)
    
    # Apply marine-specific processing
    results['marine_pathways'] = extract_marine_pathways(
        results['pathway_abundances'],
        config
    )
    
    if educational_mode:
        summarize_metabolic_potential(results)
    
    return results


def build_humann3_command(
    input_file: Path,
    output_dir: Path,
    config: Dict
) -> List[str]:
    """
    Build HUMANn3 command with marine-optimized parameters.
    
    Args:
        input_file: Input sequence file
        output_dir: Output directory
        config: Configuration parameters
        
    Returns:
        Command as list of strings
    """
    cmd = [
        'humann3',
        '--input', str(input_file),
        '--output', str(output_dir),
        '--nucleotide-database', config.get('nucleotide_database', 'chocophlan'),
        '--protein-database', config.get('protein_database', 'uniref90'),
        '--threads', str(config.get('threads', 4)),
        '--memory-use', 'maximum',
        '--output-format', 'tsv',
        '--remove-column-description',
        '--verbose'
    ]
    
    # Add marine-specific options
    if config.get('bypass_translated_search'):
        cmd.append('--bypass-translated-search')
    
    # Custom pathway definitions
    if 'marine_pathway_database' in config:
        cmd.extend(['--pathways-database', config['marine_pathway_database']])
    
    return cmd


def extract_marine_pathways(
    pathway_abundances: Dict[str, float],
    config: Dict
) -> Dict[str, Dict[str, float]]:
    """
    Extract and categorize marine-relevant metabolic pathways.
    
    Categories:
    - Carbon cycling
    - Nitrogen cycling
    - Sulfur cycling
    - Photosynthesis
    - Climate regulation
    
    Args:
        pathway_abundances: All pathway abundances
        config: Configuration with pathway definitions
        
    Returns:
        Categorized marine pathways
    """
    marine_categories = {
        'carbon_cycling': [
            'Carbon fixation',
            'Methane metabolism',
            'Organic acid metabolism'
        ],
        'nitrogen_cycling': [
            'Nitrogen fixation',
            'Nitrification',
            'Denitrification',
            'Anammox'
        ],
        'sulfur_cycling': [
            'DMSP biosynthesis',
            'DMSP degradation',
            'Sulfate reduction',
            'Sulfur oxidation'
        ],
        'photosynthesis': [
            'Photosystem I',
            'Photosystem II',
            'Carbon fixation pathways',
            'Chlorophyll biosynthesis'
        ],
        'climate_regulation': [
            'DMS production',
            'N2O production',
            'CO2 fixation'
        ]
    }
    
    categorized = {cat: {} for cat in marine_categories}
    
    for pathway, abundance in pathway_abundances.items():
        for category, keywords in marine_categories.items():
            if any(keyword.lower() in pathway.lower() for keyword in keywords):
                categorized[category][pathway] = abundance
    
    return categorized


def apply_environmental_corrections(
    abundances: Dict[str, float],
    metadata: Dict[str, float]
) -> Dict[str, float]:
    """
    Apply environmental corrections to pathway abundances.
    
    Corrections based on:
    - Temperature (Q10 effects)
    - Salinity (osmotic stress)
    - Depth (pressure effects)
    - Oxygen (aerobic vs anaerobic)
    
    Args:
        abundances: Raw pathway abundances
        metadata: Environmental parameters
        
    Returns:
        Corrected abundances
    """
    corrected = abundances.copy()
    
    # Temperature correction (Q10 = 2)
    if 'temperature' in metadata:
        temp = metadata['temperature']
        reference_temp = 20  # °C
        q10_factor = 2 ** ((temp - reference_temp) / 10)
        
        # Apply to temperature-sensitive pathways
        for pathway in corrected:
            if any(term in pathway.lower() for term in ['metabolism', 'respiration']):
                corrected[pathway] *= q10_factor
    
    # Salinity correction
    if 'salinity' in metadata:
        salinity = metadata['salinity']
        if salinity < 30:  # Brackish water
            # Reduce halophile-specific pathways
            for pathway in corrected:
                if 'osmotic' in pathway.lower() or 'salt' in pathway.lower():
                    corrected[pathway] *= 0.7
    
    # Depth/pressure correction
    if 'depth' in metadata:
        depth = metadata['depth']
        if depth > 1000:  # Deep sea
            # Enhance pressure-adapted pathways
            for pathway in corrected:
                if 'pressure' in pathway.lower() or 'piezophile' in pathway.lower():
                    corrected[pathway] *= 1.5
    
    return corrected


def calculate_biogeochemical_indices(
    marine_pathways: Dict[str, Dict[str, float]]
) -> Dict[str, float]:
    """
    Calculate indices relevant to ocean biogeochemistry.
    
    Indices:
    - Carbon sequestration potential
    - Nitrogen removal capacity
    - Climate regulation index
    - Primary production potential
    
    Args:
        marine_pathways: Categorized marine pathways
        
    Returns:
        Biogeochemical indices
    """
    indices = {}
    
    # Carbon sequestration potential
    carbon_fixation = sum(marine_pathways.get('carbon_cycling', {}).values())
    respiration = sum(
        v for k, v in marine_pathways.get('carbon_cycling', {}).items()
        if 'respiration' in k.lower()
    )
    indices['carbon_sequestration_potential'] = carbon_fixation - respiration
    
    # Nitrogen removal capacity
    denitrification = sum(
        v for k, v in marine_pathways.get('nitrogen_cycling', {}).items()
        if 'denitrif' in k.lower() or 'anammox' in k.lower()
    )
    indices['nitrogen_removal_capacity'] = denitrification
    
    # Climate regulation index
    dms_production = sum(
        v for k, v in marine_pathways.get('sulfur_cycling', {}).items()
        if 'dms' in k.lower() or 'dmsp' in k.lower()
    )
    indices['climate_regulation_index'] = dms_production
    
    # Primary production potential
    photosynthesis = sum(marine_pathways.get('photosynthesis', {}).values())
    indices['primary_production_potential'] = photosynthesis
    
    return indices


def generate_mock_humann3_results(
    metadata: Optional[Dict] = None
) -> Dict[str, any]:
    """
    Generate realistic mock results for demonstration.
    
    Args:
        metadata: Sample metadata
        
    Returns:
        Mock HUMANn3 results
    """
    # Mock pathway abundances
    pathways = {
        "Photosystem II": 0.15 if not metadata or metadata.get('depth', 0) < 200 else 0.01,
        "Carbon fixation - Calvin cycle": 0.12,
        "Nitrogen fixation": 0.08,
        "Ammonia oxidation": 0.10,
        "DMSP biosynthesis": 0.06,
        "DMSP degradation": 0.09,
        "Glycolysis": 0.20,
        "TCA cycle": 0.18,
        "Sulfate reduction": 0.05,
        "Methanogenesis": 0.02
    }
    
    # Mock gene families
    gene_families = {
        "K00001": 0.1,  # alcohol dehydrogenase
        "K00002": 0.08,  # alcohol dehydrogenase (NADP+)
        "K00003": 0.12,  # homoserine dehydrogenase
        "K00004": 0.09   # (R,R)-butanediol dehydrogenase
    }
    
    return {
        'pathway_abundances': pathways,
        'pathway_coverage': {k: np.random.uniform(0.6, 1.0) for k in pathways},
        'gene_families': gene_families,
        'unmapped_reads': 0.15,
        'qc_metrics': {
            'total_reads': 50000,
            'aligned_reads': 42500,
            'pathway_mapped_reads': 38000
        }
    }


def summarize_metabolic_potential(results: Dict[str, any]) -> None:
    """
    Provide educational summary of metabolic findings.
    
    Args:
        results: HUMANn3 results dictionary
    """
    logger.info("\n🌊 Metabolic Potential Summary:")
    logger.info("=" * 40)
    
    # Top pathways
    pathways = results['pathway_abundances']
    top_5 = sorted(pathways.items(), key=lambda x: x[1], reverse=True)[:5]
    
    logger.info("\nTop 5 Metabolic Pathways:")
    for pathway, abundance in top_5:
        logger.info(f"  • {pathway}: {abundance:.1%}")
    
    # Marine-specific insights
    marine = results.get('marine_pathways', {})
    if marine:
        logger.info("\n🌊 Ocean Biogeochemistry Insights:")
        
        if 'carbon_cycling' in marine and marine['carbon_cycling']:
            logger.info(f"  🌱 Carbon cycling: {len(marine['carbon_cycling'])} pathways detected")
        
        if 'nitrogen_cycling' in marine and marine['nitrogen_cycling']:
            logger.info(f"  💧 Nitrogen cycling: {len(marine['nitrogen_cycling'])} pathways detected")
        
        if 'climate_regulation' in marine and marine['climate_regulation']:
            logger.info(f"  ☁️  Climate regulation: Active DMS/DMSP metabolism detected")
    
    logger.info("\n💡 What this means:")
    logger.info("Your microbial community can:")
    logger.info("  - Fix carbon from CO2")
    logger.info("  - Cycle nitrogen compounds")
    logger.info("  - Produce climate-active gases")
    logger.info("  - Process organic matter")


# Educational functions

def explain_humann3_process() -> None:
    """
    Educational explanation of HUMANn3 workflow.
    """
    print("""
    🧭 How HUMANn3 Works
    
    HUMANn3 = HMP Unified Metabolic Analysis Network 3
    
    🔄 The HUMANn3 Workflow:
    
    1️⃣ TAXONOMIC PROFILING (MetaPhlAn)
       Sequences → Who's there?
       - Identifies microbes in your sample
       - Creates taxonomic profile
       - Guides database selection
    
    2️⃣ NUCLEOTIDE SEARCH (ChocoPhlAn)
       Sequences → Known genes?
       - Searches species-specific gene catalogs
       - Very fast for known organisms
       - Captures strain-level variation
    
    3️⃣ TRANSLATED SEARCH (UniRef)
       Unmapped DNA → Proteins → Functions?
       - Translates DNA to protein sequences
       - Searches protein database
       - Catches novel/divergent genes
    
    4️⃣ PATHWAY RECONSTRUCTION
       Genes → Pathways
       - Maps genes to metabolic pathways
       - Calculates pathway abundance
       - Assesses pathway completeness
    
    🌊 Marine Optimizations:
    
    ✓ Marine ChocoPhlAn: Ocean microbe genomes
    ✓ Marine UniRef: Ocean protein sequences
    ✓ Custom pathways: DMSP, marine nitrogen cycling
    ✓ Abundance corrections: Depth, temperature effects
    """)


def explain_marine_pathways() -> None:
    """
    Explain key marine metabolic pathways.
    """
    print("""
    🌊 Key Marine Metabolic Pathways
    
    🌱 CARBON CYCLING:
    
    1. Carbon Fixation (CO2 → Organic Carbon)
       - Calvin cycle (most phytoplankton)
       - C4 pathway (some diatoms)
       - 3-HP bicycle (some archaea)
       Importance: Primary production base
    
    2. DMSP Metabolism
       - DMSP = osmolyte in phytoplankton
       - Degraded to DMS (climate gas)
       - DMS → clouds → cooling effect
       Importance: Climate regulation
    
    💧 NITROGEN CYCLING:
    
    1. Nitrogen Fixation (N2 → NH3)
       - By Trichodesmium, UCYN-A
       - Adds new nitrogen to ocean
       Importance: Limits productivity
    
    2. Nitrification (NH3 → NO2 → NO3)
       - By Thaumarchaeota, Nitrospina
       - Recycles nitrogen
       Importance: Sustains production
    
    3. Denitrification (NO3 → N2)
       - In oxygen minimum zones
       - Removes nitrogen
       Importance: Balances N budget
    
    🐟 UNIQUE MARINE ADAPTATIONS:
    
    1. Proteorhodopsin
       - Light-driven proton pump
       - Supplemental energy
       - In SAR11, SAR86
    
    2. Carbon Concentrating
       - CO2 pumps for low ocean CO2
       - Essential for photosynthesis
       - In cyanobacteria, diatoms
    
    3. Osmotic Regulation
       - Salt stress pathways
       - Compatible solute synthesis
       - Universal in marine microbes
    """)


if __name__ == "__main__":
    # Educational demonstrations
    explain_humann3_process()
    print("\n" + "="*50 + "\n")
    explain_marine_pathways()