import { playlistPlaceholderSwap, getPlaylistInputValues, SubmitElementNotFound } from "./functions";

export function handleHome() {
    const artistIDSubmitButton = document.getElementById('submitArtistID');
    if (!artistIDSubmitButton) {
        console.error('Artist id submit button not found')
        return
    }

    //? Submit button
    artistIDSubmitButton.addEventListener('click', async () => {
        //TODO Check if logged in first
        try {
            var submitValues = getPlaylistInputValues()
        } catch (SubmitElementNotFound) {
            console.error(SubmitElementNotFound.msg + " not found")
        }

        var [playlistNameInputValue, artistIDInputValue, isPlaylistPrivate] = submitValues;

        const requestBody = {
            playlistName: playlistNameInputValue,
            artistID: artistIDInputValue,
            isPrivate: isPlaylistPrivate
        }

        console.log("submitting...")

        const response = await fetch('/createPlaylist', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestBody)
        })

        if (!response.ok) {
            console.log("Error creating playlist")
            console.error(response.json)
        }

        const result = await response.json()
        console.log("Success: ", result)
    })

    //? Login Button
    const logInButton: HTMLButtonElement = document.querySelector('.login-buttonn') as HTMLButtonElement;
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
    //! TEST
}