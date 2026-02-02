# Network Security System

<div align="center">

![Network Security](https://img.shields.io/badge/Network-Security-blue?style=for-the-badge&logo=shield&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge&logo=tensorflow&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge)

**A production-ready machine learning pipeline for network security threat detection and phishing classification**

</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Machine Learning Pipeline](#machine-learning-pipeline)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

---

## Overview

The **Network Security System** is a comprehensive, production-ready machine learning solution for detecting phishing attacks and network security threats. Built with enterprise-grade architecture, it features a complete ML pipeline from data ingestion to model deployment with automated validation, transformation, and monitoring capabilities.

### Key Highlights

- **Complete ML Pipeline**: End-to-end automated machine learning workflow
- **Advanced Phishing Detection**: Multi-algorithm approach for high accuracy threat classification
- **Real-time Inference**: Fast prediction capabilities for live threat detection
- **Enterprise Architecture**: Modular, scalable, and maintainable design
- **Model Performance Tracking**: Comprehensive metrics and validation with MLflow integration
- **Secure Data Handling**: Encrypted MongoDB connections and secure data processing
- **Production Ready**: Full artifact management, logging, and exception handling

---

## Features

### Security Features
- **Phishing Detection**: Binary classification system for identifying malicious websites
- **URL Analysis**: Comprehensive analysis of 31 website features including domain characteristics, SSL states, and traffic patterns
- **Real-time Classification**: Fast inference capabilities for live threat assessment
- **Data Drift Detection**: Statistical monitoring using Kolmogorov-Smirnov tests

### Technical Features
- **Modular Architecture**: Clean separation of concerns with configurable components
- **Enterprise Logging**: Structured logging with timestamp and detailed error tracking
- **Exception Handling**: Comprehensive error management with custom NetworkSecurityException
- **Configuration Management**: YAML-based schema validation and pipeline configuration
- **Artifact Management**: Complete pipeline artifact tracking with timestamp-based versioning
- **Cloud Integration**: MongoDB Atlas integration with secure SSL/TLS connections
- **Model Versioning**: MLflow integration for experiment tracking and model management

---

## Machine Learning Pipeline

### Complete Training Pipeline

The system implements a sophisticated 4-stage ML pipeline with automated artifact management:

#### 1. Data Ingestion
- **MongoDB Integration**: Secure connection to MongoDB Atlas with SSL/TLS encryption
- **Automated Data Export**: Seamless extraction of phishing dataset from cloud database
- **Train/Test Splitting**: Configurable data splitting with 80/20 ratio using scikit-learn
- **Artifact Generation**: Timestamped data lineage and version control with DataIngestionArtifact

#### 2. Data Validation  
- **Schema Validation**: YAML-based data schema enforcement with 31 predefined features
- **Column Validation**: Automated verification of required numerical columns
- **Data Drift Detection**: Statistical testing using Kolmogorov-Smirnov two-sample tests
- **Quality Assurance**: Comprehensive data quality checks with separate handling for valid/invalid data
- **Drift Reporting**: Automated generation of drift reports for model monitoring

#### 3. Data Transformation
- **KNN Imputation**: Advanced missing value handling with configurable K=3 neighbors
- **Feature Preprocessing**: Standardized preprocessing pipeline using scikit-learn Pipeline
- **Numpy Optimization**: Efficient data storage in binary format for faster processing
- **Object Serialization**: Reusable transformation objects using pickle for inference pipeline

#### 4. Model Training
- **Multi-Algorithm Support**: 
  - Random Forest Classifier with configurable estimators (8-256 trees)
  - Gradient Boosting Classifier with learning rate optimization (0.001-0.1)
  - Decision Tree Classifier with criterion selection (gini, entropy, log_loss)
  - Logistic Regression with regularization
  - AdaBoost Classifier with adaptive boosting
- **Hyperparameter Tuning**: GridSearchCV with 3-fold cross-validation for optimal parameters
- **Performance Evaluation**: Comprehensive metrics including F1-score, Precision, and Recall
- **Model Selection**: Automated best model selection based on R² score performance
- **Overfitting Prevention**: Built-in validation with 5% threshold for train-test score difference
- **MLflow & Dagshub Integration**: Experiment tracking, metric logging, and model versioning (track_mlflow method)

### Custom Components

#### NetworkModel Estimator
- **Unified Interface**: Combined preprocessing and model prediction pipeline
- **Serializable Architecture**: Complete model objects for deployment and inference  
- **Thread-Safe Operations**: Production-ready prediction capabilities

#### Classification Metrics
- **Comprehensive Evaluation**: F1-score, Precision, Recall calculation
- **Performance Artifacts**: Structured metric storage using ClassificationMetricArtifact
- **Model Validation**: Automated performance threshold validation (minimum F1-score: 0.6)

---

## Architecture

### System Design Principles
- **Modularity**: Each component is independently testable and configurable
- **Scalability**: Pipeline designed for handling large-scale data processing
- **Maintainability**: Clear separation of concerns with dependency injection
- **Reliability**: Comprehensive error handling and logging throughout the pipeline
- **Reproducibility**: Timestamped artifacts and configuration management

### Data Flow Architecture
```
MongoDB Atlas → Data Ingestion → Data Validation → Data Transformation → Model Training → Trained Model
      ↓              ↓               ↓                    ↓                ↓
  Raw Data    Feature Store    Validated Data      Preprocessed Data   Model Artifacts
```

### Configuration Management
- **Entity-Based Configuration**: Separate configuration classes for each pipeline stage
- **Artifact Tracking**: Dataclass-based artifact management for pipeline outputs
- **YAML Schema**: External configuration files for data validation and preprocessing parameters

---

## Project Structure

```
Network Security System/
├── networksecurity/                    # Core ML Package
│   ├── pipeline/                       # Pipeline Orchestration
│   │   └── training_pipeline.py       # Complete training pipeline class
│   ├── components/                     # Pipeline Components
│   │   ├── data_ingestion.py          # MongoDB data extraction and splitting

│   │   ├── data_validation.py         # Schema validation and drift detection  
│   │   ├── data_transformation.py     # KNN imputation and preprocessing
│   │   └── model_trainer.py           # Multi-algorithm training with MLflow
│   ├── entity/                        # Configuration and Artifacts
│   │   ├── config_entity.py           # Pipeline configuration classes
│   │   └── artifact_entity.py         # Dataclass-based artifacts
│   ├── constant/                      # Pipeline Constants
│   │   └── training_pipeline/         # Training configuration constants
│   ├── utils/                         # Utility Functions
│   │   ├── main_utils/                # Core utilities (YAML, serialization)
│   │   └── ml_utils/                  # ML-specific utilities
│   │       ├── model/                 # Custom estimators (NetworkModel)
│   │       └── metric/                # Evaluation metrics
│   ├── exception/                     # Custom exception handling
│   │   └── exception.py               # NetworkSecurityException class
│   ├── logging/                       # Centralized logging
│   │   └── logger.py                  # Structured logging configuration
│   └── cloud/                         # Cloud integration modules
├── data_schema/                       # Validation Schemas
│   └── schema.yaml                    # 31-feature validation schema
├── Network_Data/                      # Dataset Storage
│   └── phisingData.csv               # Phishing dataset (31 features)
├── artifact/                         # Pipeline Artifacts
│   └── {timestamp}/                  # Timestamped pipeline runs
├── logs/                             # Application Logs
├── saved_models/                     # Trained Model Storage
├── notebooks/                        # Jupyter notebooks for analysis
├── main.py                           # Complete pipeline execution
├── push_data.py                      # MongoDB data upload utility
├── test_mongodb.py                   # Database connection testing
├── requirements.txt                  # Python dependencies
├── setup.py                          # Package configuration with metadata
├── Dockerfile                        # Container configuration
└── README.md                         # Project documentation
```

---

## Installation

### Prerequisites

- **Python 3.12+** (Required for latest ML libraries compatibility)
- **MongoDB Atlas Account** (For cloud data storage)
- **Git** (For version control)
- **4GB+ RAM** (Recommended for model training)

### Quick Start

1. **Clone Repository**
   ```bash
   git clone https://github.com/HumourSpeech/Network-Security-System.git
   cd Network-Security-System
   ```

2. **Setup Virtual Environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\Activate.ps1
   
   # Linux/Mac  
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

4. **Configure Environment**
   ```bash
   # Create .env file with MongoDB connection
   echo "MONGO_DB_URL=your_mongodb_atlas_connection_string" > .env
   ```

5. **Run Complete Pipeline**
   ```bash
   python main.py
   ```

---

## Usage

### Complete Pipeline Execution

```python
from networksecurity.pipeline.training_pipeline import TrainingPipeline

# Initialize the pipeline
pipeline = TrainingPipeline()

# Execute complete ML pipeline (Ingestion → Validation → Transformation → Training)
try:
    model_artifact = pipeline.run_pipeline()
    print(f"Training completed. Best model saved at: {model_artifact.trained_model_file_path}")
    
except Exception as e:
    print(f"Pipeline execution failed: {e}")
```

### Manual Component Execution

```python
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import *

# Initialize timestamped pipeline configuration
training_config = TrainingPipelineConfig()

# Execute components step-by-step
try:
    # Data Ingestion: MongoDB → Feature Store → Train/Test Split
    data_ingestion = DataIngestion(DataIngestionConfig(training_config))
    ingestion_artifact = data_ingestion.initiate_data_ingestion()
    
    # Data Validation: Schema Check → Drift Detection
    data_validation = DataValidation(ingestion_artifact, DataValidationConfig(training_config))
    validation_artifact = data_validation.initiate_data_validation()
    
    # Data Transformation: KNN Imputation → Preprocessing
    data_transformation = DataTransformation(validation_artifact, DataTransformationConfig(training_config))
    transformation_artifact = data_transformation.initiate_data_transformation()
    
    # Model Training: Multi-Algorithm → Hyperparameter Tuning → Best Model Selection
    model_trainer = ModelTrainer(ModelTrainerConfig(training_config), transformation_artifact)
    model_artifact = model_trainer.initiate_model_trainer()
    
    print(f"Best model saved at: {model_artifact.trained_model_file_path}")
    
except Exception as e:
    print(f"Pipeline execution failed: {e}")
```

### Model Inference

```python
from networksecurity.utils.main_utils.utils import load_object
import pandas as pd
import numpy as np

# Load trained NetworkModel
model = load_object("artifact/{timestamp}/model_trainer/trained_model/model.pkl")

# Prepare new data (31 features as per schema.yaml)
new_data = pd.DataFrame({
    'having_IP_Address': [1],
    'URL_Length': [0],
    'Shortining_Service': [1],
    # ... additional 28 features
    'Statistical_report': [1]
})

# Make predictions (0: Legitimate, 1: Phishing)
predictions = model.predict(new_data)
print(f"Prediction: {'Phishing' if predictions[0] == 1 else 'Legitimate'}")
```

### Data Upload to MongoDB

```python
from push_data import NetworkDataExtract

# Initialize data extractor
extractor = NetworkDataExtract()

# Convert CSV to JSON and upload to MongoDB
FILE_PATH = "Network_Data/phisingData.csv"
DATABASE = "NitinMishra"
COLLECTION = "NetworkData"

records = extractor.csv_to_json_convertor(FILE_PATH)
count = extractor.insert_data_mongodb(records, DATABASE, COLLECTION)
print(f"Uploaded {count} records to MongoDB")
```

---

## Model Performance

### Performance Metrics
- **Expected Minimum F1-Score**: 0.6 (60% threshold for model acceptance)
- **Overfitting Threshold**: 0.05 (5% maximum difference between train/test scores)
- **Model Selection**: Automated best performer selection based on R² score
- **Cross-Validation**: 3-fold cross-validation for hyperparameter tuning

### Supported Algorithms
- **Random Forest**: Ensemble method with 8-256 estimators
- **Gradient Boosting**: Advanced boosting with learning rates 0.001-0.1
- **Decision Tree**: Interpretable classification with multiple criteria
- **Logistic Regression**: Linear classification with regularization
- **AdaBoost**: Adaptive boosting for improved performance

### Feature Set
The model analyzes 31 website characteristics:
- **URL Features**: IP address usage, URL length, shortening services
- **Domain Features**: SSL state, domain registration length, subdomain analysis
- **Content Features**: HTTPS tokens, request URLs, anchor analysis
- **Traffic Features**: Web traffic patterns, page rank, Google indexing
- **Security Features**: Right-click protection, pop-up windows, iframe usage

---

## Configuration

### Environment Variables

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `MONGO_DB_URL` | MongoDB Atlas connection string | `mongodb+srv://...` | Yes |
| `LOG_LEVEL` | Logging verbosity level | `INFO`, `DEBUG` | No |
| `ARTIFACT_DIR` | Pipeline artifacts directory | `artifact` | No |

### Pipeline Configuration

```python
# Training Pipeline Constants
TARGET_COLUMN = "Result"                    # Binary target (0: Legitimate, 1: Phishing)
TRAIN_TEST_SPLIT_RATIO = 0.2               # 80/20 train-test split
EXPECTED_SCORE = 0.6                       # Minimum acceptable F1-score
OVERFITTING_THRESHOLD = 0.05               # Maximum train-test score difference

# KNN Imputer Parameters  
IMPUTER_PARAMS = {
    "missing_values": np.nan,              # Handle NaN values
    "n_neighbors": 3,                      # Use 3 nearest neighbors
    "weights": "uniform"                   # Equal weight for all neighbors
}
```

### Data Schema (schema.yaml)
```yaml
columns:
  - having_IP_Address: int64              # IP address in URL (0/1)
  - URL_Length: int64                     # URL length classification
  - SSLfinal_State: int64                 # SSL certificate status
  - Domain_registeration_length: int64    # Domain registration period
  - web_traffic: int64                    # Website traffic ranking
  # ... 26 additional features

numerical_columns: [list of all 31 features]
```

### Logging Configuration
- **Format**: Structured logging with timestamps and stack traces
- **Location**: `logs/MM_DD_YYYY_HH_MM_SS.log`
- **Levels**: INFO, DEBUG, ERROR, WARNING
- **Features**: Custom NetworkSecurityException integration

---

## Docker Deployment

### Build and Run

```bash
# Build Docker image
docker build -t network-security-system .

# Run container with environment variables
docker run -p 8080:8080 \
  -e MONGO_DB_URL="your_mongodb_connection_string" \
  network-security-system

# Using Docker Compose (recommended for production)
docker-compose up -d
```

### Docker Configuration
- **Base Image**: Python 3.12-slim
- **Exposed Port**: 8080
- **Environment**: Production-optimized with minimal dependencies
- **Health Checks**: Built-in MongoDB connectivity validation

---

## Contributing

We welcome contributions to improve the Network Security System. Please follow our development guidelines.

### Development Setup

```bash
# Clone and setup development environment
git clone https://github.com/HumourSpeech/Network-Security-System.git
cd Network-Security-System
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

### Contribution Guidelines

1. **Code Standards**
   - Follow PEP 8 style guidelines
   - Add comprehensive docstrings
   - Include type hints where applicable
   - Maintain modular design principles

2. **Testing Requirements**
   - Add unit tests for new features
   - Ensure pipeline tests pass completely
   - Test MongoDB connectivity and data validation
   - Validate model performance metrics

3. **Documentation**
   - Update README.md for new features
   - Document configuration changes
   - Add inline code comments
   - Include usage examples

4. **Pull Request Process**
   - Create descriptive branch names
   - Write clear commit messages
   - Include detailed PR descriptions
   - Ensure all CI/CD checks pass

### Running Tests

```bash
# Test complete pipeline
python main.py

# Test MongoDB connection
python test_mongodb.py

# Validate data schema
python -c "from networksecurity.utils.main_utils.utils import read_yaml_file; print(read_yaml_file('data_schema/schema.yaml'))"
```

---

## Author

**Nitin Mishra**
- **Email**: mishranitin6076@gmail.com
- **GitHub**: [@HumourSpeech](https://github.com/HumourSpeech)
- **LinkedIn**: [Connect with me](https://linkedin.com/in/nitin-mishra)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **scikit-learn community** for providing robust machine learning algorithms
- **MongoDB** for reliable cloud database services
- **MLflow** for experiment tracking and model management
- **Open source contributors** who have made this project possible
- **Cybersecurity research community** for continuous threat intelligence

---

<div align="center">

**Star this repository if you find it helpful for your cybersecurity projects!**

**Built with Python | Powered by Machine Learning | Secured by Design**

</div>