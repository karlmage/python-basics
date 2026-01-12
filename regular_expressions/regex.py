import re

text_sample = '''
Hello!

My name is John Doe, and I was born on 1992-07-15.
You can reach me at john.doe@example.com or at j.doe99@work-mail.co.uk.
My backup email is: John_Doe123@GMAIL.com

Phone numbers:
- Office: +1-202-555-0147
- Home: (202) 555 0198
- Mobile: 202.555.0183

Important dates:
- Project started: 01/03/2024
- Deadline: March 15, 2025
- Last update: 2025-01-08 14:32:09

Websites:
- https://www.example.com
- http://sub.domain.org/path?query=123
- www.test-site.net

Order details:
Order ID: ORD-98347
Customer ID: CUST_00421
Product code: PRD-A9X-77
Price: $149.99
Discounted price: €129,50
Quantity: 3 items

Addresses:
123 Main Street, Apt #5B
New York, NY 10001
USA

Random text:
  extra   spaces   here
Tabs	are	here
Special characters: !@#$%^&*()_+-=[]{}|;':",./<>?

End of file.
'''

email_pattern = re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z.-]+\.(([a-zA-Z.-]+\.)+)?(com|edu|net|uk)')
web_pattern = re.compile(r'(https?://)?(www\.|sub\.)?([a-zA-Z0-9._-]+)\.([a-z]+)(/.+\S)?')

email_matches = email_pattern.finditer(text_sample)
web_matches = web_pattern.finditer(text_sample[385:])

# count = 0
# for match in web_matches:
#     count += 1
#     print(f'{match.group(3)}.{match.group(4)}')
# print(count)

sub_urls = web_pattern.sub(r'\3.\4', text_sample[383:467])
print(sub_urls)