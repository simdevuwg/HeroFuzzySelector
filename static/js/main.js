document.addEventListener('DOMContentLoaded', function() {
    // Handle range sliders
    const sliders = document.querySelectorAll('input[type="range"]');
    sliders.forEach(slider => {
        const valueDisplay = document.getElementById(`${slider.id}Value`);
        if (valueDisplay) {
            // Update value on input
            slider.addEventListener('input', function() {
                valueDisplay.textContent = this.value;
            });
        }
    });
    
    // Form validation
    const heroForm = document.getElementById('heroForm');
    if (heroForm) {
        heroForm.addEventListener('submit', function(event) {
            const role = document.getElementById('role').value;
            const heroId = document.getElementById('hero_id').value;
            
            if (!role && !heroId) {
                event.preventDefault();
                alert('Please select either a role or a specific hero for evaluation.');
            }
        });
    }
    
    // Tooltips for attribute explanations
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

// Helper function to filter heroes by role when a role is selected
function filterHeroesByRole(role) {
    const heroSelect = document.getElementById('hero_id');
    
    // If we have an API endpoint
    if (role) {
        fetch(`/api/heroes?role=${role}`)
            .then(response => response.json())
            .then(heroes => {
                // Clear existing options
                while (heroSelect.options.length > 1) {
                    heroSelect.remove(1);
                }
                
                // Add filtered heroes
                heroes.forEach(hero => {
                    const option = document.createElement('option');
                    option.value = hero.id;
                    option.textContent = `${hero.name} (${hero.role})`;
                    heroSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error fetching heroes:', error));
    }
}
