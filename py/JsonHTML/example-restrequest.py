import requests
from jsontohtmlform import JSONToHTMLForm 


def TestCase():
    jstest = '{      "id": 32,      "link": "https://www.target.com/p/funko-pop-games-pokemon-10-34-cubone/-/A-79641748#lnk=sametab",      "shipping_type": "Ship",      "wait_time": "1",      "crawl_queue": 4,      "vendor": 1,      "amount": 1,      "extra_settings": {"data": "s"},"status": 0,"desciption": "Cubone Pop Figure"}'
    jstest2 = '{      "id": 32,      "name": "John",      "age": 44,      "position": "Grunt"}'
    
    # Create the class instance.
    # JSONToHTMLForm(jsonstring, formName, htmlType)
    # htmlType can be 'html' or 'react'. If react, this creates a React Component.
    jsonhtml = JSONToHTMLForm(jstest, 'Crawl Setting', 'react')
    
    # Writes either an index.html or index.js, and a style.css  in a folder named after the formName you passed in previously. Give it a folder path to create the new folder and write the files to.
    jsonhtml.WriteFiles('D:\Projects\Apps\PythonScripts\py\JsonHTML')
    
    # Reload the class with a new json object or string, along with updating the form/component name.
    jsonhtml.ReloadNewJson(jstest2, 'Employee')
    jsonhtml.WriteFiles('D:\Projects\Apps\PythonScripts\py\JsonHTML')
    
    

if __name__ == '__main__':
    
    TestCase()