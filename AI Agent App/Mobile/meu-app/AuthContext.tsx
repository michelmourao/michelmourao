import React, { createContext, useState, useEffect } from "react";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { useNavigation } from "@react-navigation/native";

type AuthContextType = {
  isLoggedIn: boolean;
  login: (username: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
};

export const AuthContext = createContext<AuthContextType>({
  isLoggedIn: false,
  login: async () => {},
  logout: async () => {},
});

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  //const navigation = useNavigation();

  // Verifica se o usuário está logado ao iniciar o app
  const checkLogin = async () => {
    const token = await AsyncStorage.getItem("userToken");
    setIsLoggedIn(!!token); // Define isLoggedIn como true se o token existir
    console.log("Checando se existe token na memória: ", {token});
    console.log({isLoggedIn});

    // *** IMPLEMENTAR ENDPOINT PARA VALIDAR SE O TOKEN NÃO EXPIROU ***

    // if (!!token){
    //   navigation.navigate("Home")
    // }
  };

  // function check2(){
  //   checkLogin();
  // }
  // useEffect(check2, []);

  useEffect(() => {
    checkLogin();
  }, []);

  // Função para fazer login
  const login = async (username: string, password: string) => {
    try {
      // Cria o corpo da requisição com os parâmetros no formato URL-encoded
      const body = new URLSearchParams({
        grant_type: 'password',
        username: username,
        password: password,
        scope: '',
        client_id: 'string', // Substitua pelo seu client_id real
        client_secret: 'string', // Substitua pelo seu client_secret real
      }).toString();
  
      // Faz a requisição com o método POST
      const response = await fetch("http://192.168.15.93:8000/token", {  // Substitua com o IP do seu MacBook
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded',  // Define o tipo de conteúdo como x-www-form-urlencoded
        },
        body: body,  // Envia os dados no formato correto
      });
  
      if (!response.ok) {
        throw new Error("Falha na autenticação");
      }
  
      const data = await response.json();
      await AsyncStorage.setItem("userToken", data.access_token); // Salva o token
      setIsLoggedIn(true); // Atualiza o estado de login
  
    } catch (error) {
      console.error(error);
      throw new Error("Erro de conexão ou autenticação");
    }
  };

  // Função para fazer logout
  const logout = async () => {
    await AsyncStorage.removeItem("userToken"); // Remove o token
    setIsLoggedIn(false); // Atualiza o estado de login
  };

  return (
    <AuthContext.Provider value={{ isLoggedIn, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};