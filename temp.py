from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException, NoSuchElementException, ElementNotInteractableException
from PIL import Image
import time
from selenium.webdriver.common.by import By
import base64
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument(r"--user-data-dir=C:\Users\USER\AppData\Local\Google\Chrome\User Data")
# options.add_argument("--profile-directory=Profile 2")
#
# # Add these arguments to fix the DevToolsActivePort issue
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-gpu")
# options.add_argument("--remote-debugging-port=9223")  # Specify a debugging port
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--disable-extensions")
#
# # Optional: Add these if you still have issues
# options.add_argument("--headless=new")  # Uncomment if you want headless mode
# options.add_argument("--disable-web-security")
#
# executable_path=r'C:\Users\Webdrivers\chromedriver.exe'
try:
    driver = webdriver.Chrome(options=options)
except SessionNotCreatedException as e:
    print("Session failed to start")
    exit()

link = "https://britishonlinearchives-com.ezproxy.rice.edu/collections/39/volumes/231/kenya-east-africa-protectorate-1901-1946?filters[query]=&filters[className]=document"
driver.get(link)

time.sleep(2)

username_field = driver.find_element(By.ID, value="username")
password_field = driver.find_element(By.ID, value="password")
login_btn = driver.find_element(By.NAME, value="_eventId_proceed")

username_field.send_keys("ak61")
password_field.send_keys("#832Maghili0912")
login_btn.click()

screenshot_path = "full_screenshot.png"
driver.save_screenshot(screenshot_path)


crop_box = (50, 100, 450, 400)

img = Image.open(screenshot_path)
cropped_img = img.crop(crop_box)

cropped_img_path = "cropped_screenshot.png"
cropped_img.save(cropped_img_path)

print(f"Cropped screenshot saved to {cropped_img_path}")
#
trials = 5
while True:
    try:
        success = driver.find_element(By.ID, value="push-success-label")
    except NoSuchElementException as e:
        trials -= 1
        time.sleep(7)
        if trials == 0:
            print("He no gree accept am!!")
            trials = 4
            break
        continue

# title_num = list(range(1838, 1846))
time.sleep(2)
while True:
    try:
        accept_cookies = driver.find_element(By.ID, value="cookie-confirm")
        accept_cookies.click()
    except NoSuchElementException:
        trials -= 1
        time.sleep(3)
        if trials == 0:
            print("Cookie button not found")
            trials = 4
            break
        continue
    except ElementNotInteractableException:
        driver.execute_script("arguments[0].click();", accept_cookies)
        break

books_id = list(range(3489, 3526))
for book_id in books_id:
    default = f"https://britishonlinearchives-com.ezproxy.rice.edu/documents/{book_id}/kenya-blue"
    driver.get(default)
    time.sleep(3)
    title = driver.find_element(By.XPATH, value="//h1[ contains(@class, 'c-masthead__title')]")
    title = title.text
    os.makedirs(title, exist_ok=True)
    num_of_pages = driver.find_element(By.CLASS_NAME, value="total").text
    limit = int(num_of_pages.split()[1])
    for i in range(0, limit):
        image_col = driver.find_element(By.XPATH, value=f'//div[@id="thumb-{i}"]//div[ contains(@class, "oneCol")]')
        image_col.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".openseadragon-canvas canvas"))
        )
        canvas = driver.find_element(By.CSS_SELECTOR, ".openseadragon-canvas canvas")
        # Get the base64 image data from the canvas
        image_base64 = driver.execute_script("""
            const canvas = document.querySelector(".openseadragon-canvas canvas");
            return canvas.toDataURL("image/png").substring("data:image/png;base64,".length);
        """)
        with open(f"{title}\\output{i}.png", "wb") as f:
            f.write(base64.b64decode(image_base64))

    # search_bar = driver.find_element(By.ID, value="search-query")
    # search_bar.send_keys(f"{default} {i}")
    # time.sleep(6)
#
# page_num = 1
# while True:
#     try:
#         # Find viewer element
#         viewer = driver.find_element(By.CLASS_NAME, "openseadragon-container")
#         location = viewer.location
#         size = viewer.size
#
#         # Take full screenshot
#         driver.save_screenshot("temp_full.png")
#
#         # Crop to viewer
#         im = Image.open("temp_full.png")
#         left = location["x"]
#         top = location["y"]
#         right = left + size["width"]
#         bottom = top + size["height"]
#         cropped_im = im.crop((left, top, right, bottom))
#
#         # Save cropped image
#         img_path = os.path.join(output_folder, f"page_{page_num:03}.png")
#         cropped_im.save(img_path)
#         print(f"Saved: {img_path}")
#         page_num += 1
#
#         # Click next
#         next_btn = driver.find_element(By.CLASS_NAME, "openseadragon-next")
#         next_btn.click()
#         time.sleep(2)
#     except Exception as e:
#         print("No more pages or error occurred:", e)
#         break
