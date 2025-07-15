# health-informatics-emr-analysis
# EMR Optimization Dashboard: Workflow & User Experience Simulation

This project simulates real-world EMR workflow analysis using synthetic data, designed to align with responsibilities of a Health Informatics Analyst working with platforms like eClinicalWorks (eCW).

## 📌 Project Overview

Using Python and Power BI, the project generates and visualizes patient visit data, workflow inefficiencies, and clinical user feedback to highlight EMR bottlenecks and suggest improvement areas.

---

## 📂 Key Components

### 🔧 `generate_emr_data.py`
Python script using `Faker` and `Pandas` to create:
- **Patient records**
- **Appointment workflows**
- **User feedback and satisfaction ratings**

### 📊 Visualizations (Power BI)
- **Appointment Type Distribution**
- **Vitals Entry Compliance**
- **Workflow Errors Encountered**
- **Satisfaction Rating by Department**

### 📁 Folders
- `data/` – Contains generated CSVs
- `visuals/` – Screenshots of Power BI charts

---

## 🚀 How to Reproduce

### Set up the environment:
```bash
python -m venv venv
venv\Scripts\activate
pip install faker pandas
