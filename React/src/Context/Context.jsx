import { createContext, useState } from "react";
import sendMessage from '../API/Chatbot'
import processVideoUrl from "../API/VideoUrl";

export const Context = createContext();

const ContextProvider = (props) => {

    const [input, setInput] = useState("");
    const [recentPrompt, setRecentPrompt] = useState("");
    const [prevPrompt, setPrevPrompt] = useState([]);
    const [showResult, setShowResult] = useState(false);
    const [loading, setLoading] = useState(false);
    const [resultData, setResultData] = useState("");

    // Extract YouTube URL from text
    const extractYouTubeUrl = (text) => {
        const patterns = [
            /(https?:\/\/(?:www\.)?youtube\.com\/watch\?v=[a-zA-Z0-9_-]+(?:[^\s]*)?)/,
            /(https?:\/\/(?:www\.)?youtu\.be\/[a-zA-Z0-9_-]+(?:[^\s]*)?)/,
            /(https?:\/\/(?:www\.)?youtube\.com\/embed\/[a-zA-Z0-9_-]+(?:[^\s]*)?)/,
        ];

        for (let pattern of patterns) {
            const match = text.match(pattern);
            if (match) {
                return match[1];
            }
        }
        return null;
    };

    // Main extraction function - returns url and text separated
    const extractUrlAndText = (input) => {
        const youtubeUrl = extractYouTubeUrl(input);

        if (youtubeUrl) {
            const textWithoutUrl = input.replace(youtubeUrl, '').trim();
            return {
                url: youtubeUrl,
                text: textWithoutUrl
            };
        }

        return null; // Return null if no URL found
    };

    const delayPara = (index, nextWord) => {
        setTimeout(() => {
            setResultData(prevData => prevData + nextWord);
        }, 5 * index);
    }

    const onSent = async (prompt) => {
        setResultData("")
        setLoading(true)
        setShowResult(true)
        
        let response = "";
        const userInput = prompt !== undefined ? prompt : input;

        // Check for YouTube URL
        const urlAndText = extractUrlAndText(userInput);
        
        if (urlAndText) {
            // YouTube URL found - process video
            response = await processVideoUrl(urlAndText.url, urlAndText.text);
        } else {
            // No YouTube URL - regular chat message
            response = await sendMessage(userInput);
        }

        // Update prompts
        setRecentPrompt(userInput);
        if (prompt === undefined) {
            setPrevPrompt((prev) => [...prev, input]);
        }

        // Format response
        let newResponse = "";

        // Handle bold text
        let responseArray = response.split("**")
        for (let i = 0; i < responseArray.length; i++) {
            if (i % 2 === 0) {
                newResponse += responseArray[i];
            } else {
                newResponse += "<b>" + responseArray[i] + "</b>";
            }
        }

        newResponse = newResponse.replace(/^\* /gm, "• ");
        newResponse = newResponse.replace(/\n\* /g, "\n• ");

        // Handle italic text
        newResponse = newResponse.replace(/\*(.*?)\*/g, "<i>$1</i>");

        // Handle new lines
        newResponse = newResponse.replace(/\n/g, "<br/>");

        // Display response with character-by-character animation
        for (let j = 0; j < newResponse.length; j++) {
            delayPara(j, newResponse[j])
        }

        setLoading(false)
        setInput("")
    }

    const contextValue = {
        input,
        setInput,
        recentPrompt,
        setRecentPrompt,
        prevPrompt,
        setPrevPrompt,
        resultData,
        setResultData,
        showResult,
        setShowResult,
        loading,
        setLoading,
        onSent
    }

    return (
        <Context.Provider value={contextValue}>
            {props.children}
        </Context.Provider>
    )
}

export default ContextProvider;