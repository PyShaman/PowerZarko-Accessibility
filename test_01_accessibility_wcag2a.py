import datetime
import unittest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from access.check import AxeEngine
from sites import *

timestamp = str(datetime.datetime.now().isoformat()).replace(":", "-")[:10]


class TestAccessibilityWCAGOnly(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--enable-popup-blocking")
        options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    @classmethod
    def tearDownClass(cls):
        driver.quit()

    @staticmethod
    def test_01_prepare_directory():
        """
        This test creates bunch of directories to store data from scan
        :return:
        """
        try:
            os.mkdir(f"accessibility_results/{timestamp}_wcag2a")
            os.mkdir(f"accessibility_results/{timestamp}_wcag2aa")
            os.mkdir(f"accessibility_results/{timestamp}_all")
        except OSError:
            print(f"Creation of the directory {timestamp} failed")
        else:
            print(f"Successfully created the directory {timestamp}")

    @staticmethod
    def test_02_test_wcag2a():
        ae = AxeEngine()
        for site in SITES:
            site_name = site[23:].replace(".html", "")
            driver.get(site)
            ae.inject_wcag2a(driver, timestamp, f"{site_name}.txt", site)

    @staticmethod
    def test_02_test_wcag2aa():
        ae = AxeEngine()
        for site in SITES:
            site_name = site[23:].replace(".html", "")
            driver.get(site)
            ae.inject_wcag2aa(driver, timestamp, f"{site_name}.txt", site)

    @staticmethod
    def test_02_test_all():
        ae = AxeEngine()
        for site in SITES:
            site_name = site[23:].replace(".html", "")
            driver.get(site)
            ae.inject_all(driver, timestamp, f"{site_name}.txt", site)


if __name__ == "__main__":
    unittest.main(warnings="ignore")
