import streamlit as st
import pandas as pd
import pickle
import xgboost

st.title("Insurance Claim Fraud Detection")
usr_ip = ['Dec','Female','Divorced','Sport - Collision','No.1','Internal','1995','Collision']
input = ['Honda','Rural','Policy Holder','Sedan','20000 to 29000','more than 4','more than 7','16 to 17','No']
def user_input(all_columns, input, deductible, user_ip = usr_ip):
    df=pd.DataFrame(columns=all_columns , index=[0])
    df.fillna(0, inplace=True)
    for ip in user_ip:
        df[ip].iloc[0] = 1
    for ip in input:
        df[ip].iloc[0] = 1
    df['Deductible'].iloc[0] = deductible
    return df

all_colums = ['Deductible', 'Apr', 'Aug', 'Dec', 'Feb',
       'Jan', 'Jul', 'Jun', 'Mar', 'May', 'Nov', 'Oct', 'Sep', 'Accura', 'BMW',
       'Chevrolet', 'Dodge', 'Ferrari', 'Ford', 'Honda', 'Jaguar', 'Lexus',
       'Mazda', 'Mecedes', 'Mercury', 'Nisson', 'Pontiac', 'Porche', 'Saab',
       'Saturn', 'Toyota', 'VW', 'Rural', 'Urban', 'Female', 'Male',
       'Divorced', 'Married', 'Single', 'Widow', 'Policy Holder',
       'Third Party', 'Sedan - All Perils', 'Sedan - Collision',
       'Sedan - Liability', 'Sport - All Perils', 'Sport - Collision',
       'Sport - Liability', 'Utility - All Perils', 'Utility - Collision',
       'Utility - Liability', 'Sedan', 'Sport', 'Utility', '20000 to 29000',
       '30000 to 39000', '40000 to 59000', '60000 to 69000', 'less than 20000',
       'more than 69000', '1', '2 to 4', 'more than 4', 'none', '2 years',
       '3 years', '4 years', '5 years', '6 years', '7 years', 'more than 7',
       'new', '16 to 17', '18 to 20', '21 to 25', '26 to 30', '31 to 35',
       '36 to 40', '41 to 50', '51 to 65', 'over 65', 'No', 'Yes', 'No.1',
       'Yes.1', 'External', 'Internal', '1994', '1995', '1996', 'All Perils',
       'Collision', 'Liability']

filename = 'model.pickle'
loaded_model = pickle.load(open(filename, 'rb'))
st.write("Please enter the following information for the claim:")
input[0]= st.selectbox("Please enter the make of the car:", ['Honda', 'Toyota', 'Ford', 'BMW', 'Chevrolet', 'Pontiac', 'Mercury', 'Nisson', 'VW', 'Mecedes', 'Lexus', 'Jaguar', 'Mazda', 'Dodge', 'Saturn', 'Porche', 'Ferrari', 'Saab'])
input[1]= st.selectbox("Please enter the area of the accident:", ['Rural', 'Urban'])
input[2]= st.selectbox("Please enter the fault:", ['Policy Holder', 'Third Party'])
input[3]= st.selectbox("Please enter the vehicle category:", ['Sedan', 'Sport', 'Utility'])
input[4]= st.selectbox("Please enter the vehicle price:", ['less than 20000', '20000 to 29000', '30000 to 39000', '40000 to 59000', '60000 to 69000', 'more than 69000'])
input[5]= st.selectbox("Please enter the number of past claims:", ['1', '2 to 4', 'more than 4', 'none'])
input[6]= st.selectbox("Please enter the age of the vehicle:", ['new', '2 years', '3 years', '4 years', '5 years', '6 years', '7 years', 'more than 7'])
input[7]= st.selectbox("Please enter the age of the policy holder:", ['16 to 17', '18 to 20', '21 to 25', '26 to 30', '31 to 35', '36 to 40', '41 to 50', '51 to 65', 'over 65'])
input[8]= st.selectbox("Please enter if the police report was filed:", ['No', 'Yes'])
deductible = st.number_input("Please enter the deductible amount:")
if st.button("Predict"):
    user_data = user_input(all_colums, input, deductible)
    prediction = loaded_model.predict(user_data)
    if prediction[0] == 1:
        st.write("The claim is fraudulent.")
    else:
        st.write("The claim is not fraudulent.")
    





