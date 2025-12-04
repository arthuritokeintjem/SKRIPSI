# SKRIPSI

📘 Forecasting Daily Food Commodity Prices Using ARIMA, LSTM, and GRU (From Scratch)

Undergraduate Thesis Repository - Arthurito Keintjem

This repository contains the complete implementation, datasets, scripts, and experiment results for an undergraduate thesis project focusing on time series forecasting of daily food commodity prices in Malang City using ARIMA, LSTM, and GRU models built entirely from scratch.

The study uses official daily price records from SP2KP - Ministry of Trade, Republic of Indonesia, covering 16 essential food commodities. All deep learning architectures (LSTM, GRU) and ARIMA components are implemented manually without invoking model-ready libraries, following the academic requirements of the Bachelor Thesis.

🎯 Project Overview

The goal of this thesis project is to evaluate and compare the performance of traditional statistical models (ARIMA) with neural sequence models (LSTM and GRU) for forecasting daily prices of essential food commodities.
Since food prices in Indonesia exhibit high volatility, especially for horticultural products like chilies and onions, accurate forecasting is highly relevant for:
1. Government price stabilization policies
2. Market monitoring
3. Logistic and supply chain decision making
4. Early warning systems for inflation spikes

This repository implements the full pipeline, from data acquisition → cleaning → preprocessing → modeling → evaluation → forecasting.

🚀 Workflow Pipeline

The project follows a clear and modular workflow consisting of four main stages:

1️⃣ Data Acquisition - SP2KP API

File: data_acquisition_sp2kp.py

This script performs the official data acquisition process by:
1. Sending authenticated POST requests to the SP2KP average price endpoint
2. Using complete browser-like headers to ensure successful request handling
3. Iterating across a defined date range (daily)
4. Extracting commodity price information for Malang City
5. Storing all acquired observations into dataset_raw.csv

Each acquired record contains:
1. Commodity name
2. Observed price
3. Unit
4. Market location
5. Observation date

This provides a high-fidelity daily dataset based on authoritative government sources.

2️⃣ Data Cleaning

File: data_cleaning.ipynb

Data acquired from SP2KP may contain inconsistencies. This script performs:
1. Removal of weekend entries (no official observations)
2. Filtering invalid or zero-price values
3. Conversion of date formats
4. Regeneration of weekday labels
5. Exporting a cleaned dataset (dataset.csv)

This creates a consistent, validated daily series ready for preprocessing.

3️⃣ Data Preprocessing

File: preprocessing_daily_newest.ipynb

This stage prepares data for forecasting models through:
✔ Wide Format Transformation
Convert long-format SP2KP data into a unified wide time-series dataset where each column represents a commodity.

✔ Handling Missing Values
1. Reindex to business days
2. Time-based interpolation for short gaps
3. Forward/backward fill for remaining gaps
4. Reporting missing-value summaries

✔ Outlier Treatment (IQR Winsorization)
Limits extreme price fluctuations without discarding observations.

✔ Export
processed_daily_wide.csv - the final modeling-ready dataset.

4️⃣ Modeling & Evaluation (ARIMA, LSTM, GRU From Scratch)

File: modeling_daily_newest.ipynb

The modeling pipeline includes:
🔹 ARIMA Manual Implementation
1. Custom differencing
2. Manual seasonal handling
3. Grid search over (p, d, D)
4. One-step iterative forecasting

🔹 LSTM Manual Implementation
Fully coded from scratch, including:
1. Forget / Input / Output gates
2. Cell state propagation
3. Backpropagation through time (BPTT)
4. Custom sequence-to-one architecture

Search space includes:
1. Window size
2. Hidden units (16, 32)

🔹 GRU Manual Implementation
Implements:
1. Reset gate
2. Update gate
3. Candidate activation
4. Recurrent update mechanism
Training procedure parallels the LSTM framework.

🔹 Model Evaluation
Models are compared using:
1. MAPE (main metric)
2. MAE
3. RMSE

Outputs:
1. results_all_models_daily_final.csv
2. results_best_per_commodity_daily_final.csv

🔹 30-Day Forecast Generation
The best-performing model per commodity is refit on full historical data and used to produce:
forecast_next30_best_model_per_commodity.csv

📈 Visualization Tools

The modeling script includes functions to generate:
1. Actual vs Predicted charts
2. Rolling MAPE curves
3. Forecast projection plots

🔧 Installation & Usage

Requirements
1. Python 3.8+
2. numpy
3. pandas
4. matplotlib
5. requests
No TensorFlow or PyTorch is used - all neural models are manually implemented.

Run the Full Pipeline
1. Acquire Data
python data_acquisition_sp2kp.py

2. Clean Data
jupyter nbconvert --to notebook --execute data_cleaning.ipynb

3. Preprocess Data
jupyter nbconvert --to notebook --execute preprocessing_daily_newest.ipynb

4. Model Training & Evaluation
jupyter nbconvert --to notebook --execute modeing_daily_newest.ipynb

🧠 Key Contributions

This repository demonstrates:
1. A fully custom-built time-series forecasting framework
2. Manual implementation of ARIMA, LSTM, and GRU
3. Volatility-based hyperparameter selection
4. Evaluation across 16 essential commodities
5. Practical forecasting outputs applicable to real policy analysis

🙌 Acknowledgements

1. Ministry of Trade (SP2KP) for providing open market price data
2. Faculty of Computer Science, Universitas Brawijaya
3. Academic supervisors and reviewers
4. All collaborators contributing to the successful completion of this research.
