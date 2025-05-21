# Welcome to the International Marine AI Consortium (iMAC) Monorepo

This repository serves as the central hub for the International Marine AI Consortium (iMAC). It provides a structured, agent-ready framework designed to foster collaborative development in marine AI research, integrating scientific endeavors, hardware innovations, software solutions, and educational resources.

## Our Mission & Vision

The International Marine AI Consortium (iMAC) aims to **advance ocean science and conservation through collaborative development of open-source AI solutions and widespread knowledge sharing.** We strive to contribute to social welfare by providing new solutions for ocean-related challenges, creating new technological platforms, and fostering new leadership in marine sciences.

(Excerpted from the [iMAC Charter](./Core/charter.md))

## Guiding Principles

Our work and this repository are guided by a commitment to core values and operational principles that ensure our contributions are impactful, ethical, and accessible:

- **Open Collaboration:** We foster an inclusive environment where individuals, research groups, and AI agents can contribute and collaborate openly.
- **Scientific Rigor:** We uphold the highest standards of scientific integrity, ensuring reproducibility, transparency, and peer review.
- **Ethical AI Use:** We are committed to the responsible and ethical development and deployment of AI, prioritizing safety, fairness, and human oversight.
- **Educational Outreach:** We aim to make marine AI knowledge and tools accessible to a broad audience through comprehensive educational programs and resources.
- **Decentralization of Research:** We support decentralized approaches, enabling distributed data collection, analysis, and model training to empower a global community.
- **FAIR Data Practices:** We adhere to FAIR (Findable, Accessible, Interoperable, Reusable) principles for all data and metadata.
- **Sustainability:** We focus on developing AI solutions that contribute to the long-term health and sustainability of marine ecosystems.
- **Modularity & Autonomy:** The repository is organized into clear domains to promote modular components and enable both human and AI agent autonomy in task execution.
- **Accessibility & Clarity:** All documentation, code, and educational materials prioritize clarity and accessibility for a diverse audience, including those new to the field.

These principles are further detailed in the [iMAC Charter](./Core/charter.md) and are embedded within the structure and context files of each module.

## Repository Structure & Usage

### Modular Design

This monorepo is meticulously organized into distinct modules, each representing a core pillar of the iMAC's activities: **Core, Science, Hardware, Software, and Education.** This modular architecture promotes:

- **Clarity:** Easy navigation and understanding of different project areas.
- **Autonomy:** Allows teams and agents to work independently on specific components.
- **Scalability:** Facilitates the growth and addition of new projects or sub-domains.
- **Interdisciplinary Collaboration:** Provides a common ground for experts from various fields to contribute.

Each module contains its own `README.md` detailing its specific purpose, agentic principles for operating within that module, and a guide to its subdirectories and resources.

### How to Use This Repository

Whether you are a researcher, student, developer, or an AI agent, this repository is designed for you:

- **`*_context.md` Files:** Within each primary module directory (e.g., `Science/science_context.md`), you'll find a `*_context.md` file. These files provide essential background, objectives, and operational guidelines specific to that module. They are intended to be the first point of reference for understanding how to effectively work within and contribute to a module.
- **Jupyter Notebook Templates:** Standardized Jupyter notebook stubs (`*.ipynb`) are provided within relevant subdirectories (e.g., `Science/marine-biology/Marine_Biodiversity_Survey_Analysis.ipynb`). These templates include placeholder metadata, mission statements, and sections to guide development and ensure consistency. They are designed to be readily usable by both human researchers and AI agents for specific tasks like data analysis, model training, or hardware calibration.

### Module Quick Links

- **[Core](./Core/README.md):** Contains foundational documents like the iMAC Charter and overarching governance principles.
- **[Science](./Science/README.md):** Focuses on research activities, including marine biology, bioinformatics, and oceanography projects.
- **[Hardware](./Hardware/README.md):** Deals with the integration of physical sensors and edge AI devices, including calibration, testing, and deployment notebooks.
- **[Software](./Software/README.md):** Encompasses computational development, including AI model training pipelines and the MarineAI-Lab simulation environment.
- **[Education](./Education/README.md):** Provides educational materials, tutorials, and workshop resources to foster learning and engagement in marine AI.

## Directory Structure

iMAC-Monorepo/
├── .gitignore
├── build_plan.md
├── README.md (this file)
├── Core/
│   ├── README.md
│   └── charter.md
├── Science/
│   ├── README.md
│   ├── science_context.md
│   ├── marine-biology/
│   │   ├── README.md
│   │   └── Marine_Biodiversity_Survey_Analysis.ipynb
│   └── bioinformatics/
│       ├── README.md
│       └── Marine_eDNA_Analysis.ipynb
├── Hardware/
│   ├── README.md
│   ├── hardware_context.md
│   ├── sensors/
│   │   ├── README.md
│   │   └── Sensor_Calibration_and_Test.ipynb
│   └── EdgeAI/
│       ├── README.md
│       └── EdgeAI_Model_Deployment.ipynb
├── Software/
│   ├── README.md
│   ├── software_context.md
│   ├── MarineAI-Lab/
│   │   ├── README.md
│   │   └── MarineAI_Lab_Experiment_Tracker.ipynb
│   └── AI/
│       ├── README.md
│       └── AI_Model_Training_Pipeline.ipynb
└── Education/
    ├── README.md
    ├── education_context.md
    ├── Tutorials/
    │   ├── README.md
    │   └── Intro_to_Marine_AI.ipynb
    └── Workshops/
        ├── README.md
        └── Data_Analysis_for_Oceanographers_Workshop.ipynb

## Getting Started

1. **Explore the Charter:** Begin by reading the [iMAC Charter](./Core/charter.md) to understand our mission, values, and governance.
2. **Review this README:** Familiarize yourself with the overall structure and guiding principles outlined here.
3. **Dive into a Module:** Use the [Module Quick Links](#module-quick-links) below to navigate to a module that interests you. Read its `README.md` and `*_context.md` file.
4. **Examine Notebook Stubs:** Check out the example notebook stubs in the subdirectories to see how projects are structured.
5. **Consult the `build_plan.md`:** If you're interested in the "why" behind the structure, the [build_plan.md](./build_plan.md) offers insights.

## Contributing

iMAC thrives on community contributions! Whether you're fixing a bug, adding a new dataset, proposing a new research direction, or improving documentation, your input is valuable.

- **Guidelines:** Please refer to the "Governance Notes" section in our [iMAC Charter](./Core/charter.md) for initial contribution ideas and how decisions are made. (A more detailed `CONTRIBUTING.md` will be developed).
- **Agentic Contributions:** The structure is designed to facilitate contributions from AI agents. Ensure agent-driven changes align with the contextual guidance provided in module-specific `README.md` and `*_context.md` files.
- **Proposals:** For significant changes or new modules, please initiate a discussion by raising an issue.

## Community

Join our mission to advance marine AI! We aim to build a vibrant, inclusive, and collaborative community.

- **Discussions:** (Placeholder for links to discussion forums, mailing lists, or chat channels - to be added later).
- **Stay Updated:** (Placeholder for links to a blog, newsletter, or social media - to be added later).

We are excited to build the future of marine AI together!

(Each directory contains a detailed README and stub Jupyter notebooks as templates. The Core directory also includes a charter.md outlining iMAC’s mission and values. A build_plan.md at the root provides a step-by-step assembly guide for the entire repository.)