
# Credit Card Fraud Detection


## Overview
The Credit Card Fraud Detection project aims to identify fraudulent transactions from a dataset of credit card transactions. The project addresses the challenge of class imbalance and employs advanced machine learning techniques to build an effective fraud detection model. The final model is deployed on Streamlit for interactive use.

## Features
- **Imbalanced Dataset Handling:** Uses Random UnderSampling to address class imbalance.
- **Model Building:** Applies hyperparameter tuning and ensembling techniques to optimize performance.
- **Deployment:** Hosted the final model on Streamlit for real-time interaction.

## Technologies Used
Python, Scikit-Learn, Pandas, Matplotlib

## Data Handling
- **Random Sampling**
To address the class imbalance issue, where fraudulent transactions are much rarer than legitimate ones, Random UnderSampling was used. This technique involves undersampling the majority class (legitimate transactions) to create a balanced dataset.

## Model Building
- **Hyperparameter Tuning**
Hyperparameter tuning was performed to optimize model performance. This involved systematically exploring different combinations of model parameters to find the best configuration. Techniques such as Grid Search or Random Search were used to fine-tune parameters and improve model accuracy.
- **Ensembling Techniques**
Ensembling methods were employed to enhance model performance by combining multiple models.
## Setup

1. Clone the repository
```bash
  git clone https://github.com/aysh2603/credit-card-fraud-detection.git

```

2. Navigate to the Project Directory
```bash
  cd credit-card-fraud-detection
```

3. Install the necessary packages
```bash
  pip install -r requirements.txt
```

4. Run the Streamlit app
```bash
  streamlit run app.py
```
