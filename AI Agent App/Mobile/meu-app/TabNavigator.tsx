import React from "react";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
//import { createStackNavigator } from "@react-navigation/stack";
import { Ionicons } from "@expo/vector-icons"; // Ícones do menu

import HomeScreen from "./screens/HomeScreen";
import Contador from "./screens/Contador";
import ConfigScreen from "./screens/ConfigScreen"
//import ChatScreen from "./screens/ChatScreen";
import ChatStackNavigator from "./ChatStacknavigator";


const Tab = createBottomTabNavigator();
//const Stack = createStackNavigator();

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
          } else if (route.name === "Chat") {
            iconName = "chatbubble-ellipses";
          }
          return <Ionicons name={iconName as any} size={size} color={color} />;
        },
        tabBarActiveTintColor: "#4682B4",
        tabBarInactiveTintColor: "gray",
        tabBarStyle: {
          backgroundColor: "#f8f8f8",
          paddingBottom: 5,
          height: 60,
        },
      })}
    >
      <Tab.Screen name="Home" component={HomeScreen} />
      {/* /<Tab.Screen name="Contador" component={Contador} />/ */}
      <Tab.Screen 
        name="Chat" 
        component={ChatStackNavigator} 
        options={{
          tabBarStyle: { display: 'none' }, // Oculta a tab bar para essa aba
        }}
      />
      <Tab.Screen name="Configuração" component={ConfigScreen} />
    </Tab.Navigator>
  );
}
