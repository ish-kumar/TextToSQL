# TextToSQL

TextToSQL is a Streamlit-based application that allows users to query a realistic employee database using natural language. The app leverages Google Gemini (Generative AI) to convert user questions into SQL queries, executes them on a local SQLite database, and displays the results in a user-friendly interface.

## Features
- **Natural Language to SQL**: Ask questions about employee data in plain English.
- **Realistic Employee Database**: Includes 80+ diverse employee records with fields like name, department, role, salary, and more.
- **Google Gemini Integration**: Uses Gemini's latest models for accurate SQL generation.
- **Streamlit UI**: Simple, interactive web interface for querying and viewing results.

## Database Schema
The database (`employee.db`) contains a single table `EMPLOYEE` with the following columns:
- `ID` (integer, primary key)
- `NAME` (string)
- `DEPARTMENT` (string)
- `ROLE` (string)
- `EMAIL` (string)
- `SALARY` (integer)
- `DATE_JOINED` (date)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repo-url>
cd TextToSQL
```

### 2. Create and Activate a Virtual Environment (Recommended)
```bash
python3 -m venv texttosql
source texttosql/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root and add your Google Gemini API key:
```
GENAI_API_KEY=your_google_gemini_api_key_here
```

### 5. Initialize the Database
Run the following script to create and populate the database:
```bash
python sql.py
```

### 6. Run the Streamlit App
```bash
streamlit run app.py
```

The app will be available at [http://localhost:8501](http://localhost:8501).

## Usage
- Enter a natural language question about the employee database (e.g., "List all employees in the Engineering department who joined after 2020.").
- The app will display the generated SQL query and the results.

## Model Configuration
- The app uses the latest supported Gemini model (e.g., `models/gemini-2.5-pro`).
- You can change the model in `app.py` if needed.

## Notes
- Ensure your Google Gemini API key has access to the required models.
- The database is reset and repopulated each time you run `sql.py`.

## License
MIT License 