document.querySelectorAll('button[data-action]').forEach(button => {
    button.addEventListener('click', () => {
        const action = button.getAttribute('data-action');
        const pk = button.getAttribute('data-pk');
        const url = action === 'add' ? `/picture/${pk}/favorite/` : `/picture/${pk}/unfavorite/`;

        fetch(url, {
            method: 'POST',
            headers: { 'X-Requested-With': 'XMLHttpRequest' },
            credentials: 'same-origin'
        })
        .then(response => response.json())
        .then(data => {
            if (data.result === 'success') {
                if (action === 'add') {
                    button.textContent = 'Удалить из избранного';
                    button.setAttribute('data-action', 'remove');
                } else {
                    button.textContent = 'Добавить в избранное';
                    button.setAttribute('data-action', 'add');
                }
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
