mails=["abc@aa.com","ssss.com","sss@rerrr.com"]
#valid_mails = [mail for mail in mails if "@" in mail]

#print(valid_mails)

for mail in mails:
    if "@" in mail:
        print(mail)