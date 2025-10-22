from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ✅ Đường dẫn tuyệt đối tới file chromedriver.exe (bạn giữ nguyên nếu đúng vị trí)
driver_path = r"C:\Users\Admin\Downloads\selenium_lab\chromedriver.exe"

# ✅ Cấu hình trình duyệt
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Giữ cửa sổ Chrome mở

# ✅ Khởi tạo ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# ✅ Mở trang login.html
driver.get("file:///C:/Users/Admin/Downloads/selenium_lab/login.html")
driver.maximize_window()

# ---- TEST CASE 1: Đăng nhập đúng ----
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login_btn = driver.find_element(By.ID, "btnLogin")

username.clear()
password.clear()
username.send_keys("sv1@ptit.edu.vn")
password.send_keys("P@ssw0rd")
login_btn.click()
time.sleep(2)
print("✅ Test 1 - Login success DONE")

# ---- TEST CASE 2: Sai mật khẩu ----
driver.refresh()
time.sleep(1)
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login_btn = driver.find_element(By.ID, "btnLogin")

username.clear()
password.clear()
username.send_keys("sv1@ptit.edu.vn")
password.send_keys("12345")
login_btn.click()
time.sleep(2)
print("✅ Test 2 - Wrong password DONE")

# ✅ Đóng trình duyệt
driver.quit()
