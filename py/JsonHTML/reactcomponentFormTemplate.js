import "./style.css";

import React from 'react';

class $FORMNAME extends React.Component {
    constructor() {
        super();
        this.state = {$STATE} ;
        this.SubmitClicked = this.SubmitClicked.bind(this);
      }

    SubmitClicked(){

        console.log('SubmitClicked')

        // this.props.Submit(this.state)
    }

    
    render(){
        return <div className='$FORMNAME_Form_Container Form_Container'>
            <h1 className="$FORMNAME_Form_Header Form_Header">$FRMNAMERAW</h1>
            
            $HTML

            <button className="$FORMNAME_submitbutton" onClick={this.SubmitClicked}>Submit</button>

        </div>
    
    
    
    }


}

export default $FORMNAME;