import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


model_path = "./t5_finetuned_final"  # Path to the model
fine_tuned_model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
fine_tuned_tokenizer = AutoTokenizer.from_pretrained(model_path)

# Sample dictionary with Employee ID and Role
user_roles = {
    "E001": "Prime",
    "E002": "Non-Prime",
    "E003": "Prime",
    "E004": "Non-Prime",
   
}


st.title("Generative AI Q&A System")

# Login Console
st.sidebar.header("Login")
employee_id = st.sidebar.text_input("Enter Employee ID:")

# Function to fetch role from the dictionary based on Employee ID
def get_user_role(employee_id):
    if employee_id in user_roles:
        return user_roles[employee_id]  
    else:
        return None


role = None
if employee_id:
    role = get_user_role(employee_id)


if role is None:
    st.sidebar.warning("Invalid Employee ID or Role not assigned.")
else:
    
    st.sidebar.write(f"Logged in as {role} role")

    # Create columns for input and output
    col1, col2 = st.columns(2)

    # Column 1: Input for question and context
    with col1:
        st.header("Input")
        question = st.text_input("Ask a question:", placeholder="Type your question here...")
        context = st.text_area(
            "Provide context:", 
            placeholder="Paste your context here...",
            height=300
        )

    # Column 2: Display output
    with col2:
        st.header("Output")

        if question and context:
            
            if role == "Non-Prime":
                context = context[:500]  
                input_text = f"question: {question} context (Non-Prime Role): {context} Provide a short answer."
            else:
                input_text = f"question: {question} context (Prime Role): {context} Provide a detailed answer."

            inputs = fine_tuned_tokenizer(input_text, return_tensors="pt", truncation=True, padding=True)

           
            max_length = 100 if role == "Non-Prime" else 200
            num_beams = 3 if role == "Non-Prime" else 5

            outputs = fine_tuned_model.generate(
                inputs.input_ids,
                max_length=max_length,
                num_beams=num_beams,
                early_stopping=True
            )

            
            answer = fine_tuned_tokenizer.decode(outputs[0], skip_special_tokens=True)
            st.text_area("Predicted Answer:", answer, height=200)
        else:
            st.text_area("Predicted Answer:", "Waiting for input...", height=200)


stop = st.button("Stop Application")
if stop:
    st.stop()
