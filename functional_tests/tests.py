from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument('--headless')


class NewVisitorTest(LiveServerTestCase):  # eliminates the need for starting the test server also

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(desired_capabilities=chromeOptions.to_capabilities())

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_rowin_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title, f'Browser title was {self.browser.title}')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "Buy peacock feathers" into a text box (Edith's hobby is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits Enter, th epage updates, and now the page lists
        # '1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_rowin_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She enteres "Use peacock feathery to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_rowin_list_table('1: Buy peacock feathers')
        self.check_for_rowin_list_table('2: Use peacock feathers to make a fly')

        # Edith wonders whether the site will remember her list. Then she sees that the site has generated a unique URL
        # for her. There is some explanatory text to that effect.
        self.fail('Finish the test!')

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep
