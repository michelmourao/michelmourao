import React, { useState, useEffect, useRef } from "react";
import { View, Text, TouchableOpacity, StyleSheet, Animated } from "react-native";

export default function Contador() {
  const [contador, setContador] = useState(0);
  const scaleAnim = useRef(new Animated.Value(1)).current; // Valor inicial da animação

  useEffect(() => {
    // Quando o contador mudar, faz um efeito de "pulsação"
    Animated.sequence([
      Animated.timing(scaleAnim, {
        toValue: 1.2, // Aumenta um pouco o tamanho
        duration: 150,
        useNativeDriver: true,
      }),
      Animated.timing(scaleAnim, {
        toValue: 1, // Volta ao tamanho normal
        duration: 150,
        useNativeDriver: true,
      }),
    ]).start();
  }, [contador]); // Executa toda vez que o contador mudar

  return (
    <View style={styles.container}>
      <Animated.Text style={[styles.title, { transform: [{ scale: scaleAnim }], color: contador >= 0 ? "blue" : "red" }]}>
        Contador: {contador}
      </Animated.Text>
      <View style={styles.buttonContainer}>
        <TouchableOpacity 
          style={styles.button} 
          onPress={() => setContador(contador + 1)}
          activeOpacity={0.7} // Dá um efeito de "clicado"
        >
          <Text style={styles.buttonText}>Aumentar</Text>
        </TouchableOpacity>
        <TouchableOpacity 
          style={styles.button} 
          onPress={() => setContador(contador - 1)}
          activeOpacity={0.7}
        >
          <Text style={styles.buttonText}>Diminuir</Text>
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
