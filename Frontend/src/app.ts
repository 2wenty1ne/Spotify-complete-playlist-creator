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

const errorButton: HTMLButtonElement = document.querySelector('.error-button') as HTMLButtonElement;

document.addEventListener('DOMContentLoaded', () => {
    const bodyId = document.body.id;
    if (bodyId === "homepage") {

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

        console.log("submitting...")

        const privacySwitchButton: HTMLInputElement = document.getElementById('privacy-toggle-switch') as HTMLInputElement;
        if (!privacySwitchButton) {
            console.error('Privacy switch button not found');
            return;
        }

        isPlaylistPrivate = privacySwitchButton.checked ? true : false;

        //TODO Check if logged in

        const requestBody = {
            playlistName: playlistNameInputValue,
            artistID: artistIDInputValue,
            isPrivate: isPlaylistPrivate
        }

        // const response = await fetch('/createPlaylist', {
        //     method: 'POST',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify(requestBody)
        // })

        // if (!response.ok) {
        //     console.log("Error creating playlist")
        // }

        // const result = await response.json()
        // console.log("Success: ", result)
    })


    const logInButton: HTMLButtonElement = document.querySelector('.login-button') as HTMLButtonElement;
    if(!logInButton) {
        console.error('Login button not found')
        return;
    }
    
    logInButton.addEventListener('click', () => {

        const currentHost = window.location.origin;
        const loginPath = '/login';
        const loginUrl = `${currentHost}${loginPath}`;

        window.location.href = loginUrl;
    })

    //! TEST
    const transformButton: HTMLButtonElement = document.querySelector('.transform-button') as HTMLButtonElement;
    if(!transformButton) {
        console.error('Transorm button not found');
        return;
    }
    
    transformButton.addEventListener('click', () => {
        console.log('Transformed!'); //! TEST
        playlistPlaceholderSwap();
    })


    //! TEST
    const errorButton: HTMLButtonElement = document.querySelector('.error-button') as HTMLButtonElement;
    if (!errorButton) {
        console.log('error button not found');
        return;
    }

    errorButton.addEventListener('click', () => {
        console.log("error button clicked!");
        const currentHost = window.location.origin;
        const errorPath = '/err';
        const errorParams = new URLSearchParams({ error: 'amogus' }).toString();
        const errorUrl = `${currentHost}${errorPath}?${errorParams}`;

        window.location.href = errorUrl;
    })
    }

    //? ERROR PAGE
    if (bodyId === "errorpage") {
    
    const homeButton: HTMLButtonElement = document.querySelector('.return-home-button') as HTMLButtonElement;
    if (!homeButton) {
        console.log('home button not found');
        return;
    }

    homeButton.addEventListener('click', () => {
        const currentHost = window.location.origin;
        const homeURL = `${currentHost}/`;

        window.location.href = homeURL;
    })
    }
})
