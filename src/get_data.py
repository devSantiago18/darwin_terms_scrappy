"""
    This module has the function of downloading the html content of the necessary pages
"""
import urllib.request

NAMES = ('./resources/pages/list_history.html', './resources/pages/quick_reference.html')


def update_html_docs():
    document = urllib.request.urlopen("https://dwc.tdwg.org/list/").read().decode()
    quick_reference = urllib.request.urlopen("https://dwc.tdwg.org/terms/").read().decode()
    #print(document)
    return (document, quick_reference)

def save_html_docs(*docs):
	list_historyc , quick_reference = docs
	with open(NAMES[0], 'w') as file:
		file.write(list_historyc)
	with open(NAMES[1], 'w') as file:
		file.write(quick_reference)
  
  
def get_data_html(flat_update: bool = False):
    if flat_update:
        save_html_docs(*update_html_docs())
    html = open(NAMES[0], 'r').read()
    quick_reference_html = open(NAMES[1], 'r').read()
    return (html, quick_reference_html)
