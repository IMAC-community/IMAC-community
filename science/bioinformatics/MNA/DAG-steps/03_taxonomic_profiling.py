"""
Marine Taxonomic Profiling

Accurate taxonomic assignment in marine environments requires
specialized databases and depth-aware classification strategies.

Marine Microbial Diversity:
- Surface waters: Phototrophs dominate (Prochlorococcus, Synechococcus)
- Mesopelagic: Heterotrophs increase (SAR11, SAR86)
- Deep sea: Specialized pressure-adapted taxa
- Oxygen minimum zones: Anaerobic specialists

Challenges:
- Many marine microbes are uncultured
- High diversity but uneven coverage in databases
- Depth-specific adaptations of same species
- Seasonal and geographic variations
"""

from typing import Dict, List, Tuple, Optional, Set
import logging
from pathlib import Path
import numpy as np
import pandas as pd
from Bio import SeqIO
from collections import defaultdict, Counter
import json

logger = logging.getLogger(__name__)


def profile_marine_taxa(
    input_sequences: Path,
    output_profile: Path,
    config: Dict,
    depth_meters: Optional[float] = None,
    educational_mode: bool = False
) -> Dict[str, any]:
    """
    Assign taxonomy with marine-specific optimizations.
    
    Depth-based adjustments:
    - Photic zone (0-200m): Expect phototrophs
    - Mesopelagic (200-1000m): Expect heterotrophs
    - Deep sea (>1000m): Expect pressure-adapted taxa
    
    Args:
        input_sequences: Path to denoised sequences
        output_profile: Path for taxonomic profile output
        config: Taxonomic profiling configuration
        depth_meters: Sample depth for depth-aware profiling
        educational_mode: Enable educational output
        
    Returns:
        Dictionary with taxonomic profile and statistics
    """
    if educational_mode:
        logger.info("🧬 Starting Marine Taxonomic Profiling...")
        logger.info("\nDid you know? The ocean has distinct depth zones:")
        logger.info("☀️  Euphotic (0-200m): Sunlight penetrates, photosynthesis occurs")
        logger.info("🌙 Dysphotic (200-1000m): Twilight zone, no photosynthesis")
        logger.info("⚫ Aphotic (>1000m): No light, unique adaptations")
        
        if depth_meters:
            zone = get_depth_zone(depth_meters)
            logger.info(f"\nYour sample is from the {zone} zone!")
    
    # Initialize results
    results = {
        'total_sequences': 0,
        'classified_sequences': 0,
        'taxonomic_profile': {},
        'diversity_metrics': {},
        'depth_zone': get_depth_zone(depth_meters) if depth_meters else 'unknown',
        'contamination_removed': 0
    }
    
    # TODO: Implement actual taxonomic profiling
    # Placeholder implementation
    results['total_sequences'] = 8000
    results['classified_sequences'] = 7200
    
    # Mock taxonomic profile
    mock_profile = generate_mock_marine_profile(depth_meters)
    results['taxonomic_profile'] = mock_profile
    
    # Calculate diversity metrics
    results['diversity_metrics'] = calculate_marine_diversity(mock_profile)
    
    if educational_mode:
        logger.info("\n📊 Taxonomic Profile Summary:")
        logger.info(f"Total sequences: {results['total_sequences']:,}")
        logger.info(f"Successfully classified: {results['classified_sequences']:,}")
        logger.info(f"Shannon diversity: {results['diversity_metrics']['shannon']:.2f}")
        logger.info("\nTop 5 taxa:")
        for taxon, abundance in list(results['taxonomic_profile'].items())[:5]:
            logger.info(f"  - {taxon}: {abundance:.1%}")
    
    return results


def get_depth_zone(depth_meters: float) -> str:
    """
    Classify depth into oceanographic zones.
    
    Args:
        depth_meters: Depth in meters
        
    Returns:
        Name of depth zone
    """
    if depth_meters <= 200:
        return "euphotic"
    elif depth_meters <= 1000:
        return "dysphotic"
    elif depth_meters <= 4000:
        return "bathypelagic"
    elif depth_meters <= 6000:
        return "abyssopelagic"
    else:
        return "hadalpelagic"


def apply_depth_priors(
    taxonomic_assignments: Dict[str, float],
    depth_meters: float,
    config: Dict
) -> Dict[str, float]:
    """
    Adjust taxonomic assignments based on depth expectations.
    
    Use ecological knowledge to improve accuracy:
    - Phototrophs unlikely in deep water
    - Pressure-adapted taxa unlikely in surface
    - Some taxa have depth preferences
    
    Args:
        taxonomic_assignments: Initial assignments
        depth_meters: Sample depth
        config: Configuration with priors
        
    Returns:
        Adjusted taxonomic assignments
    """
    zone = get_depth_zone(depth_meters)
    adjusted = taxonomic_assignments.copy()
    
    if zone in ["bathypelagic", "abyssopelagic", "hadalpelagic"]:
        # Deep water adjustments
        for taxon in adjusted:
            if "Prochlorococcus" in taxon or "Synechococcus" in taxon:
                # Phototrophs very unlikely in deep water
                adjusted[taxon] *= 0.01
            elif "deep" in taxon.lower() or "bathy" in taxon.lower():
                # Boost deep-adapted taxa
                adjusted[taxon] *= 1.5
    
    elif zone == "euphotic":
        # Surface water adjustments
        for taxon in adjusted:
            if "Prochlorococcus" in taxon:
                # Very common in surface tropical waters
                adjusted[taxon] *= 1.3
    
    # Renormalize
    total = sum(adjusted.values())
    if total > 0:
        adjusted = {k: v/total for k, v in adjusted.items()}
    
    return adjusted


def remove_terrestrial_contamination(
    taxonomic_profile: Dict[str, float],
    config: Dict
) -> Tuple[Dict[str, float], Set[str]]:
    """
    Remove likely terrestrial contaminants from marine samples.
    
    Common contaminants:
    - Soil bacteria (Bacillus, Streptomyces)
    - Plant chloroplasts
    - Human microbiome (Escherichia, Staphylococcus)
    - Freshwater taxa in offshore samples
    
    Args:
        taxonomic_profile: Original profile
        config: Configuration with contamination list
        
    Returns:
        Tuple of (cleaned_profile, removed_taxa)
    """
    terrestrial_indicators = {
        "Bacillus", "Streptomyces", "Escherichia", "Staphylococcus",
        "Chloroplast", "Mitochondria", "Pseudomonas_aeruginosa",
        "Clostridium", "Mycobacterium", "plant"
    }
    
    cleaned = {}
    removed = set()
    
    for taxon, abundance in taxonomic_profile.items():
        is_contaminant = False
        for indicator in terrestrial_indicators:
            if indicator.lower() in taxon.lower():
                is_contaminant = True
                removed.add(taxon)
                break
        
        if not is_contaminant:
            cleaned[taxon] = abundance
    
    # Renormalize after removal
    total = sum(cleaned.values())
    if total > 0:
        cleaned = {k: v/total for k, v in cleaned.items()}
    
    return cleaned, removed


def calculate_marine_diversity(
    taxonomic_profile: Dict[str, float]
) -> Dict[str, float]:
    """
    Calculate diversity metrics relevant for marine communities.
    
    Metrics:
    - Shannon diversity: Overall diversity
    - Simpson index: Evenness
    - Pielou evenness: How evenly distributed
    - Marine specialist ratio: Fraction of known marine taxa
    
    Args:
        taxonomic_profile: Taxonomic abundances
        
    Returns:
        Dictionary of diversity metrics
    """
    abundances = np.array(list(taxonomic_profile.values()))
    abundances = abundances[abundances > 0]  # Remove zeros
    
    # Shannon diversity
    shannon = -np.sum(abundances * np.log(abundances))
    
    # Simpson index
    simpson = 1 - np.sum(abundances ** 2)
    
    # Pielou evenness
    S = len(abundances)  # Number of taxa
    pielou = shannon / np.log(S) if S > 1 else 0
    
    # Marine specialist ratio (mock calculation)
    marine_specialists = [
        "SAR11", "Prochlorococcus", "SAR86", "Thaumarchaeota",
        "Marine_Group_II", "SAR324", "Roseobacter"
    ]
    
    specialist_abundance = sum(
        abundance for taxon, abundance in taxonomic_profile.items()
        if any(specialist in taxon for specialist in marine_specialists)
    )
    
    return {
        'shannon': shannon,
        'simpson': simpson,
        'pielou_evenness': pielou,
        'richness': S,
        'marine_specialist_ratio': specialist_abundance
    }


def generate_mock_marine_profile(
    depth_meters: Optional[float] = None
) -> Dict[str, float]:
    """
    Generate realistic mock taxonomic profile for demonstrations.
    
    Args:
        depth_meters: Sample depth
        
    Returns:
        Mock taxonomic profile
    """
    if depth_meters is None or depth_meters < 200:
        # Surface water profile
        profile = {
            "Prochlorococcus_marinus": 0.25,
            "SAR11_clade": 0.20,
            "Synechococcus": 0.10,
            "SAR86_clade": 0.08,
            "Roseobacter_clade": 0.06,
            "SAR116_clade": 0.05,
            "Flavobacteria": 0.04,
            "SAR324_clade": 0.03,
            "Others": 0.19
        }
    else:
        # Deep water profile
        profile = {
            "SAR11_clade": 0.18,
            "Thaumarchaeota": 0.15,
            "SAR202_clade": 0.12,
            "SAR324_clade": 0.10,
            "Marine_Group_II_archaea": 0.08,
            "SAR406_clade": 0.07,
            "Nitrospinae": 0.05,
            "Deep_sea_bacteria": 0.10,
            "Others": 0.15
        }
    
    return profile


# Educational functions

def explain_marine_taxa() -> None:
    """
    Educational overview of major marine microbial groups.
    """
    print("""
    🌊 Major Marine Microbial Groups
    
    🦠 BACTERIA:
    
    1. SAR11 (Pelagibacterales)
       - Most abundant organism on Earth!
       - ~25% of ocean bacteria
       - Tiny cells, streamlined genome
       - Heterotrophs eating dissolved organic matter
    
    2. Prochlorococcus
       - Smallest photosynthetic organism
       - Dominates tropical/subtropical oceans
       - Multiple ecotypes at different depths
       - Produces ~20% of ocean's oxygen
    
    3. SAR86
       - Abundant heterotrophs
       - Have proteorhodopsin (light-harvesting)
       - Important in carbon cycling
    
    🧪 ARCHAEA:
    
    1. Thaumarchaeota
       - Ammonia oxidizers (nitrification)
       - Abundant below photic zone
       - Key players in nitrogen cycle
    
    2. Marine Group II
       - Photoheterotrophs
       - Surface water specialists
       - Seasonal abundance patterns
    
    🧬 UNDERSTANDING DIVERSITY:
    
    High diversity = Healthy ecosystem
    Low diversity = Stress or disturbance
    
    Typical Shannon diversity:
    - Coastal: 3.5-4.5
    - Open ocean: 3.0-4.0
    - Deep sea: 2.5-3.5
    """)


def demonstrate_depth_effects() -> None:
    """
    Show how depth affects microbial communities.
    """
    print("""
    🌊 Depth Effects on Marine Microbes
    
    ☀️ SURFACE (0-200m):
    Light: ✓ Abundant
    Temperature: 15-30°C
    Pressure: Low
    
    Dominant microbes:
    - Prochlorococcus (photosynthesis)
    - Synechococcus (photosynthesis)
    - SAR11 (heterotroph)
    - Roseobacter (versatile)
    
    🌙 MESOPELAGIC (200-1000m):
    Light: ✗ None for photosynthesis
    Temperature: 4-15°C
    Pressure: Increasing
    
    Dominant microbes:
    - SAR11 (different ecotypes)
    - Thaumarchaeota (ammonia oxidation)
    - SAR324 (dark carbon fixation)
    
    ⚫ DEEP SEA (>1000m):
    Light: ✗ Total darkness
    Temperature: 2-4°C
    Pressure: Extreme
    
    Dominant microbes:
    - Pressure-adapted specialists
    - Slow-growing oligotrophs
    - Unique metabolisms
    
    Key Insight: Same genus, different adaptations!
    Example: Surface vs deep SAR11 are genetically distinct
    """)


if __name__ == "__main__":
    # Educational demonstrations
    explain_marine_taxa()
    print("\n" + "="*50 + "\n")
    demonstrate_depth_effects()