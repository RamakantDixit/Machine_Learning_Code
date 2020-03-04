import json
To_Email='ramakant@xyz.com'
CC_Email='rinku@xyz.com'
Subject_Email='Invocie details as below'
invoice_amount='$ 200'
invoice_date='12/03/2019'
invoice_number=2123341
NER_Result={
    "To_Email":To_Email,
    "CC_Email":CC_Email,
    "Subject_Email":Subject_Email,
    "Entity":
    {
       "invoice_amount":invoice_amount,
        "invoice_date":invoice_date,
        "invoice_number":invoice_number
    }
}
with open(r'C:\Users\Kanan\Desktop\Wipro Python Assement\NER_data.txt', 'w') as outfile:
    json.dump(NER_Result, outfile)