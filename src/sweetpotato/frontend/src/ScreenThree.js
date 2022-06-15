import React from "react";
import { View, Button } from "react-native";
export class ScreenThree extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    return (
      <View
        style={{
          height: "100%",
          justifyContent: "center",
          alignItems: "center",
          flex: 1,
        }}
      >
        <Button title={"Press me"} />
      </View>
    );
  }
}
