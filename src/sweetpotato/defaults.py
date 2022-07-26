"""Default attributes for :class:`sweetpotato.config.default_settings.Settings` object.

Attributes:
    UI_KITTEN_COMPONENTS: Available UI Kitten components.
    APP_COMPONENT: Name of application, defaults to `'App'`.
    APP_PROPS_DEFAULT: Default props for application.
    APP_REPR_DEFAULT: String representation of .js class component
"""
UI_KITTEN_COMPONENTS: set = {
    "Text",
    "Input",
    "TextInput",
    "Button",
}

APP_COMPONENT: str = "App"

APP_PROPS_DEFAULT: set = {"state", "theme"}

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
}"""
