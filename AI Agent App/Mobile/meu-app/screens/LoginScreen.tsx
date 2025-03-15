import React, { useState, useContext } from "react";
import { View, TextInput, Button, Text, StyleSheet, Alert, ActivityIndicator } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { AuthContext } from "../AuthContext"; 

export default function LoginScreen({ navigation, setIsLoggedIn }: any) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const { login } = useContext(AuthContext);

  // Função para fazer login e salvar o token
  const handleLogin = async () => {
    if (!username || !password) {
      Alert.alert("Erro", "Preencha todos os campos!");
      return;
    }

    setLoading(true);

    try {
      //await login(username, password);
      printTokenLog();
      navigation.replace("Home");
    } catch (error) {
      Alert.alert("Erro", "Login falhou, tente novamente.");
    } finally {
      setLoading(false);
    }
  };

  const printTokenLog = async () => {
    try {
      const token = await AsyncStorage.getItem("userToken");
      if (token !== null) {
        console.log("Token recuperado:", token);
      } else {
        console.log("Nenhum token encontrado.");
      }
    } catch (error) {
      console.error("Erro ao recuperar o token:", error);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Faça login</Text>
      <TextInput
        style={styles.input}
        placeholder="E-mail"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        style={styles.input}
        placeholder="Senha"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      {loading ? (
        <ActivityIndicator size="small" color="#4682B4" />
      ) : (
        <Button
          title="Entrar"
          color="#4682B4"
          onPress={handleLogin}
          disabled={loading}
        />
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 16,
  },
  title: {
    fontSize: 24,
    marginBottom: 24,
  },
  input: {
    width: "100%",
    height: 40,
    borderColor: "#ccc",
    borderWidth: 1,
    borderRadius: 4,
    marginBottom: 12,
    paddingLeft: 8,
  },
});