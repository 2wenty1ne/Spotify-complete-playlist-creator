function playlistPlaceholderSwap() {
    const wrapper: HTMLElement = document.querySelector('.playlist-iFrame-wrapper') as HTMLElement;

    if (!wrapper) {
        console.error("Playlist wrapper div not found");
        return;
    }
    const placeholderDiv: HTMLElement = wrapper.querySelector('.playlist-placehorder') as HTMLElement;
    const playlistiFrame: HTMLIFrameElement = wrapper.querySelector('.playlist-iFrame') as HTMLIFrameElement;

    if (!placeholderDiv || !playlistiFrame) {
        console.error("Either placeholder div or playlist iFrame not found");
        return;
    }

    // Toggle visibility
    if (placeholderDiv.style.display !== 'none') {
        placeholderDiv.style.display = 'none';
        playlistiFrame.style.display = 'block';
    } else {
        placeholderDiv.style.display = 'block';
        playlistiFrame.style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const artistIDInputField: HTMLInputElement = document.getElementById('userInputArtistID') as HTMLInputElement;

    if (artistIDInputField) {
        const artistIDSubmitButton = document.getElementById('submitArtistID');

        if (artistIDSubmitButton) {
            artistIDSubmitButton.addEventListener('click', () => {
                console.log('Submitted: ', artistIDInputField.value);
            })
        }
    }
})

//? Test button
document.addEventListener('DOMContentLoaded', () => {
    const testButton = document.querySelector('.test-transform-button');

    if (testButton) {
        testButton.addEventListener('click', () => {
            console.log('Transformed!');
            playlistPlaceholderSwap();
        })
    }
})

