import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import { AuthProvider } from "./AuthContext";
import LoginScreen from "./screens/LoginScreen";
import TabNavigator from "./TabNavigator";

const Stack = createStackNavigator();

export default function App() {
  return (
    <AuthProvider>
      <NavigationContainer>
        <Stack.Navigator screenOptions={{ headerShown: false }}>
          <Stack.Screen name="Login" component={LoginScreen} />
          <Stack.Screen name="Home" component={TabNavigator} />
        </Stack.Navigator>
      </NavigationContainer>
    </AuthProvider>
  );
}