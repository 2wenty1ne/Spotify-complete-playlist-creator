import { getPlaylistInputValues, showPlaylist } from "./functions";

export async function handleSubmitButton() {
    //TODO Check if logged in first
    try {
        var submitValues = getPlaylistInputValues()
    } catch (SubmitElementNotFound) {
        console.error(SubmitElementNotFound.msg + " not found")
        //! Internal error
        return
    }

    
    var [playlistNameInputValue, artistIDInputValue, isPlaylistPrivate] = submitValues;

    const requestBody = {
        playlistName: playlistNameInputValue,
        artistID: artistIDInputValue,
        isPrivate: isPlaylistPrivate
    }

    const response = await fetch('/createPlaylist', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(requestBody)
    })

    if (response.status == 490) {
        changeSubmitErrorMessageVis("show")
        return
    }

    if (!response.ok) {
        return //! Internal Error
    }

    const result = await response.json()
    changeSubmitErrorMessageVis("hide")
    console.log("Success: " , result) //! TEST
    showPlaylist(result.playlistURL)
}


export function changeSubmitErrorMessageVis(state) {
    const submitErrorMessage: HTMLSpanElement = document.querySelector('#submit-error-message') as HTMLSpanElement;

    if (!submitErrorMessage) {
        return; //! Internal Error
    }

    var visibility = state === "show" ? "visible" : "hidden";

    submitErrorMessage.style.visibility = visibility;
}

