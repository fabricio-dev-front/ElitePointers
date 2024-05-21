function cadastro(){
    const nome = document.querySelector('#nome').value;
    const sobreNome = document.querySelector('#sobrenome').value;
    const dataNascimento = document.querySelector('#dataNascimento').value;
    const email = document.querySelector('#email').value;

    if(nome === "" && sobreNome === "" && dataNascimento === "" &&email === ""){
        alert("É preciso preencher todos os campos");
    } 

}