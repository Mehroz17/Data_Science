from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By
import  time
p = "C:\Program Files (x86)\chromedriver.exe"
facbook = webdriver.Chrome(p)

def openPage():
    facbook.get("https://www.facebook.com/login/")


def enter_Roll_reg(email,passw):
    em = facbook.find_element(By.ID,"email")
    em.send_keys(email)
    passwe = facbook.find_element(By.ID,"pass")
    passwe.send_keys(passw)
    btn = facbook.find_element(By.ID,"loginbutton")
    btn.send_keys(Keys.RETURN)
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")


def logout():
    pass
""" 
   lb = facbook.find_element(By.CSS_SELECTOR,"#mount_0_0_Gz > div > div:nth-child(1) > div > div:nth-child(4) > div.l38y3qj3.ekq1a7f9.khm9p5p9.lcfup58g.r227ecj6.on4d8346 > div.g4tp4svg.om3e55n1.k3q8kl47.ov4vj3he.alzwoclg.i85zmo3j > span > div > div.qi72231t.n3hqoq4p.r86q59rh.b3qcqh3k.fq87ekyn.fsf7x5fv.s5oniofx.m8h3af8h.l7ghb35v.kjdc1dyq.kmwttqpk.cr00lzj9.rn8ck1ys.s3jn8y49.f14ij5to.l3ldwz01.icdlwmnq.i85zmo3j.qmqpeqxj.e7u6y3za.qwcclf47.nmlomj2f.frfouenu.bonavkto.djs4p424.r7bn319e.bdao358l.alzwoclg.jcxyg2ei.srn514ro.oxkhqvkx.rl78xhln.nch0832m.om3e55n1.nq2b4knc.bis24fgy.a5wdgl2o > svg")
    lb.click()
    print("first E")
    lbtn = facbook.find_element(By.LINK_TEXT,"//span[@class='_54nh'][contains(.,'Log Out')]") #//span[@class='_54nh'][contains(.,'Log Out')]
    lbtn.click()
    facbook.quit()"""




# main()
def main():
    openPage()
    enter_Roll_reg("m_rose_786@hotmail.com","4/1/2022PM547")
    time.sleep(10)
    logout()