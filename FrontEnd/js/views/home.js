export function renderHome(container) {
    container.innerHTML = `
        <div class="main-container">
            <h1 class="title">Connect Four</h1>
            <div class="sub-container">
                <h1 class="subtitle">Play</h1>
                <div class="button-container">
                    <a href="#/game?method=0" class="btn btn-pvp">1V1</a>
                    <a href="#/ai-selection" class="btn btn-ai">AI</a>
                </div>
            </div>
        </div>
        <img 
            src="/FrontEnd/images/background.png"
            srcset="/FrontEnd/images/background.png 1x, /FrontEnd/images/background@2x.png 2x, /FrontEnd/images/background@3x.png 3x" 
            class="bottom-image"
        />
    `;
}