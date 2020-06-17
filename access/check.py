from axe_selenium_python import Axe


class AxeEngine:

    def __init__(self):
        pass

    @staticmethod
    def inject_all(driver, timestamp, file_name, site):
        """
        This method inject axe js into website and scans it against all accessibility tags
        https://github.com/dequelabs/axe-core/blob/a5ebc936a53bf8a716fed35fe7ec72b2436eab8e/doc/API.md
        :param driver: webdriver
        :param timestamp: timestamp of current scan YYYY-MM-DD
        :param file_name: file name where to save results
        :param site: url to scan
        :return:
        """
        axe = Axe(driver)
        axe.inject()
        results = axe.run()
        f = open(f"accessibility_results/{timestamp}_all/" + file_name.replace("/", "_"), "w", encoding="utf-8")
        f.write(site + "\n")
        f.write(axe.report(results["violations"]))
        f.close()

    @staticmethod
    def inject_wcag2a(driver, timestamp, file_name, site):
        """
        This method inject axe js into website and scans it against wcag2a rule
        :param driver: webdriver
        :param timestamp: timestamp of current scan YYYY-MM-DD
        :param file_name: file name where to save results
        :param site: url to scan
        :return:
        """
        options = """
        {
        runOnly: {
            type: 'tag',
            values: ['wcag2a']
            }
        }"""
        axe = Axe(driver)
        axe.inject()
        results = axe.run(context=None, options=options)
        f = open(f"accessibility_results/{timestamp}_wcag2a/" + file_name.replace("/", "_"), "w", encoding="utf-8")
        f.write(site + "\n")
        f.write(axe.report(results["violations"]))
        f.close()

    @staticmethod
    def inject_wcag2aa(driver, timestamp, file_name, site):
        """
        This method inject axe js into website and scans it against wcag2aa rule
        :param driver: webdriver
        :param timestamp: timestamp of current scan YYYY-MM-DD
        :param file_name: file name where to save results
        :param site: url to scan
        :return:
        """
        options = """
            {
            runOnly: {
                type: 'tag',
                values: ['wcag2aa']
                }
            }"""
        axe = Axe(driver)
        axe.inject()
        results = axe.run(context=None, options=options)
        f = open(f"accessibility_results/{timestamp}_wcag2aa/" + file_name.replace("/", "_"), "w", encoding="utf-8")
        f.write(site + "\n")
        f.write(axe.report(results["violations"]))
        f.close()
