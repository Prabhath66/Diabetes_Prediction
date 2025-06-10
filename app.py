import streamlit as st 
import pickle 



# Getting Details for User
gender=st.selectbox("Gender", ["F","M"],)
age=st.number_input("Age",)
urea=st.number_input("Urea", min_value=0.5 ,max_value=40.0 )
cr=st.number_input("Creatinine", min_value=6 ,max_value=800 )
hba1c=st.number_input("HbA1c", min_value= 0.9,max_value=16.0 )
chol=st.number_input("Cholesterol", min_value=0.0 ,max_value=10.3 ) 
tg=st.number_input("Triglycerides", min_value=0.3 ,max_value=13.8 ) 
hdl=st.number_input("High-density lipoprotein (HDL)", min_value=0.2 ,max_value=9.9 ) 
ldl=st.number_input("Low-density lipoprotein (LDL)", min_value=0.3 ,max_value=9.9 ) 
vldl=st.number_input("Very low-density lipoprotein (VLDL)", min_value=0.1 ,max_value=35.0 ) 
bmi=st.number_input("BMI", min_value=19 ,max_value=48 ) 




def load_pickle(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)

# Load models and encoders
std = load_pickle("Standard.pkl")
ohe = load_pickle("OneHot.pkl")  # OneHotEncoder(drop="first")
model = load_pickle("KNN.pkl")
oe_target = load_pickle("Ordinal.pkl")


# # Loading the Pickle Files
# std = pickle.load(open("Standard.pkl", "rb"))
# ohe = pickle.load(open("OneHot.pkl", "rb"))  # OneHotEncoder with drop="first"
# model = pickle.load(open("KNN.pkl", "rb"))
# oe_target = pickle.load(open("Ordinal.pkl", "rb"))  # OrdinalEncoder for target 


st.write("Click the Button for Prediction")
if st.button("Predict"):
    input_data = pd.DataFrame({"Gender": [gender], "Age": [age], "Urea": [urea], "Creatinine": [cr], "HbA1c": [hba1c], "Cholesterol": [chol],
                                "Triglycerides": [tg], "HDL": [hdl], "LDL": [ldl], "VLDL": [vldl], "BMI": [bmi]}) 

    st.write(input_data)

