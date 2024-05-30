function cadastrar(){
    window.location.href = 'cadastro.html';
}

function navegacaoSuave(){
    const linksNavMenu = document.querySelectorAll('.js-scroll a[href^="#"]');

    function scrollSuave(event){
        event.preventDefault();
        const href = event.currentTarget.getAttribute('href'); 
        const section = document.querySelector(href); // retorna a minha section que está ligada ao menu de navegação.
    
    section.scrollIntoView({ // faz um scroll de navegação suave
        behavior: 'smooth', // efeito suave
        block: 'start',
    });
    }

    linksNavMenu.forEach((link) => {
        link.addEventListener('click', scrollSuave);
    });
}
navegacaoSuave();


function animacaoDeScroll(){
    const sections = document.querySelectorAll('.js-scrollAnimado');

if(sections.length){
    const windowMetade = window.innerHeight * 0.6;

    function animaScroll(){
        sections.forEach((section) => {
            const sectionTop = section.getBoundingClientRect().top;
            const isSection = (sectionTop - windowMetade) < 0;
        
        if(isSection){
           section.classList.add('ativo'); 
        } else {
            section.classList.remove('ativo'); 
        }
        });
    }

    window.addEventListener('scroll', animaScroll);
}
}
animacaoDeScroll();