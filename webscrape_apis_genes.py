from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
driver = webdriver.Firefox(executable_path=r'geckodriver-v0.31.0-linux64/geckodriver')

dfs = []
for i in range(1,104):
    url = "https://www.genscript.com/gene/7460/honey-bee-apis-mellifera?page="+str(i)
    driver.get(url)
    driver.implicitly_wait(5)
    soup = BeautifulSoup(driver.page_source,'lxml')
    tables = soup.find_all('table')
    df1 = pd.read_html(str(tables))
    df2 = pd.DataFrame(df1[0])
    dfs.append(df2)

combined = pd.concat(dfs)
combined.reset_index(inplace=True)
combined.drop("index", inplace=True, axis=1)
combined.to_csv("genes_to_fullname.csv", sep=",", index=False)
