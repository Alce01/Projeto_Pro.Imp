document.querySelector("form").addEventListener("submit", function (event) {
    const cpf = document.getElementById("cpf").value;
    const Senha = document.getElementById("Senha").value;
  
    if (!username || !password) {
      event.preventDefault();
      alert("Preencha todos os campos!");
    }
  });