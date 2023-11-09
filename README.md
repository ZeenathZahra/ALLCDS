
<!-- markdownlint-configure-file {
  "MD013": {
    "code_blocks": false,
    "tables": false
  },
  "MD033": false,
  "MD041": false
} -->

<div align="center">

# Acute lymphoblastic leukemia Diagnosis System

 <a href="https://github.com/thlurte/dots/stargazers">
        <img src="https://img.shields.io/github/stars/thlurte/dots?color=%23BB9AF7&labelColor=%231A1B26&style=for-the-badge">
    </a>
        <img src="https://img.shields.io/github/forks/thlurte/dots?color=%237AA2F7&labelColor=%231A1B26&style=for-the-badge">
    </a>

<p>
ALLCDS is a simple web application, built to identify leukaemia cells.

This application utilizes pretrained CNN architectures in TensorFlow and uses APIs from Django to seamlessly integrate its core logic, interact with the database, manage models, and represent visual components for an enhanced user experience.<br /><br />

</p>

[Getting started](#getting-started) 
[Installation](#installation) 
[Configuration](#configuration) 
[Integrations](#contributors)

</div>

## Getting started
Follow these steps to get started with ALLCDS.

### Prerequisites
- Python: 3.8 or 3.9
- TensorFlow: 2.14.0
- Django: 4.2.5

## Installation
1. Clone the ALLCDS repository:
```bash
git clone https://github.com/thlurte/ALLCDS.git
```
2. Navigate to the project directory:
```bash
cd ALLCDS
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Run the application
```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) in your browser to access ALLCDS.

## Configuration
Configure ALLCDS by updating the settings in the `settings.py` file. Ensure that you set up the database connection and any other necessary parameters according to your environment.

## Contribution

We appreciate contributions! If you'd like to contribute to ALLCDS, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and submit a pull request.
