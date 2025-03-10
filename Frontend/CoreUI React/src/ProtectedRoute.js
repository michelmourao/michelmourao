import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from './context/AuthContext';

const ProtectedRoute = ({ element }) => {
  const { isAuthenticated } = useAuth();
  console.log('isAuthenticated at protectedroute:', isAuthenticated);
  
  if (!isAuthenticated) {
    console.log('isAuth: ', !isAuthenticated)
    return <Navigate to="/login" replace />;
  }

  return element;
};

export default ProtectedRoute;
