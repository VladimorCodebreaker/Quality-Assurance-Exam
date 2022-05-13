import time
import unittest
from selenium import webdriver

class Infinite_Scroll(unittest.TestCase):

    """http://the-internet.herokuapp.com/infinite_scroll"""
    
    def setUp(self):
        self.driver = webdriver.Safari()
        self.base_url = ("http://the-internet.herokuapp.com/infinite_scroll")
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        time.sleep(3)
        self.assertIn(self.base_url, self.driver.current_url)
        self.timeout = 1

    def test_infinite_scroll(self):
        "infinite_scroll"
        driver = self.driver
        scroll_pause_time = self.timeout
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                self.assertEquals(new_height, last_height)
                break
            last_height = new_height
        driver.save_screenshot("infinite_scroll.png")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(
    )