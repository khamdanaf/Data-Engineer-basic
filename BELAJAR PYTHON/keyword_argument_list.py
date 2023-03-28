# Belajar Keyword argument List
#membuat tag html yang di dalam ada text nya

def buat_html(teg, teks, href=''):
    htm = f"<{teg} href='{href}'>{teks}</{teg}>"
    return htm
htm = buat_html('p','halo sayang')
print(htm)
htm = buat_html('a', 'ini link!', href='www.google.com')
print(htm)
# <a href"">ini link!</a>
# dalam pemakaian keyword argument yaitu menggunakan bintang dua
#contoh **atributes keunggulannya bisa melakukan custom para meter
def create_html(tag, text ,**atribut):
    html = f"<{tag}>"
    for key, nilai in atribut.items():
        html = html + f"{key} = '{nilai}'"
    html = html +f">{text}</{tag}>"
    return html
html = create_html("p","halo sayang",info="Belajar")
print(html)
html = create_html("a", "ini link!", href="www.google.com", info="belajar python")
print(html)
html =create_html("div", "ini Div",info ="Pyton Program")
print(html)