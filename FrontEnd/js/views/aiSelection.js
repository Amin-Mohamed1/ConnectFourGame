export function renderAISelection(container) {
    container.innerHTML = `
        <h1 class="title">Connect Four</h1>
        <h1 class="subtitle">Play</h1>
        <div class="button-container">
            <a href="#/game?method=1" class="btn btn-ai">Mini-Max</a>
            <a href="#/game?method=2" class="btn btn-pvp">Alpha-Beta pruning</a>
            <a href="#/game?method=3" class="btn btn-expectiminimax">Expectiminimax</a>
        </div>
        <img 
            src="/FrontEnd/images/background.png"
            srcset="/FrontEnd/images/background.png 1x, /FrontEnd/images/background@2x.png 2x, /FrontEnd/images/background@3x.png 3x" 
            class="bottom-image"
        />
    `;
}