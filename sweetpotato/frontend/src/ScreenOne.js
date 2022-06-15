import React from "react";
import { Text } from "react-native";
import { Layout } from "@ui-kitten/components";
export class ScreenOne extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    return (
      <Layout
        style={{
          height: "100%",
          justifyContent: "center",
          alignItems: "center",
          flex: 1,
        }}
      >
        <Text>Hello</Text>
      </Layout>
    );
  }
}
