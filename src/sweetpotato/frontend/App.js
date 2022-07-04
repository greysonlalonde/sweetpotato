
import React from 'react';
import 'react-native-gesture-handler';
import * as eva from '@eva-design/eva';import * as eva from '@eva-design/eva';import AsyncStorage from @react-native-async-storage/async-storageimport * as SecureStore from expo-secure-storeimport * as eva from '@eva-design/eva';import * as RootNavigation from './src/components/RootNavigation.js'import AsyncStorage from @react-native-async-storage/async-storageimport * as SecureStore from expo-secure-store
import {AuthenticationProvider} from "./AuthenticationProvider";
import {SafeAreaProvider} from "react-native-safe-area-context";
import {ApplicationProvider} from "@ui-kitten/components";
import {NavigationContainer} from "@react-navigation/native";







export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            navigation: RootNavigation.navigationRef    
        }
    }    
    
    

    render() {
        return (
                
<NavigationContainer ref={RootNavigation.navigationRef}>
<ApplicationProvider theme={eva.dark}>
<SafeAreaProvider>
<AuthenticationProvider>[<sweetpotato.navigation.Tab object at 0x10302bd00>]</AuthenticationProvider></SafeAreaProvider></ApplicationProvider></NavigationContainer>
        );
    }
}