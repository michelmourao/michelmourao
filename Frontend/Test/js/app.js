document.getElementById('login-btn').addEventListener('click', async function () {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        // Fazendo a requisição POST para obter o token
        const response = await fetch('http://localhost:8000/token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json'
            },
            body: new URLSearchParams({
                'grant_type': 'password',
                'username': username,
                'password': password,
                'scope': '',
                'client_id': 'string',
                'client_secret': 'string'
            })
        });

        if (response.ok) {
            const data = await response.json();
            const token = data.access_token;

            // Armazena o token em localStorage para uso posterior
            localStorage.setItem('token', token);
            console.log('Login ok')

            // Exibe o menu principal e oculta o formulário de login
            document.getElementById('login-form').style.display = 'none';
            document.getElementById('main-menu').style.display = 'block';
        } 
        
        if (response.status == 401) {
            alert('Unauthorized: Invalid username or password')
        }
    } catch (error) {
        console.error('Error during login:', error);
        alert('An error occurred. Please try again.');
    }
});
