import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def web_scraper(website):
    print("launching chrome driver")

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print(f"Navigated to {website} successfully")
        html = driver.page_source
        return html
    finally:
        driver.quit()

def scrape_body(html):
    soup =BeautifulSoup(html, "html.parser")
    body_content = soup.body
    if body_content:
        return body_content.text
    else:
        return "No body content found"
    
def clean_body(body_text):
    soup =  BeautifulSoup(body_text, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_len=6000):
    return[
        dom_content[i : i + max_len]
        for i in range(0, len(dom_content), max_len)
    ]
    
