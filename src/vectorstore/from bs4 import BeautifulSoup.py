from bs4 import BeautifulSoup
import requests

content = """<html>
 <body>
  <p>
   Some
   <b>
    bad
    <i>
     HTML
    </i>
   </b>
  </p>
 </body>
</html>
"""
response = requests.get(content)
html_content = response.text


soup = BeautifulSoup(html_content, 'html.parser')
text = soup.get_text()