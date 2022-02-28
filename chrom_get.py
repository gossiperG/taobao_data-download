"""this file is served as download_script of chromedriver"""

import requests
import os
import re



driver_url='https://registry.npmmirror.com/binary.html?path=chromedriver/'

re_result=requests.get(driver_url,allow_redirects=False).text

# result = re.compile(r'>(\\d.*?/)</a>').findall(re_result)
print(re_result)
# package_results=