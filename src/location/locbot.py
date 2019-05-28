









# import os
#
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))
#
#
# def locations(self):
#     self.write_log('Starting location bot...')
#
#     # Webdriver
#     driver = webdriver.Firefox()
#     driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
#     self.write_log('Location Bot is trying login...')
#     while True:
#         try:
#             login_form = driver.find_element_by_xpath("//input[@aria-label='Phone number, username, or email']")
#             password_form = driver.find_element_by_xpath("//input[@aria-label='Password']")
#             break
#         except:
#             pass
#
#     # Trying to sign in on Instagram
#     try:
#         login_form.send_keys(os.environ.get('LOGIN', ''))
#         password_form.send_keys(os.environ.get('PASSWORD', ''))
#         driver.find_element_by_class_name('_0mzm-.sqdOP.L3NKy').click()
#         self.write_log('Location Bot login success!')
#     except:
#         self.write_log('ERROR: Login or Password is invalid! Exiting bot..')
#         return False
#
#     # All times that the Firefox open and the bot sign in the Instagram
#     # it'll ask if you want to turn on the notifications.
#     while True:
#         try:
#             driver.find_element_by_class_name('aOOlW.HoLwm').click()
#             break
#         except:
#             pass
#
#     locations_list = format_csv('Limite_Bairro.csv', 1, 1, 'Rio de Janeiro', 'Brazil')
#
#     for location in locations_list:
#         if 'https://www.instagram.com/' == driver.current_url:
#             search_field = driver.find_element_by_class_name('XTCLo.x3qfX')
#             search_field.send_keys(location)
#             while 'https://www.instagram.com/' == driver.current_url:
#                 search_field.send_keys(Keys.RETURN)
#
#         url = driver.current_url
#         url = url.split('/')
#         location_id = url[5]
#
#         driver.get('https://www.instagram.com/')
