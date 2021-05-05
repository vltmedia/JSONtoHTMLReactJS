import json

import os
js = '{      "id": 32,      "link": "https://www.target.com/p/funko-pop-games-pokemon-10-34-cubone/-/A-79641748#lnk=sametab",      "shipping_type": "Ship",      "wait_time": "1",      "crawl_queue": 4,      "vendor": 1,      "amount": 1,      "extra_settings": {"data": "s"},"status": 0,"desciption": "Cubone Pop Figure"}'
class JSONToHTMLForm:
    
    # Pass in Json string, then either 'react' or 'html' to get back either plain HTML form, or a React Component.
    def __init__(self, json_data, formname, htmlType):
        self.currentpath =  os.path.abspath(__file__)
        self.dirpath = os.path.dirname(self.currentpath) +"/"
        
        
        self.json_data = json_data
        self.htmlType = htmlType
        self.FormName = formname.replace(' ', '_')
        self.FormNameRaw = formname
        self.keys = []
        self.jsonobj = {}
        self.HTMLTextOut = ""
        self.CSSTextOut = ""
        self.HTMLText = ""
        self.HTMLForm = "<form> $DATA </form>"
        
        # Templates
        self.HTMLInputTemplate = '<div className="'+self.FormName+'_$KEY_container '+self.FormName+'_inputholder"><label  className="'+self.FormName+'_$KEY_label '+self.FormName+'_label" for="$KEY">$KEY:</label><br><input  className="'+self.FormName+'_$KEY_input '+self.FormName+'inputKey"  type="$TYPE" id="$KEY" name="$KEY" placeholder="$VALUE"><br></div>'
        self.HTMLInputTemplateReact = '<div className="'+self.FormName+'_$KEY_container '+self.FormName+'_inputholder"><label className="'+self.FormName+'_$KEY_label '+self.FormName+'_label" >$KEY:</label><br/><input onChange={e => this.setState({$KEY : e.target.value})} className="'+self.FormName+'_$KEY_input '+self.FormName+'inputKey" type="$TYPE" id="$KEY" name="$KEY" placeholder="$VALUE"/><br/></div>'
        self.ReactStateObj = {}        
        self.ReactTemplatePath = self.dirpath + 'reactcomponentFormTemplate.js'
        self.ReactCSSTemplatePath = self.dirpath + 'reactcomponentcssTemplate.css'
        self.ReactStateTemplate = '$KEY:$VALUE'
        self.ReactStateArray = []
        
        self.HTMLGeneratedInputs = []
        
        # Start Loading the data
        if isinstance(json_data, dict):
            self.json_data = json.dumps(json_data)
        else:
            self.json_data = json_data
        self.LoadJSON()

    def GetInputType(self, key):
        value = self.jsonobj[key]
        keytype = type(value)
        typee = "text"
        if keytype.__name__ == 'int' or keytype.__name__ == 'float':
            typee = "number "
        else:
            if '@' in value:
                typee = "email"
                
            if 'ssword' in key:
                typee = "password"
                        
            if '://' in key:
                typee = "url"
        return typee


    def ReloadNewJson(self, jsonn, formname):
        self.FormName = formname.replace(' ', '_')
        self.FormNameRaw = formname
        if isinstance(jsonn, dict):
            self.json_data = json.dumps(jsonn)
        else:
            self.json_data = jsonn
        self.LoadJSON()
        
        
    def GenerateKeyHTML(self, key):
        value = self.jsonobj[key]
        typee = self.GetInputType(key)
        newhtml = self.HTMLInputTemplate.replace('$KEY', key).replace('$VALUE', str(value)).replace('$TYPE', typee)
        if self.htmlType == "react":
            newhtml = self.HTMLInputTemplateReact.replace('$KEY', key).replace('$VALUE', str(value)).replace('$TYPE', typee)
            if(typee != "number"):
                self.ReactStateArray.append(self.ReactStateTemplate.replace('$KEY', key).replace('$VALUE', '"'+str(value)+ '"').replace('$TYPE', typee))
            else:
                self.ReactStateArray.append(self.ReactStateTemplate.replace('$KEY', key).replace('$VALUE', str(value)).replace('$TYPE', typee))
                
        self.HTMLGeneratedInputs.append(newhtml)
        


    def ProcessKey(self):
        for key in self.keys:
            if not isinstance(self.jsonobj[key],dict):
                self.GenerateKeyHTML(key)
                # value = self.jsonobj[key]
                # print(value, type(value))
        
        # print(self.HTMLText)
        
                
                
    
    def LoadJSON(self):
        self.ReactStateArray = []
        self.HTMLGeneratedInputs = []
        self.keys = []
        
        self.jsonobj = json.loads(self.json_data)
        self.keys = self.jsonobj.keys()
        self.ProcessKey()
        
        # self.HTMLText = self.HTMLForm.replace("\n".join(self.HTMLGeneratedInputs))
        if self.htmlType != "react":
            self.HTMLText = self.HTMLForm.replace('$DATA', "\n".join(self.HTMLGeneratedInputs))
            self.HTMLTextOut = self.HTMLText
        else:
            self.HTMLText = "\n".join(self.HTMLGeneratedInputs)
            self.CreateReactComponent()
            
        
    def CreateReactComponent(self):
        csstemplate = open(self.ReactCSSTemplatePath, "r")
        componenttemplate = open(self.ReactTemplatePath, "r")
        Componenttext = componenttemplate.read()
        CSStext = csstemplate.read()
        newComponenttext = Componenttext.replace('$FORMNAME', self.FormName.replace(' ', '_')).replace('$FRMNAMERAW', self.FormNameRaw).replace('$HTML', self.HTMLText).replace('$STATE', ",".join(self.ReactStateArray))
        newCSStext = CSStext.replace('$FORMNAME', self.FormName.replace(' ', '_'))
        self.HTMLTextOut = newComponenttext
        self.CSSTextOut = newCSStext
        print(newComponenttext)
        
        
    def WriteFiles(self, destinationpath):
        outputfolder = os.path.join(destinationpath, self.FormName)
        if os.path.exists(outputfolder) == False:
            os.makedirs(outputfolder)
            
        if self.htmlType != "react":
            outputjs = os.path.join(outputfolder, 'index.html')
            f = open(outputjs, "w")
            f.write(self.HTMLTextOut)
            f.close()
        else:
            
            outputjs = os.path.join(outputfolder, 'index.js')
            f = open(outputjs, "w")
            f.write(self.HTMLTextOut)
            f.close()
            
            outputcss = os.path.join(outputfolder, 'style.css')
            f = open(outputcss, "w")
            f.write(self.CSSTextOut)
            f.close()
            
        

def Main():
    jsonhtml = JSONToHTMLForm(js, 'Crawl Setting', 'react')
    jsonhtml.WriteFiles('D:\Projects\Apps\PythonScripts\py\JsonHTML')
    

if __name__ == '__main__':
    Main()