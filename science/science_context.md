Science Directory

Purpose: The Science directory contains notebooks and resources for marine science research, such as marine biology and bioinformatics. Its goal is to enable autonomous agents and researchers to carry out scientific analyses on marine data (e.g. species observations, environmental DNA sequences) in a rigorous, reproducible manner. This domain focuses on hypothesis-driven exploration, data analysis, and knowledge discovery about ocean life and ecosystems. Science notebooks serve as digital lab notebooks where experiments are conducted, results are documented, and insights are derived.

Key Agentic Execution Principles (Science):
    •	Reproducibility & Validation: Agents conducting scientific analyses must follow the scientific method. Each experiment or analysis should be scripted so that results can be reproduced and verified by others. Notebooks include clear methodology and validation steps (e.g. statistical tests or cross-checks). Agents are encouraged to self-verify their findings by, for example, comparing multiple data sources or running simulations for confirmation.
    •	Data Integrity & Provenance: Data used in analyses should be tracked with metadata (source, time, conditions). Agents should automatically record where data came from (sensor logs, public datasets, etc.) and any preprocessing applied. This ensures trust in the results and makes audits possible if an agent’s conclusion needs review.
    •	Continuous Learning: The Science module allows for iterative refinement. An agent might start with a simple model or analysis, observe results, then refine the approach (much like a human researcher). Notebooks can be re-run with updated data or parameters, enabling an autonomous research cycle.
    •	Collaboration & Documentation: Even though agents operate with autonomy, the notebooks are written to be easily understood by human scientists. Clear documentation, visualizations, and narrative text are included so that humans can follow the agent’s reasoning. This principle ensures that the AI’s discoveries in marine science can be communicated and taught to others, aligning with iMAC’s educational mission.

Guidance on Context & Structure (Science):
    •	Context Storage & Retrieval: Scientific notebooks often consume raw data and produce analyzed datasets or reports. Context from Hardware (e.g. sensor readings) is ingested here, and context for Software (e.g. features for model training) may be generated. Each Science notebook should load context explicitly (for example, reading a cached sensor dataset file provided by Hardware/sensors module) and after analysis, save key outputs in a standardized location or format. The Core context index will reference these outputs for future agent queries. Additionally, consider using a lightweight database or CSV files to store intermediate results with timestamps, so agents can retrieve historical data for time-series analysis or trend detection.
    •	Notebook Structure: Science templates should follow a clear structure:
    •	Introduction: What question or problem is the notebook addressing? (e.g. “Analyze coral reef biodiversity from survey images.”)
    •	Methods: Steps the agent will take – data loading, cleaning, analysis methods (statistical tests, machine learning models, etc.).
    •	Results: The outputs such as graphs, metrics, or discoveries, with the agent’s commentary on significance.
    •	Conclusion & Next Steps: Summary of findings and suggestions for further investigation or action (which an agent or human could follow up on, possibly triggering tasks in other modules like Hardware for more data or Software to update a model).
This standardized flow helps both agents and humans ensure no part of the scientific process is skipped.
    •	Inter-Module Communication: Science notebooks might call out to Software for advanced computations (for example, using a pre-trained AI model to classify species in images) or request data from Hardware (like querying a sensor log for a specific time range). Wherever possible, use clearly defined data exchange formats. For instance, a Marine Biology notebook could output a CSV of species counts, which the Education module might use in a student assignment, or the Software AI module might use to retrain a model on updated labels. Communication should be asynchronous where feasible (the agent can continue with other tasks while waiting for data processing in another module), using file existence or status flags for synchronization. Each Science subdirectory (like marine-biology, bioinformatics) can also have its own mini-context – e.g. a marine-biology/context.json file summarizing latest findings – that can be picked up by the Core or other modules.

Stubbed Jupyter Notebook Templates (Science):

• **Marine Biology:** **Marine_Biodiversity_Report_Template.ipynb** – A structured template for creating detailed biodiversity reports from marine survey data. It includes predefined sections for data acquisition, analysis methodologies, result interpretation, visualizations, and concluding remarks. Designed to facilitate systematic reporting by both agents and researchers.

• **Bioinformatics:** **Marine_eDNA_Analysis.ipynb** – An analytical pipeline template notebook for processing environmental DNA (eDNA) sequences. It systematically guides the loading and quality filtering of sequencing data, taxonomic classification, and ecological data interpretation. The notebook is structured for reproducibility and clear documentation of each analysis step.

Below is the stub for **Marine_Biodiversity_Report_Template.ipynb** (Marine Biology subdirectory):

![iMAC Logo](../../Core/logo.png)
**iMAC Mission:** The International Marine AI Consortium aims to advance ocean science and conservation through collaborative development of open-source AI solutions and widespread knowledge sharing.
**Notebook Purpose:** Structured template for generating comprehensive biodiversity reports using marine survey data, supporting systematic analysis and clear documentation of biodiversity metrics.
**Metadata:** {"module": "Science", "subdomain": "Marine Biology", "analysis_type": "Biodiversity Reporting", "input_context": ["data: survey_data.csv"], "output_context": ["report:biodiversity_report.md", "visualizations:biodiversity_figures.png"]}

Below is the stub for **Marine_eDNA_Analysis.ipynb** (Bioinformatics subdirectory):

![iMAC Logo](../../Core/logo.png)
**iMAC Mission:** The International Marine AI Consortium aims to advance ocean science and conservation through collaborative development of open-source AI solutions and widespread knowledge sharing.
**Notebook Purpose:** Template notebook for executing eDNA analysis pipelines, including data preprocessing, taxonomic identification, and biodiversity assessment from marine eDNA samples.
**Metadata:** {"module": "Science", "subdomain": "Bioinformatics", "analysis_type": "eDNA Pipeline", "input_context": ["data:raw_reads.fastq"], "output_context": ["data:species_counts.csv", "report:edna_analysis_summary.md"]}


(These metadata entries help an agent identify what each notebook does. For example, an agent looking to analyze biodiversity can search for notebooks with "analysis_type": "Biodiversity Survey". The context fields indicate what inputs are needed (like a reef survey CSV or raw reads file) and what outputs will be produced.)
