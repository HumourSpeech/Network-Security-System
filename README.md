# 🛡️ Network Security System

<div align="center">

![Network Security](https://img.shields.io/badge/Network-Security-blue?style=for-the-badge&logo=shield&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge&logo=tensorflow&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**An advanced machine learning-powered network security system for phishing detection and threat analysis**

</div>

---

## Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#️-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Data](#-data)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

## Overview

The **Network Security System** is a comprehensive machine learning solution designed to detect and prevent phishing attacks and other network security threats. This system leverages advanced data analysis techniques and machine learning algorithms to identify suspicious network activities and protect against cyber threats.

### Key Highlights

- **AI-Powered Detection**: Advanced machine learning algorithms for threat detection
- **Real-time Analysis**: Continuous monitoring and analysis of network traffic
- **Phishing Detection**: Specialized detection of phishing attempts
- **Data-Driven**: Evidence-based security decisions using comprehensive datasets
- **Modular Architecture**: Well-structured, maintainable codebase
- **Comprehensive Logging**: Detailed logging for audit and debugging

---

## Project Progress (as of August 2025)

### Implemented

- **Data Ingestion & Preprocessing**
   - Reads phishing dataset (`phisingData.csv`) using pandas.
   - Converts CSV data to JSON for further processing.

- **MongoDB Integration**
   - Loads MongoDB connection string from `.env` using `python-dotenv`.
   - Uses `pymongo` and `certifi` for secure, cloud-compatible database connections.
   - Inserts processed data into MongoDB collections.

- **Robust Exception Handling**
   - Custom exception class (`NetworkSecurityException`) for clear error reporting.
   - Centralized logging using a custom logger.

- **Project Structure**
   - Modular Python package layout (`networksecurity/`).
   - Separate folders for cloud, components, constants, entities, exceptions, logging, pipeline, and utilities.
   - All dependencies managed in `requirements.txt`.

- **Environment & Dependency Management**
   - Virtual environment setup instructions.
   - All required packages listed and upgradable.

---

## Modular Pipeline Architecture

- **Data Ingestion Pipeline**
   - `DataIngestion` class: Connects to MongoDB, exports collections as DataFrames, stores features, and splits data into train/test sets.
   - Configured via `DataIngestionConfig` and `TrainingPipelineConfig` (timestamped artifact directories).
   - Artifacts tracked using dataclasses (`DataIngestionArtifact`).

- **Data Validation Pipeline**
   - `DataValidation` class: Validates ingested data against a YAML schema, checks for data drift using statistical tests (KS test), and organizes valid/invalid data.
   - Configured via `DataValidationConfig` and tracked with `DataValidationArtifact`.

- **YAML-Based Configuration**
   - All schema and pipeline configs are loaded from YAML files for flexibility and reproducibility.
   - Utility functions for reading YAML and handling serialization.

- **Exception & Logging System**
   - Custom `NetworkSecurityException` for detailed error reporting (file, line, message).
   - Centralized logging with timestamped log files for traceability.

- **Testing & Validation**
   - Includes scripts for MongoDB connection testing and pipeline validation.

---

## How to Use (Current State)

1. **Set up your environment:**
    - Create a `.env` file with your `MONGO_DB_URL`.
    - Install dependencies:  
       `pip install -r requirements.txt`

2. **Run the data ingestion and validation pipeline:**
    - `python main.py`
    - This will connect to MongoDB, export data, validate it, and store artifacts in a timestamped directory.

3. **Logging & Error Handling:**
    - All errors are logged and reported with file and line number for easy debugging.

4. **Test MongoDB Connection:**
    - Use `test_mongodb.py` to verify your database connection.

---

## Next Steps

- Implement model training and evaluation modules.
- Add real-time monitoring and threat analysis.
- Expand data pipeline and cloud deployment options.
- Integrate more advanced validation and feature engineering steps.

### How to Use (Current State)

1. **Set up your environment:**
    - Create a `.env` file with your `MONGO_DB_URL`.
    - Install dependencies:  
       `pip install -r requirements.txt`

2. **Run the data ingestion script:**
    - `python push_data.py`
    - This will read the CSV, convert it to JSON, and insert it into your MongoDB database.

3. **Logging & Error Handling:**
    - All errors are logged and reported with file and line number for easy debugging.

### Next Steps

- Implement machine learning models for phishing detection.
- Add real-time monitoring and threat analysis.
- Expand data pipeline and cloud deployment options.

---

## Features

### Security Features
- **Phishing Detection**: Advanced algorithms to identify phishing attempts
- **Threat Analysis**: Comprehensive analysis of network security threats
- **Real-time Monitoring**: Continuous surveillance of network activities
- **Anomaly Detection**: Identification of unusual network patterns

### Technical Features
- **Modular Design**: Clean, maintainable code architecture
- **Exception Handling**: Robust error handling and reporting
- **Logging System**: Comprehensive logging for monitoring and debugging
- **Data Pipeline**: Efficient data processing and analysis pipeline
- **Cloud Integration**: Ready for cloud deployment
- **Docker Support**: Containerized deployment option

---

## Project Structure

```
Network Security System/
├── 📁 networksecurity/           # Core application package
│   ├── 📁 cloud/               # Cloud integration modules
│   ├── 📁 components/          # System components
│   ├── 📁 constant/            # Application constants
│   ├── 📁 entity/              # Data entities and models
│   ├── 📁 exception/           # Custom exception handling
│   ├── 📁 logging/             # Logging configuration
│   ├── 📁 pipeline/            # Data processing pipelines
│   └── 📁 utils/               # Utility functions
├── 📁 Network_Data/             # Dataset directory
│   └── 📄 phisingData.csv      # Phishing detection dataset
├── 📁 notebooks/               # Jupyter notebooks for analysis
├── 📄 Dockerfile              # Docker configuration
├── 📄 requirements.txt         # Python dependencies
├── 📄 setup.py                # Package setup configuration
└── 📄 README.md               # Project documentation
```

---

## 🚀 Installation

### Prerequisites

- Python 3.12 or higher
- pip package manager
- Git

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/HumourSpeech/Network-Security-System.git
   cd Network-Security-System
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   
   **Windows:**
   ```powershell
   venv\Scripts\Activate.ps1
   ```
   
   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Install Package in Development Mode**
   ```bash
   pip install -e .
   ```

---

## Usage

### Basic Usage

```python
from networksecurity import NetworkSecuritySystem

# Initialize the security system
security_system = NetworkSecuritySystem()

# Start monitoring
security_system.start_monitoring()
```

### Configuration

Create a `.env` file in the root directory:

```env
# Database Configuration
MONGO_DB_URL=your_mongodb_connection_string

# Logging Configuration
LOG_LEVEL=INFO

# Security Settings
THREAT_THRESHOLD=0.8
```

---

## Data

The system uses the `phisingData.csv` dataset located in the `Network_Data/` directory. This dataset contains:

- Network traffic patterns
- Phishing indicators
- Security threat signatures
- Historical attack data

### Data Processing Pipeline

1. **Data Ingestion**: Automated data collection and preprocessing
2. **Feature Engineering**: Advanced feature extraction for ML models
3. **Model Training**: Continuous learning and model improvement
4. **Threat Detection**: Real-time threat identification and classification

---

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `MONGO_DB_URL` | MongoDB connection string | - |
| `LOG_LEVEL` | Logging level | `INFO` |
| `THREAT_THRESHOLD` | Detection sensitivity | `0.8` |

### Logging Configuration

The system automatically generates timestamped log files in the `logs/` directory with the format:
```
MM_DD_YYYY_HH_MM_SS.log
```

---

## 🐳 Docker Deployment

```bash
# Build Docker image
docker build -t network-security-system .

# Run container
docker run -p 8080:8080 network-security-system
```

---

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

---

## 👨‍💻 Author

**Nitin Mishra**
- Email: mishranitin6076@gmail.com
- GitHub: [@HumourSpeech](https://github.com/HumourSpeech)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to all contributors who have helped build this system
- Special recognition to the cybersecurity community for their ongoing research
- Appreciation for open-source libraries that made this project possible

---

<div align="center">

**Star this repository if you find it helpful!**

Made with ❤️ by [Nitin Mishra](https://github.com/HumourSpeech)

</div>