menu = document.getElementById('btn-menu')

click = 1
// verificação do menu
function showMenu(){
    active_menu = document.getElementById("active")

    if(click == 1){
        // se o usuario clicar uma vez o menu abre
        active_menu.classList.add("active")
        click = 2
    }else if(click == 2){
        // se o usuario clicar de novo ele fecha
        active_menu.classList.remove("active")
        click = 1
    }
}



menu.addEventListener('click', showMenu)