import React, { createContext, useState, useEffect, useContext } from 'react';
import { useNavigate } from 'react-router-dom';

// Criar o contexto
export const AuthContext = createContext();

// Hook para acessar o contexto
export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(true);
  const [token, setToken] = useState(true);
  const navigate = useNavigate();

  const login = async (username, password) => {
    try {
      const response = await fetch('http://localhost:8000/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
          grant_type: 'password',
          username: username,
          password: password,
          scope: '',
          client_id: 'string',
          client_secret: 'string',
        }),
      });

      const data = await response.json();
      if (data.access_token) {
        setToken(data.access_token);
        setUser(username);
        localStorage.setItem('access_token', data.access_token);
        //navigate('/dashboard');
      } else {
        console.error('Login failed: no access token');
      }
    } catch (error) {
      console.error('Login failed', error);
    }
  };

  const logout = () => {
    setToken(null);
    setUser(null);
    localStorage.removeItem('access_token');
    navigate('/login');
  };

  useEffect(() => {
    const storedToken = localStorage.getItem('access_token');
    
    if (!storedToken) {
      setToken(false)
    }
    // if (storedToken) {
    //   setToken(storedToken);
    // } else {
    //   setToken(false)
    // }
  }, [navigate]);
  
  const isAuthenticated = !!token;
  console.log('AuthContext: isAuthenticated =', isAuthenticated);

  return (
    <AuthContext.Provider value={{ user, token, isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
