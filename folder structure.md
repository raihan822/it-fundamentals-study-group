learning_python_journal/
├── 2025_12_11_homework/
│   ├── src/
│   │   └── daily_tasks/
│   │       ├── __init__.py
│   │       ├── q1_sum.py
│   │       ├── q2_temp_converter.py
│   │       ├── q3_age_calc.py
│   │       ├── q4_welcome_message.py
│   │       ├── mini_project_calculator.py
│   │       └── personal_info_card.py
│   └── README.md
├── 2025_12_12_homework/
│   ├── src/
│   │   └── daily_tasks/
│   │       ├── __init__.py
│   │       └── ... (Tomorrow's tasks will go here)
│   └── README.md
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt


# Key Components Explained:
**File/Folder:** learning_python_journal/	
    **Purpose:**	The root of your entire project/Git repository.	
    **Location:** Root

2025_12_11_homework/	
    A self-contained directory for a specific day's work.	
    Root/Date Folder

src/	
    Standard location for all actual Python source code (the src layout).	
    Inside Date Folder

daily_tasks/	
    The actual Python package name (essential for best practices).	
    Inside src/

__init__.py	
    Marks daily_tasks as a Python package. (Can be empty).	
    Inside daily_tasks/

.py files	
    Your individual homework solutions.	
    Inside daily_tasks/

README.md	
    Documentation/instructions for that specific day's tasks.	
    Inside Date Folder

.gitignore	
    Tells Git which files to ignore (e.g., virtual environment folders).	
    Root

pyproject.toml	
    Modern standard for project metadata, dependencies, and configuration.	
    Root

requirements.txt	
    (Optional) Lists required external Python libraries.	
    Root


# How to Run Your Code:
    To run any script (like q1_sum.py) using this structure, open your terminal at the main learning_python_journal/ root level, and use the Python -m flag to treat it as a module:

```bash
```python3 -m 2025_12_11_homework.src.daily_tasks.q1_sum```