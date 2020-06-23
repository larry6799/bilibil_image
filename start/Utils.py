import time
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import logging
logging.basicConfig(level=logging.INFO,
                    filename='new.log',
                    filemode='w',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )
driver = webdriver.Chrome()


# create dir if it not exits
def create_file(filePath):
    if os.path.exists(filePath):
        logging.warning('%s: exists' % filePath)
    else:
        try:
            os.mkdir(filePath)
            logging.info('mkdir ：%s' % filePath)
        except Exception as e:
            os.makedirs(filePath)
            logging.error('mkdir multi：%s' % filePath)


# read urlList name row by row
def read_txt_name(rootdir):
    lines = []
    with open(rootdir, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    return lines


#  visit video image and screen 80 photos
def screen_img(url, save_path):
    try:
        driver.set_page_load_timeout(5)
        driver.get(url)
        time.sleep(3)
    except Exception :
        logging.error("timeout")

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[10]/div[2]/div[2]/div[3]/div[10]/button[1]').click()  # xpath定位成功后点击全屏
    logging.info('全屏成功')
    driver.find_element_by_class_name('bui-switch-input').click()
    logging.info('关闭弹幕成功')
    time.sleep(2)
    ActionChains(driver).send_keys(Keys.SPACE).perform()
    logging.info('播放视频')
    time.sleep(2)

    for i in range(0, 88):
        time.sleep(1)
        time1 = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        img_name = save_path + time1 + ".jpg"
        logging.info(img_name + " -- " + str(i))
        driver.save_screenshot(img_name)
        time.sleep(1)
    time.sleep(3)
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    logging.info(url, "end")