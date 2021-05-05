# Description

Turn a JSON string into either a plain HTML form or a ReactJS component complete with states and a hooked up submit button that returns the form data to the parent.

Currently only a Python class, but a cpp and javascript class will be added soon.

## Creates:

- HTML Form
- ReactJS component

# Quick Start

### Python:

Clone the `py.JsonHTML` folder to your app, or rename it to whatever you want, just make sure you update the import statement in this example.

#### Simple Usage:

```python
from JsonHTML.jsontohtmlform import JSONToHTMLForm 

jstest = '{      "id": 32,      "link": "https://www.target.com/p/funko-pop-games-pokemon-10-34-cubone/-/A-79641748#lnk=sametab",      "shipping_type": "Ship",      "wait_time": "1",      "crawl_queue": 4,      "vendor": 1,      "amount": 1,      "status": 0,"desciption": "Cubone Pop Figure"}'

jstest2 = '{      "id": 32,      "name": "John",      "age": 44,      "position": "Grunt"}'

def TestCase():
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

```



# Functions:

- `JSONToHTMLForm(jsonstring, formName, htmlType)`
  - Init the class.
  - **jsonstring** - A JSON string. No nested `dicts` please!
  - **formName** - The name of the resulting form/component and directory.
  - **htmlType** - Can be 'html' or 'react'. If react, this creates a React Component.
- `WriteFiles(dirpath)`
  - Writes either an index.html or index.js, and a style.css  in a folder named after the formName you passed in previously. Give it a folder path to create the new folder and write the files to.
  - **dirpath** - The directory to create the new folder and write the files to.
- `ReloadNewJson(jsonn, formname)`
  - Reload the class with a new json object or string, along with updating the form/component name.
  - **jsonstring** - A JSON string. No nested `dicts` please!
  - **formName** - The name of the resulting form/component and directory.



# React Component:

The react component uses a template which can be updated to suit your pipeline needs. This template can be found in `py\reactcomponentcssTemplate.js`

## React Component Usage:

Pass a function to the `Submit` prop of the component to create a callback with the form's details and use it down the line in your app.

```react
// Generated component:
import User_Info from "./User_Info/index";

export default function App() {
  return (
    <div className="App">

      <User_Info Submit={(e) => console.log(e)} />
      
    </div>
  );
}

```



# Problems:

- Nested `dicts` along with arrays don't work, only plain numbers and text.

# Roadmap:

- CPP class
- Javascript class
- C# class