import React from "react";
import "react-native-gesture-handler";

import * as eva from "@eva-design/eva";
import * as RootNavigation from "./src/components/RootNavigation.js";
import { EvaIconsPack } from "@ui-kitten/eva-icons";
import { IconRegistry, ApplicationProvider } from "@ui-kitten/components";
import { Home } from "./src/Home.js";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { SafeAreaProvider } from "react-native-safe-area-context";
import { NavigationContainer } from "@react-navigation/native";

const Tab = createBottomTabNavigator();

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { navigation: "RootNavigation.navigationRef" };
  }

  render() {
    return (
      <NavigationContainer ref={RootNavigation.navigationRef}>
        <ApplicationProvider {...eva} theme={{ ...eva.dark }}>
          <IconRegistry icons={EvaIconsPack} />
          <SafeAreaProvider>
            <Tab.Navigator>
              <Tab.Screen name={"Home"}>{() => <Home />}</Tab.Screen>
            </Tab.Navigator>
          </SafeAreaProvider>
        </ApplicationProvider>
      </NavigationContainer>
    );
  }
}
