import React from "react";
import { View, Text, Button } from "react-native";
export class ScreenTwo extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    return (
      <View>
        <View
          style={{
            height: "100%",
            justifyContent: "center",
            alignItems: "center",
            flex: 1,
          }}
        >
          <Text>World</Text>
        </View>
        <View>
          <Button title={"Press"} />
        </View>
      </View>
    );
  }
}
