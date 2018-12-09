import sendgrid
import os


api_key = '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'
sg = sendgrid.SendGridAPIClient(apikey= api_key)

data ={
  "personalizations": [
    {
      "to": [
        {
          "email": "musyokaew@gmail.com",
          "name": "musyoka eric"
        }
      ],
      "dynamic_template_data": {
        "name": "Anthony Wang",
        "loc": "Nairobi",
        "con_email": "facebook.com",
        "orderHistory":[
         {
            "date":"2/1/2018",
            "item":"shoes"
         },
         {
            "date":"1/4/2017",
            "item":"hat"
         }
      ]
      }
    }
  ],
  "from": {
    "email": "wambua.eric01@gmail.com",
    "name": "Ciretech"
  },
  "reply_to": {
    "email": "wambua.eric@live.com",
    "name": "Eric musyoka"
  },
  "template_id": "d-eb1f9dd6ee984781bea8d4ab5347f45b"
}
response = sg.client.mail.send.post(request_body=data)
print("status code",response.status_code)
print("body: ",response.body)
print("headers: ",response.headers)