# Build Plan (build_plan.md)

International Marine AI Consortium (iMAC) Monorepo – Build Plan
This build plan outlines a step-by-step, modular approach to constructing the iMAC mono-repo from scratch. It is designed for use by human collaborators and AI agents alike, with clear checkpoints and instructions that ensure the repository is assembled correctly and efficiently. The plan emphasizes the creation of each component in sequence, verification at each stage (user checkpoints), and guidance for maintaining the principles of decentralization, education, and accessibility throughout the process.

Overview of the Plan

Each directory (core/education/hardware/science/software) has a file called <module_name>_context.md that documents the purpose of the module, agentic principles, and guidelines on how to work within it. This should be used to generate the initial readme for the directory, and the context in that file should be 

We will create the repository structure in logical sections:
	1.	Core setup: Establish the Core directory with foundational documents (README.md and charter.md) that define the consortium’s mission and agentic principles.
	2.	Science module: Create the Science directory, its subdomains (marine-biology, bioinformatics), along with their READMEs and stub notebooks.
	3.	Hardware module: Create the Hardware directory with sensors and EdgeAI subdirectories, plus READMEs and stubs.
	4.	Software module: Create the Software directory with MarineAI-Lab and AI subdirectories, plus READMEs and stubs.
	5.	Education module: Create the Education directory, the eDNA curriculum subfolder, and educational notebook stubs.
	6.	Final integration: Review the interconnections and context references between modules to ensure consistency. Finalize the build with an autonomy check (ensure an agent could navigate the structure).

Each step includes specific files to create and content to include (with links to templates or examples in this document). User checkpoints are provided after major milestones so you (or your agent) can verify the correctness of the setup before moving on.

Step 1: Initialize Repository and Core Directory
	•	Action: Create the root repository folder (e.g., iMAC-Monorepo/) on your system or version control platform. Inside it, create a directory named Core.
	•	Files: Within Core/, create two files: README.md and charter.md.
	•	Core/README.md: Copy or write the contents as outlined in the Core Directory section above (see Core README). This includes the purpose of Core, agentic principles for coordination, guidelines on context and structure, and a list of notebook templates for Core. Ensure the Markdown formatting (headings, lists) is preserved for clarity.
	•	Core/charter.md: Populate this file with the consortium’s charter. At minimum, include:
	•	The Mission Statement of iMAC (e.g., a concise statement of how iMAC will provide AI solutions for ocean challenges, foster collaboration, and disseminate knowledge – you can derive this from the text provided, like the mission described in the Core README or use the lines from our reference: “The Consortium aims to contribute to the social welfare by providing new solutions for ocean-related challenges, creating new technological platforms, and fostering new leadership in marine sciences…” ￼).
	•	A set of Core Values/Principles (bullet points) that guide the consortium (for example: Open Collaboration, Scientific Rigor, Ethical AI Use, Educational Outreach, Decentralization of research, etc., some of which are mentioned in the charter content above).
	•	Any governance notes (optional): e.g., how new contributors (human or AI) should propose changes, an outline of the decision-making process in the consortium, etc. This sets a foundation for autonomous agents to understand the rules of engagement in the project.
	•	Agentic Consideration: The Core charter and README provide the ground truth and context for any agent working in this repo. After creating them, an agent should load this context to internal memory, as it will influence all subsequent actions.
	•	Checkpoint 1: Verify that the Core directory exists with the two files. Open Core/README.md to ensure it is well-formatted (check that headings and lists are rendered correctly) and that it clearly explains the Core module’s purpose and guidelines. Open Core/charter.md and read the mission and values to confirm they align with iMAC’s vision. If using version control, consider committing this initial structure (commit message like “Add Core directory with README and charter”).

Step 2: Build the Science Directory Structure
	•	Action: Create the Science directory at the repository root. Within Science/, create two subdirectories: marine-biology and bioinformatics. These will house domain-specific notebooks.
	•	Files: Create Science/README.md to describe the Science module. Use the content provided in the Science Directory section (see Science README). This README should cover the purpose of the Science module, agentic principles (scientific rigor, etc.), guidelines on data context and notebook format, and list the notebook templates (Marine_Biodiversity_Survey_Analysis, Marine_eDNA_Analysis). Make sure to update any internal references if needed (e.g., if you name the notebooks slightly differently, ensure the README list matches the actual file names).
	•	Notebook Stubs: Inside Science/marine-biology/, create the stub notebook Marine_Biodiversity_Report_Template.ipynb. Similarly, in Science/bioinformatics/, create Marine_eDNA_Analysis.ipynb. For each of these:
	•	Begin the notebook with the metadata block as shown in the stubs above. In practice, if you are creating a real .ipynb file, open Jupyter Notebook or JupyterLab and copy the Markdown content for the first cell (which includes the iMAC logo markdown, mission statement, etc.). Ensure the Markdown cell is at the very top. This metadata cell serves as both human-readable info and machine-readable metadata (the JSON part) that agents can parse.
	•	Optionally, you can add a second cell in each stub with a basic outline (e.g., headers for Introduction, Methods, etc., as reminders). However, since this is a template stub, it can be left mostly blank beyond the initial descriptive cell.
	•	Agentic Consideration: At this point, an AI agent following the plan could read the Science README to understand how it should behave when populating the content of these notebooks (for instance, if later tasked with completing the analysis, it knows to follow the given structure and principles).
	•	Checkpoint 2: Verify the Science directory structure. You should have:
	•	Science/README.md with appropriate content and list of notebooks.
	•	Science/marine-biology/Marine_Biodiversity_Report_Template.ipynb (open it to check that the metadata cell is present with correct info).
	•	Science/bioinformatics/Marine_eDNA_Analysis.ipynb (check similarly).
Also confirm that any internal links or references in the Science README (if any) correspond to actual files (for example, if the README says “Marine_Biodiversity_Report_Template.ipynb”, ensure the file name matches exactly).

Step 3: Build the Hardware Directory Structure
	•	Action: Create the Hardware directory at the root. Within Hardware/, create subdirectories sensors and EdgeAI.
	•	Files: Create Hardware/README.md with content from the Hardware Directory section (see Hardware README). This should explain the purpose of the Hardware module, list the agentic principles (safety, real-time, etc.), give guidance on how notebooks in this domain handle context (sensor data, calibrations) and communicate with others, and list the notebook templates (sensor_template, edgeai_template).
	•	Notebook Stubs:
	•	In Hardware/sensors/, create sensor_template.ipynb and add the metadata block as shown in the stub above (with mission, purpose, metadata JSON indicating it’s a sensor calibration task).
	•	In Hardware/EdgeAI/, create edgeai_template.ipynb with its respective metadata block.
	•	These stubs can also include a basic outline if desired (e.g., sections for Initialization, Execution, etc.), but primarily ensure the descriptive first cell is in place.
	•	Agentic Consideration: When the agent later uses these, it will, for example, ensure that before running real hardware code, possibly a simulation mode is available or the agent confirms conditions (the README’s principles should be encoded into the agent’s decision logic, such as checking “safety first” flags). For now, building the stub means providing the template the agent will fill.
	•	Checkpoint 3: Confirm that the Hardware directory contains:
	•	Hardware/README.md with well-structured content,
	•	Hardware/sensors/sensor_template.ipynb (open and verify the metadata cell is correct),
	•	Hardware/EdgeAI/edgeai_template.ipynb (check its metadata cell).
Ensure the README’s list of notebooks matches these filenames. Commit these changes or note them before proceeding.

Step 4: Build the Software Directory Structure
	•	Action: Create the Software directory. Inside Software/, create subdirectories MarineAI-Lab and AI.
	•	Files: Create Software/README.md using the content from the Software Directory section (see Software README). This README should convey the purpose of the Software module, enumerate its agentic principles (modular code, testing, continuous learning, etc.), provide guidance on how context like models and simulations are handled, and list the notebook templates (MarineAI_Lab_Deployment, Marine_Species_Classifier_Training, Marine_Species_Classifier_Testing, and Marine_Species_Classifier_Validation).
	•	Notebook Stubs:
	•	In Software/MarineAI-Lab/, create MarineAI_Lab_Deployment.ipynb and insert the metadata block from the stub (with mission, purpose, scenario metadata).
	•	In Software/AI/, create Marine_Species_Classifier_Training.ipynb with its metadata block.
	•	In Software/AI/, create Marine_Species_Classifier_Testing.ipynb with its metadata block.
	•	In Software/AI/, create Marine_Species_Classifier_Validation.ipynb with its metadata block.
	•	If desired, add minimal structure in each (like placeholders for sections mentioned in the README such as Setup, Training, Evaluation), or leave them for future fleshing out.
	•	Agentic Consideration: With these templates, an agent developer can later plug in actual code for simulation or model training. The presence of the mission and purpose at top ensures any agent (or student) opening the notebook knows exactly what it’s for. The machine-readable metadata (e.g., indicating “task”: “Model Training”) could be utilized by an orchestrator agent to automatically find all training tasks in the repo.
	•	Checkpoint 4: Verify the Software directory:
	•	Software/README.md exists and correctly lists MarineAI_Lab_Deployment.ipynb, Marine_Species_Classifier_Training.ipynb, Marine_Species_Classifier_Testing.ipynb, and Marine_Species_Classifier_Validation.ipynb (with matching capitalization and underscores, as consistency is key on case-sensitive systems).
	•	Check that Software/MarineAI-Lab/MarineAI_Lab_Deployment.ipynb and Software/AI/Marine_Species_Classifier_Training.ipynb both have the appropriate first cell content.
	•	Ensure the README covers both subdirectories clearly. After verification, these can be saved/committed.

Step 5: Build the Education Directory Structure
	•	Action: Create the Education directory. Inside it, create the subdirectory eDNA curriculum (note: spaces in a directory name are generally avoided; you might use eDNA-curriculum or eDNA_curriculum as the folder name for practicality, but here we follow the description exactly). For NBGrader compatibility in a real scenario, one might use a structure like source/ and release/ within this, but for our scaffold we will keep it simple with just the lesson notebook in a folder.
	•	Files: Create Education/README.md with content from the Education Directory section (see Education README). This README explains the purpose of the Education module, lists the agentic principles for educational content (clarity, interactivity, etc.), outlines how context and progression are handled, and describes NBGrader integration. It should list at least the Lesson1_Intro_to_bio_monitoring notebook, the Lesson2_Categories_of_biomonitoring_data notebook, and the Lesson3_eDNA notebook (and mention that more can be added). If there are any additional supporting files (like nbgrader_config.py or data files for lessons), you might list them or plan for them here as well.
	•	Notebook Stub: In Education/eDNA curriculum/, create Lesson1_Intro_to_bio_monitoring.ipynb, Lesson2_Categories_of_biomonitoring_data.ipynb, and Lesson3_eDNA.ipynb. Add the metadata block as given in the stub (with mission, purpose indicating it’s an interactive lesson, and metadata marking it as lesson 1 of curriculum).
	•	Inside these notebooks, since they are lessons, you might proactively include a few markdown headers for “Objectives”, “Background”, and a template for an exercise. For example, an markdown cell saying “### Exercise 1: [title]” followed by a blank code cell for the student, and a markdown comment for where the test would be (e.g., # NBGRADER TEST - DO NOT MODIFY to signal an autograder cell). These can be left as comments because actual tests might be added later by instructors. The key is that the structure allows such insertion.
	•	NBGrader Setup (optional): If intended to be fully NBGrader-ready, you could also create a Education/eDNA curriculum/nbgrader_config.py with basic config, and ensure the notebook has the proper metadata for NBGrader on each cell (like points, etc.). However, detailing that might be beyond the scope of the scaffold. Mention in the README that the structure is prepared for NBGrader and that instructors can use nbgrader commands to generate student versions of these notebooks.
	•	Agentic Consideration: Agents acting as tutors or content generators will rely on these templates. After building, an agent could use the Education README to identify how to format explanations and problems. Because the notebooks include a mission and purpose, any future AI reading them knows they are educational and will treat them differently (for instance, an autonomous agent wouldn’t treat a lesson notebook as a place to store final analysis results, but rather as a guide for teaching).
	•	Checkpoint 5: Check the Education directory:
	•	Education/README.md should exist and clearly reference the eDNA curriculum.
	•	Education/eDNA curriculum/Lesson1_Intro_to_bio_monitoring.ipynb, Lesson2_Categories_of_biomonitoring_data.ipynb, and Lesson3_eDNA.ipynb should have the correct metadata top cell. Optionally open it in Jupyter to see that it renders the mission statement and such properly.
	•	Confirm that the README discusses NBGrader and the educational philosophy, and that it lists the Lesson1 notebook (and any other planned ones).
	•	Everything in Education should be written with a slightly different tone (more tutorial-like), which you can verify from the content.

Step 6: Final Integration and Review
	•	Action: Now that all directories and files are in place, perform an integration review:
	•	Ensure all internal references are consistent (e.g., the build plan and READMEs refer to files with correct names). The directories and subdirectories names should match between this plan and actual structure.
	•	Check that the mission statement is consistently used across notebooks (the wording of the iMAC mission should be the same everywhere for coherence). If any variation, choose one version and update all stubs to match exactly.
	•	Review the agentic execution principles across modules to ensure they complement each other. For instance, Core emphasizes orchestration and logging, Science emphasizes reproducibility and data integrity, etc. Together they should cover all important aspects of an autonomous research workflow. If something is missing (for example, maybe add an ethical AI principle if not already mentioned, or a note on data privacy if dealing with certain data), this is the time to adjust the READMEs.
	•	Think about extensibility: if a new subdomain or module were to be added by a contributor or agent, does the structure allow it? (The answer should be yes – the monorepo style and modular READMEs are designed to be extended. You might note in the Core README or charter that new modules should follow the same format and get approval via the charter guidelines.)
	•	Files: Create the top-level build_plan.md (if not already editing it) – which is effectively this document section. Ensure it has links to each directory’s README (for example, in the steps above we reference [Core README](Core/README.md), etc., which in a GitHub setting would be clickable to open those files). Also ensure it includes all the points required: sequential steps, user checkpoints, and emphasis on using Jupyter notebooks and design principles (which we have woven into each step).
	•	Agentic Consideration: With the repository scaffolded, an AI agent can be “onboarded” simply by reading the build_plan and the charters/READMEs. The build_plan especially could be used by an agent to verify if all components exist (an agent could parse the plan and then check the file system to ensure everything mentioned is present, thus performing a self-check of the repo’s completeness).
	•	Checkpoint 6 (Final): Do a final run-through:
	•	Open each README and skim for clarity, typos, or broken formatting. They should be concise yet comprehensive, with short paragraphs and lists that are easy to read.
	•	Open each notebook stub in a Jupyter interface (if possible) to see that the metadata cell is rendering correctly (logo image will appear broken unless logo.png is added later, but the alt text should show – that’s fine for now). The bold text for mission and purpose should be easily readable. The JSON metadata should be properly formatted (well-formed JSON in one line or a few lines). This check ensures that if an agent tries to parse that JSON, it will succeed.
	•	Read the build_plan.md itself (this document) from top to bottom to confirm it flows logically, covers everything, and that the sequence of steps would make sense to someone new coming in. It should effectively allow a person or AI to recreate the repository from nothing.
	•	Finally, consider accessibility: Do all images have alt text? (Yes, the logo is referenced with alt text “iMAC Logo” implicitly by the syntax.) Are acronyms explained? (We introduced iMAC at first use as International Marine AI Consortium.) Is the language clear for non-experts? (We included definitions and context where appropriate, e.g., what eDNA is in context, what EdgeAI means, etc.) If anything seems too jargon-heavy, add a short explanation in the relevant README.
	•	Completion: Once satisfied, finalize the build by committing all files to the repository. The repository is now fully scaffolded. It provides a launchpad for agentic execution, meaning future AI agents can navigate this structure, create new content in the templates provided, or execute workflows by following the context references. The project is also ready for human contributors – researchers can fill in the notebooks with actual content, and educators can expand the curriculum, all within the organized framework established.

Checkpoint 7 (Post-build Review): Celebrate this structured foundation! At this point, a user or an agent should be able to:
	•	Read the Core/charter.md to understand why the project exists and what values guide it.
	•	Navigate to any directory’s README to understand what that part of the project does and how to work within it.
	•	Open a stub notebook and see where to begin coding or writing, with a clear idea of the notebook’s intended function and required context.
	•	Use build_plan.md (this plan) as a living document to onboard new contributors or even to plan enhancements (e.g., adding a new subdirectory would be a new step here).

By adhering to this build plan and scaffold, iMAC ensures clarity, extensibility, and autonomy for all future collaborators and intelligent agents working to advance marine AI. The design is modular and decentralized (each domain can progress in parallel), strongly educational (through the Education module and thorough documentation), and accessible (open-source with well-documented, easy-to-follow guides). Together, these elements position the iMAC monorepo as a robust platform for innovation in marine artificial intelligence.