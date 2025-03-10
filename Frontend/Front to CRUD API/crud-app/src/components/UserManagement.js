import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserManagement = () => {
  const [users, setUsers] = useState([]); // Para armazenar a lista de usuários
  const [loading, setLoading] = useState(true); // Para indicar se os dados estão carregando
  const [error, setError] = useState(null); // Para capturar erros

  // Função para buscar usuários da API
  const fetchUsers = async () => {
    try {
      const response = await axios.get('/api/users'); // Altere para o endpoint correto
      setUsers(response.data);
      setLoading(false);
    } catch (err) {
      setError(err.message);
      setLoading(false);
    }
  };

  // UseEffect para chamar a função fetchUsers quando o componente for montado
  useEffect(() => {
    fetchUsers();
  }, []);

  // Renderização condicional com base no estado
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Gerenciamento de Usuários</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.username} - {user.email}</li>
        ))}
      </ul>
      {/* Aqui você pode adicionar formulários para adicionar, editar e excluir usuários */}
    </div>
  );
};

export default UserManagement;