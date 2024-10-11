
from playwright.sync_api import sync_playwright
from unidecode import unidecode
import requests
import os


def download_image(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"Image saved at {save_path}")
        else:
            print(f"Failed to download {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


def scrape_signs(page_URL):
    with sync_playwright() as sync_p:
        browser = sync_p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(page_URL)
        page.wait_for_load_state('networkidle')
        section_counter = page.locator('body main div.container div[data-sentry-component=\'RoadsignChapter\']')
        img_counter = 0
        for img_section in range(1,section_counter.count()):
            page.click(f'body main div.container div[data-sentry-component=\'RoadsignChapter\']:nth-child({img_section})')
            page.wait_for_timeout(500)
            sign_counter = page.locator('body main div[data-sentry-component=\'Roadsign\']')
            for sign in range(1, sign_counter.count()):
                sign_name = unidecode(page.locator(f'body main div[data-sentry-component=\'Roadsign\']:nth-child({sign}) h3').text_content()).replace(' ', '_').replace('/','')
                image = page.query_selector(f'body main div[data-sentry-component=\'Roadsign\']:nth-child({sign}) a div img')
                if image != None:
                    image_url = image.get_attribute('src')
                    if image_url:
                        img_name = f'{sign_name}.png'
                        save_path = os.path.join('dataset/images', img_name)
                        download_image(image_url, save_path)
                        img_counter += 1
            page.goto(page_URL)
        print(img_counter)

scrape_signs('https://soferonline.ro/indicatoare-si-marcaje-rutiere-semne-de-circulatie-pe-capitole/')