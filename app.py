import streamlit as st 
import pickle 
import pandas as pd 



st.title("Diabetes Prediction") 
st.info("Enter the details to predict the Diabetes Status")

# Getting Details for User

col1,col2=st.columns(2)
with col1:
    gender=st.selectbox("Gender", ["F","M"],)
with col2:
    age=st.number_input("Age",) 

col3,col4=st.columns(2)
with col3:
    urea=st.number_input("Urea", min_value=0.5 ,max_value=40.0 )
with col4:
    cr=st.number_input("Creatinine", min_value=6 ,max_value=800 )

col5,col6=st.columns(2)
with col5:
    hba1c=st.number_input("HbA1c", min_value= 0.9,max_value=16.0 )
with col6:
    chol=st.number_input("Cholesterol", min_value=0.0 ,max_value=10.3 ) 

col7,col8=st.columns(2)
with col7:
    tg=st.number_input("Triglycerides", min_value=0.3 ,max_value=13.8 ) 
with col8:
    hdl=st.number_input("High-density lipoprotein (HDL)", min_value=0.2 ,max_value=9.9 ) 

col9,col10=st.columns(2)
with col9:
    ldl=st.number_input("Low-density lipoprotein (LDL)", min_value=0.3 ,max_value=9.9 ) 
with col10:
    vldl=st.number_input("Very low-density lipoprotein (VLDL)", min_value=0.1 ,max_value=35.0 ) 

col11,col2=st.columns(2)
with col11:
    bmi=st.number_input("BMI", min_value=19 ,max_value=48 ) 



# Loading Function for Pickle files
def load_pickle(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)

# Load models and encoders
std = load_pickle("Standard.pkl")
ohe = load_pickle("OneHot.pkl")  # OneHotEncoder(drop="first")
knn = load_pickle("KNN.pkl")
oe_target = load_pickle("Ordinal.pkl")



st.write("Click the Button for Diabetes Prediction")
if st.button("Predict"):
    # Create the dataframe
    input_data = pd.DataFrame({"Gender": [gender], "AGE": [age], "Urea": [urea], "Cr": [cr], "HbA1c": [hba1c], "Chol": [chol],
                                "TG": [tg], "HDL": [hdl], "LDL": [ldl], "VLDL": [vldl], "BMI": [bmi]}) 

    #st.write(input_data)

    # Encode the Gender column using OneHotEncoder
    gender_code=ohe.transform(input_data[['Gender']]) 
    input_data['Gender']=gender_code.reshape(-1)

    # Scale all the columns using StandardScalar
    input_scaled=std.transform(input_data) 

    # Predict the output using model
    output_prediction=knn.predict(input_scaled) 

    # Labeling for the result for clarity
    labeling_output={0:"Non-Diabetic", 1:"Pre-Diabetic", 2:"Diabetic"}    
    result=labeling_output.get(output_prediction[0])

    st.write(f"Prediction of the Given data results in '{result}'")
    
    # Message based on result
    if result == "Non-Diabetic":
        st.info("You are healthy, Keep maintaining a balanced diet and regular exercise.")
    elif result == "Pre-Diabetic":
        st.warning("You are at risk of diabetes. Consult a doctor soon, and maintain a healthy diet with regular exercise.")
    elif result == "Diabetic":
        st.error("You have diabetes. Please consult your doctor regularly, and maintain a healthy diet with regular exercise.")
    


    
