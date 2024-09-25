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
    if (!artistIDInputField) {
        console.error('Artist id input field not found');
        return;
    }

    const playlistNameInputField: HTMLInputElement = document.getElementById('userInputPlaylistName') as HTMLInputElement;
    if (!playlistNameInputField) {
        console.error('Playlist name field not found')
        return;
    }

    const artistIDSubmitButton = document.getElementById('submitArtistID');
    if (!artistIDSubmitButton) {
        console.error('Artist id submit button not found')
        return;
    }

    artistIDSubmitButton.addEventListener('click', () => {
        let playlistNameInputValue = playlistNameInputField.value;
        let artistIDInputValue = artistIDInputField.value;
        let isPlaylistPrivate: boolean = false;

        const privacySwitchButton: HTMLInputElement = document.getElementById('privacy-toggle-switch') as HTMLInputElement;
        if (!privacySwitchButton) {
            console.error('Privacy switch button not found');
            return;
        }

        isPlaylistPrivate = privacySwitchButton.checked ? true : false;

        console.log('Submitted playlist name: ', playlistNameInputValue);
        console.log('Submitted id: ', artistIDInputValue);
        console.log('Private playlist?', isPlaylistPrivate);
    })




    const logInButton: HTMLButtonElement = document.querySelector('.login-button') as HTMLButtonElement;
    if(!logInButton) {
        console.error('Login button not found')
        return;
    }
    
    logInButton.addEventListener('click', () => {
        console.log('Log in button clicked');
        window.location.href = 'http://127.0.0.1:8888/login';
    })


    const transformButton: HTMLButtonElement = document.querySelector('.transform-button') as HTMLButtonElement;
    if(!transformButton) {
        console.error('Transorm button not found');
        return;
    }
    transformButton.addEventListener('click', () => {
        console.log('Transformed!');
        playlistPlaceholderSwap();
    })
})
