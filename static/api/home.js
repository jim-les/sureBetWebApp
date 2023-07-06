
const modal = document.querySelector('#modal')
const closeModals = document.querySelectorAll('.close-button')

closeModals.forEach( closeModal => {
    closeModal.addEventListener('click', () => {
        modal.close();
    })
})


const container = document.querySelector('.table');
let allGames = [];
async function getData() {
    const response = await fetch('/getgames/');
    const data = await response.json();
    allGames = data.reverse();
    allGames.forEach(game => {
        if (game.game_paid == true){
            const matchDetail = document.createElement('div');
            matchDetail.className = 'matchDetail';
            matchDetail.classList.add("paid")
            matchDetail.classList.add("hide")
        
            const gameDetails = document.createElement('div');
            gameDetails.className = 'gameDetails';
    
            gameDetails.innerHTML = `
                <span>${game.game_date}/${game.game_month}/${game.game_year} </span>
                <p>${game.home_team_name} v ${game.away_team_name}</p>
                <p style="display:none;">${game.id}</p>
            `;
    
            if (game.admin_winner_choice == game.home_team_name){
                const homeOdd = document.createElement('div');
                homeOdd.className = 'homeOdd';
                homeOdd.style.backgroundColor = "green";
                homeOdd.textContent = game.home_odd;
            
                const drawOdd = document.createElement('div');
                drawOdd.className = 'drawOdd';
                drawOdd.textContent = game.draw_odd;
            
                const awayOdd = document.createElement('div');
                awayOdd.className = 'awayOdd';
                awayOdd.textContent = game.away_odd;
        
                const more = document.createElement('div');
                more.className = 'more';
                more.textContent = '+';
                matchDetail.appendChild(gameDetails);
                matchDetail.appendChild(homeOdd);
                matchDetail.appendChild(drawOdd);
                matchDetail.appendChild(awayOdd);
                matchDetail.appendChild(more);
            
                container.appendChild(matchDetail);
    
            }else if (game.admin_winner_choice == game.away_team_name) {
                const homeOdd = document.createElement('div');
                homeOdd.className = 'homeOdd';
                homeOdd.textContent = game.home_odd;
            
                const drawOdd = document.createElement('div');
                drawOdd.className = 'drawOdd';
                drawOdd.textContent = game.draw_odd;
            
                const awayOdd = document.createElement('div');
                awayOdd.className = 'awayOdd';
                awayOdd.style.backgroundColor = "green";
                awayOdd.textContent = game.away_odd;
        
                const more = document.createElement('div');
                more.className = 'more';
                more.textContent = '+';
                matchDetail.appendChild(gameDetails);
                matchDetail.appendChild(homeOdd);
                matchDetail.appendChild(drawOdd);
                matchDetail.appendChild(awayOdd);
                matchDetail.appendChild(more);
            
                container.appendChild(matchDetail);
            }else if (game.admin_winner_choice == null) {
                const homeOdd = document.createElement('div');
                homeOdd.className = 'homeOdd';
                homeOdd.textContent = game.home_odd;
            
                const drawOdd = document.createElement('div');
                drawOdd.className = 'drawOdd';
                drawOdd.textContent = game.draw_odd;
            
                const awayOdd = document.createElement('div');
                awayOdd.className = 'awayOdd';
                awayOdd.textContent = game.away_odd;
        
                const more = document.createElement('div');
                more.className = 'more';
                more.textContent = '+';
                matchDetail.appendChild(gameDetails);
                matchDetail.appendChild(homeOdd);
                matchDetail.appendChild(drawOdd);
                matchDetail.appendChild(awayOdd);
                matchDetail.appendChild(more);
            
                container.appendChild(matchDetail);
            }else{
                const homeOdd = document.createElement('div');
                homeOdd.className = 'homeOdd';
                homeOdd.textContent = game.home_odd;
            
                const drawOdd = document.createElement('div');
                drawOdd.className = 'drawOdd';
                drawOdd.style.backgroundColor = "green";
                drawOdd.textContent = game.draw_odd;
            
                const awayOdd = document.createElement('div');
                awayOdd.className = 'awayOdd';
                awayOdd.textContent = game.away_odd;
        
                const more = document.createElement('div');
                more.className = 'more';
                more.textContent = '+';
                matchDetail.appendChild(gameDetails);
                matchDetail.appendChild(homeOdd);
                matchDetail.appendChild(drawOdd);
                matchDetail.appendChild(awayOdd);
                matchDetail.appendChild(more);
            
                container.appendChild(matchDetail);
            }
    
    
        }else{

            const matchDetail = document.createElement('div');
            matchDetail.className = 'matchDetail';
            matchDetail.classList.add("free")

        
            const gameDetails = document.createElement('div');
            gameDetails.className = 'gameDetails';
    
            gameDetails.innerHTML = `
                <span>${game.game_date}/${game.game_month}/${game.game_year} </span>
                <p>${game.home_team_name} v ${game.away_team_name}</p>
                <p style="display:none;">${game.id}</p>
            `;
    
            if (game.admin_winner_choice == game.home_team_name){
                const homeOdd = document.createElement('div');
                homeOdd.className = 'homeOdd';
                homeOdd.style.backgroundColor = "green";
                homeOdd.textContent = game.home_odd;
            
                const drawOdd = document.createElement('div');
                drawOdd.className = 'drawOdd';
                drawOdd.textContent = game.draw_odd;
            
                const awayOdd = document.createElement('div');
                awayOdd.className = 'awayOdd';
                awayOdd.textContent = game.away_odd;
        
                const more = document.createElement('div');
                more.className = 'more';
                more.textContent = '+';
                matchDetail.appendChild(gameDetails);
                matchDetail.appendChild(homeOdd);
                matchDetail.appendChild(drawOdd);
                matchDetail.appendChild(awayOdd);
                matchDetail.appendChild(more);
            
                container.appendChild(matchDetail);
    
            }else if (game.admin_winner_choice == game.away_team_name) {
                const homeOdd = document.createElement('div');
                homeOdd.className = 'homeOdd';
                homeOdd.textContent = game.home_odd;
            
                const drawOdd = document.createElement('div');
                drawOdd.className = 'drawOdd';
                drawOdd.textContent = game.draw_odd;
            
                const awayOdd = document.createElement('div');
                awayOdd.className = 'awayOdd';
                awayOdd.style.backgroundColor = "green";
                awayOdd.textContent = game.away_odd;
        
                const more = document.createElement('div');
                more.className = 'more';
                more.textContent = '+';
                matchDetail.appendChild(gameDetails);
                matchDetail.appendChild(homeOdd);
                matchDetail.appendChild(drawOdd);
                matchDetail.appendChild(awayOdd);
                matchDetail.appendChild(more);
            
                container.appendChild(matchDetail);
            }else if (game.admin_winner_choice == null) {
                const homeOdd = document.createElement('div');
                homeOdd.className = 'homeOdd';
                homeOdd.textContent = game.home_odd;
            
                const drawOdd = document.createElement('div');
                drawOdd.className = 'drawOdd';
                drawOdd.textContent = game.draw_odd;
            
                const awayOdd = document.createElement('div');
                awayOdd.className = 'awayOdd';
                awayOdd.textContent = game.away_odd;
        
                const more = document.createElement('div');
                more.className = 'more';
                more.textContent = '+';
                matchDetail.appendChild(gameDetails);
                matchDetail.appendChild(homeOdd);
                matchDetail.appendChild(drawOdd);
                matchDetail.appendChild(awayOdd);
                matchDetail.appendChild(more);
            
                container.appendChild(matchDetail);
            }else{
                const homeOdd = document.createElement('div');
                homeOdd.className = 'homeOdd';
                homeOdd.textContent = game.home_odd;
            
                const drawOdd = document.createElement('div');
                drawOdd.className = 'drawOdd';
                drawOdd.style.backgroundColor = "green";
                drawOdd.textContent = game.draw_odd;
            
                const awayOdd = document.createElement('div');
                awayOdd.className = 'awayOdd';
                awayOdd.textContent = game.away_odd;
        
                const more = document.createElement('div');
                more.className = 'more';
                more.textContent = '+';
                matchDetail.appendChild(gameDetails);
                matchDetail.appendChild(homeOdd);
                matchDetail.appendChild(drawOdd);
                matchDetail.appendChild(awayOdd);
                matchDetail.appendChild(more);
            
                container.appendChild(matchDetail);
            }
    
    
        }






    })


}
getData().then( () => {
    const openModals = document.querySelectorAll('.more')
    const form = document.querySelector('#my-form')
    openModals.forEach(openModal => {
        openModal.addEventListener('click', () => {
            const gameDetails = openModal.parentNode;
            const match = gameDetails.querySelector('.gameDetails')
            const match_teams = match.querySelector('p')
            const modal_teams = modal.querySelector('.teams');
            // Check if the modal_teams already has a child
            if (!modal_teams.querySelector('p')) {
                const modal_teams_details = document.createElement('p');
                modal_teams_details.textContent = match_teams.textContent;
                modal_teams.appendChild(modal_teams_details);

                // Create a new input element
                const hiddenInput = document.createElement('input');
                hiddenInput.type = 'hidden';
                hiddenInput.classList.add('my-hidden-input-class');
                hiddenInput.name = 'gameId';
                hiddenInput.value = match.querySelectorAll('p')[1].innerHTML;
                form.appendChild(hiddenInput);

                // const modal_team_id = document.createElement('p')
                // modal_team_id.textContent = match.querySelectorAll('p')[1].innerHTML
                // modal_team_id.style.display = "none"
                // modal_teams.appendChild(modal_team_id)
            }
            else{
                const modal_teams_details = modal.querySelector('p')
                modal_teams_details.textContent = match_teams.textContent;

                const hiddenInput = form.querySelector('.my-hidden-input-class')
                hiddenInput.value = match.querySelectorAll('p')[1].innerHTML;

                // const modal_team_id = modal.querySelectorAll('p')
                // modal_team_id[1].innerHTML = match.querySelectorAll('p')[1].innerHTML;
            }
            modal.show();
        })
    })
})




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
})

