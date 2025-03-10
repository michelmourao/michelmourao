// src/context/AuthContext.js
import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';
import qs from 'qs';

// Cria o contexto de autenticação
const AuthContext = createContext();

// Cria um provedor de autenticação
export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Função para fazer login
  const login = async (username, password) => {
    try {
      // Dados a serem enviados no corpo da requisição
      const data = {
        grant_type: 'password',
        username: username,
        password: password,
        scope: '',
        client_id: 'string', // Substitua pelo seu client_id
        client_secret: 'string' // Substitua pelo seu client_secret
      };
  
      // Configuração dos cabeçalhos
      const config = {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      };
  
      // Faz a requisição POST
      const response = await axios.post('http://localhost:8000/token', qs.stringify(data), config);
  
      // Armazena o token no localStorage
      localStorage.setItem('token', response.data.access_token);
      setIsAuthenticated(true);
    } catch (error) {
      console.error('Login failed', error);
    }
  };

  // Função para logout
  const logout = () => {
    localStorage.removeItem('token');
    setIsAuthenticated(false);
  };

  // Verifica se o usuário já está autenticado no carregamento da página
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      setIsAuthenticated(true);
    }
  }, []);

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
