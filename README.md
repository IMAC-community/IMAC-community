International Marine AI Consortium (iMAC) Monorepo

Repository Overview

This repository is a mono-repo for the International Marine AI Consortium (iMAC). It provides a structured, agent-ready framework for collaborative development in marine AI research, integrating science, hardware, software, and education resources. 

The repository is organized into clear domains to promote modularity, autonomy, and interdisciplinary teamwork. Each top-level directory focuses on a specific domain (Core, Science, Hardware, Software, Education) and contains guidelines, templates, and notebook stubs to assist AI agents and human collaborators in executing tasks within that domain. 

The design emphasizes decentralization, open collaboration, educational outreach, and accessible design so that researchers, students, and automated agents can all contribute effectively.

## Module Overview & Navigation

This repository is organized into the following primary modules. For detailed information on each module's purpose, structure, and agentic principles, please refer to their respective README files:

- **[Core](./Core/README.md):** Contains foundational documents, including the [iMAC Charter](./Core/charter.md), defining the consortium's mission, values, and operational guidelines.
- **[Science](./Science/README.md):** Focuses on marine science research, with subdomains for marine biology and bioinformatics, providing tools and templates for scientific analysis.
- **[Hardware](./Hardware/README.md):** Deals with the integration of physical sensors and edge AI devices, including calibration, testing, and deployment notebooks.
- **[Software](./Software/README.md):** Encompasses computational development, including AI model training pipelines and the MarineAI-Lab simulation environment.
- **[Education](./Education/README.md):** Provides educational materials, tutorials, and workshop resources to foster learning and engagement in marine AI.

You can explore the detailed directory structure below:

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

(Each directory contains a detailed README and stub Jupyter notebooks as templates. The Core directory also includes a charter.md outlining iMAC’s mission and values. A build_plan.md at the root provides a step-by-step assembly guide for the entire repository.)