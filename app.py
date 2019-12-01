from selenium import webdriver

browser = webdriver.Chrome('/Users/natepill/dev/webdriver-practice/chromedriver')


browser.get("https://www.youtube.com/watch?v=_uk_6vfqwTA")

more_actions_bt = browser.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/yt-icon-button")

# dropdown-trigger style-scope ytd-menu-renderer
print(more_actions_bt)
more_actions_bt.click()

# More actions
