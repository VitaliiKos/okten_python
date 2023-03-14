# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com
# (Хеш то що з ліва записувати не потрібно)
try:
    with open('emails.txt') as email_file, open('filtered_emails', 'a') as email_resul:
        counter = 1
        for line in email_file:
            if line.split()[-1].endswith('@gmail.com'):
                email_resul.writelines(f'{counter}. {line.split()[-1]}' + "\n")
                counter += 1
except Exception as error:
    print(error)
