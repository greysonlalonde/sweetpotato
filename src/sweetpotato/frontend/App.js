import "react-native-gesture-handler";
import React from "react";
import { ScreenOne } from "./src/ScreenOne.js";
import { ScreenTwo } from "./src/ScreenTwo.js";
import { ScreenThree } from "./src/ScreenThree.js";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { NavigationContainer } from "@react-navigation/native";
import { SafeAreaProvider } from "react-native-safe-area-context";
import * as RootNavigation from "./src/components/RootNavigation";
import AsyncStorage from "@react-native-async-storage/async-storage";
import * as SecureStore from "expo-secure-store";

const Tab = createBottomTabNavigator();

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isAuthenticated: false,

      navigation: RootNavigation.navigationRef,
    };
  }

  render() {
    return (
      <NavigationContainer ref={this.state.navigation}>
        <SafeAreaProvider>
          <Tab.Navigator>
            <Tab.Screen name={"Screen One"} component={ScreenOne} />
            <Tab.Screen name={"Screen Two"} component={ScreenTwo} />
            <Tab.Screen name={"Screen Three"} component={ScreenThree} />
          </Tab.Navigator>
        </SafeAreaProvider>
      </NavigationContainer>
    );
  }
}
