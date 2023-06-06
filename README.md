# MyInstagram

A Python application to edit profile data on your Instagram account and scrape data from other profiles.

## Features

- Edit your Instagram profile data:
  - Profile picture
  - Username
  - Name
  - Bio
  - External website
- Scrape data from other Instagram profiles:
  - Profile Picture
  - Bio

## How to Use

1. Download the files

2. Install the required Python packages. 
You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

3. Write your Python code. 
Here's an example of how you can use this application:

```python
from my_instagram import MyInstagram
from profile_scraper import scrape_profile

my_instagram = MyInstagram()
my_instagram.login('your_username', 'your_password', 'your_email')

# Now you can use the methods of the MyInstagram class
# For example, to change your bio, you can do:
my_instagram.update_bio('New bio')

# And to scrape data from an Instagram profile, you can do:
data = scrape_profile('another_username')
print(data)
```

Replace `'your_username'`, `'your_password'`, and `'your_email'` with your actual Instagram credentials, and `'another_username'` with the username of the Instagram profile you want to scrape data from.

4. Run your program. 
You can do this by running the following command in your terminal:

```bash
python main.py
```

## Disclaimer

Please note that using a script to log into your Instagram account and change account details might be against Instagram's terms of service. Always use this application responsibly and respect Instagram's rules and user privacy.
