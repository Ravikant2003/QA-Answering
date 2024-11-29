# QA-Answering

So, I have used this dataset : https://www.kaggle.com/datasets/praneshmukhopadhyay/amazon-questionanswer-dataset?select=single_qna.csv

Now, this dataset has 3 CSV files namely, 

1) Multi_answers.csv
2) multi_questions.csv
3) single_question.csv

   Now I have combined all the three csv files and have talen the top 1000/50000 data from the dataset for fine tuning my HuggingPhase model.

   I have used the T-5 small model from huggingphase to fine tun eit to my custom dataset.


   Now, The Jupyternotebook contains the code to create a fine tuned model from my csv dataset (Named :preparaed_data.csv).
   The app.py utilises the already created fine tuned model to give a predicted outcome based on the context provided.

   The user can be divided into Prime and Non Prime user where, the Prime user gets a more detailed answer while the Non Prime user gets a less detailed answer.

   The User Interface has been built using Streamlit and the credentials of the prime and non prime users are stored in the form of Python Dictonary.  

   Some problems which i faced in making this project and would still be visible would be:

1) The dataset i am using doesnt have a fixed defined context, In general when T-5 small model is used it generally utilizes three inputs: 1) Input text : Which is a combination of question and context 
                                                                                                                                             2) Output Text: Which has the answer in it

Now, in order to make sure that anoamly is solved, I have utilized the answer as the context in the input text , hence both the answer and the context would be same.


2) If , I tried using to train the model without context i was get very vague and unclear answers, SO thats why a context is needed from the user apart from the question from the user .

3) The Logic of Assigning Prime / Non Prime User based output from the model: I was facing issues while I was trying to assign roles along with the context , question and Answer while i was trying to fine tune my model.Now, there maybe something that i might have missed while i was trying to assign user as Prime and Non Prime Hence, I decided to consider the length of output as the parameter to get the assigned answer, where :
                                                                                                                                                           a) Prime Members: Get a longer explanation
                                                                                                                                                           b) Non Prime Members: Get a shorter Explanation


I know My approach is not really perfect and it has certain flaws in it , I am open to suggestion and corrections from your side.
