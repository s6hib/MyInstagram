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
