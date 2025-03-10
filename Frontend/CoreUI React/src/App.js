import React, { Suspense, useEffect } from 'react';
import { HashRouter, Route, Routes, Navigate } from 'react-router-dom';
import { CSpinner, useColorModes } from '@coreui/react';
import './scss/style.scss';
import { AuthProvider } from './context/AuthContext';
import ProtectedRoute from './ProtectedRoute';
import { useSelector } from 'react-redux';
//import DefaultLayout from './layout/DefaultLayout';

// Containers
//const DefaultLayout = React.lazy(() => import('./layout/DefaultLayout'));

// Pages
const Login = React.lazy(() => import('./views/pages/login/Login'));
const Register = React.lazy(() => import('./views/pages/register/Register'));
const Page404 = React.lazy(() => import('./views/pages/page404/Page404'));
const Page500 = React.lazy(() => import('./views/pages/page500/Page500'));
const Dashboard = React.lazy(() => import('./views/dashboard/Dashboard'));
const Tables = React.lazy(() => import('./views/base/tables/Tables'));

const App = () => {
  const { isColorModeSet, setColorMode } = useColorModes('coreui-free-react-admin-template-theme');
  const storedTheme = useSelector((state) => state.theme);

  useEffect(() => {
    const urlParams = new URLSearchParams(window.location.href.split('?')[1]);
    const theme = urlParams.get('theme') && urlParams.get('theme').match(/^[A-Za-z0-9\s]+/)[0];
    if (theme) {
      setColorMode(theme);
    } else if (!isColorModeSet()) {
      setColorMode(storedTheme);
    }
  }, [storedTheme, setColorMode, isColorModeSet]);

  return (
    <HashRouter>
      <AuthProvider>
        <Suspense
          fallback={
            <div className="pt-3 text-center">
              <CSpinner color="primary" variant="grow" />
            </div>
          }
        > 
          <Routes>
            {/* Public Routes */}
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/404" element={<Page404 />} />
            <Route path="/500" element={<Page500 />} />

            {/* Protected Routes, with DefaultLayout */}
            {/* <Route
              path="*"
              element={
                <ProtectedRoute element={<DefaultLayout />} />
              }
            >
            <Route path="dashboard" element={<Dashboard />} />
            <Route path="tables" element={<Tables />} />
            </Route> */}

            <Route path="dashboard" element={<Dashboard />} />
            <Route path="tables" element={<Tables />} />
            
            <Route path="*" element={<Navigate to="/login" replace />} />
          </Routes>
        </Suspense>
      </AuthProvider>
    </HashRouter>
  );
};

export default App;
