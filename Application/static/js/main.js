import { renderHome } from './views/home.js';
import { renderAISelection } from './views/aiSelection.js';
import { renderGame } from './views/game.js';
import { renderSearchTree } from './views/searchTree.js';

const app = document.getElementById('app');

function router() {
    const fullHash = window.location.hash || '#/';
    const [hash, queryString] = fullHash.split('?');
    const searchParams = new URLSearchParams(queryString);
    const method = searchParams.get('method');

    switch (hash) {
        case '#/':
            renderHome(app);
            break;
        case '#/ai-selection':
            renderAISelection(app);
            break;
        case '#/game':
            renderGame(app, method);
            break;
        case '#/search-tree':
            renderSearchTree(app);
            break;
        default:
            renderHome(app);
    }
}

window.addEventListener('hashchange', router);
router();