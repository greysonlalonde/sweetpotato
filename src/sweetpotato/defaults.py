"""Default attributes for :class:`~sweetpotato.config.default_settings.Settings`."""

UI_KITTEN_COMPONENTS: set = {
    "Text",
    "Input",
    "TextInput",
    "Button",
}  #: List of @ui-kitten/components replacements.

APP_COMPONENT: str = "App"  #: Name of application component.

APP_PROPS_DEFAULT: set = {"state", "theme"}  #: Default allowed props for application.

APP_REPR_DEFAULT: str = """
import React from 'react';
<IMPORTS>

<VARIABLES>

export default class <NAME> extends React.Component {
    constructor(props) {
        super(props);
        this.state = <STATE>    
    }    
    
    <FUNCTIONS>

    render() {
        return (
                <CHILDREN>
        );
    }
}"""  #: Default .js string representation of application component.
