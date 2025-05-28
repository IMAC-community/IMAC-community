# Tutorial Sequences

This directory contains small example datasets for learning the marine eDNA analysis workflow.

## Files

### Sequence Files (to be generated)
- `coastal_sample_01.fastq` - 1000 reads from coastal surface water
- `open_ocean_sample.fastq` - 1000 reads from open ocean
- `deep_sea_sample.fastq` - 1000 reads from deep sea

### Metadata
- `../metadata_template.tsv` - Complete environmental metadata for all samples

## Generating Tutorial Data

To create example FASTQ files for testing, run:

```python
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import random
import numpy as np

def generate_tutorial_fastq(output_file, num_reads=1000, sample_type="coastal"):
    """Generate mock Nanopore reads for tutorials."""
    
    records = []
    
    for i in range(num_reads):
        # Generate random sequence length (Nanopore-like distribution)
        length = int(np.random.lognormal(7.5, 0.8))
        length = max(500, min(length, 30000))
        
        # Generate sequence with marine-typical GC content
        if sample_type == "coastal":
            gc_content = 0.45  # Typical marine
        elif sample_type == "deep":
            gc_content = 0.35  # AT-rich deep sea
        else:
            gc_content = 0.40
            
        # Create random sequence
        bases = ['A', 'T', 'G', 'C']
        weights = [(1-gc_content)/2, (1-gc_content)/2, gc_content/2, gc_content/2]
        sequence = ''.join(random.choices(bases, weights=weights, k=length))
        
        # Generate quality scores (Nanopore-like)
        qualities = np.random.normal(12, 3, length)
        qualities = np.clip(qualities, 4, 30).astype(int)
        
        # Create record
        record = SeqRecord(
            Seq(sequence),
            id=f"{sample_type}_read_{i:05d}",
            description=f"length={length}",
            letter_annotations={"phred_quality": qualities.tolist()}
        )
        records.append(record)
    
    # Write to file
    SeqIO.write(records, output_file, "fastq")
    print(f"Created {output_file} with {num_reads} reads")

# Generate example files
generate_tutorial_fastq("coastal_sample_01.fastq", 1000, "coastal")
generate_tutorial_fastq("open_ocean_sample.fastq", 1000, "ocean")
generate_tutorial_fastq("deep_sea_sample.fastq", 1000, "deep")
```

## Expected Characteristics

### Coastal Sample
- Higher diversity
- Mix of phototrophs and heterotrophs
- Some terrestrial contamination expected
- GC content ~40-50%

### Open Ocean Sample
- Dominated by SAR11, Prochlorococcus
- Lower diversity than coastal
- Very clean (no contamination)
- GC content ~35-45%

### Deep Sea Sample
- No phototrophs
- Specialized deep-sea taxa
- Lower GC content
- Unique metabolic pathways

## Tutorial Objectives

Using these samples, you will learn to:
1. Quality control Nanopore reads
2. Detect and remove contamination
3. Profile taxonomic composition
4. Quantify metabolic pathways
5. Interpret results ecologically

## Notes

- These are synthetic sequences for educational purposes
- Real marine eDNA data is available from [Ocean Sampling Day](https://www.microb3.eu/osd)
- For research, use actual sequencing data