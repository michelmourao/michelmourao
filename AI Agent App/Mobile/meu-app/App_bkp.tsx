import React, { useState, useEffect } from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import { ActivityIndicator, View } from "react-native";
import LoginScreen from "./screens/LoginScreen";
import HomeScreen from "./screens/HomeScreen";
import Contador from "./screens/Contador";
import TabNavigator from "./TabNavigator";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { AuthProvider } from "./AuthContext"; // Importe o AuthProvider

const Stack = createStackNavigator();

export default function App() {
  const [isLoggedIn, setIsLoggedIn] = useState<boolean | null>(null);

  useEffect(() => {
    const checkLogin = async () => {
      try {
        const token = await AsyncStorage.getItem("userToken");
        if (token !== null) {
          console.log("Token recuperado:", token);
          console.log("Redirecionando para Home...")
        } else {
          console.log("Nenhum token encontrado.");
          console.log("Redirecionando para Home...")
        }
      } catch (error) {
        console.error("Erro ao recuperar o token:", error);
      }
      //setIsLoggedIn(!!token);
    };
    checkLogin();
  }, []);

  if (isLoggedIn === null) {
    return (
      <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
        <ActivityIndicator size="large" color="#0000ff" />
      </View>
    );
  }

  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{ headerShown: false }}>
        <Stack.Screen name="Home" component={TabNavigator} />
        <Stack.Screen name="Login" component={TabNavigator} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

// return (
//   <AuthProvider>
//   <NavigationContainer>
//     <Stack.Navigator screenOptions={{ headerShown: false }}>
//       {isLoggedIn ? (
//         <Stack.Screen name="Home" component={TabNavigator} />
//       ) : (
//         <Stack.Screen name="Login">
//           {(props) => <LoginScreen {...props} setIsLoggedIn={setIsLoggedIn} />}
//         </Stack.Screen>
//       )}
//     </Stack.Navigator>
//   </NavigationContainer>
//   </AuthProvider>
// );
// }

