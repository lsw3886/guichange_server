
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAQ7wC7ec:APA91bEUz5oX8bwnhcSKwYi2ESrKs2KBkdwhuA9NHyzYzsmaFROed3oPSuOHmsoeFMjtYq35NFZQ1VLbwnW-V54fKwWVC5hF0mt2QWwyf0AFBMOFaG5m0rWx7hUVVu65MQ_F9INDGOB0")



# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "f0PS6Foj9q0:APA91bHAHWB0GTpm4bEqnMHgA24HQ5WynKliUE7ksZKk2PcC4Rm0yVHjcd-2og2Kp4KgrYTGReOtbsW2y8bm6b4F1tY-X_UJdV6edsa5xKyN8WghieysBDhA0T5uVItnjBGWUJT3KsNT"
message_title = "Uber update"
message_body = "Hi john, your fucking news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

print (result)
 

