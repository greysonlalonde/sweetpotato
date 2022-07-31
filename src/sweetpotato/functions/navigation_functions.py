"""
Default navigation functions.
"""

NAVIGATION_REF: str = """export const navigationRef = createNavigationContainerRef();"""

NAVIGATE: str = """export function navigate(name, params) {
  if (navigationRef.isReady()) {
    navigationRef.navigate(name, params);
  }
}"""

PUSH: str = """export function push(name, params) {
  console.log("[PUSH");
  console.log(name);
  console.log(params);
  if (navigationRef.isReady()) {
    navigationRef.dispatch(StackActions.push(name, params));
  }
}"""

GET_CURRENT_ROUTE: str = """export function getCurrentRoute() {
  if (navigationRef.isReady()) {
    return navigationRef.getCurrentRoute();
  }
}"""

SET_PARAMS: str = """export function setParams(...args) {
  if (navigationRef.isReady()) {
    navigationRef.dispatch(CommonActions.setParams(...args));
  }
}"""

TOGGLE_DRAWER: str = """export function toggleDrawer() {
  if (navigationRef.isReady()) {
    navigationRef.dispatch(DrawerActions.toggleDrawer());
  }
}"""

DISPATCH: str = """export function dispatch(...args) {
  if (navigationRef.isReady()) {
    navigationRef.dispatch(CommonActions.setParams(...args));
  }
}"""

GO_BACK: str = """export function goBack(...args) {
  if (navigationRef.isReady()) {
    navigationRef.goBack();
  }
}"""

CUSTOM_NAVIGATE: str = """export function customNavigate(name, data) {
  if (navigationRef.isReady()) {
    navigationRef.dispatch(CommonActions.push(name, data));
  }
}"""
