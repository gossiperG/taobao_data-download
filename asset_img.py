"""this file is served as convert img"""


import base64


icon_navi=open(r'.\asset\Navigation.png','rb')
icon_top=open(r'.\asset\top.png','rb')
icon=open(r'.\asset\logo.ico','rb')
js=open(r'.\token_dymatic\dynamicToken.js','rb')
navi_base64= base64.b64encode(icon_navi.read())
top_base64= base64.b64encode(icon_top.read())
icon_base64= base64.b64encode(icon.read())
js_base64= base64.b64encode(js.read())
icon_navi.close()
icon_top.close()
icon.close()
js.close()
write_navi='img_navi=%s'% navi_base64
write_top='img_top=%s'% top_base64
write_icon='img_icon=%s'% icon_base64
write_js='js_tk=%s'% js_base64

icon_file=open('icon.py','w+')
icon_file.write(write_navi+'\n')
icon_file.write(write_top+'\n')
icon_file.write(write_icon+'\n')
icon_file.write(write_js+'\n')

icon_file.close()