import React from "react";
import { View, Button, TextInput } from "react-native";
import { Layout } from "@ui-kitten/components";
export class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = { username: "", password: "", secureTextEntry: true };
  }
  setUsername = (text) => {
    this.setState({ username: text });
  };

  setPassword = (text) => {
    this.setState({ password: text, password2: text });
  };

  login = () => {
    let formData = new FormData();
    formData.append("username", this.state.username);
    formData.append("password", this.state.password);
    fetch("http://127.0.0.1:8000/login/", {
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.access) {
          this.setState({ loading: true });
          this.setState({ access_token: data.access });
        } else {
          console.log("No access token was returned");
          return false;
        }
        this.storeUserSession(data)
          .then((r) => {
            console.log(r);
          })
          .then(() => {
            this.getUserDetails();
          })
          .then(() => {});
      })
      .catch((error) => {
        console.log(`stored error = ${error}`);
      });
  };

  storeUserSession = async (data) => {
    if (this.state.platform === "mobile") {
      try {
        await SecureStore.setItemAsync("access_token", data.access);
        await SecureStore.setItemAsync("refresh_token", data.refresh);
        await this.timeout(1000);
        return true;
      } catch (error) {
        this.setState({ error: error.detail });
        return false;
      }
    } else if (this.state.platform === "web") {
      try {
        await this._storeData({
          access_token: data.access,
          refresh_token: data.refresh,
        });
        await this.timeout(1000);
        return true;
      } catch (error) {
        console.log(error);
        this.setState({ error: error.detail });
        return false;
      }
    } else {
      console.log("error");
    }
  };
  _storeData = async (tokens) => {
    try {
      await AsyncStorage.setItem("access_token", tokens.access_token);
      await AsyncStorage.setItem("refresh_token", tokens.refresh_token);
    } catch (error) {
      console.log(error);
    }
  };
  render() {
    return (
      <Layout
        style={{
          justifyContent: "center",
          alignItems: "center",
          width: "100%",
          flex: 1,
        }}
      >
        <View
          style={{
            flexDirection: "row",
            marginTop: 4,
            width: "100%",
            justifyContent: "center",
          }}
        >
          <TextInput
            placeholder={"Username"}
            value={this.state.username}
            onChangeText={(text) => this.setUsername(text)}
          />
        </View>
        <View
          style={{
            flexDirection: "row",
            marginTop: 4,
            width: "100%",
            justifyContent: "center",
          }}
        >
          <TextInput
            placeholder={"Password"}
            value={this.state.password}
            onChangeText={(text) => this.setPassword(text)}
            secureTextEntry={this.state.secureTextEntry}
          />
        </View>
        <Button title={"SUBMIT"} onPress={() => this.login()} />
      </Layout>
    );
  }
}
