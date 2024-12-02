export function renderHome(container) {
    container.innerHTML = `
        <div class="main-container">
            <h1 class="title">Connect Four</h1>
            <div class="sub-container">
                <h1 class="subtitle">Play</h1>
                <div class="button-container">
                    <a href="#/game?method=0&depth=0&starter=user" class="btn btn-red">1V1</a>
                    <a href="#/ai-selection" class="btn btn-blue">AI</a>
                </div>
            </div>
        </div>
    `;
}