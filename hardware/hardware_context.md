
Hardware Directory

Purpose: The Hardware directory focuses on physical devices and edge computing components of marine AI projects. It includes resources for sensors (e.g. water quality sensors, underwater cameras, AUVs – Autonomous Underwater Vehicles) and Edge AI platforms (running AI models on devices deployed in the field). The goal is to guide agents in interacting with hardware safely and effectively: for instance, calibrating sensors, collecting data from the environment, and deploying AI models onto embedded systems that operate in marine conditions (like on a buoy or a drone). This domain bridges the gap between the digital and physical world in the iMAC framework.

Key Agentic Execution Principles (Hardware):
    •	Safety & Robustness: Agents must prioritize safety when operating hardware. This includes checking conditions (battery levels, sensor status, environmental safety) before executing actions, and having fail-safes (e.g. if a sensor feed is inconsistent, an agent should halt data collection and alert for human review). Hardware operations are often irreversible or high-stakes, so agent scripts should simulate or dry-run actions when possible before actual execution.
    •	Real-Time Responsiveness: In the field, conditions change rapidly. Hardware agents need real-time decision-making capability, reacting to sensor inputs immediately. For example, if an underwater drone’s depth sensor indicates a rapid descent, the agent should autonomously take corrective action. The notebooks in this directory might use event loops or trigger-based cells (e.g. continuously monitoring sensor values) to illustrate how an agent can maintain reactivity.
    •	Edge Autonomy: Emphasize running AI at the edge (on the device) to reduce latency and dependence on cloud connectivity. By deploying cognitive AI models directly on sensors or vehicles, the system can achieve safety-critical autonomy in marine operations ￼. The agentic principle here is to treat each device as a semi-autonomous agent that can perform essential tasks (like hazard detection or data filtering) even when offline.
    •	Calibration & Validation: Before trusting data or deploying a model, agents should calibrate and test hardware components. This means performing self-checks (e.g. verifying a sensor’s readings against a known reference) and validating model performance on the edge device (ensuring, for example, that an object detection model running on a camera accurately identifies marine animals in real conditions). Re-calibration routines and periodic tests are included as part of agent tasks.

Guidance on Context & Structure (Hardware):
    •	Context Storage & Retrieval: Hardware notebooks often produce raw data (sensor logs, images, etc.) that will be used by Science or stored for long-term analysis. Agents in this module should timestamp and label all data collected, saving them in organized directories (for instance, Hardware/sensors/data/<sensor_name>/<date>_<time>.csv). Context retrieval in this domain means being able to fetch the latest or historical sensor data when needed. The Core context index might maintain pointers to the most recent dataset from each sensor. Additionally, if a sensor or device has a configuration (like calibration parameters), those should be stored (perhaps in a config.json in the sensors subfolder) so that any agent can load the current calibration values before using the sensor.
    •	Notebook Structure: Hardware templates are a bit different from pure analysis notebooks. They may include setup and teardown steps for devices:
    •	Initialization: Connect to hardware or simulator, load calibration constants, perform any pre-checks.
    •	Execution Loop or Procedure: The main sequence of operations (e.g. a loop reading sensor values for a duration, or a step-by-step procedure to deploy a model and then test it). Use clear markers in the notebook for each stage (like “Step 1: Calibrate sensor”, “Step 2: Start data logging”, etc.) so an agent can navigate or retry specific steps if something fails.
    •	Data Storage: After execution, ensure the data or model is saved appropriately (and possibly notify the Science module that new data is ready).
    •	Shutdown: Safely disconnect or power down hardware as needed.
Comments in the notebooks should remind the agent (or user) about physical-world assumptions (e.g. “Ensure the sensor is submerged in water before starting calibration routine”).
    •	Inter-Module Communication: The Hardware module supplies data to Science and sometimes models to Software. For example, after a Sensor_Calibration notebook runs, it might output a calibration report that the Science module can use to correct raw data. Conversely, the Software module may provide an edge-optimized model file to the EdgeAI subfolder, which an Edge device deployment notebook then loads and runs. Agents should use file-based handoff in many cases: e.g. the Software module exports a model to Hardware/EdgeAI/models/, and the EdgeAI notebook knows to look there. Communication can also involve sending status back to Core – for instance, an Edge device might periodically update a Core log with its uptime or any anomalies detected. This fosters a decentralized yet coordinated ecosystem: each hardware agent operates largely on its own (decentralized), but shares essential information with the rest of the system via common file formats or messages.

Stubbed Jupyter Notebook Templates (Hardware):

• **Sensors:** **sensor\_template.ipynb** – Template notebook structured to capture requirements and specifications of marine sensors clearly. It provides sections for sensor description, operational environment details, calibration procedures, data acquisition methods, and validation protocols. Designed to guide agents or contributors in systematically documenting sensor capabilities and deployment guidelines.

• **EdgeAI:** **edgeai\_template.ipynb** – Template notebook for specifying Edge AI device requirements, setup instructions, and performance expectations. Includes structured segments for detailing hardware configurations, software stack, AI model deployment strategies, operational checks, and benchmarks. Supports comprehensive documentation of device readiness and operational parameters.

Below is the stub for **sensor\_template.ipynb** (Sensors subdirectory):

![iMAC Logo](../../Core/logo.png)
**iMAC Mission:** The International Marine AI Consortium aims to advance ocean science and conservation through collaborative development of open-source AI solutions and widespread knowledge sharing.
**Notebook Purpose:** Capture detailed specifications and operational guidelines for marine sensor deployments, including calibration and validation procedures.
**Metadata:** {"module": "Hardware", "subdomain": "Sensors", "task": "Documentation", "input\_context": \[], "output\_context": \["specs\:sensor\_specs.md", "guidelines\:deployment\_guidelines.md"]}

Below is the stub for **edgeai\_template.ipynb** (EdgeAI subdirectory):

![iMAC Logo](../../Core/logo.png)
**iMAC Mission:** The International Marine AI Consortium aims to advance ocean science and conservation through collaborative development of open-source AI solutions and widespread knowledge sharing.
**Notebook Purpose:** Document Edge AI device specifications, deployment instructions, and performance benchmarks, enabling structured and systematic deployment of AI models on edge devices.
**Metadata:** {"module": "Hardware", "subdomain": "EdgeAI", "task": "Documentation", "input\_context": \[], "output\_context": \["specs\:edgeai\_device\_specs.md", "benchmarks\:device\_performance\_metrics.md"]}

