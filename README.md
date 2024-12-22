# Pylint of Kahooa Board Game

## Objective
For this project, I have used the **Pylint** module to conduct static code analysis (linting) on a Python program, specifically the code for the **Kahooa Board Game** (from Assignment 1). The purpose was to identify issues in the code and address them based on the recommendations provided by Pylint.
The source code for the Kahooa Board Game can be found in my [GitHub repository](https://github.com/ShivamS-9/vulture-vs-crows-game-kaooa-).

## Linting Process
### 1. Initial Linting
The Python program is first linted using Pylint to generate the **initial lint results**. These results include a Pylint score and a list of recommendations for improving the code, such as fixing style violations, improving variable naming, and resolving any errors or warnings.

### 2. Reviewing and Addressing Recommendations
The lint results are thoroughly reviewed to identify the key areas that need improvement. Based on the recommendations:
  - Code style issues such as indentation and line length are corrected.
  - Unused imports, undefined variables, and redundant code are removed.
  - Missing docstrings, comments, and documentation are added to enhance code readability and maintainability.

### 3. Repeating Linting After Fixes
Once the recommendations are addressed, the program is linted again to verify the changes. The **updated lint results** and **new Pylint score** are captured after each iteration of improvements.

## Pylint Installation

To install Pylint, use the following command:

```bash
pip install pylint
