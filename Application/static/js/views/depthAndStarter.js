export function renderDepthAndStarter(container, method) {
    container.innerHTML = `
        <div class="main-container">
            <h1 class="title">Connect Four</h1>
            <div class="sub-container">
                <form id="settings-form" class="settings-form">
                    <label class="subtitle">Max Depth</label>

                    <div class="custom-number-input">
                        <button id="decrement" type="button" aria-label="Decrease">-</button>
                        <input type="number" id="depth" name="depth" min="1" max="42" value="5" readonly>
                        <button id="increment" type="button" aria-label="Increase">+</button>
                    </div>

                    <label for="starter" class="subtitle">Who Starts</label>
                    <select id="starter" name="starter">
                        <option value="user">User</option>
                        <option value="ai">AI</option>
                    </select>

                    <button type="submit" class="btn btn-red">Start Game</button>
                </form>
            </div>
        </div>
    `;

    const form = container.querySelector("#settings-form");
    form.addEventListener("submit", (event) => {
        event.preventDefault();
        const depth = form.elements["depth"].value;
        const starter = form.elements["starter"].value;
        window.location.hash = `#/game?method=${method}&depth=${depth}&starter=${starter}`;
    });

    const input = container.querySelector("#depth");
    const incrementButton = container.querySelector("#increment");
    const decrementButton = container.querySelector("#decrement");

    const min = parseInt(input.min);
    const max = parseInt(input.max);

    function updateButtons() {
        incrementButton.disabled = parseInt(input.value) >= max;
        decrementButton.disabled = parseInt(input.value) <= min;
    }

    incrementButton.addEventListener("click", () => {
        if (parseInt(input.value) < max) {
            input.value = parseInt(input.value) + 1;
            updateButtons();
        }
    });

    decrementButton.addEventListener("click", () => {
        if (parseInt(input.value) > min) {
            input.value = parseInt(input.value) - 1;
            updateButtons();
        }
    });

    updateButtons();
}
