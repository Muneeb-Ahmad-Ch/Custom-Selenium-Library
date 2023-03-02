from utils import *

### Read Me ########################################
#   Code Created By : Muneeb Ahmad                 #
####################################################


def read_cookies(bot):
    # read cookies
    cookies = pickle.load(open(UTIL_PATH+"cookies.pkl", "rb"))
    for cookie in cookies:
        bot.driver.add_cookie(cookie)
    print('Cookies Read.')


def save_cookies(bot):
    # save cookies
    pickle.dump(bot.driver.get_cookies(), open(UTIL_PATH+"cookies.pkl", "wb"))
    print('Cookies Saved.')


class BOT ():
    running_status = False

    def __init__(self) -> None:
        pass

    def Start(self):
        print('...')
        # options = Options()
        options = uc.ChromeOptions()

        # options.headless=True
        # options.add_argument('--headless')
        # cur_path = pathlib.Path(__file__).parent.resolve()

        # options.add_argument("--incognito")
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # self.driver = webdriver.Chrome(options=options , executable_path='chromedriver.exe')
        # to get rid of save password popup

        options.add_argument("--password-store=basic")
        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
            },
        )
        self.driver = uc.Chrome(options=options, use_subprocess=True)

        self.wait = WebDriverWait(self.driver, 60)
        self.running_status = True

    def Stop(self):
        self.driver.quit()
        self.running_status = False

    def goto(self, url=BASE_URL):
        self.driver.get(url)
        sleep(2)

    # wait for methods
    def wait_css_selector(self, code):
        self.wait.until(
            ExpectedConditions.presence_of_element_located(
                (By.CSS_SELECTOR, code))
        )

    def wait_css_selectorTest(self, code):
        self.wait.until(
            ExpectedConditions.elementToBeClickable((By.CSS_SELECTOR, code))
        )

    def wait_xpath(self, code):
        self.wait.until(
            ExpectedConditions.presence_of_element_located((By.XPATH, code)))

    def check_exists_by_tagname(self, tagname):
        try:
            self.driver.find_element(By.TAG_NAME, tagname)
        except NoSuchElementException:
            return False
        return True

    def quit(self):
        self.driver.quit()
    # custom functions

    # def login(self):
    #     print('Going to login.')
    #     self.goto(BASE_URL)
    #     print('Login Done.')

    def scrap_items(self):
        pass

    def start_browser(self):
        self.Start()
        self.goto(BASE_URL)

    def __del__(self):
        self = None


if __name__ == '__main__':
    bot = BOT()
    bot.start_browser()
    bot.quit()
    bot = None
    print(bot == None)
    pass
