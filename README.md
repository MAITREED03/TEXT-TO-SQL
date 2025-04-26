# Text to SQL Query Generator

A Streamlit web application that converts natural language questions to SQL queries using the LaMini-Flan-T5 model from Hugging Face.

## Features

- Convert English questions to SQL queries
- Execute queries against a SQLite database
- Real-time query results display
- User-friendly web interface
- Free and open-source model integration

## Prerequisites

- Python 3.8+
- Hugging Face API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd TEXTTOSQL
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Hugging Face API key:
```
HF_API_KEY=your_hugging_face_api_key_here
```

## Database Setup

The application uses a SQLite database named `student.db` with the following schema:

```sql
CREATE TABLE STUDENT (
    NAME TEXT,
    CLASS TEXT,
    SECTION TEXT
);
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501`

3. Enter your question in natural language, for example:
   - "Show all students in Science class"
   - "List students in section A"
   - "Count total number of students"

4. Click "Generate SQL & Run" to see the SQL query and results

## Example Questions

- "List all students in Data Science class?"
- "How many students are there in total?"
- "Show me students from section A"

## Project Structure

```
TEXTTOSQL/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
├── student.db         # SQLite database
└── README.md          # Project documentation
```

## Technologies Used

- Streamlit: Web interface
- Hugging Face: LaMini-Flan-T5 model
- SQLite: Database
- Python: Programming language

## Limitations

- The model works best with simple queries
- Complex joins and nested queries may not be accurately generated
- First query may take longer due to model loading

## Contributing

Feel free to open issues and pull requests for any improvements.

## License

This project is open source and available under the MIT License.