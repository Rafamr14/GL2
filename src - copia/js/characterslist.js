document.addEventListener('DOMContentLoaded', function () {
    const filterRarityButtons = document.querySelectorAll('[data-rarity]');
    const filterWeapon = document.getElementById('filterWeapon');
    const filterClassButtons = document.querySelectorAll('[data-class]');
    const characterCards = document.querySelectorAll('.character-card');

    let selectedRarity = 'all';
    let selectedWeapon = 'all';
    let selectedClass = 'all';

    function filterCharacters() {
        characterCards.forEach(card => {
            const rarity = card.getAttribute('data-rarity');
            const weapon = card.getAttribute('data-weapon');
            const characterClass = card.getAttribute('data-class').toLowerCase();

            let display = true;

            if (selectedRarity !== 'all' && rarity !== selectedRarity) {
                display = false;
            }

            if (selectedWeapon !== 'all' && weapon !== selectedWeapon) {
                display = false;
            }

            if (selectedClass !== 'all' && characterClass !== selectedClass.toLowerCase()) {
                display = false;
            }

            card.style.display = display ? 'block' : 'none';
        });
    }

    function resetFilters() {
        filterRarityButtons.forEach(btn => {
            if (btn.getAttribute('data-rarity') === 'all') {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
        selectedRarity = 'all';

        filterWeapon.value = 'all';
        selectedWeapon = 'all';

        filterClassButtons.forEach(btn => {
            if (btn.getAttribute('data-class') === 'all') {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
        selectedClass = 'all';

        filterCharacters();
    }
    resetFilters();

    window.addEventListener('pageshow', function(event) {
        if (event.persisted) {
            resetFilters();
        }
    });

    filterRarityButtons.forEach(button => {
        button.addEventListener('click', function () {
            filterRarityButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            selectedRarity = this.getAttribute('data-rarity');
            filterCharacters();
        });
    });

    filterClassButtons.forEach(button => {
        button.addEventListener('click', function () {
            filterClassButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            selectedClass = this.getAttribute('data-class');
            filterCharacters();
        });
    });

    filterWeapon.addEventListener('change', function () {
        selectedWeapon = this.value;
        filterCharacters();
    });
});