// Example song data (populate this from your backend or API)
const songs = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5'];

const musicSelect = document.getElementById('musicSelect');
const recommendButton = document.getElementById('recommendButton');
const recommendations = document.getElementById('recommendations');

// Populate the song select box
songs.forEach((song) => {
    const option = document.createElement('option');
    option.value = song;
    option.textContent = song;
    musicSelect.appendChild(option);
});

recommendButton.addEventListener('click', () => {
    const selectedSong = musicSelect.value;

    if (selectedSong) {
        // You can make an API request here to get recommendations based on the selected song
        // Replace the sample code with your actual recommendations
        const recommendationsData = [
            { name: 'Recommended Song 1', image: 'url_to_image_1.jpg' },
            { name: 'Recommended Song 2', image: 'url_to_image_2.jpg' },
            { name: 'Recommended Song 3', image: 'url_to_image_3.jpg' },
            { name: 'Recommended Song 4', image: 'url_to_image_4.jpg' },
            { name: 'Recommended Song 5', image: 'url_to_image_5.jpg' },
        ];

        displayRecommendations(recommendationsData);
    }
});

function displayRecommendations(recommendationsData) {
    recommendations.innerHTML = '';
    recommendationsData.forEach((item) => {
        const recommendationItem = document.createElement('div');
        recommendationItem.classList.add('item');
        recommendationItem.innerHTML = `
            <img src="${item.image}" alt="${item.name}">
            <p>${item.name}</p>
        `;
        recommendations.appendChild(recommendationItem);
    });
}
