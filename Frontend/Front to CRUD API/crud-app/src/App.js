import React from 'react';
import { AuthProvider } from './context/AuthContext'; // Importando o AuthProvider
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Atualize aqui
import Login from './components/Login';
import UserManagement from './components/UserManagement';

const App = () => {
  return (
    <AuthProvider>
      <Router>
        <Routes> {/* Substituindo Switch por Routes */}
          <Route path="/login" element={<Login />} /> {/* Usando a prop element */}
          <Route path="/user-management" element={<UserManagement />} />
          {/* Adicione outras rotas conforme necessário */}
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default App;
