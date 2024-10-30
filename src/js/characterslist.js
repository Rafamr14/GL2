document.addEventListener('DOMContentLoaded', function () {
    // Seleccionar los botones de filtro de rareza dentro del contenedor correspondiente
    const filterRarityButtons = document.querySelectorAll('[aria-label="Rarity Filter"] button');
    // Seleccionar el filtro de arma
    const filterWeapon = document.getElementById('filterWeapon');
    // Seleccionar los botones de filtro de clase dentro del contenedor correspondiente
    const filterClassButtons = document.querySelectorAll('[aria-label="Class Filter"] button');
    // Seleccionar todas las tarjetas de personajes
    const characterCards = document.querySelectorAll('.character-card');

    let selectedRarity = 'all';
    let selectedWeapon = 'all';
    let selectedClass = 'all';

    // Función para filtrar personajes según los filtros seleccionados
    function filterCharacters() {
        characterCards.forEach(card => {
            const rarity = card.getAttribute('data-rarity').toLowerCase();
            const weapon = card.getAttribute('data-weapon').toLowerCase();
            const characterClass = card.getAttribute('data-class').toLowerCase();

            let display = true;

            if (selectedRarity !== 'all' && rarity !== selectedRarity.toLowerCase()) {
                display = false;
            }

            if (selectedWeapon !== 'all' && weapon !== selectedWeapon.toLowerCase()) {
                display = false;
            }

            if (selectedClass !== 'all' && characterClass !== selectedClass.toLowerCase()) {
                display = false;
            }

            card.style.display = display ? 'block' : 'none';
        });
    }

    // Función para resetear todos los filtros a "All"
    function resetFilters() {
        // Resetear botones de rareza
        filterRarityButtons.forEach(btn => {
            if (btn.getAttribute('data-rarity').toLowerCase() === 'all') {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
        selectedRarity = 'all';

        // Resetear filtro de arma
        filterWeapon.value = 'all';
        selectedWeapon = 'all';

        // Resetear botones de clase
        filterClassButtons.forEach(btn => {
            if (btn.getAttribute('data-class').toLowerCase() === 'all') {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
        selectedClass = 'all';

        // Aplicar el filtrado con todos los filtros reseteados
        filterCharacters();
    }

    // Inicializar los filtros al cargar la página
    resetFilters();

    // Resetear filtros si la página es cargada desde la caché del navegador
    window.addEventListener('pageshow', function(event) {
        if (event.persisted) {
            resetFilters();
        }
    });

    // Añadir event listeners a los botones de filtro de rareza
    filterRarityButtons.forEach(button => {
        button.addEventListener('click', function () {
            // Remover la clase 'active' de todos los botones de rareza
            filterRarityButtons.forEach(btn => btn.classList.remove('active'));
            // Añadir la clase 'active' al botón clicado
            this.classList.add('active');
            // Actualizar el filtro de rareza seleccionado
            selectedRarity = this.getAttribute('data-rarity');
            // Aplicar el filtrado
            filterCharacters();
        });
    });

    // Añadir event listeners a los botones de filtro de clase
    filterClassButtons.forEach(button => {
        button.addEventListener('click', function () {
            // Remover la clase 'active' de todos los botones de clase
            filterClassButtons.forEach(btn => btn.classList.remove('active'));
            // Añadir la clase 'active' al botón clicado
            this.classList.add('active');
            // Actualizar el filtro de clase seleccionado
            selectedClass = this.getAttribute('data-class');
            // Aplicar el filtrado
            filterCharacters();
        });
    });

    // Añadir event listener al selector de arma
    filterWeapon.addEventListener('change', function () {
        // Actualizar el filtro de arma seleccionado
        selectedWeapon = this.value;
        // Aplicar el filtrado
        filterCharacters();
    });
});
