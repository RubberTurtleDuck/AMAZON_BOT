import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib

target_price = 50.00
today = datetime.now().strftime("%H:%M")

if today == today:
    link = "https://www.amazon.com/Dual-Monitor-Stand-Adjustable-Mounting/dp/B0855ZBPXD/ref=sxin_15_pa_sp_search_" \
           "thematic_sspa?content-id=amzn1.sym.b5b80b36-fed9-4412-8be2-fe5bba09d25a%3Aamzn1.sym.b5b80b36-fed9-4412-" \
           "8be2-fe5bba09d25a&crid=1BWRH4NH1TH4B&cv_ct_cx=vesa+mount+dual+monitor&keywords=vesa+mount+dual+monitor&pd" \
           "_rd_i=B0855ZBPXD&pd_rd_r=1fcc7b7c-9593-4e42-a782-0f73b4b2f9ad&pd_rd_w=6Zt57&pd_rd_wg=lw6mO&pf_rd_p=b5b8" \
           "0b36-fed9-4412-8be2-fe5bba09d25a&pf_rd_r=RJETW7Q33XW1EFYP6J6P&qid=1667405711&qu=eyJxc2MiOiI0LjQxIiwicX" \
           "NhIjoiNC4xMCIsInFzcCI6IjMuNzkifQ%3D%3D&sprefix=vesa+mount%2Caps%2C235&sr=1-3-a73d1c8c-2fd2-4f19-aa41-2" \
           "df022bcb241-spons&psc=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/107.0.0.0 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    response = requests.get(url=link, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    current_price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])

    if current_price < target_price:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            my_email = "vladd.hagiu@gmail.com"
            password = "wvxczxvjbrsnyeku"
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject: Price drop!\n\nCheck out this link: {link}"
            )





