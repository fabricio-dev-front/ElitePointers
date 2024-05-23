function cadastro(){
    const nome = document.querySelector('#nome').value;
    const sobreNome = document.querySelector('#sobrenome').value;
    const dataNascimento = document.querySelector('#dataNascimento').value;
    const email = document.querySelector('#email').value;

    if(nome === ""){
        alert("campo do nome vazio. Preencha");
    } else{
        console.log(nome);  
    }
    
    if(sobreNome === ""){
        alert("campo do sobre nome vazio. Preencha");
    } else{
        console.log(sobreNome);
    }
    
    if(dataNascimento === ""){
        alert("campo da data de nascimento vazio. Preencha");
    } else{
        console.log(dataNascimento);
    }
    
    if(email === ""){
        alert("campo do email vazio. Preencha");
    } else{
        console.log(email);
    }    
}