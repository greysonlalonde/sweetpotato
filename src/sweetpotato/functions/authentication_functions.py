"""
Default authentication and credential storage functions.
"""
LOGIN: str = """
login = () => {
        let formData = new FormData();
        formData.append("username", this.state.username);
        formData.append("password", this.state.password);
        fetch('API_URL/login/', {
            method: "POST",
            body: formData,
        })
            .then((res) => res.json())
            .then((data) => {
                if (data.access) {
                    this.setState({loading: true});
                    this.setState({access_token: data.access});
                } else {
                    console.log("No access token was returned")
                    return false
                }
                this.storeUserSession(data).then((r) => {
                    console.log(r)
                }).then(() => {
                    this.getUserDetails();
                }).then(() => {

                })
            })
            .catch((error) => {
                console.log(`stored error = ${error}`);
            });
    }
"""  #: Login function for authentication.

LOGOUT: str = """
logout = () => {
        this.removeUserSession()
            .then((tokens) => {
                fetch('API_URL/logout/', {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        Authorization: `Bearer ${tokens.access}`,
                    },
                    body: JSON.stringify({
                        refresh: tokens.refresh,
                        access: tokens.access,
                    }),
                }).then((r) => {
                    this.setState({access_token: null});
                })
            })
            .catch((error) => {
                console.log(JSON.stringify(error));
            });
    }
"""  #: Logout function for authentication.

SET_CREDENTIALS: str = """
setUsername = (text) => {
        this.setState({username: text});
    }

    setPassword = (text) => {
        this.setState({password: text, password2: text});
    }
"""  #: Credential setting function for authentication.

STORE_DATA: str = """_storeData = async (tokens) => {
        try {
            await AsyncStorage.setItem(
                'access_token',
                tokens.access_token,
            );
            await AsyncStorage.setItem(
                'refresh_token',
                tokens.refresh_token,
            );
        } catch (error) {
            console.log(error)
        }
};"""  #: Data storage setting function for authentication.

RETRIEVE_DATA: str = """_retrieveData = async () => {
        try {
            const refreshToken = await AsyncStorage.getItem('refresh_token');
            const accessToken = await AsyncStorage.getItem('access_token');
            return {refresh: refreshToken, access: accessToken};
        } catch (error) {
            console.log(error);
        }
};"""  #: Data retrieval function for authentication.

STORE_SESSION: str = """
storeUserSession = async (data) => {
        if (this.state.platform === "mobile") {
            try {
                await SecureStore.setItemAsync("access_token", data.access);
                await SecureStore.setItemAsync("refresh_token", data.refresh);
                await this.timeout(1000);
                return true;
            } catch (error) {
                this.setState({error: error.detail});
                return false;
            }
        } else if (this.state.platform === "web") {
            try {
                await this._storeData({'access_token': data.access, 'refresh_token': data.refresh})
                await this.timeout(1000);
                return true;
            } catch (error) {
                console.log(error)
                this.setState({error: error.detail});
                return false;
            }

        } else {
            console.log("error")
        }
    }
"""  #: Session storage function for authentication.

RETRIEVE_SESSION: str = """
retrieveUserSession = async () => {
        if (this.state.platform === "mobile") {
            try {
                const access_token = await SecureStore.getItemAsync("access_token");
                const refresh_token = await SecureStore.getItemAsync("refresh_token");
                return {refresh: refresh_token, access: access_token};
            } catch (error) {
                this.setState({error: error.detail});
            }
        } else if (this.state.platform === "web") {
            try {
                const tokens = await this._retrieveData();
                return tokens;
            } catch (error) {
                this.setState({error: error.detail});
            }
        } else {
            console.log("error")
        }
    }
"""  #: Session retrieval function for authentication.

REMOVE_SESSION: str = """
removeUserSession = async () => {
        try {
            const access_token = await SecureStore.getItemAsync("access_token");
            const refresh_token = await SecureStore.getItemAsync("refresh_token");
            await SecureStore.deleteItemAsync("access_token");
            await SecureStore.deleteItemAsync("refresh_token");
            return {refresh: refresh_token, access: access_token};
        } catch (error) {
            this.setState({error: error.detail});
        }
    }
"""  #: Session removal function for authentication.

TIMEOUT: str = """
timeout(delay) {
        return new Promise((res) => setTimeout(res, delay));
    }
"""  #: Generic timeout function for authentication.
