# 🔧 Marine eDNA Analysis Troubleshooting Guide

## Quick Solutions
- [Installation Issues](#installation-issues)
- [Data Quality Problems](#data-quality-problems)
- [Analysis Errors](#analysis-errors)
- [Marine-Specific Issues](#marine-specific-issues)
- [Performance Problems](#performance-problems)
- [Interpretation Challenges](#interpretation-challenges)

---

## Installation Issues

### Problem: Conda environment creation fails
**Symptoms:** Error during `conda env create -f environment.yml`

**Solutions:**
1. Update conda first:
   ```bash
   conda update -n base conda
   ```

2. Try mamba (faster):
   ```bash
   conda install mamba -n base -c conda-forge
   mamba env create -f environment.yml
   ```

3. Install in stages:
   ```bash
   conda create -n marine-edna-humann3 python=3.9
   conda activate marine-edna-humann3
   conda install -c bioconda humann3 metaphlan
   conda install -c conda-forge numpy pandas matplotlib
   ```

### Problem: HUMANn3 databases won't download
**Symptoms:** Timeout or connection errors

**Solutions:**
1. Use a stable connection and be patient (downloads can take hours)
2. Download to a local directory first:
   ```bash
   humann3_databases --download chocophlan full /path/to/local
   ```
3. For testing, use the demo databases:
   ```bash
   humann3_databases --download chocophlan DEMO
   ```

---

## Data Quality Problems

### Problem: Very high contamination rates (>10%)
**Symptoms:** Many reads flagged as terrestrial

**Possible Causes & Solutions:**

1. **Coastal sampling near river mouths**
   - Expected in these environments
   - Adjust contamination threshold in config:
   ```yaml
   quality_control:
     contamination_threshold: 0.90  # More stringent
   ```

2. **Atmospheric deposition**
   - Common in surface samples
   - Document in metadata
   - Consider depth-stratified sampling

3. **Lab contamination**
   - Check negative controls
   - Review lab protocols
   - Ensure clean sampling equipment

### Problem: Low quality scores across all reads
**Symptoms:** Mean quality <Q7

**Solutions:**
1. Check Nanopore flowcell age and pore occupancy
2. Review library preparation:
   - DNA quality (check 260/280 ratio)
   - Avoid over-fragmentation
3. For marine samples specifically:
   - High salt can affect sequencing
   - Ensure proper cleanup
   - Consider dilution

### Problem: Very short read lengths
**Symptoms:** Most reads <1kb

**Solutions:**
1. Check DNA extraction method:
   - Avoid excessive mechanical shearing
   - Use wide-bore pipette tips
2. For marine samples:
   - Some marine microbes have naturally fragmented DNA
   - Adjust expectations for deep-sea samples
3. Optimize library prep for long reads

---

## Analysis Errors

### Problem: HUMANn3 produces empty output
**Symptoms:** No pathways detected

**Debugging Steps:**
1. Check if sequences passed QC:
   ```python
   # In notebook
   print(f"Reads after QC: {qc_results['passed_reads']}")
   ```

2. Verify taxonomic profiling worked:
   ```bash
   # Check MetaPhlAn output
   head humann3_output/*_metaphlan_bugs_list.tsv
   ```

3. Common causes:
   - Too stringent QC filtering
   - Wrong database for marine samples
   - Very low biomass sample

### Problem: Unusual metabolic profiles
**Symptoms:** Pathways that don't make ecological sense

**Debugging:**
1. Check sample metadata:
   ```python
   # Verify depth makes sense for detected pathways
   if 'Photosystem' in abundant_pathways and depth > 200:
       print("Warning: Photosynthesis detected in dark zone!")
   ```

2. Look for contamination:
   - High cellulose degradation → terrestrial contamination
   - Human gut pathways → handling contamination

3. Verify database version matches your samples

---

## Marine-Specific Issues

### Problem: No marine-specific pathways detected
**Symptoms:** Missing DMSP, proteorhodopsin, etc.

**Solutions:**
1. Ensure marine databases are properly installed:
   ```bash
   ls reference_data/ocean_metabolic_pathways/
   ```

2. Check if custom pathways are loaded in config:
   ```yaml
   marine_adaptations:
     marine_pathway_database: "reference_data/ocean_metabolic_pathways/"
   ```

3. Some pathways are depth-specific:
   - DMSP: mainly surface waters
   - Anammox: OMZs
   - Pressure-response: deep only

### Problem: Freshwater taxa in offshore samples
**Symptoms:** Cyanobacteria typical of lakes/rivers

**Consider:**
1. Recent rainfall and runoff
2. Sampling location relative to rivers
3. Seasonal freshwater lenses
4. Check salinity in metadata

### Problem: Very low diversity in surface waters
**Symptoms:** Shannon diversity <2.5

**Possible Explanations:**
1. Phytoplankton bloom (natural)
   - Check chlorophyll data
   - Look for dominant taxa
   - Consider seasonal timing

2. Pollution or stress
   - Check other environmental parameters
   - Look for stress indicator genes

3. Technical issue
   - Verify sequencing depth adequate
   - Check for PCR bias

---

## Performance Problems

### Problem: Analysis taking too long
**Symptoms:** HUMANn3 running for days

**Speed Optimizations:**
1. Use more threads:
   ```yaml
   humann3:
     threads: 16  # Increase if available
   ```

2. Bypass translated search for well-studied environments:
   ```yaml
   humann3:
     bypass_translated_search: true
   ```

3. Pre-filter very large files:
   ```bash
   # Random subsample for testing
   seqtk sample input.fastq 0.1 > subsample.fastq
   ```

### Problem: Out of memory errors
**Symptoms:** Process killed, memory errors

**Solutions:**
1. Increase memory allocation:
   ```yaml
   compute:
     memory_limit_gb: 64
   ```

2. Process in chunks:
   ```yaml
   compute:
     chunk_size: 500  # Smaller chunks
   ```

3. Use a high-memory node on HPC

---

## Interpretation Challenges

### Problem: Conflicting ecological signals
**Example:** Both oxygenic and anaerobic pathways abundant

**Considerations:**
1. **Microscale gradients**
   - Ocean has oxic-anoxic interfaces
   - Particles create micro-niches
   - Both can coexist

2. **Sampling integrates communities**
   - Water column not homogeneous
   - Different depths mixed
   - Check sampling protocol

3. **Metabolic versatility**
   - Many marine microbes are facultative
   - Can switch metabolisms
   - Normal for marine systems

### Problem: Seasonal patterns unclear
**Symptoms:** No clear trends in time series

**Analysis Tips:**
1. Ensure adequate temporal coverage:
   - Monthly sampling minimum
   - Cover full annual cycle
   - Account for interannual variation

2. Check environmental drivers:
   ```python
   # Correlate with temperature, nutrients
   correlation = pathway_abundance.corr(water_temperature)
   ```

3. Consider lag effects:
   - Microbial response not immediate
   - Try 2-4 week lags

---

## Getting More Help

### Community Resources
- [Ocean Microbiome Forums](https://example.com)
- [HUMANn3 User Group](https://forum.biobakery.org/)
- GitHub Issues for specific bugs

### Debug Mode
Enable verbose output:
```python
config['education']['enable_verbose_output'] = True
config['workflow']['debug_mode'] = True
```

### Logging
Check detailed logs:
```bash
tail -f humann3_output/humann3.log
```

### Contact Experts
- Technical issues: Open GitHub issue
- Marine biology questions: consult literature
- Statistical concerns: consider collaboration

---

## Prevention Tips

1. **Always run controls**
   - Negative controls (blank extractions)
   - Mock communities
   - Technical replicates

2. **Document everything**
   - Sampling conditions
   - Unusual observations
   - Protocol deviations

3. **Start small**
   - Test pipeline on subset
   - Verify each step
   - Scale up gradually

4. **Know your ecosystem**
   - Expected taxa for your region/depth
   - Seasonal patterns
   - Historical data

Remember: Marine systems are complex! Unexpected results might be real biology, not errors.