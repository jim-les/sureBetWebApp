async function getData() {
    const response = await fetch('/getgames/');
    const data = await response.json();
    allGames = data.reverse();
    allGames.forEach((game) => {
      const gameContainer = document.createElement('div');
      gameContainer.className = 'game_container';
  
      const gameContainerTop = document.createElement('div');
      gameContainerTop.className = 'game_container_top';
  
      const gameContainerTopLeft = document.createElement('div');
      gameContainerTopLeft.className = 'game_container_top_left';
  
      const gameDetails = document.createElement('div');
      gameDetails.className = 'game_details';
      const gameLogo = document.createElement('img');
      gameLogo.src = './assets/efl_logo.png';
      gameLogo.alt = '';
      gameDetails.appendChild(gameLogo);
  
      const gameTeamDetails = document.createElement('div');
      gameTeamDetails.className = 'game_team_details';
      const leagueName = document.createElement('h2');
      leagueName.textContent = 'League One';
      const homeTeamName = document.createElement('h4');
      homeTeamName.textContent = game.home_team_name;
      const awayTeamName = document.createElement('h4');
      awayTeamName.textContent = game.away_team_name;
      gameTeamDetails.appendChild(leagueName);
      gameTeamDetails.appendChild(homeTeamName);
      gameTeamDetails.appendChild(awayTeamName);
  
      const gameOdd = document.createElement('div');
      gameOdd.className = 'gameOdd';
      const oddValue = document.createElement('p');
      oddValue.textContent = game.home_odd;
      gameOdd.appendChild(oddValue);
  
      gameContainerTopLeft.appendChild(gameDetails);
      gameContainerTopLeft.appendChild(gameTeamDetails);
      gameContainerTopLeft.appendChild(gameOdd);
  
      const gameContainerTopRight = document.createElement('div');
      gameContainerTopRight.className = 'game_container_top_right';
  
      const gameDate = document.createElement('p');
      gameDate.className = 'date';
      gameDate.textContent = `${game.game_year}-${game.game_month}-${game.game_date}`;
      const gameTime = document.createElement('p');
      gameTime.className = 'time';
      gameTime.textContent = '22:00';
  
      const halfResults = document.createElement('div');
      halfResults.className = 'half_results';
      const firstHalfResult = document.createElement('p');
      firstHalfResult.className = 'first_half';
      firstHalfResult.textContent = game.first_half_result;
      const separator = document.createElement('p');
      separator.className = 'separator';
      separator.textContent = '/';
      const secondHalfResult = document.createElement('p');
      secondHalfResult.className = 'second_half';
      secondHalfResult.textContent = game.second_half_result;
  
      halfResults.appendChild(firstHalfResult);
      halfResults.appendChild(separator);
      halfResults.appendChild(secondHalfResult);
  
      gameContainerTopRight.appendChild(gameDate);
      gameContainerTopRight.appendChild(gameTime);
      gameContainerTopRight.appendChild(halfResults);
  
      gameContainerTop.appendChild(gameContainerTopLeft);
      gameContainerTop.appendChild(gameContainerTopRight);
  
      const gameContainerBottom = document.createElement('div');
      gameContainerBottom.className = 'game_container_bottom';
  
      const adminText = document.createElement('p');
      adminText.className = 'admin_text';
      adminText.textContent = 'Goals Over / Under-Over 1.5';
  
      const adminResult = document.createElement('p');
      adminResult.className = 'admin_result';
      adminResult.textContent = game.admin_result;
  
      gameContainerBottom.appendChild(adminText);
      gameContainerBottom.appendChild(adminResult);
  
      gameContainer.appendChild(gameContainerTop);
      gameContainer.appendChild(gameContainerBottom);
  
      container.appendChild(gameContainer);
});

// loadingElement.style.display = 'none';
}
//getData();


const alertImages = document.querySelectorAll('.alertImage')
function handleClick(alertImage) {
  console.log(alertImage.parentNode.querySelector('.game_container_comments'));
  // const commentContainer = document.querySelector('.game_container_comments')
  const commentContainer = alertImage.parentNode.querySelector('.game_container_comments');
  // const comment = document.querySelector(".game_comment")
  const comment = alertImage.parentNode.querySelector('.game_comment');
  // console.log(commentContainer.style.height);

  if (commentContainer.style.height == '50px' ){
    commentContainer.style.height = '0px';
    comment.style.display = 'none';
    return;
  }
  commentContainer.style.height = '50px';
  comment.style.display = 'block';
}

alertImages.forEach((alertImage) => {
  alertImage.addEventListener('click', () => handleClick(alertImage));
})


const theGames = document.querySelectorAll('.game_container')
theGames.forEach((game) => {
    let gameFeature = game.querySelector('.details')
    if (gameFeature.innerHTML == 'False'){
        return
    }
    game.style.display = 'none';

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

    const vipCards = document.querySelectorAll('.vip_card_container')
    vipCards.forEach(card => {
        card.classList.add('hide')
    })
    theGames.forEach((game) => {
        let gameFeature = game.querySelector('.details')
        if (gameFeature.innerHTML == 'False'){
            game.style.display = 'block';
            return
        }else{
            game.style.display = 'none';
        }
    })
    /*
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
    */
})

paidBtn.addEventListener("click", function() {
    paidBtn.classList.add("selected");
    freeBtn.classList.remove("selected");
    vipBtn.classList.remove("selected");
    winsBtn.classList.remove("selected");

    const vipCards = document.querySelectorAll('.vip_card_container')
    vipCards.forEach(card => {
        card.classList.add('hide')
    })
    theGames.forEach((game) => {
        let gameFeature = game.querySelector('.details')
        if (gameFeature.innerHTML == 'True'){
            game.style.display = 'block';
            return
        }else{
            game.style.display = 'none';
        }
    })
    /*
    // const paidGames = document.querySelectorAll('.paid')
    // paidGames.forEach(game => {
    //     game.classList.remove('hide')
    // })

    // const freeGames = document.querySelectorAll('.free')
    // freeGames.forEach(game => {
    //     game.classList.add('hide')
    // })
    
    // const vipList = document.querySelector('.vipList')
    // vipList.classList.add('hide')

    // const wonList = document.querySelector('.wonList')
    // wonList.classList.add('hide')
    */
})

vipBtn.addEventListener("click", function() {
    vipBtn.classList.add("selected");
    paidBtn.classList.remove("selected");
    freeBtn.classList.remove("selected");
    winsBtn.classList.remove("selected");

    // const vipList = document.querySelector('.vipList')
    // vipList.classList.remove('hide')

    // const paidGames = document.querySelectorAll('.paid')
    // paidGames.forEach(game => {
    //     game.classList.add('hide')
    // })

    const vipCards = document.querySelectorAll('.vip_card_container')
    vipCards.forEach(card => {
        card.classList.remove('hide')
    })

    // const freeGames = document.querySelectorAll('.free')
    // freeGames.forEach(game => {
    //     game.classList.add('hide')
    // })

    
    // const wonList = document.querySelector('.wonList')
    // wonList.classList.add('hide')
})

winsBtn.addEventListener("click", function() {
    winsBtn.classList.add("selected");
    paidBtn.classList.remove("selected");
    vipBtn.classList.remove("selected");
    freeBtn.classList.remove("selected");

    const vipCards = document.querySelectorAll('.vip_card_container')
    vipCards.forEach(card => {
        card.classList.add('hide')
    })

    theGames.forEach((game) => {
        let gameFeature = game.querySelector('.details')
        if (gameFeature.innerHTML == 'WON'){
            game.style.display = 'block';
            return
        }else{
            game.style.display = 'none';
        }
    })

    // const vipList = document.querySelector('.vipList')
    // vipList.classList.add('hide')

    // const paidGames = document.querySelectorAll('.paid')
    // paidGames.forEach(game => {
    //     game.classList.add('hide')
    // })

    // const freeGames = document.querySelectorAll('.free')
    // freeGames.forEach(game => {
    //     game.classList.add('hide')
    // })

    // const wonList = document.querySelector('.wonList')
    // wonList.classList.remove('hide')
})



