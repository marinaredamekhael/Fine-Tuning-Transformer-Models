####Bert=>for feedback analysis

import numpy as np
from transformers import BertTokenizer, TFBertForSequenceClassification, T5Tokenizer, T5ForConditionalGeneration, TFT5ForConditionalGeneration

#model for analysing customer feedback
def BERT(request):
    model_name="nlptown/bert-base-multilingual-uncased-sentiment"
    tokenizer=BertTokenizer.from_pretrained(model_name)
    model=TFBertForSequenceClassification.from_pretrained(model_name)
    input=tokenizer(request)
    input_ids=input['input_ids']
    prediction=model.predict([input_ids])
    logist=prediction.logits
    p_class=np.argmax(logist)
    return p_class

def mapping_value(ratio):
    sentiment_mapping={
    0:'very negative',
    1:'negative',
    2:'neutral',
    3:'positive',
    4:'very positive'
    }
    predict_sentiment=sentiment_mapping[ratio]
    return predict_sentiment

#palm=>for chatting and answer questions
import google.generativeai as genai
def palm(request,type): #the types are (replay on its message or ask new question)or code
    genai.configure(api_key='AIzaSyC7hyOeVchYMmdd7dAq6lZ1eFS3s28sUeM')
    # Create a new conversation\
    response = genai.chat(messages=request)
    
    if type == 'ask':
        response = genai.chat(messages=request)
        return response.last
    
    # Continue the conversation if it's a reply
    elif type == 'reply':
        response = genai.chat(messages=request)
        response = response.reply(request)
        return response.last
    else:
        raise ValueError("Invalid interaction type specified. Use 'ask', 'reply', or 'code'.")
    
    
        
# Model for summarizing text
# def summarize_text(text):
#     model_name = "t5-small"
#     tokenizer = T5Tokenizer.from_pretrained(model_name)
#     model = T5ForConditionalGeneration.from_pretrained(model_name)

#     input_text = "summarize: " + text
#     input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
#     summary_ids = model.generate(input_ids, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#     return summary
def summarize_text(text):
    model_name = "t5-small"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = TFT5ForConditionalGeneration.from_pretrained(model_name)

    input_text = "summarize: " + text
    input_ids = tokenizer.encode(input_text, return_tensors="tf", max_length=512, truncation=True)
    summary_ids = model.generate(input_ids, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def gemini(message):
    genai.configure(api_key='AIzaSyC7hyOeVchYMmdd7dAq6lZ1eFS3s28sUeM')

    context = """
    You are provided with the following database schema. Use this information to generate SQL queries based on the user's request.

    Tables and Their Attributes:

    1. Employee
    - id (integer, primary key, auto-generated)
    - name (varchar(255))
    - nationalID (varchar(255))
    - phoneNumber (varchar(255))
    - job (varchar(255))
    - salary (float)

    2. PetrolPrice
    - date (timestamp, primary key, default current_timestamp)
    - solarPrice (float)
    - petrol80Price (float)
    - petrol92Price (float)
    - petrol95Price (float)

    3. Expenses
    - id (integer, primary key, auto-generated)
    - date (timestamp, default current_timestamp)
    - bond (float)
    - amount (float)

    4. Customer
    - name (varchar(255))
    - national_ID (varchar(255), primary key)
    - phone_Number (varchar(255))

    5. CreditCustomer
    - id (integer, primary key, auto-generated)
    - date (timestamp, default current_timestamp)
    - customer_NID (varchar(255), foreign key references Customer(nationalID))
    - bond (float)
    - amount (float)

    6. Statement
    - name (varchar(255), primary key)

    7. CashMovement
    - id (integer, primary key, auto-generated)
    - type (enum('Receipts', 'Payments'))
    - date (timestamp, default current_timestamp)
    - bond (float)
    - amount (float)

    8. CashM_Has_Statement
    - id_cm (integer, foreign key references CashMovement(id))
    - name_S (varchar(255), foreign key references Statement(name))

    9. DailyPumpShift
    - id (integer, primary key, auto-generated)
    - date (timestamp, default current_timestamp)
    - pumpNumber (int)
    - petrolType (varchar(255))
    - start_code (float)
    - end_code (float)

    10. LoginHistory
        - date (timestamp, primary key, default current_timestamp)
        - time (time)
        - softwareType (varchar(255))

    11. UserAccount
        - userName (varchar(255), primary key)
        - password (varchar(255))
        - role (varchar(255))

    12. UserA_Has_LoginHistory
        - user_Name (varchar(255), foreign key references UserAccount(userName))
        - date_login (timestamp, default current_timestamp, foreign key references LoginHistory(date))

    13. UserA_Has_SActivity
        - userName (varchar(255), foreign key references UserAccount(userName))
        - date_systemA (timestamp, default current_timestamp, foreign key references SystemActivity(date))

    14. SystemActivity
        - date (timestamp, primary key, default current_timestamp)
        - modDate (timestamp, default current_timestamp)
        - time (time)
        - activity (varchar(255))
        - softwareType (varchar(255))

    15. Oil
        - oilName (varchar(255), primary key)
        - price (float)

    16. OilShift
        - date (timestamp, default current_timestamp)
        - startTermBalance (float)
        - endTermBalance (float)
        - inbound (float)
        - sold (float)
        - price (float)
        - oilName (varchar(255), foreign key references Oil(oilName))

    17. OilStorage
        - date (timestamp, default current_timestamp)
        - beginningBalance (float)
        - endingBalance (float)
        - inboundToWarehouse (float)
        - oilName (varchar(255), foreign key references Oil(oilName))

    18. Coupons
        - id (integer, primary key, auto-generated)
        - date (timestamp, default current_timestamp)
        - petrolType (varchar(255))
        - issuer (varchar(255))
        - category (varchar(255))
        - price (float)
        - couponSerial (varchar(255))

    19. MatchingCoupons
        - date (timestamp, default current_timestamp)
        - quantity (int)
        - petrolType (varchar(255))
        - issuer (varchar(255))
        - category (varchar(255))
        - coupon_ID (integer, foreign key references Coupons(id))

    Views:
    1. DailyPumpShift_Liter
        - SELECT id, date, pumpNumber, petrolType, start_code, end_code, (end_code - start_code) AS total_liter FROM DailyPumpShift

    2. TotalProfit_View
        - SELECT startTermBalance, endTermBalance, inbound, sold, price, oilName, (startTermBalance - endTermBalance) AS total_profit FROM OilShift

    Answer every question by returning only the SQL query without any explanation or additional words.
    """




    reply = genai.chat(context=context, messages=message)
    modified_reply=reply.last
    return modified_reply

def extract_sql_query(text):
    start = text.find("```sql") + len("```sql")
    end = text.find("```", start)
    if start != -1 and end != -1:
        return text[start:end].strip()
    return None

import pymysql

def execute_sql(sql_code):
    try:
        # Connect to the database (use your database credentials)
        conn = pymysql.connect(
            host='******',
            user='******',
            password='******',
            database='******'
        )
        cursor = conn.cursor()
        
        # Execute the SQL code
        cursor.execute(sql_code)
        
        # If the query is a SELECT statement, fetch the results and attribute names
        if sql_code.strip().lower().startswith('select'):
            results = cursor.fetchall()
            
            # Fetch attribute names from the cursor description
            attribute_names = [desc[0] for desc in cursor.description]
            
            return attribute_names, results
        else:
            # Commit changes for non-SELECT statements (e.g., INSERT, UPDATE, DELETE)
            conn.commit()
            print("Query executed successfully.")
            return None, None
    except pymysql.MySQLError as e:
        print(f"An error occurred: {e}")
        return None, None

    finally:
        # Close the connection
        if conn:
            conn.close()

from tabulate import tabulate

def parse_records_to_table(records, headers=None):
    # Check if headers are provided; otherwise, create placeholder headers
    if headers is None:
        # Determine the number of columns by the first record
        num_columns = len(records[0])
        # Create a header row with placeholder attribute names
        headers = ['Attribute {}'.format(i+1) for i in range(num_columns)]
    
    # Generate the table using tabulate
    table = tabulate(records, headers=headers, tablefmt='grid')
    
    # Print the formatted table
    return table
