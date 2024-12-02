export function renderAISelection(container) {
    container.innerHTML = `
        <div class="main-container">
            <h1 class="title">Connect Four</h1>
            <div class="sub-container">
                <h1 class="subtitle">Play</h1>
                <div class="button-container">
                    <a href="#/depth-and-starter?method=1" class="btn btn-blue">Mini-Max</a>
                    <a href="#/depth-and-starter?method=2" class="btn btn-red">Alpha-Beta pruning</a>
                    <a href="#/depth-and-starter?method=3" class="btn btn-gold">Expectiminimax</a>
                </div>
            </div>
        </div>
    `;
}