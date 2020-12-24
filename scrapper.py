from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support     import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from progress.bar import Bar
import re


PATH = "chromedriver.exe"
chromeOptions = Options()
chromeOptions.headless = True
driver  = webdriver.Chrome(PATH, options=chromeOptions)
#driver  = webdriver.Chrome(PATH)
driver.get("https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm")

driver.find_element_by_xpath("/html/body/p/table/tbody/tr[2]/td[1]/table/tbody/tr[4]").click()
driver.implicitly_wait(5)


driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/select/option[28]").click()
driver.find_element_by_xpath("//input[@type = 'submit']").click()
driver.implicitly_wait(5)

table = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody")
#rows = table.find_elements_by_tag_name("td")
row = table.find_elements_by_tag_name("tr")
row.pop(0)
#f = open("test1.txt", "a", encoding="utf-8")
l = []
s = ""
with Bar('extracting', max=len(row)) as bar:
    for text in row:
        t = text.text
        x = re.findall(".\...", t)[0]
        s += t[0:t.index(x) + 4] + '|' 
        s += t[t.index(x) + 5 :t.index('Fall/Winter 2020-2021 Course Schedule') - 1] + '|'
        a = text.find_element_by_tag_name("a").get_attribute('href')
        s += a + '\n'
        l.append(s) 
        bar.next()
        s = ""
        if len(l) == 50:
            break
f=open('pre.txt','w', encoding="utf-8")   
for line in l:
    a = re.split("\|", line)
    driver.get(a[2])
    #driver.implicitly_wait(5)
    text = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/p[3]").text
    q = re.findall("Prerequisite*", text)
    if q: 
     f.write( a[0] + "|" + a[1] + "|" + text[text.index(q[0]):] + '\n')
    else:
        f.write(a[0] + "|" + a[1] + "|" +"n/a" + '\n')    
f.close()
f=open('output.txt','w', encoding="utf-8")
with Bar('writing', max=len(l)) as bar:
    for element in l:
        f.write(element)
        bar.next()
    f.close()



# with Bar('extracting', max=len(rows)) as bar:
#     for i in rows:
#         t = i.text
#         if t.find("Course Schedule") == -1 and  t != ""  and t != "Click on Schedule to see details": ## does not contain
#             f.write(t + '|')
#         elif t != "" and t.find("Course Schedule") != -1 and t != "Click on Schedule to see details":
#             a = i.find_element_by_tag_name("a").get_attribute('href')
#             f.write(a + '\n')  
#         bar.next()
#     f.close()