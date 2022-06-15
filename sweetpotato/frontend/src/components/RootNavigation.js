import {
  CommonActions,
  createNavigationContainerRef,
  DrawerActions,
  StackActions,
} from "@react-navigation/native";

export const navigationRef = createNavigationContainerRef();

export function navigate(name, params) {
  if (navigationRef.isReady()) {
    navigationRef.navigate(name, params);
  }
}

export function push(name, params) {
  console.log("[PUSH");
  console.log(name);
  console.log(params);
  if (navigationRef.isReady()) {
    navigationRef.dispatch(StackActions.push(name, params));
  }
}

export function getCurrentRoute() {
  if (navigationRef.isReady()) {
    return navigationRef.getCurrentRoute();
  }
}

export function setParams(...args) {
  if (navigationRef.isReady()) {
    navigationRef.dispatch(CommonActions.setParams(...args));
  }
}

export function toggleDrawer() {
  if (navigationRef.isReady()) {
    navigationRef.dispatch(DrawerActions.toggleDrawer());
  }
}

export function dispatch(...args) {
  if (navigationRef.isReady()) {
    navigationRef.dispatch(CommonActions.setParams(...args));
  }
}

export function goBack(...args) {
  if (navigationRef.isReady()) {
    navigationRef.goBack();
  }
}

export function customNavigate(name, data) {
  if (navigationRef.isReady()) {
    navigationRef.dispatch(CommonActions.push(name, data));
  }
}
