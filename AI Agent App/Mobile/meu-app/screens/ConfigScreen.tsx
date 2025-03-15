import React, { useContext, useState, useEffect, useRef } from "react";
import { View, Text, TouchableOpacity, StyleSheet, Animated } from "react-native";
import { useNavigation } from "@react-navigation/native";
import { AuthContext } from "../AuthContext";

export default function Config() {
  const navigation = useNavigation();
  const { logout } = useContext(AuthContext);

  const handleLogout = async () => {
    await logout();
    navigation.replace("Login")
  };


  return (
    <View style={styles.container}>
      <Text style={styles.title}>Página de configuração</Text>
      <Text>*** Em construção ***</Text>
      <Text></Text>
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
    backgroundColor: "#4682B4",
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
