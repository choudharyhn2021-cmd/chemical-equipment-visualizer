# Chemical Equipment Visualizer

A simple web application that analyzes chemical equipment data from CSV files and generates useful insights in just a few seconds.

This project was developed as a mini-project to demonstrate how industrial equipment data can be processed, analyzed, and presented through a clean web interface. Users can upload a CSV dataset containing equipment information, and the application automatically calculates important statistics such as average flowrate, average pressure, maximum temperature, and equipment distribution.

---

## Why This Project?

In chemical and process industries, engineers often work with large datasets containing information about pumps, compressors, valves, reactors, and other equipment. Manually analyzing this data can be time-consuming.

This application simplifies that process by allowing users to upload a dataset and instantly receive a summarized analysis.

---

## Features

* Upload equipment datasets in CSV format
* Automatic validation of required columns
* Calculation of key statistics:

  * Total Equipment Count
  * Average Flowrate
  * Average Pressure
  * Maximum Temperature
* Equipment Type Distribution Analysis
* Clean and responsive web interface
* Fast processing using Pandas
* Simple architecture suitable for learning and academic projects

---

## Technologies Used

### Backend

* Python
* Flask
* Pandas

### Frontend

* HTML5
* CSS3

### Data Handling

* CSV Files

---

## Project Structure

```text
chemical-equipment-visualizer/

├── app.py
├── requirements.txt

├── templates/
│   ├── index.html
│   └── result.html

├── static/
│   └── css/
│       └── style.css

└── data/
    └── sample_equipment_data.csv
```

---

## Input Dataset Format

The uploaded CSV file should contain the following columns:

| Equipment Name | Type | Flowrate | Pressure | Temperature |
| -------------- | ---- | -------- | -------- | ----------- |

Example:

```csv
Equipment Name,Type,Flowrate,Pressure,Temperature
Pump-1,Pump,120,5.2,110
Compressor-1,Compressor,95,8.4,95
Valve-1,Valve,60,4.1,105
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd chemical-equipment-visualizer
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## How It Works

1. User uploads a CSV dataset.
2. The application validates the dataset structure.
3. Numerical parameters are processed using Pandas.
4. Statistical summaries are generated automatically.
5. Results are displayed on a dedicated report page.

---

## Future Improvements

Some features that can be added in future versions:

* Interactive charts and graphs
* PDF report generation
* Historical upload tracking
* User authentication
* Equipment performance comparison
* Database integration
* Export reports to Excel

---

## Learning Outcomes

This project helped in understanding:

* File handling in Python
* Data analysis using Pandas
* Web development using Flask
* Frontend and backend integration
* Data validation and processing
* Building complete end-to-end applications

---

## Author

Developed as an FOSSEE Internship project for learning web development and data analysis concepts.
