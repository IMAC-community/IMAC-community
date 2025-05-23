# Core Directory README

## Purpose

The Core directory contains the high-level governance and coordination resources for the iMAC project. It defines the consortium’s mission, values, and overall guidelines. Core acts as the central brain for agentic orchestration, providing configuration and context that tie together the Science, Hardware, Software, and Education modules. This is where cross-module communication protocols and project-wide context logs reside, ensuring all parts of the system remain aligned with iMAC’s mission.

## Key Agentic Execution Principles

-   **Modularity & Orchestration:** Design the system so autonomous agents can activate or coordinate different domain modules as needed, without hard-coded interdependencies. The Core provides an orchestration layer where an AI “agent coordinator” plans complex tasks into modular subtasks (Science analysis, Hardware control, etc.) and delegates them accordingly.
-   **Transparency & Logging:** All agent actions and decisions should be logged in a central, human-readable format. Core notebooks capture the chain-of-thought and decisions of AI agents to ensure transparency and allow human oversight.
-   **Iterative Planning & Safety:** Use iterative planning (e.g. Chain-of-Thought and ReAct frameworks) to let agents refine their plans with feedback. Core routines implement guardrails (like simulation checks or requiring confirmation for high-risk actions) so that agentic execution remains safe and aligned with ethical guidelines.
-   **Global Context Awareness:** The Core manages a shared context memory that agents can query for relevant information (past results, environment data, user preferences). This ensures continuity across long-running tasks and between different modules. The context store might use simple files or databases to accumulate knowledge that any module can retrieve.

## Guidance on Context & Structure

-   **Context Storage & Retrieval:** Core components maintain a knowledge base (e.g. a JSON or database of key results, configurations, and environmental context). Agents use this to store outcomes (like Science analysis summaries or latest sensor readings) and retrieve them when forming new plans. For example, a Core context index notebook might collect pointers to data files or summary reports from each module, enabling Retrieval-Augmented Generation for agent queries.
-   **Notebook/Script Structure:** Core notebooks (e.g. an Agent Orchestration notebook) should follow a structured format: Introduction (objective and plan), Planning (decompose tasks, perhaps via pseudocode or natural language steps), Execution (invoke or simulate calls to other modules), and Synthesis (compile results and next steps). This consistent structure helps both humans and AI agents understand and modify the workflow. Inline documentation and Markdown descriptions are used extensively to clarify each step of the agent’s reasoning and actions.
-   **Inter-Module Communication:** The Core defines how modules interact. This could be through shared files (e.g. Science module outputs a CSV that Hardware module reads), through function calls or APIs (if code is packaged as services), or via the agent itself routing information. The Core README and charter specify communication protocols – for instance, a standard format for data exchange (CSV, JSON) and a scheduling pattern (the agent might run Science analyses after new sensor data arrives from Hardware). Keeping communication decentralized but standardized ensures each module can operate independently yet integrate smoothly. For example, the Core might include a task scheduler that triggers the EdgeAI Model Deployment notebook when a new model is trained in the Software module.

## Stubbed Jupyter Notebook Templates

The Core directory will house templates for key agentic functions:

-   **`Agent_Orchestration_Template.ipynb`**: A notebook template for orchestrating complex tasks across modules (e.g. automatically collecting data via Hardware, analyzing it in Science, then retraining a model in Software). It demonstrates how an agent can plan and call sub-tasks, and how to log outcomes to the Core context.
-   **`Context_Index_Template.ipynb`**: A template for maintaining an index of context files and summaries. It can scan subdirectories for outputs (data files, reports) and update a central reference (this helps the agent quickly find relevant information).

These templates will include metadata cells to inform agents about their roles, inputs, and outputs, as exemplified in `core_context.md`.
