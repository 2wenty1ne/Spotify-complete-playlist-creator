//TODO rename file

export class SubmitElementNotFound extends Error {
    constructor(msg: string) {
        super(msg);

        Object.setPrototypeOf(this, SubmitElementNotFound.prototype);
    }
}

export function getPlaylistInputValues(): [string, string, boolean] {
    const playlistNameInputField: HTMLInputElement = document.getElementById('userInputPlaylistName') as HTMLInputElement;
    if (!playlistNameInputField) {
        console.error('Playlist name field not found')
        throw new SubmitElementNotFound("Playlist name field");
    }

    const artistIDInputField: HTMLInputElement = document.getElementById('userInputArtistID') as HTMLInputElement;
    if (!artistIDInputField) {
        console.error('Artist id input field not found');
        throw new SubmitElementNotFound("Artist id input field");
    }

    const privacySwitchButton: HTMLInputElement = document.getElementById('privacy-toggle-switch') as HTMLInputElement;
    if (!privacySwitchButton) {
        console.error('Privacy switch button not found');
        throw new SubmitElementNotFound("Privacy switch button");;
    }

    return [playlistNameInputField.value, artistIDInputField.value, privacySwitchButton.checked]
}


export function playlistPlaceholderSwap() {
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

    //? Toggle visibility
    if (placeholderDiv.style.display !== 'none') {
        placeholderDiv.style.display = 'none';
        playlistiFrame.style.display = 'block';
    } else {
        placeholderDiv.style.display = 'block';
        playlistiFrame.style.display = 'none';
        playlistiFrame.src = "https://open.spotify.com/embed/album/30IYyCP3Ptfat4hO5alq7b?utm_source=generator" //! Test
    }
}