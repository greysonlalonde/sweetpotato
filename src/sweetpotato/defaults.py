"""Default attributes for :class:`sweetpotato.config.default_settings.Settings` object.

Attributes:
    ~UI_KITTEN_COMPONENTS: ...
    ~APP_DEFAULT: ...
    ~APP_PROPS_DEFAULT: ...
"""
UI_KITTEN_COMPONENTS = {
    "Text",
    "Input",
    "TextInput",
    "Button",
}

APP_DEFAULT = "App"

APP_PROPS_DEFAULT = {"state", "theme"}

APP_REPR_DEFAULT = """
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
}"""
