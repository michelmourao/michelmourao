import React from "react";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { createStackNavigator } from "@react-navigation/stack";
import { NavigationContainer } from "@react-navigation/native";
import { Ionicons } from "@expo/vector-icons"; // Ícones do menu

import HomeScreen from "./screens/HomeScreen";
import Contador from "./screens/Contador";
import LoginScreen from "./screens/LoginScreen";
import ConfigScreen from "./screens/ConfigScreen"

const Tab = createBottomTabNavigator();
const Stack = createStackNavigator();

export default function TabNavigator() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        headerShown: false, // Esconde o cabeçalho
        tabBarIcon: ({ color, size }) => {
          let iconName;
          if (route.name === "Home") {
            iconName = "home";
          } else if (route.name === "Contador") {
            iconName = "calculator";
          } else if (route.name === "Configuração") {
            iconName = "settings";
          }
          return <Ionicons name={iconName as any} size={size} color={color} />;
        },
        tabBarActiveTintColor: "#6200ea",
        tabBarInactiveTintColor: "gray",
        tabBarStyle: {
          backgroundColor: "#f8f8f8",
          paddingBottom: 5,
          height: 60,
        },
      })}
    >
      <Tab.Screen name="Home" component={HomeScreen} />
      <Tab.Screen name="Contador" component={Contador} />
      <Tab.Screen name="Configuração" component={ConfigScreen} />
    </Tab.Navigator>
  );
}
