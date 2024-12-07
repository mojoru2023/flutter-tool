#! -*- coding:utf-8 -*-

# 2024.8.3

# 近一个月，日经回调明显，日银加息，重新把目光拉回交易市场，
# 期权以小博大的优势还是很明显，另外是否有套利的可能？ 所以现在想每天重新收集期权的数据
# 然后再做一个对比，每个月多一个20也是不错的，哪怕只有10 也是可以，这个也只有数据积累到一定数量
# 想法才能真出现
# 数据源1： https://svc.qri.jp/jpx/nkopm/1
# 数据源2：https://fu.minkabu.jp/chart/nk225_option

# 因为要统计最高，最低，同时作图，所以优先第二个数据源，整理好，直接用pandas插入数据库
# 积累到一定阶段之后就 用mplfinance 作图进行分析

import requests
from bs4 import BeautifulSoup
from datetime import datetime

import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver

from tqdm import tqdm
import time

# # 使用tqdm展示进度条
# for i in tqdm(range(1, 1200)):
#     # 模拟一些处理时间
#     time.sleep(0.01)

#
import uuid


class BS4Parse():
    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def parseOneElement(self, tagName):
        trans_list = []
        for single_tag in self.soup.select(tagName):
            trans_list.append(" ".join(single_tag.text.split()))
        tagText = " ".join(trans_list)
        return tagText, trans_list

    def parseClassAttribute(self, outsidetag, classAttribute):
        trans_list = []
        ret = self.soup.findAll(name=outsidetag, attrs={"class": classAttribute})

        for item in ret:
            trans_list.append("".join(item.text))
        tagText = " ".join(trans_list)
        return tagText, trans_list

    def parseIDAttribute(self, DAttribute):
        trans_list = []
        ret = self.soup.findAll(id=DAttribute)

        for item in ret:
            trans_list.append("".join(item.text))
        tagText = " ".join(trans_list)
        return tagText, trans_list

    def fetchAllText(self):
        AllText = "".join(self.soup.get_text().split())
        return AllText




driver = webdriver.Chrome()


# 把find_elements 改为　find_element
def fetch_data(url):
    driver.get(url)

    html = driver.page_source
    time.sleep(5)
    return html






def write_to_txt(txt_name,list_item):
    for item in list_item:
        # 打开文件，以追加模式 ('a') 写入
        with open(txt_name, 'a', encoding='utf-8') as file:
            file.write(item)







if __name__ == '__main__':
    url_list = ["https://flutter.ducafecat.com/pubs/splash-screen-packages","https://flutter.ducafecat.com/pubs/onboarding-carousel-packages","https://flutter.ducafecat.com/pubs/feature-discovery-coach-marks-packages","https://flutter.ducafecat.com/pubs/authentication-packages","https://flutter.ducafecat.com/pubs/biometric-local-auth-packages","https://flutter.ducafecat.com/pubs/pin-password-field-packages","https://flutter.ducafecat.com/pubs/feedback-packages","https://flutter.ducafecat.com/pubs/app-update-packages","https://flutter.ducafecat.com/pubs/chatgpt-llm-genai-packages","https://flutter.ducafecat.com/pubs/ar-vr-packages","https://flutter.ducafecat.com/pubs/machine-learning-packages","https://flutter.ducafecat.com/pubs/ai-voice-assistant-packages","https://flutter.ducafecat.com/pubs/3d-packages","https://flutter.ducafecat.com/pubs/game-development-packages","https://flutter.ducafecat.com/pubs/geolocation-maps-packages","https://flutter.ducafecat.com/pubs/ad-serving-packages","https://flutter.ducafecat.com/pubs/analytics-consumer-insights-packages","https://flutter.ducafecat.com/pubs/health-fitness-packages","https://flutter.ducafecat.com/pubs/cryptography-security-permissions-packages","https://flutter.ducafecat.com/pubs/localization-internationalization-packages","https://flutter.ducafecat.com/pubs/sql-database-packages","https://flutter.ducafecat.com/pubs/nosql-database-packages","https://flutter.ducafecat.com/pubs/database-adapter-packages","https://flutter.ducafecat.com/pubs/cloud-storage-database-packages","https://flutter.ducafecat.com/pubs/cache-temporary-storage-packages","https://flutter.ducafecat.com/pubs/graph-query-language-packages","https://flutter.ducafecat.com/pubs/qr-code-bar-code-packages","https://flutter.ducafecat.com/pubs/document-scanner-packages","https://flutter.ducafecat.com/pubs/pdf-packages","https://flutter.ducafecat.com/pubs/printing-packages","https://flutter.ducafecat.com/pubs/design-system-packages","https://flutter.ducafecat.com/pubs/light-mode-dark-mode-themes-packages","https://flutter.ducafecat.com/pubs/widget-library-ui-framework-packages","https://flutter.ducafecat.com/pubs/responsive-ui-packages","https://flutter.ducafecat.com/pubs/neumorphic-ui-packages","https://flutter.ducafecat.com/pubs/glassmorphic-ui-packages","https://flutter.ducafecat.com/pubs/liquid-squishy-ui-packages","https://flutter.ducafecat.com/pubs/dual-screen-folding-device-ui-packages","https://flutter.ducafecat.com/pubs/color-picker-utilities-packages","https://flutter.ducafecat.com/pubs/wifi-iot-packages","https://flutter.ducafecat.com/pubs/sensors-packages","https://flutter.ducafecat.com/pubs/bluetooth-nfc-beacon-packages","https://flutter.ducafecat.com/pubs/network-connectivity-status-packages","https://flutter.ducafecat.com/pubs/http-client-utilities-packages","https://flutter.ducafecat.com/pubs/websocket-packages","https://flutter.ducafecat.com/pubs/openapi-packages","https://flutter.ducafecat.com/pubs/api-packages","https://flutter.ducafecat.com/pubs/dio-packages","https://flutter.ducafecat.com/pubs/chat-packages","https://flutter.ducafecat.com/pubs/sms-packages","https://flutter.ducafecat.com/pubs/messaging-push-notification-packages","https://flutter.ducafecat.com/pubs/real-time-communication-packages","https://flutter.ducafecat.com/pubs/social-media-packages","https://flutter.ducafecat.com/pubs/avatar-profile-picture-chat-heads-packages","https://flutter.ducafecat.com/pubs/image-packages","https://flutter.ducafecat.com/pubs/video-packages","https://flutter.ducafecat.com/pubs/camera-packages","https://flutter.ducafecat.com/pubs/audio-packages","https://flutter.ducafecat.com/pubs/picture-in-picture-packages","https://flutter.ducafecat.com/pubs/carousel-cover-flow-packages","https://flutter.ducafecat.com/pubs/story-view-packages","https://flutter.ducafecat.com/pubs/tinder-swipe-cards-packages","https://flutter.ducafecat.com/pubs/placeholder-packages","https://flutter.ducafecat.com/pubs/crop-image-packages","https://flutter.ducafecat.com/pubs/edit-save-compress-multimedia-packages","https://flutter.ducafecat.com/pubs/multimedia-utilities-packages","https://flutter.ducafecat.com/pubs/routing-packages","https://flutter.ducafecat.com/pubs/deep-linking-packages","https://flutter.ducafecat.com/pubs/app-bar-action-bar-packages","https://flutter.ducafecat.com/pubs/drawer-packages","https://flutter.ducafecat.com/pubs/menu-packages","https://flutter.ducafecat.com/pubs/tab-packages","https://flutter.ducafecat.com/pubs/bottom-navigation-bar-packages","https://flutter.ducafecat.com/pubs/search-bar-apis-utilities-packages","https://flutter.ducafecat.com/pubs/sharing-intent-packages","https://flutter.ducafecat.com/pubs/status-bar-packages","https://flutter.ducafecat.com/pubs/badge-packages","https://flutter.ducafecat.com/pubs/notification-toast-packages","https://flutter.ducafecat.com/pubs/indicators-loading-refresh-progress-packages","https://flutter.ducafecat.com/pubs/card-expansion-tile-packages","https://flutter.ducafecat.com/pubs/dialogs-packages","https://flutter.ducafecat.com/pubs/webview-packages","https://flutter.ducafecat.com/pubs/header-packages","https://flutter.ducafecat.com/pubs/bottom-panels-bottomsheets-packages","https://flutter.ducafecat.com/pubs/floating-action-button-packages","https://flutter.ducafecat.com/pubs/table-packages","https://flutter.ducafecat.com/pubs/widget-generation-rendering-packages","https://flutter.ducafecat.com/pubs/widget-extension-packages","https://flutter.ducafecat.com/pubs/scrollable-scrollview-scrollbar-packages","https://flutter.ducafecat.com/pubs/list-packages","https://flutter.ducafecat.com/pubs/pagination-lazy-loading-packages","https://flutter.ducafecat.com/pubs/timeline-packages","https://flutter.ducafecat.com/pubs/grid-packages","https://flutter.ducafecat.com/pubs/tree-view-packages","https://flutter.ducafecat.com/pubs/settings-ui-packages","https://flutter.ducafecat.com/pubs/form-packages","https://flutter.ducafecat.com/pubs/stepper-packages","https://flutter.ducafecat.com/pubs/checkbox-radio-button-packages","https://flutter.ducafecat.com/pubs/dropdown-packages","https://flutter.ducafecat.com/pubs/spin-box-packages","https://flutter.ducafecat.com/pubs/button-progress-button-packages","https://flutter.ducafecat.com/pubs/chip-tag-packages","https://flutter.ducafecat.com/pubs/switch-packages","https://flutter.ducafecat.com/pubs/slider-packages","https://flutter.ducafecat.com/pubs/country-country-code-picker-packages","https://flutter.ducafecat.com/pubs/file-picker-packages","https://flutter.ducafecat.com/pubs/multimedia-picker-packages","https://flutter.ducafecat.com/pubs/contact-picker-packages","https://flutter.ducafecat.com/pubs/location-place-address-picker-packages","https://flutter.ducafecat.com/pubs/generic-picker-packages","https://flutter.ducafecat.com/pubs/date-time-picker-packages","https://flutter.ducafecat.com/pubs/icons-packages","https://flutter.ducafecat.com/pubs/fonts-packages","https://flutter.ducafecat.com/pubs/emoji-rich-text-packages","https://flutter.ducafecat.com/pubs/text-decoration-effect-animation-packages","https://flutter.ducafecat.com/pubs/editor-syntax-highlighter-packages","https://flutter.ducafecat.com/pubs/autoformat-masking-validation-packages","https://flutter.ducafecat.com/pubs/autocomplete-packages","https://flutter.ducafecat.com/pubs/parsing-other-utilities-packages","https://flutter.ducafecat.com/pubs/keyboard-packages","https://flutter.ducafecat.com/pubs/stopwatch-timer-countdown-packages","https://flutter.ducafecat.com/pubs/clock-packages","https://flutter.ducafecat.com/pubs/calendar-packages","https://flutter.ducafecat.com/pubs/date-time-utilities-packages","https://flutter.ducafecat.com/pubs/shapes-path-packages","https://flutter.ducafecat.com/pubs/animation-transition-packages","https://flutter.ducafecat.com/pubs/effects-gradients-shaders-packages","https://flutter.ducafecat.com/pubs/clipper-decoration-packages","https://flutter.ducafecat.com/pubs/plots-visualization-packages","https://flutter.ducafecat.com/pubs/drawing-painting-signature-packages","https://flutter.ducafecat.com/pubs/touch-gesture-packages","https://flutter.ducafecat.com/pubs/layout-overlay-packages","https://flutter.ducafecat.com/pubs/packaging-publishing-packages","https://flutter.ducafecat.com/pubs/storybook-packages","https://flutter.ducafecat.com/pubs/device-preview-screenshot-packages","https://flutter.ducafecat.com/pubs/linter-packages","https://flutter.ducafecat.com/pubs/testing-packages","https://flutter.ducafecat.com/pubs/debugging-logging-packages","https://flutter.ducafecat.com/pubs/performance-crash-insights-packages","https://flutter.ducafecat.com/pubs/code-generator-serialization-packages","https://flutter.ducafecat.com/pubs/language-extension-enhancement-packages","https://flutter.ducafecat.com/pubs/state-management-packages","https://flutter.ducafecat.com/pubs/flutter-framework-packages","https://flutter.ducafecat.com/pubs/hooks-packages","https://flutter.ducafecat.com/pubs/web-server-packages","https://flutter.ducafecat.com/pubs/firebase-packages","https://flutter.ducafecat.com/pubs/aws-packages","https://flutter.ducafecat.com/pubs/payment-api-sdk-packages","https://flutter.ducafecat.com/pubs/web3-crypto-blockchain-packages","https://flutter.ducafecat.com/pubs/credit-card-ui-scanner-packages","https://flutter.ducafecat.com/pubs/games-rewards-packages","https://flutter.ducafecat.com/pubs/json-packages","https://flutter.ducafecat.com/pubs/xml-json-other-interchange-formats-packages","https://flutter.ducafecat.com/pubs/ods-xlsx-sheets-packages","https://flutter.ducafecat.com/pubs/markdown-packages","https://flutter.ducafecat.com/pubs/html-css-packages","https://flutter.ducafecat.com/pubs/epub-packages","https://flutter.ducafecat.com/pubs/javascript-packages","https://flutter.ducafecat.com/pubs/compressed-files-packages","https://flutter.ducafecat.com/pubs/odt-doc-docx-packages","https://flutter.ducafecat.com/pubs/latex-packages","https://flutter.ducafecat.com/pubs/cli-packages","https://flutter.ducafecat.com/pubs/windows-packages","https://flutter.ducafecat.com/pubs/web-packages","https://flutter.ducafecat.com/pubs/android-ios-packages","https://flutter.ducafecat.com/pubs/tv-watch-car-packages","https://flutter.ducafecat.com/pubs/iot-hardware-packages","https://flutter.ducafecat.com/pubs/device-utilities-packages","https://flutter.ducafecat.com/pubs/package-utilities-packages","https://flutter.ducafecat.com/pubs/geolocation-utilities-packages","https://flutter.ducafecat.com/pubs/math-utilities-packages","https://flutter.ducafecat.com/pubs/file-folder-path-util-packages","https://flutter.ducafecat.com"]
    for url in url_list:
        try:

            html_doc = fetch_data(url)
            input_items = []
            element = etree.HTML(html_doc)

            theme_title = element.xpath('//*[@id="__nuxt"]/div/div/div/div/section[2]/h2/text()')
            input_items.append(theme_title[0])
            theme_info = element.xpath('//*[@id="__nuxt"]/div/div/div/div/section[2]/p/text()')
            input_items.append(theme_info[0])
            case_title = element.xpath('//*[@id="__nuxt"]/div/div/div/div/section[2]/div[1]/div/a[1]/div/p[1]/text()')
            case_description = element.xpath('//*[@id="__nuxt"]/div/div/div/div/section[2]/div[1]/div/a[1]/p/text()')

            case_url = element.xpath('//*[@id="__nuxt"]/div/div/div/div/section[2]/div[1]/div/a[2]/@href')
            if len(case_url) == 0:
                print(url)
                break
            for i1,i2,i3 in zip(case_title,case_description,case_url):
                input_items.append(i1)
                input_items.append("\n")
                input_items.append(i2)
                input_items.append("\n")
                input_items.append("https://flutter.ducafecat.com" + i3)
                input_items.append("\n")
            write_to_txt("flutter.txt",input_items)
        except:
            print(url)




