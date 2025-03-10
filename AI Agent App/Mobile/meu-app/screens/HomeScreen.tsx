import React, { useContext } from "react";
import { View, Text, Button, StyleSheet, TouchableOpacity } from "react-native";
import { useNavigation } from "@react-navigation/native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { AuthContext } from "../AuthContext"; // Importe o AuthContext

export default function HomeScreen() {
  const navigation = useNavigation();
  const { isLoggedIn, logout } = useContext(AuthContext);

  const handleLogout = async () => {
    await logout();
    navigation.replace("Login")
  };

  function checkLogin(){
    console.log({isLoggedIn});
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Bem-vindo à Home!</Text>
        <View style={styles.buttonContainer}>
            <TouchableOpacity 
                style={styles.button} 
                onPress={handleLogout}
                activeOpacity={0.7}
            >
                <Text style={styles.buttonText}>Sair</Text>
            </TouchableOpacity>
          </View>
    </View>
  );
}

const styles = StyleSheet.create({
    container: {
      flex: 1, 
      justifyContent: "center",
      alignItems: "center",
      backgroundColor: "#f5f5f5",
    },
    title: {
      fontSize: 28,
      fontWeight: "bold",
      marginBottom: 20,
      color: "#333",
    },
    buttonContainer: {
      flexDirection: "row",
      gap: 10,
    },
    button: {
      backgroundColor: "#007bff",
      paddingVertical: 10,
      paddingHorizontal: 20,
      borderRadius: 8,
    },
    buttonText: {
      color: "#fff",
      fontSize: 18,
      fontWeight: "bold",
    },
});
