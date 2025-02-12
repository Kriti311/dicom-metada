# DICOM Metadata Extractor

## Overview
This is a Django web application that enables users to upload DICOM files and extract relevant metadata, including patient information, study details, and image attributes. The extracted metadata is stored in a database, displayed to the user, and can be searched within the application.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Kriti311/dicom-metada.git
cd dicom-metada
```

### 2. Create and Activate a Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
```


### 3. Install Dependencies
Ensure you have Python installed, then install the required dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
Apply migrations to set up the database schema:
```bash
python manage.py makemigrations
python manage.py 
```
### 5. Start the Development Server
Start the Django development server to run the application locally:
```bash
python manage.py runserver
```

### 6. Access the Application
Open your web browser and go to: http://127.0.0.1:8000

