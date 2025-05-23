# Hardware Directory README

## Purpose

The Hardware directory focuses on physical devices and edge computing components of marine AI projects. It includes resources for sensors (e.g., water quality sensors, underwater cameras, AUVs – Autonomous Underwater Vehicles) and Edge AI platforms (running AI models on devices deployed in the field). The goal is to guide agents in interacting with hardware safely and effectively: for instance, calibrating sensors, collecting data from the environment, and deploying AI models onto embedded systems that operate in marine conditions.

## Key Agentic Execution Principles (Hardware)

-   **Safety & Robustness:** Agents must prioritize safety when operating hardware, including pre-checks and fail-safes. Simulations or dry-runs should be used where possible.
-   **Real-Time Responsiveness:** Hardware agents need real-time decision-making capabilities to react to changing environmental conditions.
-   **Edge Autonomy:** Emphasize running AI at the edge to reduce latency and dependency on cloud connectivity, enabling devices to perform essential tasks autonomously.
-   **Calibration & Validation:** Agents should calibrate and test hardware components and validate model performance on edge devices to ensure data trustworthiness and operational reliability.

## Guidance on Context & Structure (Hardware)

-   **Context Storage & Retrieval:** Hardware notebooks produce raw data (sensor logs, images) that are timestamped, labeled, and saved in organized directories. Configuration files (e.g., calibration parameters) are also stored for agent access. The Core context index may point to the latest datasets.
-   **Notebook Structure:** Hardware templates often include:
    1.  **Initialization:** Connect to hardware/simulator, load calibrations, perform pre-checks.
    2.  **Execution Loop/Procedure:** Main operational sequence (e.g., data logging, model deployment, testing).
    3.  **Data Storage:** Save data/model outputs and notify relevant modules (e.g., Science).
    4.  **Shutdown:** Safely disconnect or power down hardware.
    Notebooks should include comments on physical-world assumptions.
-   **Inter-Module Communication:** The Hardware module supplies data to Science and may receive models from Software. File-based handoffs are common (e.g., Software exports a model to `Hardware/EdgeAI/models/`). Status updates may be sent to Core.

## Subdirectories

This directory is organized into the following subdirectories:

-   `sensors/`: Contains resources related to marine sensor deployment, calibration, data acquisition, and testing.
-   `EdgeAI/`: Focuses on deploying and managing AI models on edge computing devices used in marine environments.

Each subdirectory has its own `README.md` with further details and notebook templates.
