# Science Directory README

## Purpose

The Science directory contains notebooks and resources for marine science research, such as marine biology and bioinformatics. Its goal is to enable autonomous agents and researchers to carry out scientific analyses on marine data (e.g., species observations, environmental DNA sequences) in a rigorous, reproducible manner. This domain focuses on hypothesis-driven exploration, data analysis, and knowledge discovery about ocean life and ecosystems. Science notebooks serve as digital lab notebooks where experiments are conducted, results are documented, and insights are derived.

## Key Agentic Execution Principles (Science)

-   **Reproducibility & Validation:** Agents conducting scientific analyses must follow the scientific method. Each experiment or analysis should be scripted so that results can be reproduced and verified by others. Notebooks include clear methodology and validation steps.
-   **Data Integrity & Provenance:** Data used in analyses should be tracked with metadata (source, time, conditions). Agents should automatically record data origins and any preprocessing applied.
-   **Continuous Learning:** The Science module allows for iterative refinement. An agent might start with a simple model or analysis, observe results, then refine the approach. Notebooks can be re-run with updated data or parameters.
-   **Collaboration & Documentation:** Notebooks are written to be easily understood by human scientists, with clear documentation, visualizations, and narrative text to follow an agent’s reasoning, aligning with iMAC’s educational mission.

## Guidance on Context & Structure (Science)

-   **Context Storage & Retrieval:** Scientific notebooks consume raw data and produce analyzed datasets or reports. Context from other modules (e.g., Hardware) is ingested, and context for other modules (e.g., Software) may be generated. Outputs are saved in standardized locations/formats, referenced by the Core context index.
-   **Notebook Structure:** Science templates follow a clear structure:
    1.  **Introduction:** The research question or problem.
    2.  **Methods:** Data loading, cleaning, analysis techniques.
    3.  **Results:** Outputs, graphs, metrics, and agent commentary.
    4.  **Conclusion & Next Steps:** Summary of findings and suggestions for further work.
-   **Inter-Module Communication:** Science notebooks may interact with other modules (e.g., Software for computations, Hardware for data requests) using clearly defined data exchange formats (e.g., CSV, JSON) and asynchronous communication where feasible.

## Subdirectories

This directory is organized into the following subdirectories, each focusing on a specific area of marine science:

-   `marine-biology/`: Focuses on the study of marine organisms, their behaviors, and their interactions with the environment.
-   `bioinformatics/`: Deals with the application of computational tools to analyze biological data, particularly molecular data like eDNA.

Each subdirectory contains its own `README.md` with more specific details and relevant Jupyter notebook templates.
