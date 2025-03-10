import React, { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import AuthContext from '../context/AuthContext';

const ProtectedRoute = ({ element: Element }) => {
  const { isAuthenticated } = useContext(AuthContext);
  return isAuthenticated ? <Element /> : <Navigate to="/" />;
};

export default ProtectedRoute;
