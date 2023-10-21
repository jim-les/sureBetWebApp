const freeBtn = document.querySelector('#idFree');
const paidBtn = document.querySelector('#idPaid');
const vipBtn = document.querySelector('#idVIP');
const winsBtn = document.querySelector('#idWins');

freeBtn.addEventListener("click", function() {
    freeBtn.classList.add("selected");
    paidBtn.classList.remove("selected");
    vipBtn.classList.remove("selected");
    winsBtn.classList.remove("selected");
    const paidGames = document.querySelectorAll('.paid')
    paidGames.forEach(game => {
        game.classList.add('hide')
    })

    const freeGames = document.querySelectorAll('.free')
    freeGames.forEach(game => {
        game.classList.remove('hide')
    })
    const vipList = document.querySelector('.vipList')
    vipList.classList.add('hide')

    const wonList = document.querySelector('.wonList')
    wonList.classList.add('hide')

    const completeGames = document.querySelectorAll('.complete')
    completeGames.forEach(game => {
        game.classList.add('hide')
    })
})

paidBtn.addEventListener("click", function() {
    paidBtn.classList.add("selected");
    freeBtn.classList.remove("selected");
    vipBtn.classList.remove("selected");
    winsBtn.classList.remove("selected");
    const paidGames = document.querySelectorAll('.paid')
    paidGames.forEach(game => {
        game.classList.remove('hide')
    })

    const freeGames = document.querySelectorAll('.free')
    freeGames.forEach(game => {
        game.classList.add('hide')
    })
    
    const vipList = document.querySelector('.vipList')
    vipList.classList.add('hide')

    const wonList = document.querySelector('.wonList')
    wonList.classList.add('hide')

    const completeGames = document.querySelectorAll('.complete')
    completeGames.forEach(game => {
        game.classList.add('hide')
    })
})

vipBtn.addEventListener("click", function() {
    vipBtn.classList.add("selected");
    paidBtn.classList.remove("selected");
    freeBtn.classList.remove("selected");
    winsBtn.classList.remove("selected");

    const vipList = document.querySelector('.vipList')
    vipList.classList.remove('hide')

    const paidGames = document.querySelectorAll('.paid')
    paidGames.forEach(game => {
        game.classList.add('hide')
    })

    const freeGames = document.querySelectorAll('.free')
    freeGames.forEach(game => {
        game.classList.add('hide')
    })

    
    const wonList = document.querySelector('.wonList')
    wonList.classList.add('hide')

    const completeGames = document.querySelectorAll('.complete')
    completeGames.forEach(game => {
        game.classList.add('hide')
    })
})

winsBtn.addEventListener("click", function() {
    winsBtn.classList.add("selected");
    paidBtn.classList.remove("selected");
    vipBtn.classList.remove("selected");
    freeBtn.classList.remove("selected");

    const vipList = document.querySelector('.vipList')
    vipList.classList.add('hide')

    const paidGames = document.querySelectorAll('.paid')
    paidGames.forEach(game => {
        game.classList.add('hide')
    })

    const freeGames = document.querySelectorAll('.free')
    freeGames.forEach(game => {
        game.classList.add('hide')
    })

    const wonList = document.querySelector('.wonList')
    wonList.classList.remove('hide')

    const completeGames = document.querySelectorAll('.complete')
    completeGames.forEach(game => {
        game.classList.remove('hide')
    })
})
