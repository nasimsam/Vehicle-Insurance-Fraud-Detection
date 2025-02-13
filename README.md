<h1>💬Vehicle Insurance Claim Fraud Detection App</h1>
<br>
In this project, I worked on detecting fraud Vehicle insurance claims. The data set for this project is downloaded from the Kaggle website. The correlation matrix is used to extract meaningful features from data. I used one hot encoding to convert the categorical values to numerical values. Since our dataset was imbalanced I used the resampling method to deal with the imbalanced dataset. 
<br>
For model selection, I trained different machine learning models such as SVM, Random Forest, and XGboost for fraud detection. Finally, the models are evaluated using Confusion Matrix and F1-Score. 
<br>
<br>
You can check out the app at the following URL: https://vehicle-insurance-fraud-detection-n2ikx2sbgogbdlbedjuk8i.streamlit.app/
<br>
<h1>About the dataset</h1>
<br>
The dataset has 33 columns with positive and negative samples of fraud insurance claims. Some of these columns are Vehicle Category, PolicyType, Vehicle Price, Past Number of Claims, Driver Rating, and Age of Vehicle.
Dataset Kaggle Link: https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection

<h1> How to run it on your own machine</h1>

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run app.py
   ```

